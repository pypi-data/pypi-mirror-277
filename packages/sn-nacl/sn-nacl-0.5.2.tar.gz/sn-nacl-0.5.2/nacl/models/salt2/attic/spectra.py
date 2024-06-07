"""The spectral part of the model


TODO: remove color law evaluation from SpectrumEvalUnitFast
TODO: rename SpectrumEvalUnitFast
"""


import time
import numpy as np
import scipy


class SpectrumEvalUnitFast(object):
    """Evaluate the model for all SN spectra in the training dataset

    This class is one of the two type of "eval units". Given a chunk of the
    training dataset which corresponds the spectral observations, and given the
    :math:`(X_0, X_1, c, t_{max})` parameters of the SN, compute the quantity:

    .. math::

         \frac{1}{1+z} \left[M_0\left(\frac{\lambda}{1+z}, \mathrm{p}\right) + X_1\ M_1\left(\frac{\lambda}{1+z},
         \mathrm{p}\right) \right]\ 10^{0.4\ c\ P(\frac{\lambda}{1+z})}\ s(\lambda_{rec})

    where

    .. math::
        M_{0|1}(\lambda, \mathrm{p}) = \sum_{k\ell} \theta_{k\ell} B_k(\mathrm{p}) B_l(\mathrm{\lambda})

    and

    .. math::
         \mathrm{p} = \frac{t - t_{max}}{1+z}

    and where :math:`R_s(\lambda)` is a polynomial correction which
    absorbs the wavelength-dependent large scale calibration errors
    affecting the spectrum.

    Again, the evaluation reduces to a sparse matrix multiplication.
    """
    def __init__(self, tds, model):
        """Constructor.

        Parameters
        ----------
        tds : nacl.dataset.TrainingDataset
            Data set of photometric and spectroscopic observations.
        model : nacl.models.salt.SALT2Like
            Model.
        """
        self.training_dataset = tds
        self.data = tds.spec_data
        self.model = model

        self.spec_index = self.data.spec_index
        self.sn_index = self.data.sn_index
        # self.z = self.training_dataset.sn_data.z[self.sn_id]
        self.z = self.data.z

        # Look at that later
        self.color_law = model.color_law
        self.pars = model.pars
        self.basis = model.basis

        self.wl_basis_size = len(model.basis.bx)
        self.ph_basis_size = len(model.basis.by)

        # restframe wavelengths
        self.restframe_wl = self.data.wavelength/(1.+self.z)
        #        self.Jl = model.basis.bx.eval(self.restframe_wl).tocsr()

        # and we can connect directly to the global parameters
        self.M0 = model.pars['M0'].full
        self.M1 = model.pars['M1'].full
        self.cl_pars = model.pars['CL'].full

        # recalibration polynomial (one per spectrum, because we adapt to the spectrum wavelength range)
        #        self.recal_func = SpectrumRecalibrationPolynomials(self.training_dataset, self.model,
        #                                                           self.model.recalibration_degree)
        self.recal_func = self.model.recal_func

    def __call__(self, jac=False, debug_mode=False):
        r"""
        Evaluate the model for a all spectra

        Parameters
        ----------
        jac : bool
            if True compute and return the jacobian matrix
        debug_mode : bool
            if true, just return the model components.

        Returns
        -------
        val : numpy.array
            Model evaluations.
        jacobian : scipy.sparse.csr_matrix
            Jacobian matrix (if jac is true).
        """
        t0 = time.perf_counter()
        pars = self.pars

        # sn-related parameters
        x0, x1 = pars['X0'].full[self.sn_index], pars['X1'].full[self.sn_index]
        c, tmax = pars['col'].full[self.sn_index],  pars['tmax'].full[self.sn_index]

        # we need to re-evaluate the basis on the phases, since tmax changes
        restframe_phases = (self.data.mjd-tmax)/(1.+self.z)
        jacobian = self.basis.eval(self.restframe_wl, restframe_phases + self.model.delta_phase).tocsr()

        # model components
        component_0 = jacobian.dot(self.M0)
        component_1 = jacobian.dot(self.M1)
        polynome_color_law, jacobian_color_law = self.color_law(self.restframe_wl, self.cl_pars, jac=jac)
        color_law = np.power(10., 0.4*c*polynome_color_law)
        zz = 1. + self.z

        # recalibration polynomial
        # if we evaluate this, then recal_func must be instantiated
        # if self.recal_func is not None:
        assert self.recal_func is not None
        recal, jacobian_spec_rec = self.recal_func(jac=jac)
        if jacobian_spec_rec is not None:
            jacobian_spec_rec = jacobian_spec_rec.tocoo()
            # don't know what to do with this
            # jacobian_spec_rec.data *= recal[jacobian_spec_rec.row]

        # recal = np.exp(recal)
        pca = (component_0 + x1 * component_1)
        model = pca * color_law * recal / zz

        if debug_mode:
            return component_0, component_1, color_law, recal, model

        self.model.val.append(model)
        if not jac:
            self.model.timing.append(time.perf_counter()-t0)
            return model

        jacobian = jacobian.tocoo()
        # X0 does not appear in the spectral part of the model
        # hence, dmdX0 = 0

        # dMdX1
        jacobian_i, jacobian_j, jacobian_val = self.model.jacobian_i, self.model.jacobian_j, self.model.jacobian_val
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['X1'].indexof(self.sn_index))
        jacobian_val.append(component_1 * color_law * recal / zz)

        # dMdc
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['col'].indexof(self.sn_index))
        jacobian_val.append(model * 0.4 * np.log(10.) * polynome_color_law)

        # dMdtmax
        # we can gain a little here, by not evaluating the gradient along the wavelength (ddlambda)
        _, deval_phase = self.model.basis.gradient(self.restframe_wl, restframe_phases + self.model.delta_phase)
        deval_phase = deval_phase.tocsr()
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['tmax'].indexof(self.sn_index))
        jacobian_val.append(-1. * (deval_phase.dot(self.M0) + x1*deval_phase.dot(self.M1)) * color_law * recal / zz**2)

        # dmdtheta_0
        jacobian_i.append(self.data.row[jacobian.row])
        jacobian_j.append(self.model.pars['M0'].indexof(jacobian.col))
        jacobian_val.append(jacobian.data * color_law[jacobian.row] * recal[jacobian.row] / zz[jacobian.row])

        # dmdtheta_1
        jacobian_i.append(self.data.row[jacobian.row])
        jacobian_j.append(self.model.pars['M1'].indexof(jacobian.col))
        jacobian_val.append(x1[jacobian.row] * jacobian.data * color_law[jacobian.row] *
                            recal[jacobian.row] / zz[jacobian.row])

        # dMdcl (color law)
        jacobian_color_law = scipy.sparse.coo_matrix(jacobian_color_law)
        jacobian_i.append(self.data.row[jacobian_color_law.row])
        jacobian_j.append(self.model.pars['CL'].indexof(jacobian_color_law.col))
        jacobian_val.append(c[jacobian_color_law.row] * 0.4 * np.log(10.) * jacobian_color_law.data *
                            model[jacobian_color_law.row])

        # dMdr (recalibration)
        if jacobian_spec_rec is not None:
            jacobian_i.append(self.data.row[jacobian_spec_rec.row])
            jacobian_j.append(self.model.pars['SpectrumRecalibration'].indexof(jacobian_spec_rec.col))
            jacobian_val.append(jacobian_spec_rec.data * (pca*color_law)[jacobian_spec_rec.row]/zz[jacobian_spec_rec.row])

        if self.model.disable_cache:
            self.model.clear_cache()
        self.model.timing.append(time.perf_counter()-t0)

        return model


class SpectrumRecalibrationPolynomials:
    """A class to manage the spectrum recalibration polynomials

    The photometric calibration of spectra is generally affected by significant
    error modes at large wavelength scales. It is imperative to remove these
    error modes, while preserving the information provided by the spectra at
    small scales (spectral features)

    This is achieved during training by multiplying the spectral predictions of
    the model by a recalibration polynomial specific to each spectrum, function
    of the observation wavelength :math:`\lambda_o`, and of order :math:`N_s =
    3`, common to all spectra:

    .. math::
            s(\lambda_{rec}) = \sum_i^{N_s} s_i \lambda_{rec}^{N_s - i} %quad \mbox{and}
            \quad \lambda_{0} = \frac{\lambda - 5000}{9000 - 2700}

    with:

    .. math::
            \lambda_{rec} = \frac{2 (\lambda_o - \lambda_{max})}{\lambda_{max} - \lambda_{min}+1
    """

    def __init__(self, tds, model, pol_degrees):
        """Constructor

           Parameters
           ----------
            tds : nacl.dataset.TrainingDataset
                Data set of photometric and spectroscopic observations.
            model : nacl.model.salt
                Model.
            pol_degrees : int or indexable structure
                Polynomial degree for each spectrum.
            """
        self.tds = tds
        self.model = model
        self.pol_degrees = pol_degrees
        self.jacobian = None

        self.N = len(self.tds.spec_data)
        o = np.cumsum(np.hstack(([0], self.pol_degrees+1)))
        self.offset, self.n = o[:-1], o[-1]
        self.build_jacobian_matrix()

    def init_pars(self):
        """return a parameter vector initialized such that
            the recalibration polynomials are evaluated to 1
            for each spectra.

            Returns
            -------
            array
                Initiated parameters.
        """
        p = np.zeros(self.n)
        o = np.cumsum(self.pol_degrees+1) - 1
        p[o] = 1.
        return p

    def build_jacobian_matrix(self):
        """
            Create the jacobian matrix where line correspond to all spectral data point and
            the colones to parameters.
            """
        i, j, v = [], [], []

        # easier to write this with the spectra index
        for sp in self.tds.spectra:
            spec_index = sp.spec_index[0]
            lmin, lmax = sp.wavelength.min(), sp.wavelength.max()
            a = 2. / (lmax-lmin)
            b = 1 - 2. * lmax / (lmax-lmin)
            rwl = a * sp.wavelength + b
            deg = self.pol_degrees[spec_index]
            jacobian_spec_rec = scipy.sparse.coo_matrix(np.vander(rwl, deg+1))
            i.append(jacobian_spec_rec.row + sp.slc.start)
            j.append(jacobian_spec_rec.col + self.offset[spec_index])
            v.append(jacobian_spec_rec.data)
        i = np.hstack(i)
        j = np.hstack(j)
        v = np.hstack(v)
        self.jacobian = scipy.sparse.coo_matrix((v, (i, j)), shape=(self.N, self.n)).tocsr()

    def __call__(self, jac=False):
        """Evaluate the recalibration polynomials

        Parameters
        ----------
        jac : bool
          whether the jacobian is needed.

        Returns
        -------
        v : numpy.array
          Recalibration parameter evaluated.
        self.jacobian : None or scipy.sparse.coo_matrix
          Jacobian matrix of the recalibration polynomial functions.
        """
        p_full = self.model.pars['SpectrumRecalibration'].full
        v = self.jacobian.dot(p_full)
        if not jac:
            return v, None
        return v, self.jacobian


class SpectroPhotoEvalUnit(object):

    def __init__(self, tds, model):
        """Constructor.

        Parameters
        ----------
        tds : nacl.dataset.TrainingDataset
            Data set of photometric and spectroscopic observations.
        model : nacl.models.salt.SALT2Like
            Model.
        """
        self.training_dataset = tds
        self.data = tds.spectrophotometric_data
        self.model = model

        self.spec_index = self.data.spec_index
        self.sn_index = self.data.sn_index
        self.z = self.data.z

        # Look at that later
        self.color_law = model.color_law
        self.pars = model.pars
        self.basis = model.basis

        self.wl_basis_size = len(model.basis.bx)
        self.ph_basis_size = len(model.basis.by)

        # restframe wavelengths
        self.restframe_wl = self.data.wavelength/(1.+self.z)
        #        self.Jl = model.basis.bx.eval(self.restframe_wl).tocsr()

        # and we can connect directly to the global parameters
        self.M0 = model.pars['M0'].full
        self.M1 = model.pars['M1'].full
        self.cl_pars = model.pars['CL'].full

    def __call__(self, jac=False, debug_mode=False):
        r"""
        Evaluate the model for a all spectra

        Parameters
        ----------
        jac : bool
            if True compute and return the jacobian matrix
        debug_mode : bool
            if true, just return the model components.

        Returns
        -------
        val : numpy.array
            Model evaluations.
        jacobian : scipy.sparse.csr_matrix
            Jacobian matrix (if jac is true).
        """

        t0 = time.perf_counter()
        pars = self.pars

        # sn-related parameters
        x0, x1 = pars['X0'].full[self.sn_index], pars['X1'].full[self.sn_index]
        c, tmax = pars['col'].full[self.sn_index],  pars['tmax'].full[self.sn_index]
        # c, tmax = pars['col'].full[self.sn_index],  pars['tmax'].full[self.training_dataset.spectrophotometric_data.isn]

        # we need to re-evaluate the basis on the phases, since tmax changes
        restframe_phases = (self.data.mjd-tmax)/(1.+self.z)
        jacobian = self.basis.eval(self.restframe_wl, restframe_phases + self.model.delta_phase).tocsr()

        # norm
        norm = self.model.norm

        # model components
        component_0 = jacobian.dot(self.M0)
        component_1 = jacobian.dot(self.M1)

        polynome_color_law, jacobian_color_law = self.color_law(self.restframe_wl, self.cl_pars, jac=jac)
        color_law = np.power(10., 0.4*c*polynome_color_law)
        zz = 1. + self.z

        pca = (component_0 + x1 * component_1)
        model = x0 * norm * pca * color_law / zz

        self.model.val.append(model)
        if not jac:
            self.model.timing.append(time.perf_counter()-t0)
            return model

        jacobian = jacobian.tocoo()
        # jacobian_spec_rec = jacobian_spec_rec.tocoo()

        jacobian_i, jacobian_j, jacobian_val = self.model.jacobian_i, self.model.jacobian_j, self.model.jacobian_val
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['X0'].indexof(self.sn_index))
        # jacobian_val.append((component_0 + x1*component_1) * color_law * recal / zz)
        jacobian_val.append(norm * pca * color_law / zz)

        # dMdX1
        # jacobian_i, jacobian_j, jacobian_val = self.model.jacobian_i, self.model.jacobian_j, self.model.jacobian_val
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['X1'].indexof(self.sn_index))
        # jacobian_val.append(x0 * component_1 * color_law * recal / zz)
        jacobian_val.append(x0 * norm * component_1 * color_law / zz)

        # dMdc
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['col'].indexof(self.sn_index))
        jacobian_val.append(model * 0.4 * np.log(10.) * polynome_color_law)

        # dMdtmax
        # we can gain a little here, by not evaluating the gradient along the wavelength (ddlambda)
        _, deval_phase = self.model.basis.gradient(self.restframe_wl, restframe_phases + self.model.delta_phase)
        deval_phase = deval_phase.tocsr()
        jacobian_i.append(self.data.row)
        jacobian_j.append(self.model.pars['tmax'].indexof(self.sn_index))
        #jacobian_val.append(-1. *x0* (deval_phase.dot(self.M0) + x1*deval_phase.dot(self.M1)) * color_law * recal / zz**2)
        jacobian_val.append(-1. * x0 * norm * (deval_phase.dot(self.M0) + x1*deval_phase.dot(self.M1)) * color_law / zz**2)

        # dmdtheta_0
        jacobian_i.append(self.data.row[jacobian.row])
        jacobian_j.append(self.model.pars['M0'].indexof(jacobian.col))
        #jacobian_val.append(x0[jacobian.row] *jacobian.data * color_law[jacobian.row] * recal[jacobian.row] / zz[jacobian.row])
        jacobian_val.append(x0[jacobian.row] * norm * jacobian.data * color_law[jacobian.row] / zz[jacobian.row])

        # dmdtheta_1
        jacobian_i.append(self.data.row[jacobian.row])
        jacobian_j.append(self.model.pars['M1'].indexof(jacobian.col))
        #jacobian_val.append(x0[jacobian.row]*x1[jacobian.row] * jacobian.data * color_law[jacobian.row] *
        #                    recal[jacobian.row] / zz[jacobian.row])
        jacobian_val.append(x0[jacobian.row] * x1[jacobian.row] * norm *  jacobian.data * color_law[jacobian.row]/ zz[jacobian.row])

        # dMdcl (color law)
        jacobian_color_law = scipy.sparse.coo_matrix(jacobian_color_law)
        jacobian_i.append(self.data.row[jacobian_color_law.row])
        jacobian_j.append(self.model.pars['CL'].indexof(jacobian_color_law.col))
        jacobian_val.append(c[jacobian_color_law.row] * 0.4 * np.log(10.) * jacobian_color_law.data *
                            model[jacobian_color_law.row])

        if self.model.disable_cache:
            self.model.clear_cache()
        self.model.timing.append(time.perf_counter()-t0)


        return model

