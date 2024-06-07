"""The photometric part of the model

(light curve evaluation)
"""

import time
import numpy as np
import scipy




class LightcurveEvalUnitTz(object):
    """Compute an SN light curve of one supernova in one single band.

    This class is one of the two types of "computing unit". Given a set of
    dates, and the :math:`(X_0, X_1, c, t_{max})` parameters of the SN, compute
    the quantities:

    .. math::

         X_0 \times (1+z) \times \left[I_0 + X_1 I_1\right]

    with

    .. math::
         I_{0|1} = \int M_{0|1}(\lambda, \mathrm{p}) \frac{\lambda}{hc} T((1+z)\lambda) 10^{0.4\ c\ P(\lambda)} d\lambda

    In practice, we can speed up the computations by decomposing the filter on
    a spline basis: :math:`T(\lambda (1+z)) = \sum_q t_q(z) B_q(\lambda)=
    \sum_q (1+z) t_q B_q(\lambda)`, which allows to decompose the integral
    above as:

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

    where :math:`J`, :math:`G`,
    :math:`\Lambda^{\mathrm{eff}}` and :math:`t_z` are sparse
    and where :math:`G, \Lambda^{\mathrm{eff}}`
    can be precomputed once for all.

    Matrix :math:`G` is called the Gramian of the model and filter spline
    bases. It is precomputed exactly, using Gaussian quadrature when the model
    is instantiated.

    This strategy decompose :math:`T((1+z)\lambda)` and work with a single
    Gramian and an SN-dependant :math:`t_z` vector. This option is probably
    computationally less intensive, as we can factorize the evaluation of the
    color law.

    """

    def __init__(self, lcdata, model):
        """Constructor
        Retrieve the band shape :math:`T(\lambda)` and project :math:`T(\lambda(1+z))` on the basis

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
        self.band = lcdata.band[0]
        tr = model.filter_db.transmission_db[self.band]
        self.tqz, _ = model.filter_db.insert(tr, z=self.z)
        # set to zero very small values
        self.tqz[(np.abs(self.tqz)/self.tqz.max() < 1e-10)] = 0.

        # self.sn_id = lcdata.sn_id
        self.sn_index = lcdata.sn_index[0]

        #        self.wl_basis_size = len(model.basis.bx)
        self.ph_basis_size = len(model.basis.by)

        self.M0 = model.pars['M0'].full.reshape(self.ph_basis_size, -1)
        self.M1 = model.pars['M1'].full.reshape(self.ph_basis_size, -1)
        self.cl_pars = model.pars['CL'].full

    def __call__(self, jac=False, debug_mode=False):
        """
        Evaluate the SN light curve.

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
        jacobian : scipy.sparse.csr_matrix
            Jacobian matrix (optional)

        """
        t0 = time.perf_counter()
        sn_index = self.sn_index
        zz = 1. + self.z
        pars = self.model.pars
        # data = self.lcdata.data
        # band_index = self.lcdata.band_index[0]

        # band_id = self.lcdata.data['band_id'][0]
        # print(self.model.bands[band_id], self.lcdata.data['Filter'][0])
        # lc_id = self.lcdata.data['lc_id'][0]
        # lc_index = self.lcdata.lc_index[0]
        sn_index = self.lcdata.sn_index[0]

        # sn-related parameters
        x0, x1 = pars['X0'].full[sn_index], pars['X1'].full[sn_index]
        c, tmax = pars['col'].full[sn_index],  pars['tmax'].full[sn_index]
        if self.model.calib_error_model is not None:
            # eta = pars['eta_calib'].full[band_index]
            calib_corr = self.model.calib_error_model.correction(lcdata=self.lcdata)
        else:
            calib_corr = np.ones(len(self.lcdata))
        if self.model.color_scatter_model is not None:
            # kappa = pars['kappa_color'].full[lc_index]
            cs_corr = self.model.color_scatter_model.correction()
        else:
            cs_corr = 1.
        # model_to_meas_scale = self.lc_data.norm
        flux_scale = self.model.norm * self.lcdata.norm

        phase_eval = self.model.phase_eval[self.lcdata.slc]
        # color law evaluation -- on the Gram \lambda_eff's
        cl = np.power(10., 0.4 * c * self.model.polynome_color_law.data)
        csr_color_law = scipy.sparse.csr_matrix((cl, (self.model.L_eff.row, self.model.L_eff.col)),
                                                shape=self.model.L_eff.shape)
        gram = self.model.gram.multiply(csr_color_law)
        tqz = self.tqz

        # much faster with the .dot's (instead of @)
        integral_surface_0 = phase_eval.dot(self.M0.dot(gram.dot(tqz)))
        integral_surface_1 = phase_eval.dot(self.M1.dot(gram.dot(tqz)))
        flux = flux_scale * zz * x0 * (integral_surface_0+x1*integral_surface_1) * calib_corr * cs_corr  # (1+eta)*(1+kappa)

        # if debug_mode:
        #     return model_norm * integral_surface_0, model_norm * integral_surface_1, \
        #            cl, flux, x0, x1, model_norm

        self.model.val.append(flux)
        if not jac:
            self.model.timing.append(time.perf_counter()-t0)
            return flux

        # n_data = len(self.lcdata)
        # sn_index = np.full(n_data, self.sn_index)
        # norm = self.model.norm

        # shortcut names to the internal cache holding the
        # jacobian matrix definition
        jacobian_i, jacobian_j, jacobian_val = self.model.jacobian_i, self.model.jacobian_j, self.model.jacobian_val

        # dMdX0
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(self.model.pars['X0'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(self.model.pars['X0'].indexof(self.lcdata.sn_index))
        jacobian_val.append(flux_scale * zz * (integral_surface_0 + x1*integral_surface_1) * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdX1
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(self.model.pars['X1'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(self.model.pars['X1'].indexof(self.lcdata.sn_index))
        jacobian_val.append(flux_scale * zz * x0 * integral_surface_1 * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdc
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(self.model.pars['col'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(self.model.pars['col'].indexof(self.lcdata.sn_index))
        gram_color_law = gram.multiply(self.model.polynome_color_law)
        dintegral0_dc = 0.4 * np.log(10.) * phase_eval.dot(self.M0.dot(gram_color_law.dot(tqz)))
        dintegral1_dc = 0.4 * np.log(10.) * phase_eval.dot(self.M1.dot(gram_color_law.dot(tqz)))
        jacobian_val.append(flux_scale * zz * x0 * (dintegral0_dc + x1*dintegral1_dc) * calib_corr * cs_corr)  # (1+eta) * (1+kappa))

        # dMdtmax
        dphase_dtmax = self.model.dphase_dtmax[self.lcdata.slc]
        jacobian_i.append(self.lcdata.row)
        jacobian_j.append(self.model.pars['tmax'].indexof(self.lcdata.sn_index))
        assert len(self.lcdata.row) == len(self.model.pars['tmax'].indexof(self.lcdata.sn_index))
        dintegral0_dtmax = -dphase_dtmax.dot(self.M0.dot(gram.dot(tqz))) / zz
        dintegral1_dtmax = -dphase_dtmax.dot(self.M1.dot(gram.dot(tqz))) / zz
        jacobian_val.append(flux_scale * zz * x0 * (dintegral0_dtmax + x1*dintegral1_dtmax) * calib_corr * cs_corr)  # (1+eta)*(1+kappa))

        # dMdtheta_0
        dbase_dtheta = scipy.sparse.kron(phase_eval, gram.dot(tqz)).tocoo()
        jacobian_i.append(self.lcdata.row[dbase_dtheta.row])
        jacobian_j.append(self.model.pars['M0'].indexof(dbase_dtheta.col))
        assert len(self.lcdata.row[dbase_dtheta.row]) == len(self.model.pars['M0'].indexof(dbase_dtheta.col))
        jacobian_val.append(flux_scale[dbase_dtheta.row] * zz * x0 * dbase_dtheta.data * calib_corr[dbase_dtheta.row] * cs_corr)  # (1+eta) * (1+kappa))

        # dMdtheta_1
        jacobian_i.append(self.lcdata.row[dbase_dtheta.row])
        jacobian_j.append(self.model.pars['M1'].indexof(dbase_dtheta.col))
        assert len(self.lcdata.row[dbase_dtheta.row]) == len(self.model.pars['M1'].indexof(dbase_dtheta.col))
        jacobian_val.append(flux_scale[dbase_dtheta.row] * zz * x0 * x1 * dbase_dtheta.data * calib_corr[dbase_dtheta.row] * cs_corr)  # (1+eta) * (1+kappa))

        # dMdcl
        # I really don't know how to vectorize the computation
        # of these derivatives. If somebody has an idea let me know.
        buff = np.zeros(len(self.lcdata)).astype(int)
        for i, jacobian_color_law in enumerate(self.model.jacobian_color_law):
            buff[:] = i
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(self.model.pars['CL'].indexof(buff))
            gram_jacobian_color_law = gram.multiply(jacobian_color_law)
            jacobian_surface0_color_law = 0.4 * np.log(10.) * c * phase_eval.dot(self.M0.dot(
                gram_jacobian_color_law.dot(tqz)))
            jacobian_surface1_color_law = 0.4 * np.log(10.) * c * phase_eval.dot(self.M1.dot(
                gram_jacobian_color_law.dot(tqz)))
            jacobian_val.append(flux_scale * zz * x0 * (jacobian_surface0_color_law + x1*jacobian_surface1_color_law)
                                * calib_corr * cs_corr)  # * (1+eta) * (1+kappa))

        # dMdeta
        if self.model.calib_error_model is not None:
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(self.model.pars['eta_calib'].indexof(self.lcdata.band_index))
            jacobian_val.append(flux_scale * x0 * zz * (integral_surface_0 + x1*integral_surface_1) * cs_corr)  # *(1+kappa))

        # dKappa
        if self.model.color_scatter_model is not None:
            jacobian_i.append(self.lcdata.row)
            jacobian_j.append(self.model.pars['kappa_color'].indexof(self.lcdata.band_index))
            jacobian_val.append(flux_scale * x0 * zz * (integral_surface_0 + x1*integral_surface_1) * calib_corr)  # (1+eta))

        if self.model.disable_cache:
            self.model.clear_cache()
        self.model.timing.append(time.perf_counter()-t0)
        return flux
