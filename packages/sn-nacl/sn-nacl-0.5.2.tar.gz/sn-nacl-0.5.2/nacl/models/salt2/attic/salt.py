#!/usr/bin/python

####
# Re-implementation of the original SALT2 model.
####

import logging

import numpy as np
import scipy.sparse
import sncosmo

try:
    from sksparse.cholmod import cholesky_AAt
except ImportError:
    from scikits.sparse.cholmod import cholesky_AAt

from nacl.instruments import FilterDb
from nacl.lib import bspline
from nacl.lib.fitparameters import FitParameters
from nacl.lib.instruments import MagSys
from . import colorlaw, lightcurves, spectra

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

from lemaitre import bandpasses
from nacl import bandpasses as bp

class SALT2Like(object):
    """A re-implementation of the SALT2 model

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
    :math:`CL(\lambda)` is a global "extinction correction" describing the
    color diversity of the SNIa family.

    :math:`(X_0, X_1, c)` are SN-dependent. :math:`X_0` is the amplitude of the
    "SN-frame B-band lightcurve" as inferred from the observer-frame fluxes.
    :math:`X_1` is the coordinate of the SN along :math:`M_1`. In practice, it
    quantifies the variations of the light curve width. :math:`c` is the SN
    color -- or more exactly, the SN color excess with respect to the average
    SN color.

    Each Light Curve are evaluated interactively to use multi-threading and
    spectra are evaluated simultaneously.
    """
    def __init__(self, training_dataset,
                 wl_range=(2000., 9000.),  # . 11000.),
                 phase_range=(-20., 50.), 
                 basis_knots=[127, 20],
                 basis_filter_knots=900,
                 wl_grid=None, phase_grid=None,
                 spectrum_recal_degree=3,
                 init_from_salt2_file=None,
                 init_from_training_dataset=False,
                 normalization_band_name='SWOPE::B'):
        """Constructor.
              - instantiate the bases (phase, wavelength, filter)
              - compute the Grams
              - compute the lambda_eff matrix
              - instantiate a color law and evaluate it on the lambda_eff's

        Parameters
        ----------
        training_dataset : nacl.dataset.TrainingDataset
          training dataset.
        phase_range : 2-tuple
          nominal phase range of the model.
        wl_range : 2-tuple
          nominal wavelength range of the model.
        basis_knots : 2-list
          number of wavelength and photometric knot.
        basis_filter_knots : int
          number of knot for the filter basis
        spectrum_recal_degree : int
          degree of the spectrum recalibration polynomials
        init_from_salt2_file : str
          uf the model is to be initialized with the original
          SALT2-4 surfaces and bases, get them from this file.
        normalization_band_name : str
          use this band to normalize the model.
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
        self.filterpath = self.training_dataset.filterpath
        if self.training_dataset.lc_data is not None:
            self.bands = list(self.training_dataset.transmissions.keys())
        self.normalization_band_name = normalization_band_name
        # self.calib_variance = calib_variance

        self.timing = []
        
        self.y = training_dataset.get_all_fluxes()
        self.yerr = training_dataset.get_all_fluxerr()
        self.bads = training_dataset.get_valid()==0

        self.basis, self.gram, self.G2, self.L_eff = None, None, None, None
        self.val, self.jacobian_val, self.jacobian_i, self.jacobian_j = None, None, None, None
        self.polynome_color_law, self.jacobian_color_law = None, None

        # Filter database
        # TODO: we should be able to optimize this a little
        # (i.e. adapt the filter bases, to lower the size of the grams)
        self.filter_basis = bspline.BSpline(np.linspace(self.wl_range[0], self.wl_range[1],  # 2000., 9000.,  #
                                                        basis_filter_knots), order=4)  # was 9000
        try:
            self.filter_db = FilterDb(self.filter_basis, self.training_dataset,
                                      additional_band=[normalization_band_name],
                                      filterpath=self.filterpath)
        except:
            self.filter_db = bp.FilterDb(self.filter_basis, self.training_dataset, bands=['standard::b'])
        self.color_law = colorlaw.ColorLaw()

        n_lc_meas, n_spec_meas, n_spectrophot_meas = \
            self.training_dataset.nb_meas(split_by_type=1)

        # lc = self.training_dataset.lc_data
        # d = dict({(lc[i]['band_id'], lc[i]['Filter']) for i in np.arange(len(lc))})
        # self.bands = np.array([d[i] for i in range(len(d))])
        # self.bands = self.lc_data.band_index

        # lambda_c needed for the color scatter estimation
        # lambda_c = self.training_dataset.lc_data['Wavelength']/(1+self.training_dataset.lc_data['ZHelio'])
        # idx_lam_c = np.array([lc.data['i'][0] for lc in self.training_dataset.lcs])
        # self.lambda_c = lambda_c[idx_lam_c]
        # self.lambda_c_red = self.color_law.reduce(self.lambda_c)
        #
        # TODO: where is this used ?
        # TODO: we may replace this by n_lc_meas > 0
        if self.training_dataset.lc_data is not None:
            tds = self.training_dataset
            ii = self.training_dataset.i_lc_first
            self.lambda_c = tds.lc_data.wavelength[ii] / (1+tds.lc_data.z[ii])
            self.lambda_c_red = self.color_law.reduce(self.lambda_c)

        # initialize degree of the spectral recalibration polynomial
        self._init_spectral_polynomial()

        # initialize model basis and model parameter vector
        # model component: bases, color law, and parameter vector
        self._init_bases(wl_grid, phase_grid,
                         wl_range, phase_range, basis_knots)

        # OK. For now, the color scatter and the calibration scatter
        # are explicitely instantiated in the model constructor
        self.error_snake_model = None
        self.calib_error_model = None
        self.color_scatter_model = None

        # finally, it is better to have it here.
        # NOTE: if there are spectra, the model must be evaluated for them.
        # even if they are marked as invalid
        self.recal_func = None
        if self.training_dataset.spec_data is not None:
            self.recal_func = \
                spectra.SpectrumRecalibrationPolynomials(self.training_dataset, self,
                                                 self.recalibration_degree)

        # initialize the global model parameters (M0, M1, CL)
        if init_from_salt2_file:
            self.init_from_salt2(init_from_salt2_file)
        else:
            self.pars = self.init_pars()
        # why ?
        # self.pars0 = self.pars.full.copy()

        # some of the classes gravitating around the model
        # the constraints for example, sometimes need to have
        # access to the index of some paramters in the full parameter
        # vector (all parameters released)
        self.all_pars_released = self.pars.copy()
        self.all_pars_released.release()

        # initialize the SN specific parameters (X0, X1, col, tmax)
        if init_from_training_dataset:
            self.init_from_training_dataset()

        # finalize the initialization of the error models
        # which need a fully operational parameter vector
        if self.calib_error_model is not None:
            self.calib_error_model.finalize()

        # we use a default model normalization
        # this is what guarantees that the SALT2.4 absolute mag
        # is -19.5 in the SWOPE::B band. Of course, this default
        # normalization may be changed explicitely, by calling
        # self.renorm(band_name=, Mb=, magsys='AB')
        self.norm = self.normalization(band_name=normalization_band_name,
                                       default_norm=1.01907246e-12)

        # grams
        self.init_grams_and_cc_grid()

        # and finally, prepare the computing units
        self.queue = self._init_computing_units()

        # clear the cache
        self.clear_cache()

        # if we need to run queue units separately,
        # could be useful to disable caching of the results
        self.disable_cache = False

    def register_variance_models(self, **kwargs):
        """register the (optional) error models

        Parameters
        ----------
        error_snake: salt2.variancemodels.ErrorSnake
          error snake
        calib: salt2.variancemodels.ExternalizedPrior
          calibration error model
        color_scatter: salt2.variancemodels.ExternalizedPrior
          color scatter model
        """
        self.error_snake_model = kwargs.get('error_snake', None)
        self.calib_error_model = kwargs.get('calib', None)
        self.color_scatter_model = kwargs.get('color_scatter', None)
        self.pars = self.init_pars()
        if self.color_scatter_model:
            self.color_scatter_model.update_pars(self.pars)
        if self.calib_error_model:
            self.calib_error_model.update_pars(self.pars)
        if self.color_scatter_model:
            self.color_scatter_model.update_pars(self.pars)

    def clone(self, training_dataset):
        """return a clone (same basis, same color law) for a different tds
        """
        ret = SALT2Like(training_dataset,
                        phase_range=self.phase_range,
                        wl_range=self.wl_range,
                        basis_knots=self.basis_knots,
                        basis_filter_knots=self.basis_filter_knots,
                        spectrum_recal_degree=self.spectrum_recal_degree,
                        normalization_band_name=self.normalization_band_name,
                        error_snake_model=self.error_snake_model,
                        calib_error_model=self.calib_error_model,
                        color_scatter_model=self.color_scatter_model)
                        #  calib_variance=self.calib_variance)
        for block_name in ['M0', 'M1', 'CL']:
            ret.pars[block_name].full[:] = self.pars[block_name].full[:]
        ret.norm = ret.normalization(band_name=ret.normalization_band_name)

        return ret

    def get_gram_dot_filter(self, band_name=None):
        """Used by the integral constraints
        """
        try:
            key = band_name if band_name is not None else self.normalization_band_name
            coeffs, _ = self.filter_db[key]
        except:
            key = 'standard::b'
            coeffs, _ = self.filter_db[key]
        return self.gram.dot(coeffs)

    def init_from_salt2_old(self, model_name, version=None):
        """Load & adapt the SALT2.4 global surfaces and color law.

        Load the coefficients of the SALT2.4 surfaces and color law. The
        definition of the model spline bases differs from the original
        definition of the SALT2.4 bases; so, we reproject the original SALT2
        surfaces on the model basis.

        Parameters
        ----------
        salt2_filename : str
        the classical salt2.npz filename containing the definition of the
        SALT2.4 bases, M0, M1 surfaces and color_law.
        """
        f = np.load(salt2_filename)
        phase_grid = f['phase_grid']
        wl_grid = f['wl_grid']
        basis = bspline.BSpline2D(wl_grid, phase_grid, x_order=4, y_order=4)

        if stick_to_original_model:
            # don't remember why we have this
            self.delta_phase = +0.7
            self.basis = basis
            self.pars = self.init_pars()
            self.pars['M0'].full[:] = f['M0'].T.ravel()
            self.pars['M1'].full[:] = f['M1'].T.ravel()
            self.pars['CL'].full[:] = f['CL_pars'][0:4]
            return

        # TODO: replace this with
        # xx = self.basis.bx.grid
        # yy = self.basis.by.grid
        xx = np.linspace(wl_grid[0], wl_grid[-1], basis.bx.nj)
        yy = np.linspace(phase_grid[0], phase_grid[-1], basis.by.nj)
        x,y = np.meshgrid(xx,yy)
        x,y = x.ravel(), y.ravel()
        jac = self.basis.eval(x,y).tocsr()
        factor = cholesky_AAt(jac.T, beta=1.E-6)

        # and initialize the parameters
        self.pars = self.init_pars()
        self.pars['M0'].full[:] = factor(jac.T * f['M0'])
        self.pars['M1'].full[:] = factor(jac.T * f['M1'])
        self.pars['CL'].full[:] = f['CL_pars'][0:4]
    
    def init_from_salt2(self, salt2_filename, stick_to_original_model=False):
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
        
        #f = np.load(salt2_filename)
        #phase_grid = f['phase_grid']
        #wl_grid = f['wl_grid']
        
        #phase_grid = salt2_source._phase
        #wl_grid = salt2_source._wave
        
        
        phase_grid = np.linspace(self.phase_range[0], self.phase_range[1], self.n_ph)
        wl_grid = np.linspace(self.wl_range[0], self.wl_range[1], self.n_wl)
        basis = bspline.BSpline2D(wl_grid, phase_grid, x_order=4, y_order=4)
        
        phase_salt = salt2_source._phase
        wl_salt = salt2_source._wave
        
        w, p = np.meshgrid(wl_salt, phase_salt)
        
        sncosmo_scale = salt2_source._SCALE_FACTOR
        salt2_m0 = salt2_source._model['M0'](phase_salt, wl_salt).ravel() #/ sncosmo_scale
        salt2_m1 = salt2_source._model['M1'](phase_salt, wl_salt).ravel() #/ sncosmo_scale
        salt2_cl = np.array(salt2_source._colorlaw_coeffs)[::-1]
        
        jac = self.basis.eval(w.ravel(), p.ravel())
        factor = cholesky_AAt(jac.T, beta=1.E-1)

        # and initialize the parameters
        self.pars = self.init_pars()
        
        
        self.pars['M0'].full[:] = factor(jac.T * salt2_m0)
        self.pars['M1'].full[:] = factor(jac.T * salt2_m1)
        self.pars['CL'].full[:] = salt2_cl
    
    
    def reduce(self, wl):
        return self.color_law.reduce(wl)

    def _instantiate_error_model(self, error_model_type):
        if error_model_type is None:
            return None
        if type(error_model_type) == tuple:
            cls, args = error_model_type
            return cls(self, **args)
        if type(error_model_type) == type:
            return error_model_type(self)
        raise TypeError('arg should either be: None|(model_class, (args))|(model_class)')

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
        performed by the model itself.  What the model can do, is to return the
        description of the fit parameter blocks it knows about.
        """
        nb_sne = self.training_dataset.nb_sne(valid_only=False)
        # nb_spectra = self.training_dataset.nb_spectra()
        # nb_passbands = len(self.bands)
        spec_recalibration_npars = self.recalibration_degree + 1
        nb_lightcurves = self.training_dataset.nb_lcs(valid_only=False)
        d = [('X0',   nb_sne),
             ('X1',   nb_sne),
             ('col',  nb_sne),
             ('tmax', nb_sne),
             ('M0',   self.basis.bx.nj * self.basis.by.nj),
             ('M1',   self.basis.bx.nj * self.basis.by.nj),
             ('CL',  4)]
        if self.training_dataset.spec_data is not None:
            d.append(('SpectrumRecalibration', spec_recalibration_npars.sum()))
        return d

    def init_pars(self):
        """instantiate a fit parameter vector

        Returns
        -------
        fp : nacl.lib.fitparameters.FitParameters
            Model parameters.
        """
        p_struct = self.get_struct()
        if self.calib_error_model is not None:
            p_struct.extend(self.calib_error_model.get_struct())
        if self.color_scatter_model is not None:
            p_struct.extend(self.color_scatter_model.get_struct())
        if self.error_snake_model is not None:
            p_struct.extend(self.error_snake_model.get_struct())
        fp = FitParameters(list(set(p_struct)))

        # minimal initialization
        fp['X0'].full[:] = 1.
        if 'SpectrumRecalibration' in fp._struct:
            assert self.recal_func is not None
            fp['SpectrumRecalibration'].full[:] = self.recal_func.init_pars()
        return fp

    def init_from_training_dataset(self):
        """load initial sn parameters from the training dataset
        """
        sn_data = self.training_dataset.sn_data
        self.pars['X0'].full[sn_data.sn_index] = sn_data.x0
        self.pars['X1'].full[sn_data.sn_index] = sn_data.x1
        self.pars['col'].full[sn_data.sn_index] = sn_data.col
        self.pars['tmax'].full[sn_data.sn_index] = sn_data.tmax

    def _init_spectral_polynomial(self):
        """instantiate the recalibration polynomials

        if a degree is specified, all spectra have the same degree. Since the
        degree of the polynomial must not exceed the number of Light curves :
        this degree is large odd number inferior to the numbers of light curves
        for this SN.
        """
        # note: the model is evaluated on the full dataset.
        # not just the valid data.
        nb_spectra = self.training_dataset.nb_spectra(valid_only=False)
        self.recalibration_degree = np.full(nb_spectra, self.spectrum_recal_degree)

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

    @property
    def noise_models(self):
        """return a list of all the noise models contained by the model
        """
        ret = [self.calib_error_model,
               self.color_scatter_model,
               self.error_snake_model]
        return list(filter(lambda x: x is not None, ret))

    def normalization(self, band_name='SWOPE::B', Mb=-19.5, magsys='AB',
                      default_norm=None):
        """model normalization

        The SALT2Like normalization is set during training by the constraint
        on the integral of M0 at phase zero.

        Therefore, by default, we do not renormalize the model during
        evaluation.
        """
        try:
            tq, filter_basis = self.filter_db[band_name]
        except:
            tq, filter_basis = self.filter_db['standard::b']
        phase_eval = self.basis.by.eval(np.array([0. + self.delta_phase])).tocsr()
        gram = get_gram(z=0., model_basis=self.basis.bx,
                        filter_basis=filter_basis, lambda_power=1)
        surface_0 = self.pars['M0'].full.reshape(len(self.basis.by), -1)
        # evaluate the integral of the model in the specified band
        self.int_M0_phase_0 = phase_eval.dot(surface_0.dot(gram.dot(tq)))

        # AB flux in the specified band
        try:
            ms = MagSys(magsys)
            zp = ms.ZeroPoint(self.filter_db.transmission_db[band_name])
        except:
            m_AB = sncosmo.ABMagSystem()
            band = sncosmo.get_bandpass('standard::b')
            zp = -2.5*np.log10(m_AB.zpbandflux(band))
            
        self.int_ab_spec = 10**(0.4 * zp)

        # normalization quantities
        self.flux_at_10pc = np.power(10., -0.4 * (Mb-zp))
        self.flux_at_10Mpc = np.power(10., -0.4 * (Mb+30.-zp))

        if default_norm is not None:
            return default_norm

        return self.flux_at_10Mpc / self.int_M0_phase_0
        #return 1.

    def renorm(self, band_name='SWOPE::B', Mb=-19.5, magsys='AB'):
        """Adjust the model normalization
        """
        # explicitely recompute a normalization
        self.norm = self.normalization(band_name, Mb, magsys,
                                       default_norm=None)

    def _init_computing_units(self):
        """Prepare and queue all the computing units

        The model evaluation is deferred to two kinds of so-called
        'eval units'.

            - Photometric eval units, which compute the light curves
              (i.e. the integral of the SALT2 surfaces). In our current
              design, a Photometric eval unit predicts the lightcurve
              for a given SN in a given band.
            - Spectroscopic eval units, which predict SN spectra.
              In our current design, a spectroscopic eval unit
              predicts one spectrum for a given SN.

        All units are grouped in a single execution queue.

        .. note:: we designed things like this because we had some
             hope that we could gain in speed from using explicit
             parallelism (using joblib or some similar framework).  In
             practice, it seems that the overheads from using python
             parallelism at this level are high (because of the GIL)
             and that we gain much more by using numpy/scipy implicit
             multithreading. We stick to this design because it makes
             things clearer in fact.

        """
        # n_lc_meas, n_spec_meas, n_spectrophot_meas = \
        #     self.training_dataset.nb_meas(valid=True, split_by_type=True)
        queue = []
        if self.training_dataset.lc_data is not None:
            for lc in self.training_dataset.lcs:
                queue.append(lightcurves.LightcurveEvalUnitTz(lc, self))
        if self.training_dataset.spec_data is not None:
            queue.append(spectra.SpectrumEvalUnitFast(self.training_dataset, self))
        if self.training_dataset.spectrophotometric_data is not None:
            queue.append(spectra.SpectroPhotoEvalUnit(self.training_dataset, self))
        return queue

    def update_computing_units(self, ilc=None, spec=False):
        """
        Recreate the model queue as a function of the wanted LCs and spectra.

        Parameters
        -------
        ilc : None or int
            If None all light curve are evaluated, else only teh desired one.
        spec : bool
            Whether Spectra need to be evaluated.

        Returns
        -------
        queue : list
            The new queue
        """
        queue = []
        if ilc is not None:
            for lc in [self.training_dataset.lcs[ilc]]:
                queue.append(lightcurves.LightcurveEvalUnitTz(lc, self))
        if spec:
            queue.append(spectra.SpectrumEvalUnitFast(self.training_dataset, self))
        return queue

    def clear_cache(self):
        """
        Clear model evaluation, derivatives and timing.
        """
        self.val = []
        self.jacobian_i = []
        self.jacobian_j = []
        self.jacobian_val = []
        self.timing = []

    def precompute_color_law(self, cl_pars=None, jac=False):
        """
        Precompute the color law for the photometric data.

        Parameters
        -------
        cl_pars : None or numpy.array
            Color law parameters
        jac : bool
            If derivatives are needed.
        """
        if cl_pars is None:
            cl_pars = self.pars['CL'].full

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

    def get_restframe_phases(self, data):
        """
        Given a chunk of data, return the restframe phases

        Returns
        -------
        numpy.array
            data SN-restframe phase
        """
        sn_index = data.sn_index
        tmax = self.pars['tmax'].full[sn_index]
        return (data.mjd - tmax) / (1.+data.z)

    def __call__(self, p, jac=False, plotting=False, ilc_plot=None, spec_plot=False):
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

        plotting : bool
            Plotting need to evaluated only some data [plotting needs]
        ilc_plot : list
            Light curves to be evaluated [plotting needs]
        spec_plot : bool
            Spectra to be evaluated [plotting needs]

        Returns
        -------
        val : numpy.array
            model results
        jacobian : scipy.sparse.csr_matrix
            jacobian matrix (if jac is true)
        """
        # update pars
        #self.pars.free = p.free

        # pre-evaluate the color law (shared between all light curves)
        self.precompute_color_law(jac=jac)

        # precompute the values of the phase basis on the full dataset
        # significantly faster that way
        if self.training_dataset.lc_data is not None:
            restframe_phases = self.get_restframe_phases(self.lc_data)
            self.phase_eval = self.basis.by.eval(restframe_phases + self.delta_phase).tocsr()
            if jac:
                self.dphase_dtmax = self.basis.by.deriv(restframe_phases + self.delta_phase).tocsr()
            else:
                self.dphase_dtmax = None

        self.clear_cache()

        # queue all Eval Unit for minimization or for plotting
        if plotting:
            queue = self.update_computing_units(ilc=ilc_plot, spec=spec_plot)
        else:
            queue = self.queue

        # now, we are ready to loop over the eval units
        for q in queue:
            q(jac)
        val = np.hstack(self.val)

        if not jac:
            return val

        # collect and assemble the results
        # n_data = len(self.training_dataset.lc_data)  + len(self.training_dataset.spec_data)
        n_data = self.training_dataset.nb_meas(valid_only=False)

        # nrl: I don't know what this is for. Commented out.
        # fit_spec = False
        # for ique in self.queue:
        #     if ique.data['spec_id'].mean() != -1:
        #         fit_spec = True

        # if fit_spec:
        #     n_data += len(self.training_dataset.spec_data)

        logging.debug('computing derivatives: hstack...')
        n = len(p.free)
        i = np.hstack(self.jacobian_i)
        j = np.hstack(self.jacobian_j)
        v = np.hstack(self.jacobian_val)
        logging.debug('building coo_matrix...')
        idx = j >= 0  # self.pars.indexof(j) >= 0
        jacobian = scipy.sparse.coo_matrix((v[idx], (i[idx], j[idx])), shape=(n_data, n))
        logging.debug('ok, done.')
        return val, jacobian


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


