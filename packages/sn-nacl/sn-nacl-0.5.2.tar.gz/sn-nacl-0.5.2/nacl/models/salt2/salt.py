"""Pure python reimplementation of the original salt2 model
"""


import logging
import numpy as np
import scipy.sparse
import sncosmo

try:
    from sksparse.cholmod import cholesky_AAt
except ImportError:
    from scikits.sparse.cholmod import cholesky_AAt

from bbf import bspline, SNFilterSet, SNMagSys
from saltworks import FitParameters

from .colorlaw import ColorLaw
from .lightcurves import LightcurveEvalUnit
from .spectra import CompressedSpectrumEvalUnit, CompressedSpectroPhotoEvalUnit #  SpectrumRecalibrationPolynomials



class SALT2Like(object):
    r"""A re-implementation of the SALT2 model

    SALT2 is an empirical SN spectrophotometric model. This class provides a
    pure python re-implementation of SALT2 with a number of improvements.

    The SALT2 parametrization is defined as follows. In the SN restframe the
    absolute spectral density :math:`S(\lambda)` is:

    .. math::
        S(\lambda, \mathrm{p}) = X_0 \times \left[M_0(\lambda, \mathrm{p}) + X_1
           \times M_1(\lambda, \mathrm{p})\right]\ 10^{0.4 c CL(\lambda)}

    where :math:`\mathrm{p}` is the SN phase, i.e. the restframe time since SN
    peak luminosity:

    .. math::
        \mathrm{ph} = \frac{t_{MJD} - t_{max}}{1 + z}

    :math:`M_0`, :math:`M_1` are global surfaces describing the spectral
    evolution of the average SN and its principal variation, and
    :math:`CL(\lambda)` is a global "extinction correction" describing the color
    diversity of the SNIa family.

    :math:`(X_0, X_1, c)` are SN-dependent. :math:`X_0` is the amplitude of the
    "SN-frame B-band lightcurve" as inferred from the observer-frame fluxes.
    :math:`X_1` is the coordinate of the SN along :math:`M_1`. In practice, it
    quantifies the variations of the light curve width. :math:`c` is the SN
    color -- or more exactly, the SN color excess with respect to the average SN
    color.

    """

    def __init__(self, training_dataset,
                 phase_range=(-20., 50.), wl_range=(2000., 9000.),
                 basis_knots=[127, 20],
                 basis_filter_knots=900,
                 wl_grid=None, phase_grid=None,
                 spectrum_recal_degree=3,
                 normalization_band_name='swope2::b'):
        """Constructor

          - instantiate the bases (phase, wavelength, filter)
          - compute the Gram
          - compute the lambda_eff matrix
          - instantiate a color law and evaluate it on the lambda_eff's
          - organizes the data into spectral/photometric computing units

        Parameters
        ----------
        training_dataset : nacl.dataset.TrainingDataset
            Training dataset.
        phase_range : 2-tuple
            Nominal phase range of the model.
        wl_range : 2-tuple
            Nominal wavelength range of the model.
        basis_knots : 2-list
            Number of wavelength and photometric knot.
        basis_filter_knots : int
            Number of knot for the filter basis
        spectrum_recal_degree : int
            Degree of the spectrum recalibration polynomials
        normalization_band_name : str
            Use this band to normalize the model.
        """
        self.training_dataset = training_dataset
        self.lc_data = training_dataset.lc_data
        self.phase_range = phase_range
        self.wl_range = wl_range
        self.n_wl, self.n_ph = basis_knots[0],  basis_knots[1]
        self.basis_knots = basis_knots
        self.basis_filter_knots = basis_filter_knots
        self.spectrum_recal_degree = spectrum_recal_degree
        self.delta_phase = 0. # check: do not remember what this is
        # self.filterpath = self.training_dataset.filterpath
        if self.training_dataset.lc_data is not None:
            self.bands = list(self.training_dataset.transmissions.keys())
        self.normalization_band_name = normalization_band_name
        # self.calib_variance = calib_variance

        self.timing = []

        self.basis, self.gram, self.G2, self.L_eff = None, None, None, None
        self.val, self.jacobian_val, self.jacobian_i, self.jacobian_j = None, None, None, None
        self.polynome_color_law, self.jacobian_color_law = None, None

        # Filter database
        # TODO: we should be able to optimize this a little
        # (i.e. adapt the filter bases, to lower the size of the grams)
        self.filter_basis = bspline.BSpline(np.linspace(self.wl_range[0],
                                                        self.wl_range[1],
                                                        basis_filter_knots), order=4)
        self.filter_db = SNFilterSet(basis=self.filter_basis)
        self.filter_db.insert('swope2::b', z=0.)
        self.color_law = ColorLaw()

        n_lc_meas, n_spec_meas, n_spectrophot_meas = \
            self.training_dataset.nb_meas(split_by_type=1)

        # TODO: where is this used ?
        # TODO: we may replace this by n_lc_meas > 0
        if self.training_dataset.lc_data is not None:
            tds = self.training_dataset
            ii = self.training_dataset.i_lc_first
            self.lambda_c = tds.lc_data.wavelength[ii] / (1+tds.lc_data.z[ii])
            self.lambda_c_red = self.color_law.reduce(self.lambda_c)

        # initialize degree of the spectral recalibration polynomial
        # self._init_spectral_polynomial()

        # initialize model basis and model parameter vector
        # model component: bases, color law, and parameter vector
        self._init_bases(wl_grid, phase_grid,
                         wl_range, phase_range, basis_knots)

        # OK. For now, the color scatter and the calibration scatter
        # are explicitely instantiated in the model constructor
        #        self.error_snake_model = self._instantiate_error_model(error_snake_model_type)
        #        self.calib_error_model = self._instantiate_error_model(calib_error_model_type)
        #        self.color_scatter_model = self._instantiate_error_model(color_scatter_model_type)

        # finally, it is better to have it here.
        # NOTE: if there are spectra, the model must be evaluated for them.
        # even if they are marked as invalid
        #self.recal_func = None
        #if self.training_dataset.spec_data is not None:
        #    self.recal_func = \
        #        SpectrumRecalibrationPolynomials(self.training_dataset, self,
        #                                         self.recalibration_degree)

        # initialize the global model parameters (M0, M1, CL)
        # self.pars = self.init_pars()

        # some of the classes gravitating around the model
        # the constraints for example, sometimes need to have
        # access to the index of some paramters in the full parameter
        # vector (all parameters released)
        # self.all_pars_released = self.pars.copy()
        # self.all_pars_released.release()

        # initialize the SN specific parameters (X0, X1, col, tmax)
        # if init_from_training_dataset:
        #     self.init_from_training_dataset()

        # finalize the initialization of the error models 
        # which need a fully operational parameter vector 
#        if self.calib_error_model is not None:
#            self.calib_error_model.finalize()

        # we use a default model normalization
        # this is what guarantees that the SALT2.4 absolute mag
        # is -19.5 in the SWOPE::B band. Of course, this default
        # normalization may be changed explicitely, by calling
        # self.renorm(band_name=, Mb=, magsys='AB')
        self.norm = self.normalization(pars=None, band_name=normalization_band_name,
                                       default_norm=1.01907246e-12)

        # grams
        self.init_grams_and_cc_grid()

        # and finally, prepare the computing units
        self.queue = self._init_eval_units()

        # clear the cache
        # self.clear_cache()

        # if we need to run queue units separately,
        # could be useful to disable caching of the results
        # self.disable_cache = False

    # def clone(self, training_dataset):
    #     """return a clone (same basis, same color law) for a different tds
    #     """
    #     ret = SALT2Like(training_dataset,
    #                     phase_range=self.phase_range,
    #                     wl_range=self.wl_range,
    #                     basis_knots=self.basis_knots,
    #                     basis_filter_knots=self.basis_filter_knots,
    #                     spectrum_recal_degree=self.spectrum_recal_degree,
    #                     normalization_band_name=self.normalization_band_name,
    #                     error_snake_model=self.error_snake_model,
    #                     calib_error_model=self.calib_error_model,
    #                     color_scatter_model=self.color_scatter_model)
    #                      calib_variance=self.calib_variance)
    #     for block_name in ['M0', 'M1', 'CL']:
    #         ret.pars[block_name].full[:] = self.pars[block_name].full[:]
    #     ret.norm = ret.normalization(band_name=ret.normalization_band_name)

    #     return ret

    def get_gram_dot_filter(self, band_name=None):
        """Used by the integral constraints
        """
        key = band_name if band_name is not None else self.normalization_band_name
        coeffs, _ = self.filter_db[key]
        return self.gram.dot(coeffs)

    def reduce(self, wl):
        return self.color_law.reduce(wl)

    # def _instantiate_error_model(self, error_model_type):
    #     if error_model_type is None:
    #         return None
    #     if type(error_model_type) == tuple:
    #         cls, args = error_model_type
    #         return cls(self, **args)
    #     if type(error_model_type) == type:
    #         return error_model_type(self)
    #     raise TypeError('arg should either be: None|(model_class, (args))|(model_class)')

    def init_grams_and_cc_grid(self):
        r"""Compute the :math:`\Lambda^{\mathrm{eff}}_{\ell q}` matrix (see definition above) on which the color
        law is evaluated.

        .. math::
             \bar{\lambda}_{\ell q} = \frac{\int \lambda^2 B_\ell(\lambda) B_q(\lambda)
             d\lambda}{\int \lambda B_\ell(\lambda) B_q(\lambda) d\lambda}

        Compute de grammian of order one, :math:`G` and two :math:`G2` of the model :

        .. math::
            G = \int \lambda B_\ell(\lambda) B_q(\lambda) d\lambda \\
            G2 = \int \lambda^2 B_\ell(\lambda) B_q(\lambda) d\lambda


        .. note::
             this method will be moved to the main model class (since we may work
             with one single :math:`\Lambda^{\mathrm{eff}}` matrix in a near future).
        """
        self.gram = get_gram(0., self.basis.bx, self.filter_basis, lambda_power=1)
        self.G2 = get_gram(0., self.basis.bx, self.filter_basis, lambda_power=2)

        gram = self.gram.tocoo()
        gram2 = self.G2.tocoo()
        assert(~np.any(gram.row-gram2.row) and ~np.any(gram.col-gram2.col))
        l_eff = gram2.data / gram.data
        self.L_eff = scipy.sparse.coo_matrix((l_eff, (gram.row, gram.col)), shape=gram.shape)

    def get_struct(self):
        """return the structure of the fit parameter vector

        In practice, the fit parameter vector is larger than just the model
        parameters: it also contains the parameters of the error models (error
        snake, color scatter, calibration, see e.g. variancemodels.py). The
        instantiation of the final fit parameter vector cannot therefore be
        performed by the model itself. What the model can do, is to return the
        description of the fit parameter blocks it knows about.

        """
        nb_sne = self.training_dataset.nb_sne()
        # nb_spectra = self.training_dataset.nb_spectra()
        # nb_passbands = len(self.bands)
        # spec_recalibration_npars = self.recalibration_degree + 1
        nb_lightcurves = self.training_dataset.nb_lcs(valid_only=False)
        d = [('X0',   nb_sne),
             ('X1',   nb_sne),
             ('c',  nb_sne),
             ('tmax', nb_sne),
             ('M0',   self.basis.bx.nj * self.basis.by.nj),
             ('M1',   self.basis.bx.nj * self.basis.by.nj),
             ('CL',  4)]
        if hasattr(self, 'recal_func'):
            d.extend(self.recal_func.get_struct())
            #        if self.training_dataset.spec_data is not None:
            #            d.append(('SpectrumRecalibration', spec_recalibration_npars.sum()))
        return d

    def init_pars(self, pars=None, model_name='salt2.4', version='2.4'):
        """instantiate a fit parameter vector

        Returns
        -------
        fp : nacl.lib.fitparameters.FitParameters
            Model parameters.
        """
        if pars is None:
            pars = FitParameters(self.get_struct())

        self.init_model_pars(pars, model_name=model_name, version=version)
        self.init_from_training_dataset(pars)

        if 'SpectrumRecalibration' in pars._struct:
            self.recal_func.init_pars(pars)

        return pars

    def init_from_training_dataset(self, pars):
        """load initial sn parameters from the training dataset
        """
        sn_data = self.training_dataset.sn_data
        pars['X0'].full[sn_data.sn_index] = sn_data.x0
        pars['X1'].full[sn_data.sn_index] = sn_data.x1
        pars['c'].full[sn_data.sn_index] = sn_data.col
        pars['tmax'].full[sn_data.sn_index] = sn_data.tmax

    def init_model_pars(self, pars, model_name='salt2', version='2.4'):
        """Load & adapt the SALT2.4 global surfaces and color law from sncosmo.

        Load the coefficients of the SALT2.4 surfaces and color law. The
        definition of the model spline bases differs from the original
        definition of the SALT2.4 bases; so, we reproject the original SALT2
        surfaces on the model basis.

        Parameters
        ----------
        salt2_filename : str

        """
        salt2_source = sncosmo.get_source('salt2', version='2.4')

        phase_grid = np.linspace(self.phase_range[0], self.phase_range[1], self.n_ph)
        wl_grid = np.linspace(self.wl_range[0], self.wl_range[1], self.n_wl)
        basis = bspline.BSpline2D(wl_grid, phase_grid, x_order=4, y_order=4)

        phase_salt = salt2_source._phase
        wl_salt = salt2_source._wave

        w, p = np.meshgrid(wl_salt, phase_salt)

        sncosmo_scale = salt2_source._SCALE_FACTOR
        salt2_m0 = salt2_source._model['M0'](phase_salt, wl_salt).ravel() / sncosmo_scale
        salt2_m1 = salt2_source._model['M1'](phase_salt, wl_salt).ravel() / sncosmo_scale
        salt2_cl = np.array(salt2_source._colorlaw_coeffs)[::-1]

        jac = self.basis.eval(w.ravel(), p.ravel()).tocsr()
        factor = cholesky_AAt(jac.T, beta=1.E-6)

        pars['M0'].full[:] = factor(jac.T * salt2_m0)
        pars['M1'].full[:] = factor(jac.T * salt2_m1)
        pars['CL'].full[:] = salt2_cl

    # def _init_spectral_polynomial(self):
    #     """instantiate the recalibration polynomials

    #     if a degree is specified, all spectra have the same degree. Since the
    #     degree of the polynomial must not exceed the number of Light curves :
    #     this degree is large odd number inferior to the numbers of light curves
    #     for this SN.

    #     """
    #     # note: the model is evaluated on the full dataset.
    #     # not just the valid data.
    #     nb_spectra = self.training_dataset.nb_spectra(valid_only=False)
    #     self.recalibration_degree = np.full(nb_spectra, self.spectrum_recal_degree)

    def _init_bases(self, wl_grid=None, phase_grid=None,
                    wl_range=(2000., 9000.),
                    phase_range=(-20., 50.), basis_knots=(127,20)):
        """
        Instantiate model bases
        """
        if wl_grid is None:
            assert wl_range is not None and basis_knots is not None
            logging.info('default regular grid in wavelength')
            wl_grid = np.linspace(self.wl_range[0], self.wl_range[1],
                                  self.n_wl)
        else:
            logging.info('user provided grid in wavelength')
        if phase_grid is None:
            assert phase_range is not None and basis_knots is not None
            logging.info('default regular grid in phase')
            phase_grid = np.hstack([np.linspace(self.phase_range[0],
                                                self.phase_range[1],
                                                self.n_ph)])
        else:
            logging.info('user provided grid in phase')
        self.basis = bspline.BSpline2D(wl_grid, phase_grid,
                                       x_order=4, y_order=4)

    #    @property
    #    def noise_models(self):
    #        """return a list of all the noise models contained by the model
    #        """
    #        ret = [self.calib_error_model,
    #               self.color_scatter_model,
    #               self.error_snake_model]
    #        return list(filter(lambda x: x is not None, ret))

    def normalization(self, pars=None, band_name='swope2::b', Mb=-19.5, magsys='AB',
                      default_norm=1.01907246e-12):
        """model normalization

        The SALT2Like normalization is set during training by the constraint
        on the integral of M0 at phase zero.

        Therefore, by default, we do not renormalize the model during
        evaluation.
        """
        default_norm = default_norm if default_norm is not None else 1.01907246e-12
        tq, filter_basis = self.filter_db[band_name]

        # AB flux in the specified band
        ms = SNMagSys(self.filter_db, magsys)
        # zp = ms.ZeroPoint(self.filter_db.transmission_db[band_name])
        zp = ms.get_zp(band_name)
        self.int_ab_spec = 10**(0.4 * zp)

        # normalization quantities
        self.flux_at_10pc = np.power(10., -0.4 * (Mb-zp))
        self.flux_at_10Mpc = np.power(10., -0.4 * (Mb+30.-zp))

        if pars is None:
            return default_norm

        phase_eval = self.basis.by.eval(np.array([0. + self.delta_phase])).tocsr()
        gram = get_gram(z=0., model_basis=self.basis.bx,
                        filter_basis=filter_basis, lambda_power=1)
        surface_0 = pars['M0'].full.reshape(len(self.basis.by), -1)
        # evaluate the integral of the model in the specified band
        self.int_M0_phase_0 = phase_eval.dot(surface_0.dot(gram.dot(tq)))

        return self.flux_at_10Mpc / self.int_M0_phase_0

    def renorm(self, pars, band_name='swope2::b', Mb=-19.5, magsys='AB'):
        """Adjust the model normalization
        """
        # explicitely recompute a normalization
        self.norm = self.normalization(pars, band_name, Mb, magsys,
                                       default_norm=None)

    def _init_eval_units(self):
        """Initialize the photometric and spectroscopic eval units

        The actual evaluation of the model is deferred to specialized
        sub-units, which are called one after the other. These units
        are stored in a queue.

        """
        # n_lc_meas, n_spec_meas, n_spectrophot_meas = \
        #     self.training_dataset.nb_meas(valid=True, split_by_type=True)
        queue = []
        if self.training_dataset.lc_data is not None:
            logging.info('initializing lightcurve eval unit')
            queue.append(LightcurveEvalUnit(self))
        if self.training_dataset.spec_data is not None:
            logging.info('initializing spectrum eval unit')
            queue.append(CompressedSpectrumEvalUnit(self, spec_recal_degree=self.spectrum_recal_degree))
        if self.training_dataset.spectrophotometric_data is not None:
            logging.info('initializing spectrophotometric eval unit')
            queue.append(CompressedSpectroPhotoEvalUnit(self))
        return queue

    # def update_computing_units(self, ilc=None, spec=False):
    #     """
    #     Recreate the model queue as a function of the wanted LCs and spectra.

    #     Parameters
    #     -------
    #     ilc : None or int
    #         If None all light curve are evaluated, else only teh desired one.
    #     spec : bool
    #         Whether Spectra need to be evaluated.

    #     Returns
    #     -------
    #     queue : list
    #         The new queue
    #     """
    #     queue = []
    #     if ilc is not None:
    #         for lc in [self.training_dataset.lcs[ilc]]:
    #             queue.append(LightcurveEvalUnitTz(lc, self))
    #     if spec:
    #         queue.append(SpectrumEvalUnitFast(self.training_dataset, self))
    #     return queue

    # def clear_cache(self):
    #     """
    #     Clear model evaluation, derivatives and timing.
    #     """
    #     self.val = []
    #     self.jacobian_i = []
    #     self.jacobian_j = []
    #     self.jacobian_val = []
    #     self.timing = []

    def precompute_color_law(self, cl_pars, jac=False):
        """
        Precompute the color law for the photometric data.

        Parameters
        -------
        cl_pars : None or numpy.array
            Color law parameters
        jac : bool
            If derivatives are needed.
        """
        polynome_color_law, jacobian_color_law = \
            self.color_law(self.L_eff.data, cl_pars,
                           jac=jac)  # return_jacobian_as_coo_matrix=False)
        self.polynome_color_law = \
            scipy.sparse.csr_matrix((polynome_color_law,
                                     (self.L_eff.row, self.L_eff.col)),
                                    shape=self.L_eff.shape)
        if jac:
            self.jacobian_color_law = []
            _, n = jacobian_color_law.shape
            for i in range(n):
                jacobian_cl = \
                    scipy.sparse.csr_matrix((jacobian_color_law[:, i],
                                             (self.L_eff.row, self.L_eff.col)), shape=self.L_eff.shape)
                self.jacobian_color_law.append(jacobian_cl)

    def get_restframe_phases(self, pars, data):
        """
        Given a chunk of data, return the restframe phases

        Returns
        -------
        numpy.array
            data SN-restframe phase
        """
        sn_index = data.sn_index
        tmax = pars['tmax'].full[sn_index]
        return (data.mjd - tmax) / (1.+data.z)

    def __call__(self, pars, jac=False): # , plotting=False, ilc_plot=None, spec_plot=False):
        """Evaluate the model for the parameter set p

        In practice, loop over the queue and run each eval unit.
        Assemble the results into one single vector and (optionally)
        one single jacobian matrix.

        Parameters
        -------
        p : numpy.array
            Vector containing the free parameters only.
        jac : bool
            Whether it return the jacobian matrix.

        Returns
        -------
        val : numpy.array
            model results
        jacobian : scipy.sparse.csr_matrix
            jacobian matrix (if jac is true)
        """
        # pre-evaluate the color law (shared between all light curves)
        # cl_pars = pars['CL'].full
        # self.precompute_color_law(cl_pars, jac=jac)

        # # precompute the values of the phase basis on the full dataset
        # # significantly faster that way
        # if self.training_dataset.lc_data is not None:
        #     restframe_phases = self.get_restframe_phases(pars, self.lc_data)
        #     self.phase_eval = self.basis.by.eval(restframe_phases + self.delta_phase).tocsr()
        #     if jac:
        #         self.dphase_dtmax = self.basis.by.deriv(restframe_phases + self.delta_phase).tocsr()
        #     else:
        #         self.dphase_dtmax = None

        # self.clear_cache()

        # now, we are ready to loop over the eval units
        res = [q(pars, jac) for q in self.queue]


        if not jac:
            model_val = np.add.reduce([r for r in res])
            return model_val

        model_val = np.add.reduce([r[0] for r in res])

        rows = np.hstack([r[1].row for r in res])
        cols = np.hstack([r[1].col for r in res])
        vals = np.hstack([r[1].data for r in res])

        idx = cols >= 0
        JJ = scipy.sparse.coo_matrix((vals[idx], (rows[idx], cols[idx])),
                                     shape=res[0][1].shape)
        # JJ = scipy.sparse.dok_matrix(res[0][1].shape)
#        for r in res:
#            JJ += r[1]
#
        return model_val, JJ

        # n_data = self.training_dataset.nb_meas(valid_only=False)

        # logging.debug('computing derivatives: hstack...')
        # n = len(pars.free)
        # i = np.hstack(self.jacobian_i)
        # j = np.hstack(self.jacobian_j)
        # v = np.hstack(self.jacobian_val)
        # logging.debug('building coo_matrix...')
        # idx = j >= 0  # self.pars.indexof(j) >= 0
        # jacobian = scipy.sparse.coo_matrix((v[idx], (i[idx], j[idx])), shape=(n_data, n))
        # logging.debug('ok, done.')
        # return val, jacobian


    @property
    def y(self):
        return self.training_dataset.get_all_fluxes()

    @property
    def yerr(self):
        return self.training_dataset.get_all_fluxerr()

    @property
    def bads(self):
        return self.training_dataset.get_bads()


_G, _G2 = {}, {}


def get_gram(z, model_basis, filter_basis, lambda_power=1):
    """
    Calculate the grammian of to spline basis.

    The grammian :math:`G` of order :math:`N`, to basis :math:`B_0` (define on wavelength,
    in our case surfaces wavelength basis) and
    :math:`B_1` (define on SN-restframe wavelength, filter basis) is defined as :

    .. math::
        G = \\int \\lambda^N B_0(\\lambda) B_q(\\lambda (1+z)) d\\lambda

    Parameters
    -------
    z : numpy.array
        Vector containing the data redshift.
    model_basis : nacl.lib.bspline.BSpline
        Wavelength basis.
    filter_basis : nacl.lib.bspline.BSpline
        Filter basis defined common to all the bands.
    lambda_power : int
        Grammian order.

    Returns
    -------
    gram : scipy.sparse.csc_matrix
        Grammian
    """
    global _G
    global _G2
    key = (z, model_basis, filter_basis, lambda_power)

    gram = _G.get(key, None)
    if gram is None:
        gram = bspline.lgram(model_basis, filter_basis, z=z, lambda_power=lambda_power).tocsc()
        _G[key] = gram

    return gram




# class SALT2Eval:
#     """Evaluate the model, for one single SN
#     """
#     def __init__(self, model, bands=['SWOPE::B'],
#                  n_spectra=1, n_phot_spectra=1):
#         """
#         """
#         self.orig_model = model
#         self.phase_range = model.phase_range
#         self.wl_range = model.wl_range
#         self.tds = SimTrainingDataset(bands,
#                                       n_spectra=n_spectra,
#                                       n_phot_spectra=n_phot_spectra)
#         # it is essential that the model is an exact duplicate
#         # of the original model - just 1 SN instead of many
#         self.model = model.clone(self.tds)

#     # def clone_model(self):
#     #     """instantiate a duplicate of the original model

#     #     .. note :: a model should be able to clone itself - would be cleaner
#     #     """
#     #     model = self.orig_model
#     #     ret = \
#     #         SALT2Like(self.tds,
#     #                   phase_range=model.phase_range,
#     #                   wl_range=model.wl_range,
#     #                   basis_knots=model.basis_knots,
#     #                   basis_filter_knots=model.basis_filter_knots,
#     #                   spectrum_recal_degree=model.spectrum_recal_degree,
#     #                   normalization_band_name=model.normalization_band_name,
#     #                   calib_variance=model.calib_variance)
#     #     return ret

#     def set(self, **kwargs):
#         """initialize the sn parameters

#         This function updates the dataset, and then the model
#         parameters.
#         """
#         # sn parameters
#         if 'z' in kwargs:
#             z = kwargs.get('z')
#             self.tds.sn_data.nt['z'] = z
#             if self.tds.lc_data:
#                 self.tds.lc_data.z[:] = z
#             if self.tds.spec_data:
#                 self.tds.spec_data.z[:] = z
#             if self.tds.spectrophotometric_data:
#                 self.tds.spectrophotometric_data.z[:] = z
#         if 'x0' in kwargs:
#             self.tds.sn_data.nt['x0'] = kwargs['x0']
#         if 'x1' in kwargs:
#             self.tds.sn_data.nt['x1'] = kwargs['x1']
#         if 'c' in kwargs:
#             self.tds.sn_data.nt['c'] = kwargs['c']
#         if 'tmax' in kwargs:
#             tmax = kwargs['tmax']
#             self.tds.sn_data.nt['tmax'] = kwargs['tmax']
#             if self.tds.lc_data:
#                 self.tds.lc_data.nt['mjd'] = self.tds.mjd +tmax
#         if 'ebv' in kwargs:
#             self.tds.sn_data.nt['ebv'] = kwargs['ebv']

#         if 'spec_mjd' in kwargs:
#             if self.tds.spec_data:
#                 self.tds.spec_data.nt['mjd'] = kwargs['spec_mjd']
#             if self.tds.spectrophotometric_data:
#                 self.tds.spectrophotometric_data.nt['mjd'] = kwargs['spec_mjd']

#         # light curve zero points and magsys
#         if 'zp' in kwargs:
#             zps = kwargs['zp']
#             for band_name in zps:
#                 idx = self.tds.lc_data.band == band_name
#                 self.tds.lc_data.nt['zp'] = zps[band_name]
#         if 'magsys' in kwargs:
#             magsys = kwargs['magsys']
#             if type(magsys) is str:
#                 self.tds.lc_data.nt['magsys'][:] = magsys
#             for band_name in magsys:
#                 idx = self.tds.lc_data.magsys == band_name
#                 self.tds.lc_data.nt['magsys'] = magsys[band_name]

#         # recompute the photometric norm factors
#         self.tds.compute_photometric_norm_factors()
#         # propagate this into the model parameters
#         self.model = self.orig_model.clone(self.tds)
#         self.model.init_from_training_dataset()

#     def set_from_tds(self, sn, tds):
#         """load the sn parameters from a training dataset
#         """
#         sn_pars = tds.get_sn_pars(sn)
#         if self.tds.lc_data:
#             sn_pars['zp'] = tds.get_zp(sn)
#             sn_pars['magsys'] = tds.get_magsys(sn)
#         self.set(**sn_pars)
#         # self.set(z=sn_pars['z'], x0=sn_pars['x0'],
#         #          x1=sn_pars['x1'], col=sn_pars['c'],
#         #          tmax=sn_pars['tmax'], ebv=sn_pars['ebv'],
#         #          zp=zp, magsys=magsys)

#     def update_global_pars(self, pars):
#         """
#         """
#         for block_name in ['M0', 'M1', 'CL']:
#             self.orig_model.pars[block_name].full[:] = pars[block_name].full[:]
#             self.model.pars[block_name].full[:] = pars[block_name].full[:]

#     def __call__(self):
#         """evaluate the model and update the dataset with the model values

#         This is the simplest way to evaluate the model.
#         No need to clone the dataset or anything.
#         """
#         v = self.model(self.model.pars.free)
#         self.tds.update_flux(v)

#     def bandflux(self, bands, mjds, zp, zpsys):
#         """evaluate the model for the requested bands and at the requested mjds

#         This one in a little more costly, as we need to instantiate
#         a new training dataset and re-instantiate a model.
#         """
#         pass

#     def bandmag(self, bands, mjd, magsys):
#         """return mags for the requested bands and at the requested mjds

#         This is also a little more costly, as we need to instantiate
#         a new training dataset and re-instantiate a model.
#         """
#         pass

#     def spectrum(self, mjd):
#         """evaluate and return a spectrophotometric spectrum
#         """
#         pass

#     def photspectrum(self, mjd):
#         """evaluate and return a spectrophotometric spectrum
#         """
#         pass

#     def color_law(self, col=None):
#         pass


# # def main():
# #     model = ...
# #     m = SALT2LikeEval(model, bands=['SWOPE::B'])

# #     # evaluate the model on all the data for this SN
# #     # with the default parameters
# #     m.eval(sn=sn)

# #     # evaluate the model on all the data for this SN
# #     # with alternative parameters
# #     m.eval(sn=sn, sn_pars=sn_pars, model_pars=model_pars)



    # def init_from_salt2_old(self, salt2_filename, stick_to_original_model=False):
    #     """Load & adapt the SALT2.4 global surfaces and color law.

    #     Load the coefficients of the SALT2.4 surfaces and color law. The
    #     definition of the model spline bases differs from the original
    #     definition of the SALT2.4 bases; so, we reproject the original SALT2
    #     surfaces on the model basis.

    #     Parameters
    #     ----------
    #     salt2_filename : str
    #         the classical salt2.npz filename containing the definition of the
    #         SALT2.4 bases, M0, M1 surfaces and color_law.
    #     """
    #     f = np.load(salt2_filename)
    #     phase_grid = f['phase_grid']
    #     wl_grid = f['wl_grid']
    #     basis = bspline.BSpline2D(wl_grid, phase_grid, x_order=4, y_order=4)

    #     if stick_to_original_model:
    #         # don't remember why we have this
    #         self.delta_phase = +0.7
    #         self.basis = basis
    #         self.pars = self.init_pars()
    #         self.pars['M0'].full[:] = f['M0'].T.ravel()
    #         self.pars['M1'].full[:] = f['M1'].T.ravel()
    #         self.pars['CL'].full[:] = f['CL_pars'][0:4]
    #         return

    #     # TODO: replace this with
    #     # xx = self.basis.bx.grid
    #     # yy = self.basis.by.grid
    #     xx = np.linspace(wl_grid[0], wl_grid[-1], basis.bx.nj)
    #     yy = np.linspace(phase_grid[0], phase_grid[-1], basis.by.nj)
    #     x,y = np.meshgrid(xx,yy)
    #     x,y = x.ravel(), y.ravel()
    #     jac = self.basis.eval(x,y).tocsr()
    #     factor = cholesky_AAt(jac.T, beta=1.E-6)

    #     # and initialize the parameters
    #     self.pars = self.init_pars()
    #     self.pars['M0'].full[:] = factor(jac.T * f['M0'])
    #     self.pars['M1'].full[:] = factor(jac.T * f['M1'])
    #     self.pars['CL'].full[:] = f['CL_pars'][0:4]
