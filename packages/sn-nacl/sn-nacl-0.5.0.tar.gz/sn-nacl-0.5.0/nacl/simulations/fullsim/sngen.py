"""SN generation.

.. todo :: if many SNe and random name generation,
           add a piece of code to make sure that no name collisions.

"""

import collections.abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Protocol, Tuple, Union

import astropy.cosmology
import numpy as np
import pandas
import pylab as pl

from ..randutils import draw_from_hist

STERADIAN2SQDEG = 180.**2 / np.pi**2


def perret_rate(z):
    """The SNLS SNIa rate according to (Perret et al, 201?)
    """
    rate = 0.17E-4
    expn = 2.11
    my_z = np.copy(z)
    my_z[my_z>1.] = 1.
    return rate * np.power(1+my_z, expn)


def ripoche_rate(z):
    """The SNLS SNIa rate according to the (unpublished) Ripoche et al study.
    """
    rate = 1.53e-4*0.343
    expn = 2.14
    my_z = np.copy(z)
    my_z[my_z>1.] = 1.
    return rate * np.power((1+my_z)/1.5, expn)

# move this into utils.
def random_sn_names(length=10, size=1):
    import string
    letters = np.random.choice(list(string.ascii_lowercase),
                               size=length * size).reshape((size, length))
    names = [''.join(line) for line in letters]
    return names

class DVDzSNGenerator:
    """Generate a SN sample.

    The simplest SN generator possible: the SN redshift distribution follows
    the volume. The supernova X1 and C follow centered normal distributions of
    sigma 1. and 0.1 respectively. The SN luminosity distances are computed
    using the cosmological model passed in argument (LambdaCDM by default).

    This generator ignores the spatial distribution of SNe.
    """

    def __init__(self, cosmo=None, survey_area=1., mjd_range=(0., 150.),
                 z_range=(0., 1.), nsn=None, account_for_edges=False,
                 restframe_phase_range=(-15, 30.), string_ids=True,
                 Mb=-19.0906, alpha=0.13, beta=3, sigma_int=0.0):
        """Constructor

        Parameters
        ----------
        cosmo : cosmology calculator (volumes + distances), optional
            we need to compute the survey volume as a function of z,
            and the SN luminosity distances. If set to `None`, an
            instance of `astropy.cosmology.FlatLambdaCDM` is used.
        survey_area : float, optional
            area covered by the survey (in square-degrees), by default 1.
        mjd_range : tuple(float,float), optional
            survey duration (in days), by default (0., 150.)
        z_range : tuple(float,float), optional
            redshift range, by default (0., 1.)
        nsn : _type_, optional
            number of supernovae to generate, by default None
        account_for_edges : bool, optional
            if `True` discard the SNe with no full
            follow-up because survey season is finite.
            Used only in `number_of_supernovae()` by default False
        restframe_phase_range : tuple(float,float), optional
            defines the "usedful coverage zone", in restframe
            days. Follow-up points outside this zone are not generated.
            If `account_for_edges` is `True`, this range is used to
            compute an "effective survey duration. By default (-15, 30.)
        """
        self.cosmo = cosmo if cosmo is not None else \
            astropy.cosmology.FlatLambdaCDM(H0=70., Om0=0.3)
        self.survey_area = survey_area
        self.mjd_range = mjd_range
        self.dz = 0.01
        self.z_range = z_range
        self.sn_rate = perret_rate
        self.nsn_tot = nsn
        self.account_for_edges = account_for_edges
        self.restframe_phase_range = restframe_phase_range
        self.string_ids = string_ids

        # SN normalization
        self.Mb = Mb
        self.alpha = alpha
        self.beta = beta
        self.sigma_int = sigma_int
        self.flux_at_10pc = np.power(10., -0.4 * self.Mb)
        # was 10^-4 because sncosmo was returning distances in kpc
        # now that we are using astropy, distances are in Mpc
        # self.X0_norm = self.flux_at_10pc * 1.E-10
        #
        self.X0_norm = 100.
        # self.X0_norm = 1.E-10

    def number_of_supernovae(self, **kwargs):
        """Number of supernovae per redshift bin

        .. math::
           N_{SN} = \\Delta t \\int {\\cal R}(z) dV(z)

        Parameters
        ----------
        zbins: numpy.ndarray
          redshift bins
        dz: float
          redshift bin size
        snrate: [default: perret_rate]
          a function giving the SN rate as a function of z

        Returns
        -------
        `numpy.ndarray`
          expected SN number per bin size
        """
        # parameters
        sn_rate = kwargs.get('sn_rate', self.sn_rate)
        survey_area = kwargs.get('survey_area', self.survey_area) / STERADIAN2SQDEG
        dz = kwargs.get('dz', 0.1)
        zmin, zmax = kwargs.get('z_range', self.z_range)
        min_phase, max_phase = kwargs.get('restframe_phase_range',
                                          self.restframe_phase_range)
        z_bins = kwargs.get('z_bins', np.arange(zmin, zmax, dz))
        account_for_edges = kwargs.get('account_for_edges',
                                       self.account_for_edges)

        # comoving volume
        zz = 0.5 * (z_bins[1:] + z_bins[:-1])
        rate = sn_rate(zz)
        dvol = self.cosmo.comoving_volume(z_bins)
        dvol = np.array(dvol[1:] - dvol[:-1])

        # the comoving volume is for the entire celestial sphere.
        # we need to know the fraction of the celestial sphere
        # covered by the survey
        dOmega = survey_area / (4 * np.pi)

        # effective survey duration
        survey_duration = self.mjd_range[1] - self.mjd_range[0]
        if account_for_edges:
            margin = (1.+zz) * (max_phase - min_phase)
            effective_duration = (survey_duration - margin)
            effective_duration[effective_duration <= 0.] = 0.
        else:
            effective_duration = survey_duration

        # the rate is in SN/year/Mpc
        # converting survey duration to years
        effective_duration /= 365.25

        return zz, rate * dOmega * dvol * effective_duration / (1. + zz)

    def _generate_X0(self, dL, x1, col):
        X0 = self.X0_norm / dL**2
        dm = self.alpha*x1 - self.beta*col
        if self.sigma_int is not None:
            dm += np.random.normal(scale=self.sigma_int, size=len(dm))
        X0 *= np.power(10., 0.4*dm)
        return X0

    def generate_sample(self, **kwargs):
        """Generate the SN sample.

        If nsn is None, then the size of the sample is determined by
        the surey solid angle and the redshift range (modulo the
        cosmology). Otherwise, `nsn` supernovae are generated.

        Parameters
        ----------
        z_range: (float,float)
          SN redshift range
        """
        # redshift bins
        zmin, zmax = kwargs.get('z_range', self.z_range)
        dz = kwargs.get('dz', self.dz)
        z_bins = kwargs.get('z_bins', np.arange(zmin, zmax+1.E-6, dz))
        mjd_start, mjd_end = kwargs.get('mjd_range', self.mjd_range)
        nsn_tot = kwargs.get('nsn', self.nsn_tot)

        # number of supernovae
        zz, nsn = self.number_of_supernovae(z_bins=z_bins,
                                            account_for_edges=False, **kwargs)
        if nsn_tot is None:
            nsn_tot = int(nsn.sum())

        # SN sample
        sample = {}
        sample['z'] = draw_from_hist(z_bins, nsn, size=nsn_tot)
        sample['dL'] = self.cosmo.luminosity_distance(sample['z'])
        sample['x1'] = np.random.normal(scale=1., size=nsn_tot)
        sample['col'] = np.random.normal(scale=0.1, size=nsn_tot)
        sample['x0'] = self._generate_X0(sample['dL'],
                                         sample['x1'],
                                         sample['col'])
        sample['tmax'] = np.random.uniform(mjd_start, mjd_end, size=nsn_tot)
        sample['ra'] = 0.
        sample['dec'] = 0.
        sample['field'] = 0
        sample = pandas.DataFrame(sample)
        # finally, we need to generate a unique identificator per SN
        if self.string_ids:
            sample['sn'] = random_sn_names(10, nsn_tot)
        else:
            sample['sn'] = np.array(sample.index)

        return sample
