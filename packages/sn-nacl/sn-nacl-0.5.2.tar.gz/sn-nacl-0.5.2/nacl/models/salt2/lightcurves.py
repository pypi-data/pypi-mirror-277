"""SN light curve eval unit
"""

import logging

import time
import numpy as np
import scipy

import numexpr as ne

try:
    from sparse_dot_mkl import gram_matrix_mkl, dot_product_mkl
except:
    logging.warning('module: `sparse_dot_mkl` not available')
else:
    logging.info('sparse_dot_mkl found. Building hessian should be faster.')

from ...sparseutils import kron_product_by_line, CooMatrixBuff, CooMatrixBuff2
from bbf import magsys

class LightcurveEvalUnitTz(object):
    r"""Evaluate the light curve of a single SN in a single band

    Given a set of dates, and the :math:`(X_0, X_1, c, t_{max})` parameters of
    the SN, compute the quantities:

    .. math::

         X_0 \times (1+z) \times \left[I_0 + X_1 I_1\right]

    with

    .. math::
         I_{0|1} = \int M_{0|1}(\lambda, \mathrm{p}) \frac{\lambda}{hc} T((1+z)\lambda) 10^{0.4\ c\ P(\lambda)} d\lambda

    In practice, we can speed up the computations by decomposing the filter on a
    spline basis: :math:`T(\lambda (1+z)) = \sum_q t_q(z) B_q(\lambda)= \sum_q
    (1+z) t_q B_q(\lambda)`, which allows to decompose the integral above as:

    .. math::
        I_{0|1} = \sum_{k\ell q} \theta_{0|1, k\ell} t_q(z) B_k(\mathrm{p})\ \int B_\ell(\lambda)
        \frac{\lambda}{hc} B_q(\lambda)\ 10^{0.4\ c\ P(\lambda)} d\lambda

    We use the fact that the color law is a slowly variable function of
    :math:`\lambda` (compared to the individual splines) to expel the color law
    from the integral:

    .. math::
       \int B_\ell(\lambda) \frac{\lambda}{hc} B_q(\lambda) CL(\lambda) d\lambda \approx
       CL(\lambda^{\mathrm{eff}}_{\ell q})\ \times \int B_\ell(\lambda) \frac{\lambda}{hc} B_q(\lambda) d\lambda

    up to second order, if we define:

    .. math::
       \lambda^{\mathrm{eff}}_{\ell q} = \frac{\int B_\ell(\lambda)
       \lambda^2 B_q(\lambda) d\lambda}{\int B_\ell(\lambda) \lambda B_q(\lambda) d\lambda}


    and so, defining: :math:`\Lambda^{\mathrm{eff}} =
    (\lambda^{\mathrm{eff}}_{\ell q})` and ::math:`G = (G_{\ell q}) = (\int
    B_\ell(\lambda)\frac{\lambda}{hc} B_q(\lambda)) d\lambda`, the integral
    evaluation reduces to:

    .. math::
        I_{0|1} = J\ \cdot \Theta\ \cdot \left[G \Lambda^{\mathrm{eff}}\right] \cdot t_z

    where :math:`J`, :math:`G`, :math:`\Lambda^{\mathrm{eff}}` and :math:`t_z`
    are sparse and where :math:`G, \Lambda^{\mathrm{eff}}` can be precomputed
    once for all.

    Matrix :math:`G` is called the Gramian of the model and filter spline bases.
    It is precomputed exactly, using Gaussian quadrature when the model is
    instantiated.

    This strategy decomposes :math:`T((1+z)\lambda)` and work with a single
    Gramian and an SN-dependant :math:`t_z` vector. This option is probably
    computationally less intensive, as we can factorize the evaluation of the
    color law.

    """

    def __init__(self, lcdata, model):
        r"""Constructor

        Retrieve the band shape :math:`T(\lambda)` and project
        :math:`T(\lambda(1+z))` on the basis

        Parameters
        ----------
        lcdata : nacl.dataset.LcData
            Photometric of one Lc of one SN nacl data class.
        model : nacl.models.salt.SALT2Like
            Model.

        """
        self.lcdata = lcdata
        # self.data = lcdata.data # we no longer use this
        self.model = model
        self.z = lcdata.z[0]

        # TODO: here, we take only the default band
        # we should specialize and take the band at default location
        # tr = model.filter_db.transmission_db[self.band]
        self.band = lcdata.band[0]
        self.tqz, _ = model.filter_db.insert(self.band, z=self.z)
        # set to zero very small values
        self.tqz[(np.abs(self.tqz)/self.tqz.max() < 1e-10)] = 0.
        
        # self.sn_id = lcdata.sn_id
        self.sn_index = lcdata.sn_index[0]

        #        self.wl_basis_size = len(model.basis.bx)
        self.ph_basis_size = len(model.basis.by)

        # just in case
        self.corr = np.ones(len(lcdata.band_index))

    def __call__(self, pars, jac=False, debug_mode=False):
        """Evaluate the light curve.

        Parameters
        ----------
        jac : bool
            Whether it return the jacobian matrix
        debug_mode : bool
            if True, return the model components instead of the
            model results.

        Returns
        ----------
        val : numpy.array
            Model evaluation
        jacobian : scipy.sparse.csr_matrix, optional
            Jacobian matrix.

        """
        t0 = time.perf_counter()
        sn_index = self.sn_index
        zz = 1. + self.z
        model = self.model
        #       pars = self.model.pars

        M0 = pars['M0'].full.reshape(self.ph_basis_size, -1)
        M1 = pars['M1'].full.reshape(self.ph_basis_size, -1)
        # cl_pars = model.pars['CL'].full

        # data = self.lcdata.data
        # band_index = self.lcdata.band_index[0]

        # band_id = self.lcdata.data['band_id'][0]
        # print(self.model.bands[band_id], self.lcdata.data['Filter'][0])
        # lc_id = self.lcdata.data['lc_id'][0]
        # lc_index = self.lcdata.lc_index[0]
        sn_index = self.lcdata.sn_index[0]

        # sn-related parameters
        x0, x1 = pars['X0'].full[sn_index], pars['X1'].full[sn_index]
        c, tmax = pars['c'].full[sn_index],  pars['tmax'].full[sn_index]

        if 'eta_calib' in pars._struct.slices:
            calib_corr = 1. + pars['eta_calib'].full[self.lcdata.band_index]
        else:
            calib_corr = self.corr

        if 'kappa_color' in pars._struct.slices:
            cs_corr = 1. + pars['kappa'].full[self.lcdata.lc_index]
        else:
            cs_corr = self.corr
#        if model.calib_error_model is not None:
#            # eta = pars['eta_calib'].full[band_index]
#            calib_corr = model.calib_error_model.correction(lcdata=self.lcdata)
#        else:
#            calib_corr = np.ones(len(self.lcdata))
#        if model.color_scatter_model is not None:
#            # kappa = pars['kappa_color'].full[lc_index]
#            cs_corr = model.color_scatter_model.correction()
#        else:
#            cs_corr = 1.
        # model_to_meas_scale = self.lc_data.norm
        flux_scale = model.norm * self.lcdata.zp_scale

        phase_eval = model.phase_eval[self.lcdata.slc]
        # color law evaluation -- on the Gram \lambda_eff's
        cl = np.power(10., 0.4 * c * model.polynome_color_law.data)
        csr_color_law = scipy.sparse.csr_matrix((cl, (model.L_eff.row, model.L_eff.col)),
                                                shape=model.L_eff.shape)
        gram = model.gram.multiply(csr_color_law)
        tqz = self.tqz

        # much faster with the .dot's (instead of @)
        integral_surface_0 = phase_eval.dot(M0.dot(gram.dot(tqz)))
        integral_surface_1 = phase_eval.dot(M1.dot(gram.dot(tqz)))
        flux = flux_scale * zz * x0 * (integral_surface_0+x1*integral_surface_1) * calib_corr * cs_corr  # (1+eta)*(1+kappa)

        # if debug_mode:
        #     return model_norm * integral_surface_0, model_norm * integral_surface_1, \
        #            cl, flux, x0, x1, model_norm

        model.val.append(flux)
        if not jac:
            model.timing.append(time.perf_counter()-t0)
            return flux

        # n_data = len(self.lcdata)
        # sn_index = np.full(n_data, self.sn_index)
        # norm = self.model.norm

        # shortcut names to the internal cache holding the
        # jacobian matrix definition
        jacobian_i, jacobian_j, jacobian_val = model.jacobian_i, model.jacobian_j, model.jacobian_val

        # dMdX0
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(pars['X0'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(pars['X0'].indexof(self.lcdata.sn_index))
        jacobian_val.append(flux_scale * zz * (integral_surface_0 + x1*integral_surface_1) * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdX1
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(pars['X1'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(pars['X1'].indexof(self.lcdata.sn_index))
        jacobian_val.append(flux_scale * zz * x0 * integral_surface_1 * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdc
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(pars['c'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(pars['c'].indexof(self.lcdata.sn_index))
        gram_color_law = gram.multiply(model.polynome_color_law)
        dintegral0_dc = 0.4 * np.log(10.) * phase_eval.dot(M0.dot(gram_color_law.dot(tqz)))
        dintegral1_dc = 0.4 * np.log(10.) * phase_eval.dot(M1.dot(gram_color_law.dot(tqz)))
        jacobian_val.append(flux_scale * zz * x0 * (dintegral0_dc + x1*dintegral1_dc) * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdtmax
        dphase_dtmax = model.dphase_dtmax[self.lcdata.slc]
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(pars['tmax'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(pars['tmax'].indexof(self.lcdata.sn_index))
        dintegral0_dtmax = -dphase_dtmax.dot(M0.dot(gram.dot(tqz))) / zz
        dintegral1_dtmax = -dphase_dtmax.dot(M1.dot(gram.dot(tqz))) / zz
        jacobian_val.append(flux_scale * zz * x0 * (dintegral0_dtmax + x1*dintegral1_dtmax) * calib_corr * cs_corr)  # (1+eta)*(1+kappa))

        # dMdtheta_0
        dbase_dtheta = scipy.sparse.kron(phase_eval, gram.dot(tqz)).tocoo()
        jacobian_i.append(self.lcdata.row[dbase_dtheta.row])
        jacobian_j.append(pars['M0'].indexof(dbase_dtheta.col))
        assert len(self.lcdata.row[dbase_dtheta.row]) == len(pars['M0'].indexof(dbase_dtheta.col))
        jacobian_val.append(flux_scale[dbase_dtheta.row] * zz * x0 * dbase_dtheta.data * calib_corr[dbase_dtheta.row] * cs_corr[dbase_dtheta.row])  # (1+eta) * (1+kappa))

        # dMdtheta_1
        jacobian_i.append(self.lcdata.row[dbase_dtheta.row])
        jacobian_j.append(pars['M1'].indexof(dbase_dtheta.col))
        assert len(self.lcdata.row[dbase_dtheta.row]) == len(pars['M1'].indexof(dbase_dtheta.col))
        jacobian_val.append(flux_scale[dbase_dtheta.row] * zz * x0 * x1 * dbase_dtheta.data * calib_corr[dbase_dtheta.row] * cs_corr[dbase_dtheta.row])  # (1+eta) * (1+kappa))

        # dMdcl
        # I really don't know how to vectorize the computation
        # of these derivatives. If somebody has an idea let me know.
        buff = np.zeros(len(self.lcdata)).astype(int)
        for i, jacobian_color_law in enumerate(model.jacobian_color_law):
            buff[:] = i
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(pars['CL'].indexof(buff))
            gram_jacobian_color_law = gram.multiply(jacobian_color_law)
            jacobian_surface0_color_law = 0.4 * np.log(10.) * c * phase_eval.dot(M0.dot(
                gram_jacobian_color_law.dot(tqz)))
            jacobian_surface1_color_law = 0.4 * np.log(10.) * c * phase_eval.dot(M1.dot(
                gram_jacobian_color_law.dot(tqz)))
            jacobian_val.append(flux_scale * zz * x0 * (jacobian_surface0_color_law + x1*jacobian_surface1_color_law)
                                * calib_corr * cs_corr)  # * (1+eta) * (1+kappa))

        # dMdeta
        #        if model.calib_error_model is not None:
        if 'eta_calib' in pars._struct:
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(pars['eta_calib'].indexof(self.lcdata.band_index))
            jacobian_val.append(flux_scale * x0 * zz * (integral_surface_0 + x1*integral_surface_1) * cs_corr)  # *(1+kappa))

        # dKappa
        # if model.color_scatter_model is not None:
        if 'kappa_color' in pars._struct:
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(pars['kappa_color'].indexof(self.lcdata.band_index))
            jacobian_val.append(flux_scale * x0 * zz * (integral_surface_0 + x1*integral_surface_1) * calib_corr)  # (1+eta))

        if model.disable_cache:
            model.clear_cache()
        model.timing.append(time.perf_counter()-t0)
        return flux


class LightcurveEvalUnit:
    """An experimental eval unit for light curves

    Evaluates all light curves at once - should be faster
    """
    def __init__(self, model):
        """
        """
        self.model = model
        self.training_dataset = model.training_dataset
        self.gram = self.model.gram.todense()
        self.color_law = self.model.color_law

        nb_lightcurves = len(self.training_dataset.lc_db)
        filter_db_basis_size = len(model.filter_db.basis)
        F = np.zeros((nb_lightcurves, filter_db_basis_size))
        for lc in self.training_dataset.lc_db:
            tqz, _ = self.model.filter_db.insert(lc.band, z=lc.z)
            F[lc.lc_index, :] = tqz

        self.flux_scales = self.compute_flux_scales()
        self.flux_scales *= self.model.norm

        # filter projections
        self.filter_projections = (self.gram @ F.T).T
        self.meas_filter_projections = \
            self.filter_projections[self.training_dataset.lc_data.lc_index]


    def compute_flux_scales(self):
        """the training dataset contains fluxes and fluxerrs expressed in units defined by the observer. 
        The observer is supposed to give the connection between its unit system natural calibrated magnitudes 
        in some system (generally AB). 

        .. math::
           -2.5 \log_{10} 

        To predict these fluxes, the model values need to be multiplied by a scale, equal to:
          
        .. note::
           here, we assume that all mags are in the AB mag system. This may not be true.
        """
        zp_scale = self.training_dataset.lc_data.zp_scale
        
        # also insert the filter at z = 0, we need it
        # to compute integrals of AB spectrum
        bands = np.unique(self.training_dataset.lc_db.band)
        for b in bands:
            self.model.filter_db.insert(b, z=0.)

        ms = magsys.SNMagSys(self.model.filter_db)            
        int_AB_dict = dict(zip(bands, [10.**(0.4 * ms.get_zp(b.lower())) for b in bands]))
        int_AB = np.array([int_AB_dict[b] for b in self.training_dataset.lc_data.band])
        flux_scales = int_AB / zp_scale
        return flux_scales
        
    def __call__(self, pars, jac=False):
        """
        """
        lc_data = self.training_dataset.lc_data
        lc_db = self.training_dataset.lc_db

        wl_basis = self.model.basis.bx
        ph_basis = self.model.basis.by
        n_wl, n_ph = len(wl_basis), len(ph_basis)

        # pick matrix
        n_lc, n_meas = len(lc_db), len(lc_data)

        # phases
        zz = 1. + lc_data.z
        tmax = pars['tmax'].full[lc_data.sn_index]
        restframe_phases = (lc_data.mjd - tmax) / zz
        J_phase_sparse = ph_basis.eval(restframe_phases + self.model.delta_phase)
        J_phase = np.array(J_phase_sparse.todense())


        if 'eta_calib' in pars._struct.slices:
            calib_corr = 1. + pars['eta_calib'].full[lc_data.band_index]
        else:
            calib_corr = np.ones(len(lc_data.band_index))

        if 'kappa_color' in pars._struct.slices:
            cs_corr = 1. + pars['kappa'].full[lc_data.lc_index]
        else:
            cs_corr = np.ones(len(lc_data.lc_index))

        M0 = pars['M0'].full.reshape(n_ph, n_wl)
        M1 = pars['M1'].full.reshape(n_ph, n_wl)
        C0_ = np.array(M0.dot(self.meas_filter_projections.T))
        C0 = (J_phase * C0_.T).sum(axis=1)
        C1_ = np.array(M1.dot(self.meas_filter_projections.T))
        C1 = (J_phase * C1_.T).sum(axis=1)

        X0 = pars['X0'].full[lc_data.sn_index]
        X1 = pars['X1'].full[lc_data.sn_index]
        col = pars['c'].full[lc_data.sn_index]

        # color law - so here, we decide to move it out of the integral
        # maybe we need to add a small correction
        cl_pars = pars['CL'].full

        restframe_wavelength = lc_data.wavelength / zz
        cl_pol, J_cl_pol = self.color_law(restframe_wavelength,
                                          cl_pars, jac=jac)
        cl = np.power(10., 0.4 * col * cl_pol)

        pca = C0 + X1 * C1
        model_val = X0 * pca * cl * zz * calib_corr * cs_corr

        if not jac:
            v = np.zeros(len(self.training_dataset))
            v[lc_data.row] = self.flux_scales * model_val
            return v

        # jacobian
        N = len(self.training_dataset)
        n_free_pars = len(pars.free)

        # since the hstack is taking a lot of time and memory, we do things differently:
        # we allocate 3 large buffers for the jacobian i, j, vals, and we
        # update them in place.

        # estimated size of the derivatives
        logging.debug(' ... kron')
        K = kron_product_by_line(J_phase_sparse, self.meas_filter_projections)
        logging.debug(f'     -> done, K.nnz={K.nnz} nnz_real={(K.data != 0.).sum()} {len(K.row)}')
        estimated_size = 2 * K.nnz   # dMdM0 and dMdM1
        estimated_size += 6 * N      # local parameters (dMdX0, dMdX1, dMdcol, dMtmax, dMdeta, dMdkappa)
        nnz = len(J_cl_pol.nonzero()[0])
        estimated_size += nnz
        logging.debug(f'estimated size: {estimated_size}')

        buff = CooMatrixBuff2((N, n_free_pars)) # , estimated_size)
        self.K = K
        self.X0 = X0
        self.cl = cl
        self.calib_corr = calib_corr
        self.cs_corr = cs_corr
        self.zz = zz

        # we start with the largest derivatives: dMdM0 and dMdM1
        # dMdM0
        # we could write it as:
        # v_ = X0[K.row] * K.data * cl[K.row] * calib_corr[K.row] * cs_corr[K.row] * zz[K.row]
        # but it is slow. So, we re-arrange it as:
        i_ = lc_data.row[K.row]
        v_ = X0 * cl * calib_corr * cs_corr * zz
        # vv_, dd_ = v_[K.row], K.data
        # v_ = ne.evaluate('vv_ * dd_')
        v_ = v_[K.row] * K.data
        buff.append(i_,
                    pars['M0'].indexof(K.col),
                    v_)

        # dMdM1
        # X1_ = X1[K.row]
        buff.append(lc_data.row[K.row],
                    pars['M1'].indexof(K.col),
                    v_ * X1[K.row])

        del K
        del i_
        del v_

        # dMdtmax
        phase_basis = self.model.basis.by
        dJ = np.array(phase_basis.deriv(restframe_phases + self.model.delta_phase).todense())
        dC0 = (dJ * C0_.T).sum(axis=1)
        dC1 = (dJ * C1_.T).sum(axis=1)
        buff.append(lc_data.row,
                    pars['tmax'].indexof(lc_data.sn_index),
                    # ne.evaluate('-X0 * (dC0 + X1 * dC1) * cl * calib_corr * cs_corr'))
                    -X0 * (dC0 + X1 * dC1) * cl * calib_corr * cs_corr)

        del dJ
        del C0_
        del C1_

        # dMdcl
        JJ = scipy.sparse.coo_matrix(J_cl_pol)
        model_val_, col_, d_ = model_val[JJ.row], col[JJ.row], JJ.data
        buff.append(JJ.row,
                    pars['CL'].indexof(JJ.col),
                    # ne.evaluate('model_val_ * 0.4 * np.log(10.) * col_ * d_'))
                    # self.flux_scales[JJ.row] * model_val[JJ.row] * 0.4 * np.log(10.) * col[JJ.row] * JJ.data)
                    model_val[JJ.row] * 0.4 * np.log(10.) * col[JJ.row] * JJ.data)

        del JJ
        del model_val_
        del col_
        del d_

        # dMdX0
        buff.append(lc_data.row,
                    pars['X0'].indexof(lc_data.sn_index),
                    pca * cl * zz * calib_corr * cs_corr)

        # dMdX1
        buff.append(lc_data.row,
                    pars['X1'].indexof(lc_data.sn_index),
                    X0 * C1 * cl * zz * calib_corr * cs_corr)

        # dMdcol
        buff.append(
            lc_data.row,
            pars['c'].indexof(lc_data.sn_index),
            model_val * 0.4 * np.log(10.) * cl_pol)

        # dMdeta
        if 'eta_calib' in pars._struct:
            buff.append(lc_data.row,
                        pars['eta_calib'].indexof(lc_data.band_index),
                        X0 * pca * cl * zz * cs_corr)

        # dMkappa
        if 'kappa_color' in pars._struct:
            buff.append(lc_data.row,
                        pars['kappa_color'].indexof(lc_data.band_index),
                        X0 * pca * cl * zz * calib_corr)

        logging.debug(' -> tocoo()')
        J = buff.tocoo()
        del buff

        # multiply the data by the flux scales
        # to express fluxes in observer units
        J.data *= self.flux_scales[J.row]
        v = np.zeros(len(self.training_dataset))
        v[lc_data.row] = self.flux_scales * model_val

        return v, J

    def call_deprecated(self, pars, jac=False):
        """
        """
        lc_data = self.training_dataset.lc_data
        lc_db = self.training_dataset.lc_db

        wl_basis = self.model.basis.bx
        ph_basis = self.model.basis.by
        n_wl, n_ph = len(wl_basis), len(ph_basis)

        # pick matrix
        n_lc, n_meas = len(lc_db), len(lc_data)
        #        P = scipy.sparse.coo_matrix((np.ones(n_meas),
        #                                     (lc_data.row, lc_data.lc_index)),
        #                                    shape=(n_meas, n_lc)).tocsc()
        #        F = self.gram.dot(P.dot(self.filter_projections).T)

        # phases
        zz = 1. + lc_data.z
        tmax = pars['tmax'].full[lc_data.sn_index]
        restframe_phases = (lc_data.mjd - tmax) / zz
        J_phase_sparse = ph_basis.eval(restframe_phases + self.model.delta_phase)
        J_phase = np.array(J_phase_sparse.todense())


        if 'eta_calib' in pars._struct.slices:
            calib_corr = 1. + pars['eta_calib'].full[lc_data.band_index]
        else:
            calib_corr = np.ones(len(lc_data.band_index))

        if 'kappa_color' in pars._struct.slices:
            cs_corr = 1. + pars['kappa'].full[lc_data.lc_index]
        else:
            cs_corr = np.ones(len(lc_data.lc_index))

        M0 = pars['M0'].full.reshape(n_ph, n_wl)
        M1 = pars['M1'].full.reshape(n_ph, n_wl)
        C0_ = np.array(M0.dot(self.meas_filter_projections.T))
        C0 = (J_phase * C0_.T).sum(axis=1)
        C1_ = np.array(M1.dot(self.meas_filter_projections.T))
        C1 = (J_phase * C1_.T).sum(axis=1)

        X0 = pars['X0'].full[lc_data.sn_index]
        X1 = pars['X1'].full[lc_data.sn_index]
        col = pars['c'].full[lc_data.sn_index]

        # color law - so here, we decide to move it out of the integral
        # maybe we need to add a small correction
        cl_pars = pars['CL'].full

        restframe_wavelength = lc_data.wavelength / zz
        cl_pol, J_cl_pol = self.color_law(restframe_wavelength,
                                          cl_pars, jac=jac)
        cl = np.power(10., 0.4 * col * cl_pol)

        pca = C0 + X1 * C1
        model_val = X0 * pca * cl * zz * calib_corr * cs_corr

        if not jac:
            v = np.zeros(len(self.training_dataset))
            v[lc_data.row] = model_val
            return v


        # jacobian
        J_i, J_j, J_val = [], [], []

        N = len(self.training_dataset)
        n_free_pars = len(pars.free)
        jacobian = scipy.sparse.dok_matrix((N,n_free_pars)).tocsr()

        # dMdX0
        #        J_i.append(lc_data.row)
        #        J_j.append(pars['X0'].indexof(lc_data.sn_index))
        #        J_val.append(pca * cl * zz * calib_corr * cs_corr)
        i = lc_data.row
        j = pars['X0'].indexof(lc_data.sn_index)
        val = pca * cl * zz * calib_corr * cs_corr
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMdX1
        #        J_i.append(lc_data.row)
        #        J_j.append(pars['X1'].indexof(lc_data.sn_index))
        #        J_val.append(X0 * C1 * cl * zz * calib_corr * cs_corr)
        i = lc_data.row
        j = pars['X1'].indexof(lc_data.sn_index)
        val = X0 * C1 * cl * zz * calib_corr * cs_corr
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMdcol
        #        J_i.append(lc_data.row)
        #        J_j.append(pars['c'].indexof(lc_data.sn_index))
        #        J_val.append(model_val * 0.4 * np.log(10.) * cl_pol)
        i = lc_data.row
        j = pars['c'].indexof(lc_data.sn_index)
        val = model_val * 0.4 * np.log(10.) * cl_pol
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMdtmax
        phase_basis = self.model.basis.by
        dJ = np.array(phase_basis.deriv(restframe_phases + self.model.delta_phase).todense())
        # C0 = np.array(M0.dot(self.meas_filter_projections.T))
        dC0 = (dJ * C0_.T).sum(axis=1)
        # C1 = np.array(M0.dot(self.meas_filter_projections.T))
        dC1 = (dJ * C1_.T).sum(axis=1)
        #        J_i.append(lc_data.row)
        #        J_j.append(pars['tmax'].indexof(lc_data.sn_index))
        #        J_val.append(-X0 * (dC0 + X1 * dC1) * cl * calib_corr * cs_corr)
        i = lc_data.row
        j = pars['tmax'].indexof(lc_data.sn_index)
        val = -X0 * (dC0 + X1 * dC1) * cl * calib_corr * cs_corr
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMdM0
        # J = scipy.sparse.kron(J_phase_sparse, self.meas_filter_projections)
        # J = sparse_kron_along_cols(J_phase_sparse, self.meas_filter_projections)
        logging.debug(' ... kron')
        J = kron_product_by_line(J_phase_sparse, self.meas_filter_projections)
        logging.debug('     -> done')

        logging.debug(' ... dMdM0')
        #        J_i.append(lc_data.row[J.row])
        #        J_j.append(pars['M0'].indexof(J.col))
        #        J_val.append(X0[J.row] * J.data * cl[J.row] * calib_corr[J.row] * cs_corr[J.row] * zz[J.row])
        i = lc_data.row[J.row]
        j = pars['M0'].indexof(J.col)
        val = X0[J.row] * J.data * cl[J.row] * calib_corr[J.row] * cs_corr[J.row] * zz[J.row]
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)
        logging.debug('done')

        # dMdM1
        logging.debug(' ... dMdM1')
        #        J_i.append(lc_data.row[J.row])
        #        J_j.append(pars['M1'].indexof(J.col))
        #        J_val.append(X0[J.row] * X1[J.row] * J.data * cl[J.row] * calib_corr[J.row] * cs_corr[J.row] * zz[J.row])
        i = lc_data.row[J.row]
        j = pars['M1'].indexof(J.col)
        val = X0[J.row] * X1[J.row] * J.data * cl[J.row] * calib_corr[J.row] * cs_corr[J.row] * zz[J.row]
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)
        logging.debug('done')

        # saves some memory here
        del J

        # dMdcl
        logging.debug(' -> dMdcl')
        JJ = scipy.sparse.coo_matrix(J_cl_pol)
        # J_i.append(JJ.row)
        # J_j.append(pars['CL'].indexof(JJ.col))
        # J_val.append(model_val[JJ.row] * 0.4 * np.log(10.) * col[JJ.row] * JJ.data)
        i = JJ.row
        j = pars['CL'].indexof(JJ.col)
        val = model_val[JJ.row] * 0.4 * np.log(10.) * col[JJ.row] * JJ.data
        idx = j >= 0
        jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMdeta
        logging.debug(' -> dMdeta')
        if 'eta_calib' in pars._struct:
            #            J_i.append(lc_data.row)
            #            J_j.append(pars['eta_calib'].indexof(lc_data.band_index))
            #            J_val.append(X0 * pca * cl * zz * cs_corr)
            i = lc_data.row
            j = pars['eta_calib'].indexof(lc_data.band_index)
            val = X0 * pca * cl * zz * cs_corr
            idx = j >= 0
            jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # dMkappa
        logging.debug(' -> dMdkappa')
        if 'kappa_color' in pars._struct:
            #            J_i.append(lc_data.row)
            #            J_j.append(pars['kappa_color'].indexof(lc_data.band_index))
            #            J_val.append(X0 * pca * cl * zz * calib_corr)
            i = lc_data.row
            j = pars['kappa_color'].indexof(lc_data.band_index)
            val = X0 * pca * cl * zz * calib_corr
            idx = j >= 0
            jacobian += scipy.sparse.coo_matrix((val[idx], (i[idx], j[idx])), shape=jacobian.shape)

        # logging.info(' -> all together...')
        # J_i = np.hstack(J_i)
        # J_j = np.hstack(J_j)
        # J_val = np.hstack(J_val).astype(np.float32)
        # idx = J_j >= 0
        # N = len(self.training_dataset)
        # n_free_pars = len(pars.free)
        # JJ = scipy.sparse.coo_matrix((J_val[idx], (J_i[idx], J_j[idx])),
        #                              shape=(N, n_free_pars))

        v = np.zeros(len(self.training_dataset))
        v[lc_data.row] = model_val
        return v, jacobian


# def sparse_kron_along_cols(A, B):
#     """
#     """
#     A = A.tocsr()

#     m, n1 = A.shape
#     n2 = B.shape[1]
#     Cshape = (m, n1*n2)

#     data = []
#     col =  []
#     row =  []
#     ind2 = np.arange(n2)

#     for i in range(A.shape[0]):
#         slc1 = slice(A.indptr[i], A.indptr[i+1])
#         data1 = A.data[slc1]
#         ind1 = A.indices[slc1]
#         # slc2 = slice(B.indptr[i],B.indptr[i+1])
#         # data2 = B.data[slc2]; ind2 = B.indices[slc2]
#         data2 = np.array(B[i]).squeeze()
#         data.append(np.outer(data1, data2).ravel())
#         col.append(((ind1*n2)[:,None]+ind2).ravel())
#         row.append(np.full(len(data1) * len(data2), i))
#     data = np.concatenate(data)
#     col = np.concatenate(col)
#     row = np.concatenate(row)
#     return scipy.sparse.coo_matrix((data,(row,col)),shape=Cshape)



