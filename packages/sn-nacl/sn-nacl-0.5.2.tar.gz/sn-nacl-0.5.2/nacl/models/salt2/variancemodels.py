"""NaCl SALT2Like error models
"""

import logging

import numpy as np
from scipy import sparse

from bbf.bspline import BSpline, CardinalBSplineC, BSpline2D, lgram
from saltworks import FitParameters
from ...sparseutils import CooMatrixBuff2

try:
    from sksparse.cholmod import cholesky_AAt
except ImportError:
    from scikits.sparse.cholmod import cholesky_AAt


class SimpleErrorSnake:
    """A simplistic error snake : 1 parameter

    ..math ::
      V = g^2 model^2
    """
    def __init__(self, model):
        self.model = model

    def get_struct(self):
        return [("gamma", 1)]

    def init_pars(self, pars):
        pars['gamma'].full[:] = 0.01
        
    def __call__(self, pars, jac=False):
        v, J = None, None
        if jac:
            v, J = self.model(pars, jac=True)
        else:
            v = self.model(pars, jac=False)
        N = len(v)
        g = pars['gamma'].full[0]
        var = np.full(N, g**2 * v**2)

        if not jac:
            return var

        J = J.tocoo()

        n_free_pars = len(pars.free)
        i = [J.row]
        j = [J.col]
        data = [2. * g**2 * v[J.row] * J.data]
        i.append(np.arange(N))
        j.append(np.full(N, pars['gamma'].indexof(np.zeros(N).astype(int))))
        data.append(2. * g * v**2)

        i = np.hstack(i)
        j = np.hstack(j)
        data = np.hstack(data)

        idx = j >= 0
        J = sparse.coo_matrix((data[idx], (i[idx], j[idx])),
                              shape=(N, n_free_pars))

        return var, J


class LocalErrorSnake:
    """Error snake variance - as a function of phase and wavelength

    .. math::
    V(\lambda, p) = \sigma_{Err}^2 + \sigma_{\mathrm{Mod}}^2(\lambda,p)

    where :

    .. math::
        \sigma_{\mathrm{Mod}}^{spec} &= g(\lambda, p) \times \phi_{\mathrm{spec}}(p,\lambda)\ \ (\mathrm{spectra}) \\
        \sigma_{\mathrm{Mod}}^{phot} &= g(\lambda, p) \times \phi_{\mathrm{phot}}(p,\lambda)\ \ (\mathrm{photometric})

    :math:`\gamma(\lambda, p)` is a global surface describing the spectral
    residual of a 2D spline surface defined on the same ranges as the
    corresponding model.
    """
    def __init__(self, model, bins=(10, 10), order=4):
        """Constructor
        """
        self.model = model
        self.training_dataset = model.training_dataset

        # instantiate a basis
        ph_bins, wl_bins = bins
        phase_grid = np.linspace(model.basis.by.range[0], model.basis.by.range[-1], ph_bins)
        wl_grid = np.linspace(model.basis.bx.range[0], model.basis.bx.range[-1], wl_bins)
        self.basis = BSpline2D(wl_grid, phase_grid, x_order=order, y_order=order)

    def get_struct(self):
        """
        """
        return [('gamma', len(self.basis))]

    def init_pars(self, pars):
        """
        """
        pars['gamma'].full[:] = 0.01

    def __call__(self, pars, jac=False):
        """evaluate the variance model, and optionnaly, its derivatives
        """
        # too bad we need to call the model again here...
        # let's see whether we could cache this call
        if jac:
            flux, Jm = self.model(pars, jac=True)
        else:
            flux = self.model(pars, jac=False)
            Jm = None

        tds = self.training_dataset
        zz = tds.lc_data.z
        tmax = pars['tmax'].full[tds.lc_data.sn_index]
        wl = tds.lc_data.wavelength / (1. + zz)
        phase = (tds.lc_data.mjd - tmax) / (1. + zz)
        Jv = self.basis.eval(wl, phase)

        g = np.zeros(len(tds))
        g[:len(tds.lc_data)] = np.exp(Jv @ pars['gamma'].full)
        v = g * flux**2
        if not jac:
            return v

        # derivatives
        N = len(tds)
        n_free_pars = len(pars.free)
        buff = CooMatrixBuff2((N, n_free_pars))

        # d_gamma
        buff.append(Jv.row,
                    pars['gamma'].indexof(Jv.col),
                    g[Jv.row] * Jv.data * flux[Jv.row]**2)

        # d_dpars
        buff.append(Jm.row,
                    Jm.col,
                    2. * g[Jm.row] * flux[Jm.row] * Jm.data)

        J = buff.tocoo()

        return v, J



class SNLambdaErrorSnake:

    def __init__(self, model, deg=3):
        self.model = model
        self.training_dataset = self.model.training_dataset
        self.deg = deg
        
        #pre construction of the vandermonde matrix
        lc_data = self.training_dataset.lc_data
        restframe_wl = lc_data.wavelength / (1. + lc_data.z)
        r_wl = np.zeros(len(self.training_dataset))
        r_wl[:len(lc_data)] = restframe_wl
        self.vander_matrix = self.get_vander_matrix(r_wl)

    def get_struct(self):
        nsn = len(self.training_dataset.sn_data.sn_set)
        npars = self.deg # deg + 1 - 1 constraint
        return [('gamma_sn', nsn), ('gamma_snake', npars)]

    def init_pars(self, pars):
        pars['gamma_sn'].full[:] = 0.01
        pars['gamma_snake'].full[:] = 0.

    def _reduce(self, restframe_wl):
        return (restframe_wl-4500.) / (9000. - 2000.)
    
    def get_vander_matrix(self, restframe_wl):
        reduced_wl = self._reduce(restframe_wl)
        vander_mat = np.vander(reduced_wl, self.deg, increasing = False)
        return vander_mat
    
    def __call__(self, pars, jac=False):
        if jac:
            flux, Jm = self.model(pars, jac=True)
        else:
            flux = self.model(pars, jac=False)
            Jm = None

        tds = self.training_dataset
        zz = tds.lc_data.z
        restframe_wl = tds.lc_data.wavelength / (1. + zz)
        reduced_wl = self._reduce(restframe_wl)
        snake = np.zeros(len(tds))
        snake[:len(tds.lc_data)] = np.exp(np.polyval(pars['gamma_snake'].full, reduced_wl))

        g = np.zeros(len(tds))
        g[:len(tds.lc_data)] = pars['gamma_sn'].full[tds.lc_data.sn_index]
        variance = g**2 * snake * flux**2
        
        if not jac:
            return variance
        
        # derivatives
        N = len(tds)
        n_free_pars = len(pars.free)
        buff = CooMatrixBuff2((N, n_free_pars))
        
        # d_gamma = 2 * snake * g_i * flux**2
        buff.append(tds.lc_data.row,
                    pars['gamma_sn'].indexof(tds.lc_data.sn_index),
                    2 * snake[tds.lc_data.row] * g[tds.lc_data.row] * flux[tds.lc_data.row]**2)
        
        # d_snake = g**2 * flux**2 * reduced_wl ** i * snake
        data_d_snake = sparse.coo_matrix(variance[:,np.newaxis] * self.vander_matrix[:,0:self.deg-1])
        row_d_snake = data_d_snake.row
        col_d_snake = pars['gamma_snake'].indexof(data_d_snake.col)
        buff.append(row_d_snake,
                    col_d_snake,
                    data_d_snake.data)
        
        # d_pars = 2 * snake * g**2 + flux * Jm
        buff.append(Jm.row,
                    Jm.col,
                    2. * g[Jm.row]**2 * snake[Jm.row] * flux[Jm.row] * Jm.data)

        J = buff.tocoo()

        return variance, J


class SNLocalErrorSnake:
    """Error snake variance - as a function of phase and wavelength

    .. math::
    V(\lambda, p) = \sigma_{Err}^2 + \sigma_{\mathrm{Mod}}^2(\lambda,p) \times \sigma_{\mahtrm{SN}}

    where :

    .. math::
        \sigma_{\mathrm{Mod}}^{spec} &= g(\lambda, p) \times \gamma_{\mahtrm{SN}} \times \phi_{\mathrm{spec}}(p,\lambda)\ \ (\mathrm{spectra}) \\
        \sigma_{\mathrm{Mod}}^{phot} &= g(\lambda, p) \times \gamma_{\mahtrm{SN}} \times \phi_{\mathrm{phot}}(p,\lambda)\ \ (\mathrm{photometric})

    :math:`\gamma(\lambda, p)` is a global surface describing the spectral
    residual of a 2D spline surface defined on the same ranges as the
    corresponding model.
    :math:`\gamma_{\mahtrm{SN}}` is a de-weighting factor for each SN to capture
    SN variability
    """
    def __init__(self, model, bins=(10, 10), order=4):
        """Constructor
        """
        self.model = model
        self.training_dataset = model.training_dataset

        # instantiate a basis
        ph_bins, wl_bins = bins
        phase_grid = np.linspace(model.basis.by.range[0], model.basis.by.range[-1], ph_bins)
        wl_grid = np.linspace(model.basis.bx.range[0], model.basis.bx.range[-1], wl_bins)
        self.basis = BSpline2D(wl_grid, phase_grid, x_order=order, y_order=order)

    def get_struct(self):
        """
        """
        nsn = len(self.training_dataset.sn_data.sn_set)
        return [('gamma_snake', len(self.basis)), ('gamma_sn', nsn)]

    def init_pars(self, pars):
        """
        """
        pars['gamma_sn'].full[:] = 0.01
        pars['gamma_snake'].full[:] = 0.01

    def __call__(self, pars, jac=False):
        """evaluate the variance model, and optionnaly, its derivatives
        """
        if jac:
            flux, Jm = self.model(pars, jac=True)
        else:
            flux = self.model(pars, jac=False)
            Jm = None

        tds = self.training_dataset
        zz = tds.lc_data.z
        tmax = pars['tmax'].full[tds.lc_data.sn_index]
        wl = tds.lc_data.wavelength / (1. + zz)
        phase = (tds.lc_data.mjd - tmax) / (1. + zz)
        Jv = self.basis.eval(wl, phase)
        
        # fixing phase edges parameters
        njx = self.basis.bx.nj
        nj = self.basis.nj
        cols_to_keep = np.arange(0, nj-njx-1, 1)
        
        #cols_full = np.arange(0, nj, 1)
        #b = np.array([0, njy -1])
        #c = np.arange(0, njy, 1)
        #a = c*njy
        #x = [b+i for i in a]
        #x = np.hstack(x)
        #cols_remove = np.isin(cols_full, x)
        #cols_to_keep = ~cols_remove
        
        mask = np.isin(Jv.col, cols_to_keep)
        
        filtered_data = Jv.data[mask]
        filtered_row = Jv.row[mask]
        filtered_col = Jv.col[mask]
        
        col_map = {old_col:new_col for new_col, old_col in enumerate(cols_to_keep)}
        filtered_col = np.array([ col_map[c] for c in filtered_col ])
        new_shape = (Jv.shape[0], len(cols_to_keep))
        Jv = sparse.coo_matrix( (filtered_data, (filtered_row, filtered_col)), shape=new_shape)
        
        #
        g_snake = np.zeros(len(tds))
        g_snake[:len(tds.lc_data)] = np.exp(Jv @ pars['gamma_snake'].full[:-njx-1])
        
        g_sn = np.zeros(len(tds))
        g_sn[:len(tds.lc_data)] = pars['gamma_sn'].full[tds.lc_data.sn_index]
        
        v = g_snake * g_sn**2 * flux**2
        if not jac:
            return v

        # derivatives
        N = len(tds)
        n_free_pars = len(pars.free)
        buff = CooMatrixBuff2((N, n_free_pars))

        # d_gamma_snake
        buff.append(Jv.row,
                    pars['gamma_snake'].indexof(Jv.col),
                    g_snake[Jv.row] * Jv.data * g_sn[Jv.row]**2 * flux[Jv.row]**2)
        
        # d_gamma_sn
        buff.append(tds.lc_data.row,
                    pars['gamma_sn'].indexof(tds.lc_data.sn_index),
                    2 * g_sn[tds.lc_data.row] * g_snake[tds.lc_data.row] * flux[tds.lc_data.row]**2)
        
        # d_dpars
        buff.append(Jm.row,
                    Jm.col,
                    2. * g_snake[Jm.row] * g_sn[Jm.row]**2 * flux[Jm.row] * Jm.data)

        J = buff.tocoo()

        return v, J


class SimpleErrorSnake_:
    """Simple, 1 parameter error snake: :math:`\\sigma_f = \\sigma_m \\times f`

    This is the simplest error snake possible. We add a pedestal variance,
    constant in magnitude (i.e. of the form :math:`\\sigma_m \times flux` in
    flux).
    """

    def __init__(self, model):  # , var_pedestal=0.001):
        self.model = model
        self.training_dataset = self.model.training_dataset
        # self.var_pedestal = var_pedestal

    def get_struct(self):
        """
        """
        return [('sigma_snake', 1)]

    def __call__(self, pars, jac=False, model_flux=None, model_jac=None):
        """return the diagonal of the error snake variance + derivatives
        """
        mflux, mjac = None, None
        # if parameters are given, we need to re-evaluate the model
        if p is not None:
            if not jac:
                mflux = self.model(p)
            else:
                mflux, mjac = self.model(p, jac=True)
        # otherwise, we re-evaluate it only if it is necessary
        else:
            if not jac:
                mflux = model_flux if model_flux is not None else self.model(self.model.pars.free)
            else:
                if model_flux is not None and model_jac is not None:
                    mflux, mjac = model_flux, model_jac
                else:
                    mflux, mjac = self.model(self.model.pars.free, jac=True)

        # model parameters
        pars = self.model.pars
        sigma_m = self.model.pars['sigma_snake'].full[0]

        # evaluate the variance
        var = (sigma_m * mflux)**2

        # we should only apply it to the photometric measurements
        # nlc, _, _ = self.model.training_dataset.n

        # and return it if this is the only thing requested
        if not jac:
            return var

        # derivatives
        n = len(self.model.pars.full)
        n_free = len(self.model.pars.free)
        N = self.training_dataset.nb_meas(valid_only=False)

        # dV / dsigma_snake
        i = np.arange(N).astype(int)
        j = np.full(N, pars['sigma_snake'].indexof())
        dVds = 2. * sigma_m * mflux**2
        idx = j>=0
        J_dVds = sparse.coo_matrix((dVds[idx], (i[idx],j[idx])), shape=(N,n_free))

        # dV/dbeta
        # mjac.data *= (2. * sigma_m**2 * mflux[mjac.row])
        J_dVdbeta = sparse.coo_matrix((mjac.data * 2. * sigma_m**2 * mflux[mjac.row],
                                (mjac.row, mjac.col)),
                                shape=mjac.shape)

        # i = np.hstack((i, mjac.row))
        # j = np.hstack((j, mjac.col))
        # v = np.hstack((dVds, mjac.data))
        # idx = j>=0
        # J = coo_matrix((v[idx], (i[idx],j[idx])), shape=(N, n_free))
        # J = J_dVds.tocsc() + J_dVdbeta.tocsc()
        J = J_dVds.tocoo() + J_dVdbeta.tocoo()

        return var, J

    def noise(self, p=None, **kwargs):
        """draw one realization of the error snake noise
        """
        var = self(p, jac=False, **kwargs)
        nlc, nsp, nphotspec = self.training_dataset.nb_meas(valid_only=False,
                                                            split_by_type=True)
        N = nlc + nsp + nphotspec
        n = np.zeros(N)
        # this error snake only applies to the photometric dataset
        n[:nlc] = np.random.normal(loc=0., scale=np.sqrt(var[:nlc]))
        return n


class CalibErrorModel:

    def __init__(self, model, calib_variance, 
                 default_calib_variance=0.5**2):
        """Constructor

        Parameters
        ----------
        model : a NaCl model (e.g. SALT2Like)
            the underlying model
        calib_variance : float or pandas.DataFrame
            the calibration covariance matrix. It is either a float, if all
            bands have the same calibration variance (uncorrelated), or if all
            calibration uncertainties are uncorrelated, the diagonal of the
            covariance matrix, or the full covariance matrix.
        """
        self.model = model
        self.training_dataset = self.model.training_dataset
        self.calib_variance = calib_variance
        self.default_calib_variance = default_calib_variance
        self.inv_full_covmat = None
        self.sub_covmat = None

    # def finalize(self):
    #     """
    #     """
    #     self.build_covmat(calib_variance=self.calib_variance,
    #                       default_calib_variance=self.default_calib_variance)

    def get_struct(self):
        nb_bands = self.training_dataset.nb_bands()
        return [('eta_calib', nb_bands)]

    def init_pars(self, pars):
        pass

    def build_covmat(self, pars,
                     calib_variance, bands=None,
                     default_calib_variance=0.5):
        """build a covmat (ordered to match the lc_data.band_index)

        Returns
        -------
        np.ndarray
            the re-ordered covmat
        """
        npars = len(pars.full)
        pfull = pars.copy()
        pfull.release()

        sz = len(pfull['eta_calib'].full)

        # if all bands have the same variance, that's easy
        if isinstance(calib_variance, float):
            nb_bands = self.training_dataset.nb_bands()
            i = pfull['eta_calib'].indexof()
            v = np.full(sz, 1./self.calib_variance)
            self.sub_covmat = np.diag(np.full(nb_bands, calib_variance))
            self.inv_full_covmat = sparse.coo_matrix((v, (i, i)), shape=(npars, npars))

        # otherwise, we may get a dict of the form {<band_name>: var, ...}
        # in which case it is also easy
        elif isinstance(calib_variance, dict):
            tds = self.model.training_dataset
            diag = []
            for bn in tds.lc_data.band_set:
                if bn not in calib_variance:
                    logging.warning(f'no calibration variance specified for band: {bn} -- will assign {default_calib_variance} by default')
                diag.append(calib_variance.get(bn, default_calib_variance))
            diag = np.array(diag)
            assert np.all(diag)
            i = pfull['eta_calib'].indexof()
            self.sub_covmat = np.diag(diag)
            self.inv_full_covmat = sparse.coo_matrix((1./diag, (i,i)), shape=(npars, npars))

        # finally, we may get a real matrix, along with a dict that
        # specifies the indices to band mapping. Then, all we have
        # to do, is to make sure all the bands are here, fill out the blank
        # if necessary, and re-order it if necessary
        elif isinstance(calib_variance, tuple):
            covmat, bands  = calib_variance
            # extend band into a simple map
            band_map = dict([(y,x) for x,y in enumerate(bands)])

            # extend calib covmat with a defaut value
            nr,nc = covmat.shape
            assert nr == nc
            extended_covmat = np.zeros((nr+1,nc+1))
            extended_covmat[:nr,:nc] = covmat
            extended_covmat[nr,nr] = default_calib_variance
            #            print('extended_covmat: ', extended_covmat)
            # re-order covmat
            i = []
            for bn in self.model.training_dataset.lc_data.band_set:
                if bn not in bands:
                    logging.warning('no calibration variance specified for band: {bn} -- will assign {default_calib_variance} by default')
                    i.append(nr)
                else:
                    i.append(band_map[bn])
            ii,jj = np.meshgrid(i,i)
            reordered_covmat = extended_covmat[ii,jj]

            # invert the covmat 
            w = np.linalg.inv(reordered_covmat)

            # and re-index it into a larger (n,n) matrix, where n = number of parameters
            nn, _ = w.shape
            ii, jj = np.mgrid[:nn,:nn]
            self.sub_covmat = reordered_covmat
            self.inv_full_covmat = sparse.coo_matrix((w.flatten(),
                                               (pfull['eta_calib'].indexof(ii.flatten()), 
                                                pfull['eta_calib'].indexof(jj.flatten()))), 
                                              shape=(npars, npars))
        else:
            raise ValueError(f"build_covmat(): don't know what to do with {calib_variance}")

        # # otherwise, if a matrix is passed, we may need to re-order
        # # the calibration matrix, so that it matches the band_index
        # if isinstance(calib_variance, np.matrix):
        #     C = coo_matrix(calib_variance)
        #     assert (len(C.shape) == 2) and (C.shape[0] == C.shape[1])

        # if isinstance(self.calib_variance, float):
        #     n_bands = self.training_dataset.nb_bands()
        #     return np.diag(np.full(n_bands, self.calib_variance))

        # if isinstance(self.calib_variance, pandas.DataFrame) and self.calib_variance.shape[0] == 1:
        #     diag = self.calib_variance[self.lc_data.band_set].flatten()
        #     return np.diag(diag)

        # if isinstance(self.calib_variance, pandas.DataFrame):
        #     bs = self.lc_data.band_set
        #     covmat = self.calib_variance[bs].loc[bs].to_numpy()
        #     return covmat

    def __call__(self, pars, deriv=False):
        """evaluate the calib prior (and optionally its gradient and Hessian)
        """
        #        if p is not None:
        #            self.model.pars.free = p

        if self.sub_covmat is None or self.inv_full_covmat is None:
            self.build_covmat(pars, self.calib_variance)

        pfull = pars.full
        prior = np.dot(pfull, (self.inv_full_covmat.dot(pfull)))
        if not deriv:
            return prior

        # TODO: add some sanity and change the sign in the LogLikelihood
        # so that can return grad and not -grad ...
        # TODO: I am here ! -> reduce size, depending on fixed parameters
        grad = -2. * self.inv_full_covmat.dot(pfull)
        hess = +2. * self.inv_full_covmat

        return prior, grad, hess

    def correction(self, pars, lcdata=None):
        """the multiplicative correction to apply to the photometric data

        Parameters
        ----------
        p: (ndarray), optional
          vector of free parameters
        lcdata: stff, optional
          something that has a band_index

        Returns:
          a ndarray with the corrections
        """
#        if p is not None:
#            self.model.pars.free = p
        if lcdata is None:
            lcdata = self.training_dataset.lc_data
        corr = 1. + pars['eta_calib'].full[lcdata.band_index]
        return corr

    def noise(self, pars):
        """the noise component, to apply to the photometric data
        """
        # if p is not None:
        #     self.model.pars.free = p

        lc_data = self.training_dataset.lc_data

        nphot, nsp, nspphot = self.training_dataset.nb_meas(valid_only=False,
                                                            split_by_type=True)
        scales = np.ones(nphot + nsp + nspphot)
        nb_bands = self.training_dataset.nb_bands()

        # covmat = self.build_covmat()
        L = np.linalg.cholesky(self.sub_covmat)
        dm = L @ np.random.normal(0., scale=1., size=nb_bands)
        # dm = [dm[self.band_map[i]] for i in range(len(self.bands))]
        scales[:nphot] = 1. + dm[lc_data.band_index]
        return scales # 1.+ dm[lc_data.band_index]


class ColorScatterModel:
    """An adaptation of the color scatter model developed by Guy Augarde
    """
    U_WAVELENGTH = 3650.88
    B_WAVELENGTH = 4302.57
    V_WAVELENGTH = 5428.55
    R_WAVELENGTH = 6418.01
    I_WAVELENGTH = 7968.34
    WAVELENGTH = {"U": U_WAVELENGTH, "B": B_WAVELENGTH, "V": V_WAVELENGTH,
                  "R": R_WAVELENGTH, "I": I_WAVELENGTH}

    def __init__(self, model):
        """Constructor
        """
        self.model = model
        self.training_dataset = model.training_dataset
        lc_data = self.training_dataset.lc_data
        restframe_wl = lc_data.wavelength / (1. + lc_data.z)
        self.reduced_restframe_wl = self.model.reduce(restframe_wl)

    def get_struct(self):
        """
        """
        nb_lightcurves = self.training_dataset.nb_lcs()
        return [('sigma_kappa', 3),
                ('kappa_color', nb_lightcurves)]

    def __call__(self, p=None, deriv=False):
        """return the color scatter prior, and (optionaly) its grad and hessian
        """
        pass

    def correction(self, pars):
        """return the multiplicative correction to be applied to the model
        """
        # if p is not None:
        #    self.model.pars.free = p
        tds = self.training_dataset
        corr = 1. + pars['kappa_color'].full[tds.lc_data.lc_index]
        return corr

    def noise(self, pars):
        """generate one realization of the noise -- to add directly to the data
        """
        # if p is not None:
        #     self.model.pars.free = p
        var = self.__call__(pars, jac=False)
        nn = np.random.normal(scale=np.sqrt(var), size=len(var))
        return 1. * nn[self.training_dataset.lc_data.lc_index]


class ColorScatter:
    r"""color scatter model

    To model the residual variability of the SNe color not described by the
    model, we allow the relative amplitude of each light curve to vary by a
    quantity :math:`(1+kappa)`:

    .. math::
        \phi_{phot}(p_0) = X_0 (1+z) (1+kappa) \int S(\lambda, p) T\left( \lambda \right) \frac{\lambda}{hc} d\lambda

    where :math:`\kappa` is an additional parameter, depending on the SN and the
    observation band.

    The variability of :math:`\kappa` is defined by a Gaussian prior, whose
    variance is a function of the wavelength restframe, and must be determined
    during the adjustment. In our model, this term is implemented by a
    polynomial of the wavelength restframe of the SN. For a light curve observed
    in a band :math:`X`, of average wavelength :math:`\lambda^X`, the
    corresponding variance is:

    .. math::
        \sigma_\kappa^2 = P\left(\frac{\lambda^X}{1+z}\right)

    where :math:`z` is redshift of the supernova and :math:`P` is a polynomial
    of the wavelength restframe. In practice, :math:`P` is implemented in terms
    of a reduced restframe wavelength: :math:`\lambda_{r}`

    Attributes
    ----------
    WL_REDUCED : numpy.array
        Reduced SN-restframe mean wavelength
    pars : nacl.lib.fitparameters.FitParameters
        Color scatter parameters
    """
    U_WAVELENGTH = 3650.88
    B_WAVELENGTH = 4302.57
    V_WAVELENGTH = 5428.55
    R_WAVELENGTH = 6418.01
    I_WAVELENGTH = 7968.34
    WAVELENGTH = {"U": U_WAVELENGTH, "B": B_WAVELENGTH, "V": V_WAVELENGTH,
                  "R": R_WAVELENGTH, "I": I_WAVELENGTH}

    def __init__(self, model): # wavelength_rest_reduced, sigma_kappa):
        """Constructor

        Parameters
        ----------
        wavelength_rest_reduced :
            Reduced SN-restframe mean wavelength
        sigma_kappa : numpy.array
            Color scatter parameter initialisation.
        """
        self.model = model
        self.training_dataset = model.training_dataset
        lc_data = self.training_dataset.lc_data
        restframe_wl = lc_data.wavelength / (1. + lc_data.z)
        self.reduced_restframe_wl = self.model.reduce(restframe_wl)

        # self.WL_REDUCED = wavelength_rest_reduced
        # self.pars = self.init_pars(sigma_kappa)

    def get_struct(self):
        """
        """
        nb_lightcurves = self.training_dataset.nb_lcs()
        return [('sigma_kappa', 3),
                ('kappa_color', nb_lightcurves)]

    # def init_pars(self):
    #     fp = FitParameters(self.get_struct())

    # @staticmethod
    # def init_pars(sigma_kappa):
    #     """initialize a parameter vector

    #     Parameters
    #     ----------
    #     sigma_kappa : numpy.array
    #         Color scatter parameter initialisation.

    #     Returns
    #     -------
    #     pars : nacl.lib.fitparameters.FitParameters
    #         Color scatter parameter.
    #     """
    #     pars = FitParameters([('sigma_kappa', len(sigma_kappa))])
    #     pars['sigma_kappa'] = sigma_kappa
    #     return pars

    def __call__(self, pars, jac=False):
        """Return the color scatter variance (the :math:`V_\kappa` matrix)

        Parameters
        ----------
        p : np.ndarray
          free parameter vector

        Returns
        -------
        val : numpy.ndarray
            the diagonal of the color scatter variance matrix (used in the kappa prior)
        if jac:
            jacobian of the color scatter.
        """
        # if p is not None:
        #     self.model.pars.free = p
        sigma_kappa = pars['sigma_kappa'].full
        val = np.polyval(sigma_kappa, self.reduced_restframe_wl)  # * self.WL_REDUCED

        if jac:
            vander = (np.vander(self.reduced_restframe_wl, len(sigma_kappa)).T )  # * self.WL_REDUCED)
            jj = (vander * val * 2).T
            return val, jj  # coo_matrix(jj)
        return val

    def correction(self, pars):
        """return the multiplicative correction to be applied to the model
        """
        # if p is not None:
        #     self.model.pars.free = p
        corr = 1. + pars['kappa_color'].full[self.training_dataset.lc_data.lc_index]
        return corr

    def noise(self, pars):
        """generate one realization of the noise -- to add directly to the data
        """
        # if p is not None:
        #     self.model.pars.free = p
        var = self.__call__(pars, jac=False)
        nn = np.random.normal(scale=np.sqrt(var), size=len(var))
        return nn[self.training_dataset.lc_data.lc_index]



class SimpleVarianceModel:
    """Error snake variance

    The error snake variance describes the excess of variance observed in the
    training residuals, that arise from the fact that the model is not able to
    entirely capture the SN-to-SN variability.

    In NaCl, this component incorporated in the fit, and determined along with
    the model itself.

    .. math::
    V(\lambda, p) = \sigma_{Err}^2 + \sigma_{\mathrm{Mod}}^2(\lambda,p)

    where :

    .. math::
        \sigma_{\mathrm{Mod}}^{spec} &= g(\lambda, p) \times \phi_{\mathrm{spec}}(p,\lambda)\ \ (\mathrm{spectra}) \\
        \sigma_{\mathrm{Mod}}^{phot} &= g(\lambda, p) \times \phi_{\mathrm{phot}}(p,\lambda)\ \ (\mathrm{photometric})

    :math:`\gamma(\lambda, p)` is a global surface describing the spectral
    residual of a 2D spline surface defined on the same ranges as the
    corresponding model.


    Attributes
    ----------
    disconnect_sp : bool
        Whether error snake of spectral data is considered.
    model : nacl.salt
        Model.
    sp : nacl.dataset.SpectrumData
        Spectral data
    lc : nacl.dataset.LcData
        Photometric data
    filter_db : nacl.instruments.FilterDb
        Filter transmission projected on B-splines
    bands : numpy.array
        Bands used for photometric data
    threshold : int
        Fix the spline parameters for bin that gather less data points than this
        threshold value.
    wl_grid : numpy.array
        Wavelength grid.
    phase_grid : numpy.array
        Phase grid.
    basis : nacl.lib.bspline.BSpline2D
        2D spline basis.
    factor_int : float
        Model normalisation.
    lambda_c : numpy.array
        Mean wavelength of the filter in the SN-restframe.
    pars : nacl.lib.fitparameters.FitParameters
        Parameters :math:`\gamma`.
    pars0 : numpy.array
        Parameters used to initialize the error snake.
    """
    def __init__(self, model, gamma_init=0.01,
                #  disconnect_sp=False,
                threshold=None,
                #  adaptive_grid=False,
                 bins=(3, 3), order=4):
        """Constructor

        - instantiate the bases (phase, wavelength)
        - compute the \lambda_c for each light curve
        - initiate the parameters

        Parameters
        ----------
        model : nacl.salt
            Model.
        gamma_init : numpy.array ou float
            Parameters used to initialize the error snake.
        disconnect_sp : bool
            Whether error snake of spectral data is considered.
        threshold : int
            Fix the spline parameters for bin that gather less data points than this threshold value.
        adaptive_grid : bool
            It true, define Bspline knots where parameter space has data.
        bins : tuple
            Number of bins if the grid is not adaptive.
        order :
            Spline order.
        """
        # no reason to apply this to the spectral data
        # self.disconnect_sp = disconnect_sp

        self.model = model
        self.training_dataset = model.training_dataset
        self.filter_db = self.model.filter_db
        self.bands = self.model.bands
        self.threshold = threshold
        order = order

        lc_data = self.training_dataset.lc_data
        sp_data = self.training_dataset.spec_data

        # if we need an adaptive grid, we'll reconnect that later
        # if adaptive_grid:
        #     phase_lc = self.model.get_restframe_phases(self.lc)
        #     phase_sp = self.model.get_restframe_phases(self.sp)
        #     wavelength_lc = lc_data.wavelength/(1. + lc_data.z)
        #     wavelength_sp = sp_data.wavelength/(1. + sp_data.z)
        #     phase = np.hstack((phase_sp, phase_lc))
        #     wavelength = np.hstack((wavelength_sp, wavelength_lc))
        #     _, wl_grid, phase_grid, _ = pl.hist2d(wavelength, phase, bins=2)
        # else:
            # print(f'\n VarModel N bins : ph : {ph_bin}, wl {wl_bin}')
        ph_bins, wl_bins = bins
        phase_grid = np.linspace(model.basis.by.range[0], model.basis.by.range[-1], ph_bins)
        wl_grid = np.linspace(model.basis.bx.range[0], model.basis.bx.range[-1], wl_bins)
        self.basis = BSpline2D(wl_grid, phase_grid, x_order=order, y_order=order)

        # not sure what this is...
        # Guy tells me it is not used anymore.
        # self.factor_int = self.model.norm

        # this should not happen. If it does, this is certainly not the
        # responsibility of a subcomponent of the error model to correct for
        # this.
        # if lc_data.wavelength.sum() == 0:
        #     filter_mean_wl = [self.model.filter_db.transmission_db[bd].mean() for bd in self.model.bands.astype(str)]
        #     self.lambda_c = np.array(filter_mean_wl)[self.lc['band_id']]/(1+self.lc['ZHelio'])
        # else:
        self.lambda_c = lc_data.wavelength / (1.+lc_data.z) # ['Wavelength']/(1+self.lc['ZHelio'])
        self.pars = self.init_pars(gamma_init=gamma_init)
        # self.pars0 = self.pars.full.copy() # ?

    def fix_non_constrained_pars(self, threshold):
        """index of parameters of the parameter space that don't have enough data to constraint the error snake.

        Parameters
        ----------
        threshold : int
            Threshold value defining the "enough". If the sum of the data in a bin is less than this value,
            the corresponding parameter is fixed.

        Returns
        ----------
        idx : numpy.array
            Index of parameters that will be fixed.
        """
        lc_data = self.training_dataset.lc_data
        # sp_data = self.training_dataset.spec_data
        lc_phases = self.model.get_restframe_phases(lc_data)
        # sp_phases = self.model.get_restframe_phases(sp_data)
        lc_wl = lc_data.wavelength / (1. + lc_data.z)
        # sp_wl = sp_data.wavelength / (1. + sp_data.z)

        # x = np.hstack((wl_sp, wl_lc))
        # y = np.hstack((ph_sp, ph_lc))
        jj = self.basis.eval(lc_wl, lc_phases)
        idx = np.where(np.bincount(np.sort(jj.col)) < threshold)
        return idx[0]

    def init_pars(self, gamma_init):
        """
        Initiate model parameters.

        Parameters
        ----------
        gamma_init : float
            Parameters used to initialize the error snake.

        Returns
        ----------
        gamma : nacl.lib.fitparameters.FitParameters
            Parameters :math:`\gamma`.
        """
        gamma = FitParameters([('gamma', self.basis.bx.nj * self.basis.by.nj)])
        gamma['gamma'] = gamma_init
        if self.threshold is not None:
          idx = self.fix_non_constrained_pars(self.threshold)
          gamma.fix(idx)
        return gamma
        #pass

    def get_struct(self):
        npars = self.basis.bx.nj * self.basis.by.nj
        return [('gamma', npars)]

    def noise(self, p=None):
        lc_data = self.training_dataset.lc_data
        var = self(p=None)
        noise = np.random.normal(scale=var, size=len(lc_data))
        return noise

    def __call__(self, pars, jacobian=None, debug_mode=False):
        """evaluate the model - return a variance and (optionally) its derivatives

        Evaluate the model for a set of parameter :math:`\gamma` (variance model parameters)
        and :math:`\beta` (flux model parameters).

        Parameters
        ----------
        gamma : np.array
           set of parameter of the variance model;
        beta : np.array
           set of parameter of the flux model;
        jacobian : None or scipy.sparse.coo_matrix
           derivative of the flux, not necessary if derivative of variance model not needed,
        debug_mode : bool
           to get some variables...
        lc : nacl.dataset.LcData
           to get variance model of a set of light curve and is None will get for all
        sp : nacl.dataset.SpectrumData
           to get variance model of a set of spectra and is None will get for all

        Returns
        ----------
        var : numpy.array
            Variance value of the model, quadratic sum of the error measurement and the error snake.
        if jacobian is not None:
        var : numpy.array
            Variance value of the model, quadratic sum of the error measurement and the error snake.
        jacobian_var : scipy.sparse.coo_matrix
            Jacobian (derivatives wrt :math:`\beta` and :math:`\gamma`)matrix of the error model.
        """
        # self.model.pars.free = p

        lc_data = self.training_dataset.lc_data
        lc_phases = self.model.get_restframe_phases(lc_data)
        sp_data = self.training_dataset.spec_data
        sp_phases = self.model.get_restframe_phases(sp_data)
        lambda_c = lc_data.wavelength / (1. + lc_data.z)

        # too bad we need to call the model again here...
        # let's see whether we could cache this call
        flux = self.model(p, jac=False)

        J_lc = self.basis.eval(lambda_c, lc_phases)
        dsig = J_lc @ pars['gamma'].full
        sigma_lc = dsig * lc_data.flux
        # sigma_sp = np.zeros_like(sp_phases)
        # sig = np.hstack((sigma_lc, sigma_sp))
        var = sigma_lc**2

        if jacobian is not None:
            return var, None

            # n_pars, n_data = len(self.model.pars.free) + len(self.pars.free), len(sig)
            # v, jacobian = self.model(beta, jac=True)

            # i_dp, j_dp, jacobian_pars, i_dg0, j_dg0, jacobian_gamma = [], [], [], [], [], []

            # # dtmax
            # idx = self.model.pars['tmax'].indexof(sp['sn_id'])
            # jacobian_wrt_phase, jacobian_wrt_wavelength = self.basis.gradient(wl_sp,
            #                                                                   phase_sp + self.model.delta_phase)
            # if len(jacobian_pars) != 0.:
            #     jacobian_pars[idx] -= 2 * (jacobian_wrt_phase * self.pars['gamma'].full) / \
            #                           (1+sp['ZHelio']) * v[sp['i']] * sigma_spectra
            # # dg
            # i_dg0 = spline_sp.row.copy()
            # j_dg0 = self.pars['gamma'].indexof(spline_sp.col) + len(self.model.pars.free)
            # jacobian_gamma = 2 * v[sp['i']][i_dg0]**2 * spline_sp.data * ss_sp[i_dg0]
            # if debug_mode:
            #     return i_dp, j_dp, jacobian_pars, i_dg0, j_dg0, jacobian_gamma, v, sp, spline_sp, ss_sp

            # v_lc = v[lc['i']]
            # jacobian_lightcurve = jacobian.tocsc()[lc['i']].tocoo()

            # i_dp_lc = jacobian_lightcurve.row.copy()
            # j_dp_lc = jacobian_lightcurve.col.copy()
            # jacobian_pars_lightcurve = 2 * jacobian_lightcurve.data * (sigma_lightcurve * ss_lc)[i_dp_lc]

            # # dtmax
            # if self.model.pars['tmax'].indexof().sum() != len(self.model.pars['tmax'].full) * -1:
            #     jacobian_wrt_phase, jacobian_wrt_wavelength = self.basis.gradient(lambda_c,
            #                                                                             phase_lc +
            #                                                                             self.model.delta_phase)
            #     idx_lc = np.where(np.in1d(jacobian_lightcurve.col, self.model.pars['tmax'].indexof()))
            #     if len(jacobian_pars_lightcurve) != 0.:
            #         jacobian_pars_lightcurve[idx_lc] -= 2 * (jacobian_wrt_phase * self.pars['gamma'].full) / (1+lc['ZHelio']) * v_lc * sigma_lightcurve

            # # dg
            # i_dg0_lc = spline_lc.row.copy()
            # j_dg0_lc = self.pars['gamma'].indexof(spline_lc.col) + len(self.model.pars.free)
            # jacobian_gamma_lightcurve = 2 * v_lc[i_dg0_lc] ** 2 * spline_lc.data * ss_lc[i_dg0_lc]

            # if len(i_dg0) != 0:
            #     i_dg0 += len(lc)
            # if len(i_dp) != 0:
            #     i_dp += len(lc)

            # i = np.hstack((i_dp, i_dg0, i_dp_lc, i_dg0_lc))
            # j = np.hstack((j_dp, j_dg0, j_dp_lc, j_dg0_lc))
            # val = np.hstack((jacobian_pars, jacobian_gamma, jacobian_pars_lightcurve, jacobian_gamma_lightcurve))

            # idx_zeros = np.where((j != -1))[0]
            # jacobian_var = coo_matrix((val[idx_zeros], (i[idx_zeros], j[idx_zeros])), shape=(n_data, n_pars))

            # return var, jacobian_var.T

        return var
