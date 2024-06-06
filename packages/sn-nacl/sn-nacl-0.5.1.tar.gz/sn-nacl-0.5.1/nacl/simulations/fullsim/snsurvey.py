"""Code to generate a simulated training sample from a SN sample and an observing cadence.

  - determine the effective observation log for each supernova
  - generate the SN light curves and spectra
  - add noise to the SN light curves and spectra


"""

import collections.abc
import logging

from numpy.linalg import tensorsolve

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Protocol, Tuple, Union

import astropy.cosmology
import numpy as np
import pandas
import pylab as pl

from ...dataset import TrainingDataset
from ...lib.dataproxy import DataProxy
from ..randutils import draw_from_hist
from . import cadences as cads
from ...handles import SNData, LcData, SpectrumData

class SnSurvey(Protocol):
    """An interface for SnSurveys

    SnSurvey-like objects are given a SN sample and an observing
    log and generate a supernova training sample from that.

    They do not generate fluxes.
    """
    def observe(self):
        """Determine the observation log for each SN
        """
        ...


class ToOVisitor(Protocol):
    def obs_type(self) -> str:
        ...
    def observe(self, sample) -> pandas.DataFrame:
        ...


class StandardSpectroscopicObservations(ToOVisitor):

    def __init__(self, frac_sne_with_spectra=1., n_obs_per_sn=1, z_range=None, wl_range=(3000., 8000.), wl_step=10., nsn=None):
        """Constructor

        Parameters
        ----------
        frac_sne_with_spectra : float, optional
            the fraction of SNe with spectra, by default 1.
        n_obs_per_sn : int, optional
            number of spectra per SN, by default 1
        z_range : tuple[float,float], optional
            selection range, by default None
        wl_range : tuple[float,float], optional
            observer-frame wavelength range (for the spectra), by default (3000., 8000.)
        wl_step : float, optional
            wavelength step in math::`\AA`, by default 10.
        nsn : int, optional
            _description_, by default None
        """
        self.frac_sne_with_spectra = frac_sne_with_spectra
        self.n_obs_per_sn = n_obs_per_sn
        self.z_range = z_range
        self.wl_range = wl_range
        self.wl_step = 10. # \AA
        self.nsn = nsn

    def obs_type(self) -> str:
        return 'spectra'

    def _select(self, sample):
        """Select the subsample to process

        A visitor may visit only a subsample of full sample, the selection
        criterion being specific to the visitor.

        Parameters
        ----------
        sample : pandas.DataFrame
            the original SN sample

        Returns
        -------
        pandas.DataFrame
            the selected SN subsample.
        """
        z_min, z_max = self.z_range if self.z_range is not None else (0., 2.)
        idx = (sample.z>=z_min) & (sample.z<=z_max)
        if isinstance(sample, DataProxy):
            s = sample.nt[idx]
        else:
            s = sample[idx]
        if self.nsn is not None:
            observed = s.sample(self.nsn, replace=False)
        else:
            observed = s.sample(frac=self.frac_sne_with_spectra, replace=False)
        return observed

    def _obs_date(self, sample):
        """Generate the (observer frame) obs dates for all the spectra.

        Parameters
        ----------
        sample : pandas.DataFrame
            _description_

        Returns
        -------
        numpy.ndarray of floats
            the (observer frame) observation dates for all the spectra.

        .. note:: Guy was using np.random.gumbel(-2, 8.) to generate
                  the spectrum restframe phase.  I think gumbel(0,6)
                  is probably more realistic.
        """
        N = len(sample)
        ph = np.random.gumbel(0, 6, N)
        return ph * (1+sample.z) + sample.tmax

    def _obs_dataset(self, sample, mjd):
        """generate the dataset (skeleton) for the observations performed by this visitor

        Parameters
        ----------
        sample : pandas.DataFrame
            the SN sample to process

        Returns
        -------
        pandas.DataFrame
            the dataset containing all the observations performed by this visitor.
        """
        wl_min, wl_max = self.wl_range
        obs_wl = np.arange(wl_min, wl_max+0.5*self.wl_step, self.wl_step)
        N = len(obs_wl)
        nsn = len(sample)
        # logging.info(f' -> N={N}, nsn={nsn}')

        df = pandas.DataFrame({
            'mjd': np.repeat(mjd, N),
            'flux': np.zeros(N*nsn),
            'fluxerr': np.zeros(N*nsn),
            'wavelength': np.tile(obs_wl, nsn),
            'sn': sample.sn.repeat(N),
            'spec': np.repeat(np.arange(0, nsn), N),
            'valid': 1,
            })
        return df

    def observe(self, sample):
        """generate the observations

        Parameters
        ----------
        sample : pandas.DataFrame
            the SNe to be observed

        Returns
        -------
        pandas.DataFrame
            spectral data
        """
        logging.info(f'StandardSpectroscopicObservations.observe: nsn={len(sample)}')
        # select the SNe to be observed
        observed = self.observed = self._select(sample)
        logging.info(f'{len(observed)} spectra to generate')
        mjd = self._obs_date(observed)
        sp_data = self._obs_dataset(observed, mjd)
        return sp_data


class FieldBasedSNSurvey:
    """
    Utility class to build a `TrainingDataset` from a sample, an observation log
    and a series of ToO visitors. The fluxes and errors are not generated: this
    is the job of FluxSim
    """

    def __init__(self, sample, obslog, visits=None, restframe_phase_range=(-20., 40.)):
        """Constructor

        Parameters
        ----------
        sample : pandas.DataFrame
            The supernova sample
        obslog : pandas.DataFrame
            The observation log
        visits : List[Visits], optional
            The list of visitors implementing ToO observations, by default None
        restframe_phase_range : tuple, optional
            observations restricted to this phase range, by default (-20., 40.)

        .. todo :: add a utility method to uniformize the things
                (e.g. add a valid field etc.)
        """
        # since we are trashing the sample and obslog, let's work on copies
        # they are not that big anyways.
        s = sample.copy()
        s['valid'] = 1
        self.sample = DataProxy(s, z='z', field='field', tmax='tmax', sn='sn')
        self.sample.add_field('fmjd', self.sample.field * 100000 + self.sample.tmax)

        # we copy the obslog, since we are going to trash it
        o = obslog.sort_values(['field', 'mjd'])
        # o['sn'] = -1
        self.obslog = DataProxy(o, field='field', mjd='mjd')
        self.obslog.add_field('fmjd', self.obslog.field * 100000 + self.obslog.mjd)

        self.visits = visits
        self.restframe_phase_range = restframe_phase_range

        # self.too_obs = {'spectra': [], 'lcs': []}
        self.lcs = []
        self.spectra = []

    def observe(self):
        """generate the structure of the training dataset.

        i.e. determine the observation log for each SN. The core of
        the photometric followup is determine from the observation log
        passed to the class.

        Then, additional observations are generated using a strategy
        analog to a ToO-like mode: the subsample of objects with
        additional follow-up is selected, the additional follow-up
        observations are then generated and added to the main
        observation log. These selection and generation are performed
        by external `Visitor` objects which are passed to the class.

        All spectroscopic observations are generated in Visitor
        mode. Photometric observations (e.g. HST observations) may
        also be generated in this mode.
        """
        self.lcs = []
        self.spectra = []

        z = self.sample.z
        ph_min, ph_max = self.restframe_phase_range

        # generate the photometric observations log from the general cadence
        logging.info('SN observation blocks')
        fmjd_min = 100000 * self.sample.field + self.sample.tmax + (1+z) * ph_min
        i_min = self.obslog.fmjd.searchsorted(fmjd_min)
        fmjd_max = 100000 * self.sample.field + self.sample.tmax + (1+z) * ph_max
        i_max = self.obslog.fmjd.searchsorted(fmjd_max)

        logging.info('building indices')
        nsn = len(self.sample.nt)
        ii, sn_index = [], []
        for i in range(nsn):
            ii.extend(list(range(i_min[i], i_max[i])))
            sn_index.extend([i] * (i_max[i]-i_min[i]))
        sn_index = np.array(sn_index)

        logging.info(f'extracting SN observation log: {len(z)} SNe/{len(ii)} obs')
        lcs = self.obslog.nt.iloc[ii].copy()
        # add missing mandatory fields
        lcs.loc[:,'sn'] = self.sample.nt.sn.iloc[sn_index].to_numpy()
        lcs.loc[:,'lc'] = -1
        lcs.loc[:,'flux'] = 0.
        lcs.loc[:,'fluxerr'] = 0.
        lcs.loc[:,'magsys'] = 'AB'
        lcs.loc[:,'zp'] = 25.
        lcs.loc[:,'valid'] = 1
        # lcs.magsys = lcs.magsys.astype('S10')
        # lcs.band = lcs.band.astype('S20')
        self.lcs.append(lcs)

        # then, the ToO visits (spectro & photometric ToO)
        logging.info('ToO visits')
        if self.visits is not None:
            for v in self.visits:
                if 'spec' in v.obs_type():
                    self.spectra.append(v.observe(self.sample))
                elif 'phot' in v.obs_type():
                    self.lcs.append(v.observe(self.sample))

        # build a Training dataset from the observations
        logging.info('assembling the light curves')
        lcs = pandas.concat(self.lcs)

        # build an index for the light curves
        logging.info('unique identifier for each light curve')
        dp = DataProxy(lcs, sn='sn', band='band')
        dp.make_index('band')
        dp.make_index('sn')
        lcs['lc'] = dp.sn_index * 100 + dp.band_index

        logging.info('assembling the spectra')
        spectra = pandas.concat(self.spectra) if self.spectra else None

        logging.info('Building the training dataset')
        tds = TrainingDataset(self.sample.nt, lc_data=lcs, spec_data=spectra)
        logging.info('done.')

        # we do not need a local copy of the lcs and spectra
        del self.lcs
        del self.spectra

        return tds

class HealpixSNSurvey(SnSurvey):

    def __init__(self, sample, obslog, model):
        self.sample = sample
        self.obslog = obslog
        self.model = model

