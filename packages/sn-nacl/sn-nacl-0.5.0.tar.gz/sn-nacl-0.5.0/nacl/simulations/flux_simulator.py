import logging
import numpy as np
import pickle

from nacl.lib.instruments import MagSys

from ..models.salt import SALT2Like
from ..lib import bspline
from . import etc, reindex
from ..dataset import TrainingDataset


try:
    from sksparse.cholmod import cholesky_AAt
except ImportError:
    from scikits.sparse.cholmod import cholesky_AAt

NORM_SNSIM = 290090.4311080577

class FluxSimulatorError(Exception): pass

#
# replaced by a CalibrationScatter variance model
#
# class CalibrationNoise:
#     """Hold a description of the calibration uncertainties & generate offsets
#     """
#     def __init__(self, bands, calib_variance):
#         """Constructor

#         Parameters
#         ----------
#         covmat : float or np.ndarray or np.matrix
#             calibration uncertainties
#         bands : List[str]
#             the band order
#         """
#         self.bands = bands
#         self.band_index = dict([(b,i) for i,b in enumerate(bands)])
#         N = len(self.bands)

#         #
#         if isinstance(calib_variance, float):
#             self.covmat = np.diag(np.full(N, calib_variance))
#         elif isinstance(calib_variance, np.ndarray):
#             if calib_variance.ndim == 1:
#                 assert(len(calib_variance) == N)
#                 self.covmat = np.diag(calib_variance)
#             elif calib_variance.ndim == 2:
#                 self.covmat = calib_variance

#     def __call__(self, bands):
#         L = np.linalg.cholesky(self.covmat)
#         N = len(self.bands)
#         dm = L @ np.random.normal(0., 1., size=N)
#         idx = self.band_index
#         return np.array([dm[idx[b]] for b in bands])


class SpecUncertainties:
    def __init__(self, frac=0.05, pedestal=0.01):
        self.frac = frac
        self.pedestal = pedestal

    def __call__(self, sp_data):
        v = np.sqrt(self.frac**2 * sp_data.flux**2  + self.pedestal**2)
        return v


class FluxSimulator:
    """Update simulated fluxes and (optionally) simulated flux uncertainties
    """

    def __init__(self, model,
                 seed=None, phase_range=(-15., 45.), wl_range=(2000., 9000.),
                 basis_knots=[127, 20],
                 salt2_filename=None, stick_to_original_salt2_model=False,
                 error_snake=None, color_scatter=None, calib_scatter=None,
                 instrument_model=None, phot_uncertainty_pedestal=0.01,
                 magsys_name='AB',
                 spec_uncertainty_func=SpecUncertainties(),
                 measurement_noise=True):

        self.model = model
        self.training_dataset = model.training_dataset
        self.phase_range = phase_range
        self.wl_range = wl_range
        self.basis_knots = basis_knots
        self.salt2_filename = salt2_filename
        self.stick_to_original_salt2_model = stick_to_original_salt2_model
        self.instrument_model = instrument_model
        self.phot_uncertainty_pedestal = phot_uncertainty_pedestal
        self.spec_uncertainty_func = spec_uncertainty_func
        self.measurement_noise = measurement_noise
        # self.gamma_init=gamma_init
        # self.eta_covmatrix=eta_covmatrix
        # self.sigma_kappa_init=sigma_kappa_init

        # reset the seed -- if None, reset the generator with fresh,
        # unpredictable entropy
        np.random.seed(seed=seed)

        # initialize a model and an error model
#        self.model = SALT2Like(self.training_dataset,
#                               phase_range=self.phase_range, wl_range=self.wl_range, basis_knots=self.basis_knots,
#                               init_from_salt2_file=salt2_filename)
        self.pars = self.model.pars.copy()
        # self.model.init_pars(salt2_filename=self.salt2_filename, stick_to_original_salt2_model=self.stick_to_original_salt2_model)

        self.error_snake = error_snake
        self.color_scatter = color_scatter
        self.calib_scatter = calib_scatter

        # TODO: here, we assume that the fluxes are all in the same system
        # normally, this is the case (I hope).
        # self.load_zero_points()

    def load_truth_from_tds(self):
        """load the true parameters stored in the training dataset.

        The training dataset contains the true SN (X0,X1,col,tmax)
        parameters (if pure simulation) or estimates of these parameters
        (if JLA or K21). This methods updates the model parameters vector
        from these values.

        """
        sn_data = self.training_dataset.sn_data
        self.pars['X0'].full[sn_data.sn_index] = sn_data.x0
        self.pars['X1'].full[sn_data.sn_index] = sn_data.x1
        self.pars['col'].full[sn_data.sn_index] = sn_data.col
        self.pars['tmax'].full[sn_data.sn_index] = sn_data.tmax
        self.model.pars.full[:] = self.pars.full[:]

    def load_zero_points(self):
        """load the instrument zero points (magsys_name -> instrumental fluxes)

        If an instrument model has been specified to simulate the measurement
        uncertainties, then we need to translate the calibrated fluxes stored
        in the training dataset into instrumental fluxes. To do this, we
        compute the magsys zero points for each instrumental band in the
        dataset and generate a zp vector.

        """
        tds = self.training_dataset
        zp = np.zeros(tds.nb_bands())
        for b in tds.transmissions:
            magsys = MagSys(tds.filter_sys[b])
            zp[tds.lc_data.band_map[b]] = magsys.ZeroPoint(tds.transmissions[b])
        self.zp = zp[tds.lc_data.band_index]

    def update_fluxes(self):
        """Instantiate a model/errormodel and compute the fluxes and fluxerrs

        """
        # to evaluate the model, we need to know the target instrument


        # evaluate the model
        v = self.model(self.pars.free, jac=False)
        self.sigma_lc = np.abs(self.model.training_dataset.lc_data.fluxerr) /\
            np.abs(self.model.training_dataset.lc_data.flux)
        self.sigma_sp = np.abs(self.model.training_dataset.spec_data.fluxerr) /\
            np.abs(self.model.training_dataset.spec_data.flux)

        # and update the flux fields of the tds (in place)
        N = len(self.training_dataset.lc_data)
        self.training_dataset.lc_data.flux[:] = v[:N]
        self.training_dataset.spec_data.flux[:] = v[N:]
        self.training_dataset.lc_data.fluxerr[:] = np.abs(v[:N]*self.sigma_lc)
        self.training_dataset.spec_data.fluxerr[:] = np.abs(v[N:]*self.sigma_sp)

    def _can_generate_phot_measurement_errors(self):
        lc_data = self.training_dataset.lc_data
        ok = self.instrument_model is not None
        ok &= hasattr(lc_data, 'exptime') & lc_data.exptime.all()
        ok &= hasattr(lc_data, 'mag_sky') & lc_data.mag_sky.all()
        ok &= hasattr(lc_data, 'seeing') & lc_data.seeing.all()
        return ok

    def update_photometric_uncertainties(self):
        """evaluate the measurement noise and update the lc_data
        """
        lc_data = self.training_dataset.lc_data
        # if an instrument model, along with the necessary information
        # are available, we can simulate flux uncertainties
        if self._can_generate_phot_measurement_errors():
            mag = -2.5 * np.log10(lc_data.flux) + lc_data.zp # self.zp
            # # we need to do something about the negative fluxes
            # negative_fluxes = np.isnan(mag)
            # mag[negative_fluxes] = 40.
            self.mag = mag
            instrumental_flux = self.instrument_model.mag_to_flux(mag, lc_data.band)
            # for negative or zero fluxes, we decide that the instrumental flux is zero
            instrumental_flux[np.isnan(instrumental_flux) | np.isinf(instrumental_flux)] = 0.
            self.instrumental_flux = instrumental_flux
            skyflux = self.instrument_model.mag_to_flux(lc_data.mag_sky, lc_data.band)
            var = self.instrument_model.flux_variance(exptime=lc_data.exptime,
                                                      flux=instrumental_flux, skyflux=skyflux,  # norm snsim ?
                                                      seeing=lc_data.seeing, band=lc_data.band)
            # now, go back to the calibrated fluxes
            # all we need to know
            mag_sigma = np.sqrt(var) / instrumental_flux
            lc_data.fluxerr[:] = mag_sigma * lc_data.flux[:]

            # dealing with the negative fluxes
            idx = np.isnan(mag) | np.isinf(mag)
            lc_data.fluxerr[idx] = 1000.
            lc_data.valid[idx] = 0
            logging.info(f'killed {idx.sum()} photometric data points with negative fluxes')
        # if not, this means that we need to rely on the flux uncertainties
        # stored in the training dataset. Let's check that they are non zero
        elif not (lc_data.fluxerr > 0).all():
            raise FluxSimulatorError('can neither rely on existing flux uncertainties nor generate new ones')

    def update_spectroscopic_uncertainties(self):
        # we don't have spectroscopic exposure time calculators
        # for now, so, the uncertainty is just a fraction of the flux
        spec_data = self.training_dataset.spec_data
        if self.spec_uncertainty_func is not None:
            # fluxerr = np.abs(self.sigma_spec * spec_data.flux)
            fluxerr = self.spec_uncertainty_func(spec_data)
            spec_data.fluxerr[:] = fluxerr
            idx = spec_data.flux <= 0.
            spec_data.fluxerr[idx] = 1000.
            spec_data.valid[idx] = 0
            logging.info(f'killed {idx.sum()} spectroscopic data points with negative fluxes')
        elif not (spec_data.fluxerr > 0).all():
            raise FluxSimulatorError('can neither rely on existing spec uncertainties nor generate new ones')

    def add_measurement_noise(self):
        N = len(self.training_dataset.lc_data)
        noise = np.random.normal(scale=self.training_dataset.lc_data.fluxerr, size=N)
        noise[self.training_dataset.lc_data.valid == 0] = 0.
        self.training_dataset.lc_data.flux += noise
        N = len(self.training_dataset.spec_data)
        noise = np.random.normal(scale=self.training_dataset.spec_data.fluxerr, size=N)
        noise[self.training_dataset.spec_data.valid == 0] = 0.
        self.training_dataset.spec_data.flux += noise

    def add_error_snake_noise(self):
        """generate a realization of the error snake noise.

        If an error snake has been specified, this function generates
        a realization of it. If `self.error_snake==None` does nothing.

        .. note: modifies the data in-place
        """
        # here, we call the error model and compute the error snake
        # contribution to the variance for each data point
        if self.error_snake is None:
            return
        lc_data = self.training_dataset.lc_data
        mod_err=self.error_snake(self.model)
        self.pars['gamma']=self.gamma_init
        var = mod_err(self.pars.free)
        lc_data.add_field('error_snake_sigma', np.sqrt(var))
        noise = np.random.normal(scale=var, size=len(lc_data))
        # noise = np.random.normal(scale=np.sqrt(var))
        lc_data.add_field('error_snake_noise', noise)
        lc_data.flux += noise
        # sig = np.zeros(len(lc_data))
        # var = self.error_model(self.error_model.pars.free, self.model.pars.free)
        # lc_data.add_field('error_snake_sigma', np.sqrt(var))

    def add_calibration_noise(self):
        """generate a realization of the calibration noise.

        If some calibration noise has been specified, then
        generate a realization of it and add it to the data.
        If not, does nothing.

        .. note: modifies the data in-place.
        """
        if self.calib_scatter is None:
            return
        lc_data = self.training_dataset.lc_data

        # mod_err=self.calib_scatter(self.model,self.eta_covmatrix)
        noise = mod_err.noise(self.pars.free)
        lc_data.add_field('calibration_noise', noise)
        lc_data.flux *= (1.+noise)

        #Add calibration noise to pars file for each band
        # ind_filt=np.unique(lc_data.band_index,return_index=True)[0][np.argsort(np.unique(lc_data.band_index, return_index=True)[1])]
        # self.pars['eta_calib'][ind_filt]=np.unique(noise,return_index=True)[0][np.argsort(np.unique(noise, return_index=True)[1])]

    def add_color_scatter_noise(self):
        """generate color scatter noise, and add it to the photometric measurements
        """
        if self.color_scatter is None:
            return
        lc_data = self.training_dataset.lc_data
        var = self.color_scatter(self.pars.free)
        # mod_err=self.color_scatter(self.model)
        # self.pars['sigma_kappa']=self.sigma_kappa_init
        # var = mod_err(self.pars.free)
        N = len(var)
        # lc_data.add_field('color_scatter_sigma', np.sqrt(var))
        noise = mod_err.noise(self.pars.free)
        lc_data.add_field('color_scatter_noise', noise)
        #Add color scatter noise to pars file for each LC
        # self.pars['kappa_color'].full[:]=np.unique(noise,return_index=True)[0][np.argsort(np.unique(noise, return_index=True)[1])]
        lc_data.flux *= (1.+noise)

    def __call__(self):
        """_summary_

        Parameters
        ----------
        tds : _type_
            _description_
        pars : _type_
            _description_
        """
        tds = self.training_dataset

        self.update_fluxes()
        self.update_photometric_uncertainties()
        self.update_spectroscopic_uncertainties()
        if self.measurement_noise==True:
            self.add_measurement_noise()
        self.add_error_snake_noise()
        self.add_calibration_noise()
        self.add_color_scatter_noise()

