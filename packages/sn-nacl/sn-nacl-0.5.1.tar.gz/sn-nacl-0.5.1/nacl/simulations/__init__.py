"""Simulated training dataset generation framework.

We generate datasets of two kinds:

 - full simulations :
     simulated dataset from a simulated cadence and models of the photometric / spectroscopic instruments.
 - hybrid simulations :
     emulated datasets from real observing logs, and recycling the real SNR of the measurements.

The module provides a generic interface for data generation, from
which all generators should derive.
"""
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)
import numpy as np
from ..dataset import TrainingDataset
from ..models import variancemodels


class SpecUncertainties:
    """The dumbest Spectroscopic error model we can imagine
    """
    def __init__(self, frac=0.05, pedestal=0.01):
        self.frac = frac
        self.pedestal = pedestal

    def __call__(self, sp_data):
        v = np.sqrt(self.frac**2 * sp_data.flux**2  + self.pedestal**2)
        return v


class FluxSimulatorError(Exception):
    pass


class FluxSimulator:
    """Simple class to instantiate a training dataset initialized from a model

    Examples
    --------
    >>> jla = load_training_dataset('JLA')
    >>> model = SALT2Like(jla)
    >>> fs = FluxSimulator(model, reset_uncertainties=False)
    >>> jla_realization = fs(inplace=False, reset_fluxes=False)
    """
    def __init__(self, model,
                 reset_uncertainties=False,
                 reset_valid=False, **kwargs):
        """Constructor - instantiate a model and the rest
        """
        self.model = model
        self.reset_uncertainties = reset_uncertainties
        self.reset_valid = reset_valid

    def update(self, p=None, reset_valid=False, phot_etc=None, spec_etc=None,
               phot_uncertainty_pedestal=None):
        """update the fluxes, and, if requested, the photometric uncertainties
        """
        if reset_valid:
            self.model.training_dataset.reset_valid()

        if p is not None:
            self.model.pars.free = p

        self._update_fluxes()
        if phot_etc is not None:
            self._update_photometric_uncertainties(phot_etc, 
                                                   phot_uncertainty_pedestal=phot_uncertainty_pedestal)
        if spec_etc is not None:
            self._update_spectroscopic_uncertainties(spec_etc)

    def _update_fluxes(self, p=None):
        """Evaluate the model, and update its internal dataset with the fluxes
        """
        if p is None:
            p = self.model.pars.free
        v = self.model(p, jac=False)
        self.model.training_dataset.update_fluxes(v)

    def _can_generate_phot_measurement_uncertainties(self):
        lc_data = self.model.training_dataset.lc_data
        ok = hasattr(lc_data, 'exptime') & lc_data.exptime.all()
        ok &= hasattr(lc_data, 'mag_sky') & lc_data.mag_sky.all()
        ok &= hasattr(lc_data, 'seeing') & lc_data.seeing.all()
        return ok

    def _update_photometric_uncertainties(self, etc, phot_uncertainty_pedestal=None):
        """
        """
        if not self._can_generate_phot_measurement_uncertainties():
            logging.error('unable to generate measurement uncertainties')
            return

        lc_data = self.model.training_dataset.lc_data
        mag = -2.5 * np.log10(lc_data.flux) + lc_data.zp
        instrumental_flux = etc.mag_to_flux(mag, lc_data.band)
        bads = np.isnan(instrumental_flux) | np.isinf(instrumental_flux)
        instrumental_flux[bads] = 1.E-6
        skyflux = etc.mag_to_flux(lc_data.mag_sky, lc_data.band)
        var = etc.flux_variance(exptime=lc_data.exptime,
                                flux=instrumental_flux,
                                skyflux=skyflux,
                                seeing=lc_data.seeing,
                                band=lc_data.band)
        if phot_uncertainty_pedestal is not None:
            var += (phot_uncertainty_pedestal * instrumental_flux)**2
        mag_sigma = np.sqrt(var) / instrumental_flux
        lc_data.fluxerr[:] = mag_sigma * lc_data.flux[:]

        # let's remove the negative fluxes
        lc_data.valid[bads] = 0
        lc_data.fluxerr[bads] = 1000.
        logging.info(f'killed {bads.sum()} photometric data points with negative fluxes')

    def _update_spectroscopic_uncertainties(self, etc):
        """
        """
        spec_data = self.model.training_dataset.spec_data
        fluxerr = etc(spec_data)
        spec_data.fluxerr[:] = fluxerr
        # idx = spec_data.flux <= 0.
        # spec_data.fluxerr[idx] = 1000.
        # spec_data.valid[idx] = 0
        # logging.info(f'killed {idx.sum()} spectroscopic data points with negative fluxes')

    def _add_measurement_noise(self, tds):
        """Add noise to the training dataset passed in argument
        """
        flx = tds.get_all_fluxes()
        sig = tds.get_all_fluxerr()
        noise = np.random.normal(loc=0., scale=sig, size=len(sig))
        bads = tds.get_valid() == 0
        noise[bads] = 0.
        tds.update_fluxes(flx + noise)

    def _apply_noise_models(self, tds):
        """Generate a realization of the model noise and apply it to the fluxes
        """
        N = tds.nb_meas(valid_only=False)
        # nphot, nsp, nspphot = tds.nb_meas(valid_only=False, split_by_type=True)
        noise = np.zeros(N)
        scales = np.ones(N)
        for nm in self.model.noise_models:
            if isinstance(nm, variancemodels.Multiplicative):
                scales *= nm.noise()
            elif isinstance(nm, variancemodels.Additive):
                noise += nm.noise()
            else:
                raise FluxSimulatorError(f'Dont know what to do with {nm.__class__} of noise models')
        flx = tds.get_all_fluxes()
        bads = tds.get_valid() == 0
        nflx = scales * flx + noise
        nflx[bads] = flx[bads]
        tds.update_fluxes(nflx)
#        flx = tds.lc_data.flux
#        bads = tds.lc_data.valid == 0
#        nflx = scales * flx + noise
#        nflx[bads] = flx[bads]
#        tds.lc_data.flux = nflx

    def __call__(self):
        """generate a realization of the current training dataset
        """
        tds = self.model.training_dataset.copy()
        self._apply_noise_models(tds)
        self._add_measurement_noise(tds)
        return tds
