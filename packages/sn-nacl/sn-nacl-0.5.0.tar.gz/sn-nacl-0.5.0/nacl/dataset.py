# """A set of classes to handle the NaCl training datasets

# The NaCl models are trained on lightcurves and spectra. The TrainingDataset
# objects presents the models with a uniform interface, which allows to
# navigate easily in this hybrid dataset. TrainingDataset objects have three
# main purposes: (1) they maintain the relations between the SN meta
# information (z, identifier, x0, ...) and the related light curves and spectra
# (2) they map the SN, lightcurve or spectra unique ID's (int or str) into
# continuous integer indexes (3) they allow to track whether a data point is
# valid or not (i.e.  whether it should be included in the likelihood
# computation or not) (4) they maintain access to the passband shapes.

# Tests have shown that accessing data stored in a pandas DataFrame is
# significantly slower than slice-based access on raw numpy arrays (by about a
# factor 10 as of writing this code). For this reason, we have decided to keep
# our old implementation and store the data internally into `numpy.recarray`s.
# A TrainingDataset may be passed numpy arrays or pandas DataFrame. The data is
# sorted to ensure that light curves and spectra of a same SN are stored
# contiguously in memory.

# Internals, format
# -----------------

# A TrainingDataset maintains 3 main arrays, encapsulated into
# `nacl.lib.dataproxy.DataProxy`'s objects. The dataproxies maintain the
# contiguous indexing described above, and allow to seamlessly add fields to
# the arrays.

# A) `TrainingDataset` needs 3 inputs: lc_data, spec_data, sne. All the
# elements are dataframes or recarrays

#  `sn_data`: Information regarding the SN. Need at 8 columns.
#   One row corresponds to one SN. The minimal amount of information
#   required is:
#      - sn : a unique identifier (int or str) for the SN.
#        May be the TNS/IAU name
#      - z : heliocentric redshfit
#      - valid : whether the SN (and all its follow-up data) is valid
#      - tmax : time of the maximum in B band
#      - x1 : x1 parameter from SALT2
#      - x0 : x0 parameter from SALT2
#      - c : color parameter from SALT2


# Example of a sn_data row:
#     sn          z         tmax         x1         x0        col       valid
#     b'sn1981b'  0.006030  44672.524515 -0.423846  0.294523  0.042690    1


# B) `lc_data`: a larger array that contains all the photometric follow-up
# points.  Needs at least 9 columns. One row corresponds to one photometric
# point.

#     - sn : sn unique identifier, as specified in `sn_data` (see above)
#     - lc : unique light curve identifier
#     - mjd : observation date (Modified Julian Day)
#     - flux : flux
#     - fluxerr : flux error
#     - band : band name  instrument::filter, e.g STANDARD::B or LSST::g
#     - magsys : magnitude system, e.g., Vega2, AB_B12C,
#     - mag_sky : magnitude of the sky
#     - seeing : seeing of the night
#     - exptime : Exposure time. NaN when you use real data like JLA, K21
#     - valid : 0 or 1. 0 the data point is bad, we do not use it

# Example of Lc_data:
# sn   mjd        flux       fluxerr   band             magsys     exptime  valid    lc	seeing	mag_sys
# 0    44669.300  18.685584  0.913621  b'STANDARD::B'    VEGA2      NaN      1       0	NaN	NaN


# C) `spec_data`: Information regarding the spectroscopy. Need at 8 columns.
#     One row corresponds to one spectrum bin.

#     - sn : sn unique identifier, as specified in `sn_data` (see above)
#     - spec : spectrum unique identifier
#     - mjd : spectrum observation date (Modified Julian Day)
#     - wavelength : observer frame wavelength in Angs
#     - flux : flux
#     - fluxerr : flux error
#     - exptime : Exposure time (seconds) NaN when you use real data
#                 like JLA, K21
#     - valid : 0 or 1. 0 the spectrun data point is bad, we do not use it

# Example of spec_data:
# sn   mjd      wavelength   flux          fluxerr        valid   spec  exptime
# 107  52905.0  3739.254     5.588000e-17  1.792800e-17   1       0     NaN


# Indexes
# -------


# Input/Output
# ------------
# A TrainingDataset may be written on disk in several different formats:
# pickle, numpy:npz (compressed or not) and parquet.  We recommend parquet,
# which seems to offer the best performances in terms of speed and compression.

# # to create a dataset, we just have to pass the sn, lc and spec arrays
# # they can be passed as numpy.recarrays or as pandas.DataFrames
# >>> tds = TrainingDataset(lc_data, spec_data, sample)

# # a dataset can be saved to disk and re-read in several formats.
# # we recommend parquet, but npz and pickle are also available
# >>> tds.to_parquet(name='JLA', path='./')
# >>> tds = nacl.dataset.read_parquet(name='JLA', path='./')

# # it is easy to invalidate data. This functionality is used
# # for example, during outlier removal. The corresponding data entries
# # are just flagged, and subsequently ignored in the likelihood computation.
# >>> tds.kill_sne([58]) # specify the SN unique ID
# >>> tds.kill_lc([729])
# >>> tds.kill_spec([1255, 3280])

# if one want to get rid of the data for real, it is possible
# to use .compress() -- costly however, since it necessitates rebuilding
# the indexes.
# >>> tds.compress()

# .. todo :: add a piece of code in the constructor of TrainingDataset,
#            to make sure that no name collisions
#            (i.e. SN identifier is unique).
# """

import logging
import pathlib
from typing import List
from copy import copy as cp
import re
import pickle

import numpy as np
import pandas

import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt

# from nacl.handles import LcData, SNData, SpectrumData
from saltworks import DataProxy


from sncosmo._registry import Registry
import sncosmo


_TRAINING_DATASETS = Registry()


def get_training_dataset(name, version=None, copy=False):
    """Retrieve a training dataset from the registry

    Parameters
    ----------
    name : str
        Name of training dataset in the registry
    version : str, optional
        version identifier for sources with multiple versions. Default
        is `None` (i.e. latest version)
    copy : bool, optional
       If True, and if `name` already a Source instance, return a copy of it.
    """
    if isinstance(name, TrainingDataset):
        if copy:
            return cp(name)
        else:
            return name
    else:
        return cp(_TRAINING_DATASETS.retrieve(name, version=version))

class TrainingDatasetError(Exception):
    pass


def opt_band_name_order(bn):
    _, band = re.match('(.+)::([ugrizyUBVRIYJHK]+)', bn).groups()
    return 'ugrizyUBVRIYJHK'.index(band)


class TrainingDataset:
    """A class to hold and index the training dataset.

    A typical training dataset contains light curves, spectra, plus
    meta-information to link these light curves and spectra to their respective
    SNe, plus meta information relative to these SNe (e.g. redshift).

    The TrainingDataset is used to organize and index the spectroscopic and
    photometric data and present an abstract interface to the models.

    """

    sn_data_dtype = np.dtype(
        [('index', '<i8'), ('sn', '<i8'), ('z', '<f8'),
         ('tmax', '<f8'), ('x1', '<f8'), ('x0', '<f8'), ('c', '<f8'),
         ('ebv', '<f8'), ('valid', '<i8'), ('IAU', 'O')]
    )

    lc_data_dtype = np.dtype(
        [('index', '<i8'), ('sn', '<i8'),
         ('mjd', '<f8'), ('flux', '<f8'), ('fluxerr', '<f8'),
         ('band', 'O'), ('magsys', 'O'), ('exptime', '<f8'),
         ('valid', '<i8'), ('lc', '<i8'),
         ('zp', '<f8'), ('mag_sky', '<f8'), ('seeing', '<f8'), ('x', '<f8'), ('y', '<f8'), ('sensor_id', '<i8')]
    )

    # was do we need exptime here ?
    spec_data_dtype = np.dtype(
        [('index', '<i8'), ('sn', '<i8'),
         ('mjd', '<f8'), ('wavelength', '<f8'), ('flux', '<f8'), ('fluxerr', '<f8'),
         ('i_basis', '<i8'),
         ('valid', '<i8'), ('spec', '<i8'), ('exptime', '<f8')]
    )

    def __init__(self, sne, lc_data=None, spec_data=None, spectrophotometric_data=None,
                 filterpath=None, spectra=None, lcs=None, filterlib=None, basis=None):
        """load the file, sort by data type (lc/spec) and SN

        Parameters
        ----------
        sne : array-like or DataFrame
            sn catalog (sn, name, z, X0, X1, c...)
        lc_data : recarray or DataFrame
            light curve photometric data.
        spec_data : recarray or DataFrame
            spectra
        spectrophotometric_data : recarray or DataFrame
            spectrophotometric data (e.g. SNIFS spectra)
        """
        sne = _df_to_recarray(sne)
        self.sn_data = DataProxy(sne, sn='sn', z='z',
                                 tmax='tmax', x0='x0', x1='x1', col='c',
                                 valid='valid')

        # at this stage, we convert everything into recarrays in order to
        # minimize the access times. We found indeed that access times
        # to a pandas.DataFrame can be up to an order of magnitude slower
        # than access time to a numpy.recarray
        self.lc_data = None
        self.spec_data = None
        self.spectrophotometric_data = None

        if lc_data is not None:
            lc_data = _df_to_recarray(lc_data, sort_by=['sn', 'band'])
            self.lc_data = DataProxy(lc_data, sn='sn', lc='lc', mjd='mjd',
                                     band='band', exptime='exptime',
                                     magsys='magsys', zp='zp',
                                     mag_sky='mag_sky', seeing='seeing',
                                     flux='flux', fluxerr='fluxerr',
                                     x='x', y='y', sensor_id='sensor_id',
                                     valid='valid')
            self.update_zp_scale()

        if spec_data is not None:
            spec_data = _df_to_recarray(spec_data)  # , sort_by=['sn', 'mjd'])
            self.spec_data = DataProxy(spec_data, sn='sn', spec='spec',
                                       mjd='mjd',
                                       wavelength='wavelength',
                                       flux='flux', fluxerr='fluxerr',
                                       i_basis='i_basis',
                                       valid='valid')

        if spectrophotometric_data is not None:
            spectrophotometric_data = _df_to_recarray(spectrophotometric_data)
            self.spectrophotometric_data = DataProxy(spectrophotometric_data, sn='sn',
                                                     spec='spec', mjd='mjd',
                                                     wavelength='wavelength',
                                                     flux='flux',
                                                     fluxerr='fluxerr',
                                                     i_basis='i_basis',
                                                     valid='valid')

        # we need to have either of these
        # assert(self.lc_data or self.spectrophotometric_data)

        # we probably need to update this after a compress ... ?
        # load all the transmissions and a mean_wavelength field
        # to the light curve data
        self.filterlib = filterlib
        if filterlib is not None:
            if not self.lc_data:
                logging.warning('will not load filters - no photometric data in the training dataset')
            else:
                trans = self.get_all_transmissions()
                self.band_wavelength = dict([(nm, tr.wave_eff()) for nm, tr in trans.items()])
                wl = np.array([self.band_wavelength[k] for k in self.lc_data.band])
                self.lc_data.add_field('wavelength', wl)
                # self.get_magsys_zp()
                # self.compute_photometric_norm_factors()

        # build a general index for the SN data
        self._index_sne()

        # build an index for the LC data
        # and connect it to the SN index
        if lcs is None and self.lc_data:
            self.lcs = []
            self._index_lcs()
        else:
            self.lcs = lcs

        # build an index for the spectroscopic data
        # and connect it to the SN index
        self.spectra = []
        self._index_spectra()

        # if we have spectrophotometric data available
        # (e.g. the SNfactory dataset), then build an index
        # of these spectra
        if self.spectrophotometric_data is not None:
            self._index_photometric_spectra()

        # build a global index. it is costly, but it can help
        # self.sne, self.lcs, self.spectra = build_index(self)

        self.plotter = None
        
        self.basis = basis
        
    @staticmethod
    def from_hdf(path):
        """
        """
        tds = read_hdf(path)
        return tds

    def extract(self, sn):
        """extract just the sn data
        """
        idx = self.sn_data.sn == sn
        if idx.sum() == 0:
            return None
        sn_data = self.sn_data.nt[idx]

        lc_data = None
        if self.lc_data:
            idx = self.lc_data.sn == sn
            lc_data = self.lc_data.nt[idx]

        spec_data = None
        if self.spec_data:
            idx = self.spec_data.sn == sn
            spec_data = self.spec_data.nt[idx]

        spectrophotometric_data = None
        if self.spectrophotometric_data is not None:
            idx = self.spectrophotometric_data.sn == sn
            spectrophotometric_data = self.spectrophotometric_data.nt[idx]

        return TrainingDataset(sn_data,
                               lc_data=lc_data,
                               spec_data=spec_data,
                               spectrophotometric_data=spectrophotometric_data)

    # def init_model_plotter(self):
    #     return ModelPlotter(SALT2Like, self.get_all_filter_names())

    def copy(self):
        sn_data = self.sn_data.nt.copy()

        lc_data, spec_data, spectrophotometric_data = None, None, None
        if self.lc_data:
            lc_data = self.lc_data.nt.copy()
        if self.spec_data:
            spec_data = self.spec_data.nt.copy()
        if self.spectrophotometric_data:
            spectrophotometric_data = self.spectrophotometric_data.nt.copy()

        return TrainingDataset(sn_data, lc_data,
                               spec_data, spectrophotometric_data)

    def _select(self, selectors=None):
        """perform a data selection, before indexation.

        We may want to perform some a-priori selection, before the dataset is
        built and indexed. Re-indexation after selection is a little costly
        (seconds for O(10^4) SNe, dozens of seconds for a LSST-like sample).

        For this reason, this selection is done only once, when building the
        dataset. Outlier removal is then done by maintaining a `valid` field
        in the spec_data and lc_data arrays.
        """
        for select in selectors:
            select(self)

    def kill_sne(self, sn_list):
        """kill the SNe listed in argument

        invalidate the SNe listed in argument, along with their associated
        follow-up data points (light curves and spectra). This method only
        modified the `valid` field in self.sne, self.lc_data and
        self.spec_data.  Call `self.compress` to effectively remove the data
        and re-index the dataset.

        Parameters
        ----------
        sn_list : List[int]
            the ids of the supernovae to remove
        """
        for sn in sn_list:
            # invalidate the SN
            idx = self.sn_data.sn == sn
            if idx.sum() == 0:
                logging.warning(f'kill_sne: no SN with index {sn}')
                continue
            if idx.sum() > 1:
                raise TrainingDatasetError(f'more than one SN with index {sn}')
            self.sn_data.valid[idx] = 0
            # the associated light curves
            if self.lc_data:
                self.lc_data.valid[self.lc_data.sn == sn] = 0
            # and the associated spectra
            if self.spec_data:
                self.spec_data.valid[self.spec_data.sn == sn] = 0
            if self.spectrophotometric_data:
                self.spectrophotometric_data.valid[self.spectrophotometric_data.sn == sn] = 0

    def kill_spectra(self, spec_list):
        """kill the spectra listed in argument
        """
        if self.spec_data is None:
            logging.warning('kill_spectra: no spectra in this dataset')
            return
        for spec in spec_list:
            idx = self.spec_data.spec == spec
            if idx.sum() == 0:
                logging.warning(f'no spectral data for index {spec}')
                continue
            self.spec_data.valid[idx] = 0

    def kill_photometric_spectra(self, spec_list):
        """kill the spectra listed in argument
        """
        if self.spectrophotometric_data is None:
            logging.warning('kill_photometric_spectra: no spectra in this dataset')
            return
        for spec in spec_list:
            idx = self.spectrophotometric_data.spec == spec
            if idx.sum() == 0:
                logging.warning(f'no spectral data for index {spec}')
                continue
            self.spectrophotometric_data.valid[idx] = 0

    def kill_lcs(self, lc_list):
        """kill the light curves with the specified indexes

        Parameters
        ----------
        lc_list : List[int]
            the indexes of the light curves to kill
        """
        if self.lc_data is None:
            logging.warning('kill_lcs: no spectra in this dataset')
            return
        for lc in lc_list:
            idx = self.lc_data.lc == lc
            if idx.sum() == 0:
                logging.warning(f'no light curve points for index {lc}')
                continue
            self.lc_data.valid[idx] = 0

    def compress(self):
        """get rid of all the data that has been invalidated

        If a large amount of data has been flagged as invalid, then it may make
        sense to get rid of it. This operation is costly however, as the data
        is copied and the entire index needs to be rebuilt.  """
        nlc, nsp, nspp = self.nb_meas(valid_only=True, split_by_type=True)

        self.sn_data.compress(self.sn_data.valid==1)
        if nlc > 0:
            self.lc_data.compress(self.lc_data.valid==1)
        else:
            self.lc_data = None

        if nsp > 0:
            self.spec_data.compress(self.spec_data.valid==1)
        else:
            self.spec_data = None

        if nspp > 0:
            self.spectrophotometric_data.compress(self.spectrophotometric_data.valid==1)
        else:
            self.spectrophotometric_data = None

        self._index_sne()
        if self.lc_data:
            self._index_lcs()
        if self.spec_data:
            self._index_spectra()
        if self.spectrophotometric_data:
            self._index_photometric_spectra()

        # build a global index. it is costly, but it can help
        # self.sne, self.lcs, self.spectra = build_index(self)

    def _index_sne(self):
        """
        """
        # contiguous index for SNe
        self.sn_data.make_index('sn')
        # row number of each SN
        self.isn = dict([(self.sn_data.sn_index[i], i) for i in range(len(self.sn_data))])

    def _index_lcs(self):
        """Sort and index the light curve data

        Sort the light curve data, so that the light curve measurements are
        stored in continuous chunks and can be indexed easily.

        Build an index for each light curve. Here, a light curve is the set of
        all photometric points, for one sn, measured in one band). The index
        entries contains a slice object and links to the original data.
        """
        logging.info('indexing light curves')
        if not self.lc_data:
            logging.warning('_index_lcs: no lc data')
            return

        self.lc_data.make_index('lc')
        self.lc_data.make_index('band')
        # we need to recycle the SN index generated for sn_data
        # otherwise, we may get inconsistant sn_indexes between
        # the three structures
        sn_index = np.array([self.sn_data.sn_map[sn] for sn in self.lc_data.sn])
        self.lc_data.add_field('sn_index', sn_index)

        # add a pointer to the SN row
        if not hasattr(self, 'isn'):
            self._index_sne()
        nsn = len(self.isn)
        lc_isn = np.array([self.isn[idx] for idx in self.lc_data.sn_index])
        self.lc_data.add_field('isn', lc_isn)

        # since we keep using the SN redshift in the model evaluations,
        # add it to the LC data
        self.lc_data.add_field('z', self.sn_data.z[self.lc_data.isn])

        # we also need a field to identify the row number. It is used a lot
        # when building the model jacobian matrices. With DataFrames, we would
        # have an index. Here, we need to build one ourselves.
        self.lc_data.add_field('row', np.arange(len(self.lc_data)))

        # array pointing to the first row of each light curve
        # useful to handle per-lightcurve information
        _, self.i_lc_first = np.unique(self.lc_data.lc_index, return_index=True)

        # create a small lc index
        self.lc_db = np.unique(np.rec.fromarrays((self.lc_data.lc_index,
                                                  self.lc_data.sn_index,
                                                  self.lc_data.band,
                                                  self.lc_data.z), \
                                                 names=['lc_index', 'sn_index', 'band', 'z']))


    def _index_spectra(self):
        """Sort and index the spectral data

        Sort the spectral data, so that the spectrum measurements are stored in
        contiguous chunks and can be indexed easily.

        Build an index for each spectrum. An index entry contains a slice object
        and links to the original data.

        """
        logging.info('indexing spectra')
        if not hasattr(self, 'spec_data') or not self.spec_data:
            logging.warning('_index_spectra: no spectra no index - pass')
            return

        self.spec_data.make_index('spec')
        # we need to recycle the SN index generated by the sn_data proxy
        sn_index = np.array([self.sn_data.sn_map[sn] for sn in self.spec_data.sn])
        self.spec_data.add_field('sn_index', sn_index)

        # add a pointer to each SN row
        if not hasattr(self, 'isn'):
            self._index_sne()
        spec_isn = np.array([self.isn[idx] for idx in self.spec_data.sn_index])
        self.spec_data.add_field('isn', spec_isn)

        # add the redshift, since we keep using it when evaluating the model
        self.spec_data.add_field('z', self.sn_data.z[self.spec_data.isn])

        # we need a field to identify the row number. It is used a lot when
        # building the model jacobian matrix. With pandas.DataFrames, we would
        # have an index. Here, we need to build it ourselves.
        nlc, nspec, nphotspec = self.nb_meas(valid_only=False,
                                             split_by_type=True)
        self.spec_data.add_field('row', nlc + np.arange(len(self.spec_data)))

        # create a small spectrum index
        self.spec_db = np.unique(np.rec.fromarrays((self.spec_data.spec_index,
                                                    self.spec_data.mjd,
                                                    self.spec_data.sn_index,
                                                    self.spec_data.z), \
                                                   names=['spec_index', 'mjd', 'sn_index', 'z']))

    def _index_photometric_spectra(self):
        """Same, for the photometric spectra (a.k.a. photometric dataset)

        Sort the spectral data, so that the spectrum measurements are stored
        contiguously and can be indexed easily.

        For now, we do not build an index (as list of SpectrumData objects) for
        each spectrum. This is not necessary, as the model evaluation is
        totally vectorized (this is not the :wcase for the light curves, which
        is why we still build a separate index).
        """
        logging.info('indexing photometric (calibrated) spectra')
        if not hasattr(self, 'spectrophotometric_data') or not self.spectrophotometric_data:
            logging.warning('_index_photometric_spectra: no data to index - pass')
            return

        # index the spectra
        self.spectrophotometric_data.make_index('spec')
        sn_index = np.array([self.sn_data.sn_map[sn] for sn in self.spectrophotometric_data.sn])
        self.spectrophotometric_data.add_field('sn_index', sn_index)

        # add a pointer to each SN row
        if not hasattr(self, 'isn'):
            self._index_sne()
        spec_isn = np.array([self.isn[idx] for idx in self.spectrophotometric_data.sn_index])
        self.spectrophotometric_data.add_field('isn', spec_isn)

        # add the redshift, since we keep using it when evaluating the model
        self.spectrophotometric_data.add_field('z', self.sn_data.z[self.spectrophotometric_data.isn])

        # we need a field to identify the row number. It is used a lot when
        # building the model jacobian matrix. With pandas.DataFrames, we would
        # have an index. Here, we need to build it ourselves.
        nlc, nspec, nphotspec = self.nb_meas(valid_only=False, split_by_type=True)
        self.spectrophotometric_data.add_field('row', nlc + nspec + np.arange(nphotspec))

        # create a small spectrum index
        self.spectrophot_db = np.unique(np.rec.fromarrays((self.spectrophotometric_data.spec_index,
                                                           self.spectrophotometric_data.mjd,
                                                           self.spectrophotometric_data.sn_index,
                                                           self.spectrophotometric_data.z), \
                                                          names=['spec_index', 'mjd', 'sn_index', 'z']))

    def __len__(self):
        """number of data points (spec+phot, valid+invalid)"""
        return self.nb_meas(valid_only=False, split_by_type=False)

    def nb_meas(self, valid_only=True, split_by_type=False):
        """number of measurements, (spec+phot)"""
        if valid_only:
            n_phot_meas = int(self.lc_data.valid.sum()) if self.lc_data is not None else 0
            n_spec_meas = int(self.spec_data.valid.sum()) if self.spec_data is not None else 0
            n_spectrophot_meas = int(self.spectrophotometric_data.valid.sum()) if self.spectrophotometric_data is not None else 0
        else:
            n_phot_meas = len(self.lc_data) if self.lc_data is not None else 0
            n_spec_meas = len(self.spec_data) if self.spec_data is not None else 0
            n_spectrophot_meas = len(self.spectrophotometric_data) if self.spectrophotometric_data is not None else 0

        if split_by_type:
            return n_phot_meas, n_spec_meas, n_spectrophot_meas
        return n_phot_meas + n_spec_meas + n_spectrophot_meas

    def concat(self):
        """return a concatenation of all data
        """
        pass

    def nb_sne(self, valid_only=True):
        """
        Return number of (valid) SNe.
        """
        if valid_only:
            return int(self.sn_data.valid.sum())
        return len(self.sn_data)

    def nb_lcs(self, valid_only=True):
        """
        Return number of (valid) light curves.

        .. todo:: implement valid_only
        """
        if not hasattr(self, 'lc_data') or not self.lc_data:
            return 0

        if valid_only:
            idx = self.lc_data.valid > 0
            return len(np.unique(self.lc_data.lc[idx]))
        return len(np.unique(self.lc_data.lc))

    def nb_spectra(self, valid_only=True):
        """
        Return number of spectra.

        .. todo:: implement valid_only
        """
        if not hasattr(self, 'spec_data') or not self.spec_data:
            return 0

        if valid_only:
            idx = self.spec_data.valid > 0
            return len(np.unique(self.spec_data.spec[idx]))
        return len(np.unique(self.spec_data.spec))

    def nb_photometric_spectra(self, valid_only=True):
        """Return number of photometric spectra
        (i.e. SNfactory like spectra)
        """
        if not hasattr(self, 'spectrophotometric_data') or not self.spectrophotometric_data:
            return 0

        if valid_only:
            idx = self.spectrophotometric_data.valid > 0
            return len(np.unique(self.spectrophotometric_data.spec[idx]))
        return len(np.unique(self.spectrophotometric_data.spec))

    def nb_bands(self):
        return len(self.transmissions)

    def update_fluxes(self, flx):
        """update the fluxes of all data blocks
        """
        nlc, nsp, nspphot = self.nb_meas(valid_only=False,
                                         split_by_type=True)
        if nlc > 0:
            self.lc_data.flux[:] = flx[:nlc]
        if nsp > 0:
            self.spec_data.flux[:] = flx[nlc:nlc+nsp]
        if nspphot > 0:
            self.spectrophotometric_data.flux[:] = flx[nlc+nsp:]

    def get_all_fluxes(self):
        blocks = []
        for block in [self.lc_data, self.spec_data,
                      self.spectrophotometric_data]:
            if block is not None:
                blocks.append(block.flux)
        assert(len(blocks) > 0)
        return np.hstack(blocks)

    # def set_fluxes(self, all_fluxes=None, **kwargs):
    #     if all_fluxes is not None:
    #         nlc, nspec, _ = self.nb_meas(valid_only=False,
    #                                      split_by_type=True)
    #         if self.lc_data:
    #             self.lc_data.flux[:] = all_fluxes[0:nlc]
    #         if self.spec_data:
    #             self.spec_data.flux[:] = all_fluxes[nlc:nlc+nspec]
    #         if self.spectrophotometric_data:
    #             self.spectrophotometric_data[:] = all_fluxes[nlc+nspec:]

    def get_all_fluxerr(self):
        blocks = []
        for block in [self.lc_data, self.spec_data,
                      self.spectrophotometric_data]:
            if block is not None:
                blocks.append(block.fluxerr)
        assert(len(blocks) > 0)
        return np.hstack(blocks)

    def get_valid(self):
        blocks = []
        for block in [self.lc_data, self.spec_data,
                      self.spectrophotometric_data]:
            if block is not None:
                blocks.append(block.valid)
        assert(len(blocks) > 0)
        return np.hstack(blocks)

    def reset_valid(self, valid=1):
        for block in [self.lc_data, self.spec_data,
                      self.spectrophotometric_data]:
            if block is not None:
                block.valid[:] = valid

    def get_bads(self):
        blocks = []
        for block in [self.lc_data, self.spec_data,
                      self.spectrophotometric_data]:
            if block is not None:
                blocks.append(block.valid==0)
        assert(len(blocks) > 0)
        return np.hstack(blocks)

    def get_sn_pars(self, sn):
        """retrieve the sn pars from the training dataset (if available)
        """
        ret = {}
        idx = self.sn_data.sn == sn
        sn_info = self.sn_data.nt[idx]
        keys = sn_info.dtype.names
        for k in ['z', 'x0', 'x1', 'c', 'tmax', 'ebv']:
            ret[k] = float(sn_info[k]) if k in keys else 0.
        return ret

    def get_all_filter_names(self, force=False) -> List[str]:
        """passbands used in the dataset

        scan the dataset and return a list containing the full names
        (`instrument`::`band_name`) of all the passbands that were used in the
        photometric follow-up.

        Returns
        -------
        List[str]
            List of filter names
        """
        if not hasattr(self, 'lc_data') or not self.lc_data:
            return None

        if hasattr(self, 'filter_names') and not force:
            return self.filter_names
        t = np.unique(self.lc_data.band)
        self.filter_names = t.astype(t.dtype.str.replace('S', 'U'))
        return self.filter_names
    
    
    def get_all_transmissions(self, force=False):
        """transmissions used in the dataset

        from the list of passbands (see above) fetch all the corresponding
        transmissions and return them.

        Returns
        -------
        list
            List of filter transmission.

        """
        if not hasattr(self, 'filterlib') or self.filterlib is None:
            logging.warning('unable to load transmissions: no filterlib')
            return

        if not hasattr(self, 'lc_data') or not self.lc_data:
            logging.warning('no transmissions to load: no photometric data')
            return

        if hasattr(self, 'transmissions') and not force:
            return self.transmissions
        self.transmissions = dict([(fn, self.filterlib[fn]) for fn in self.get_all_filter_names(force=force)])

        return self.transmissions

    def get_zp(self, sn):
        """
        """
        idx = self.lc_data.sn == sn
        return dict(zip(self.lc_data.band[idx], self.lc_data.zp[idx]))

    def get_magsys(self, sn):
        """
        """
        idx = self.lc_data.sn == sn
        return dict(zip(self.lc_data.band[idx], self.lc_data.magsys[idx]))

    # def get_magsys_zp(self, force=False):
    #     """
    #     """
    #     if not hasattr(self, 'lc_data') or not self.lc_data:
    #         return

    #     if hasattr(self, 'magsys_zp') and not force:
    #         return self.magsys_zp

    #     try:
    #         # if force, we need to update the transmissions
    #         self.get_all_transmissions(force=force)

    #         lc_data = self.lc_data
    #         self.magsys = dict([(magsys_name, MagSys(magsys_name)) for magsys_name in np.unique(lc_data.magsys)])

    #         self.magsys_zp = {}
    #         for magsys_name, band_name in set(zip(lc_data.magsys, lc_data.band)):
    #             ms = self.magsys[magsys_name]
    #             tr = self.transmissions[band_name]
    #             self.magsys_zp[(magsys_name, band_name)] = ms.ZeroPoint(tr)
    #         zp = np.array([self.magsys_zp[(m,b)] for m,b in zip(lc_data.magsys, lc_data.band)])
    #         lc_data.add_field('magsys_zp', zp)


    #     except:
    #     # if force, we need to update the transmissions
    #         self.get_all_transmissions(force=force)

    #         m_AB = sncosmo.ABMagSystem()
    #         self.magsys_zp ={}

    #         lc_data = self.lc_data
    #         self.magsys = dict([(magsys_name, m_AB) for magsys_name in np.unique(lc_data.magsys)])

    #         self.magsys_zp = {}
    #         for magsys_name, band_name in set(zip(lc_data.magsys, lc_data.band)):
    #             ms = self.magsys[magsys_name]
    #             tr = self.transmissions[band_name]
    #             band = sncosmo.get_bandpass(band_name)
    #             self.magsys_zp[(magsys_name, band_name)] =  -2.5*np.log10(m_AB.zpbandflux(band)) #ms.ZeroPoint(tr)
    #         zp = np.array([self.magsys_zp[(m,b)] for m,b in zip(lc_data.magsys, lc_data.band)])
    #         lc_data.add_field('magsys_zp', zp)

    # def compute_photometric_norm_factors(self, force=False):
    #     """
    #     """
    #     if not hasattr(self, 'lc_data') or not self.lc_data:
    #         return

    #     # self.get_magsys_zp(force=force)

    #     lc_data = self.lc_data
    #     meas_zp_norm = 10**(-0.4 * lc_data.zp)
    #     # magsys_zp_norm = 10**(-0.4 * lc_data.magsys_zp)  # was -0.4
    #     norm = meas_zp_norm # * magsys_zp_norm
    #     lc_data.add_field('norm', norm)

    def update_zp_scale(self):
        """derive a multiplicative calibration scale from the zero point
        """
        if not hasattr(self, 'lc_data') or not self.lc_data:
            return

        scale = 10.**(-0.4 * self.lc_data.zp)
        self.lc_data.add_field('zp_scale', scale)

    def to_parquet(self, name, path=pathlib.Path('./')):
        """Write the internal dataframes to the binary parquet format

        This method writes each of the internal array (sn index, lightcurves,
        spectra, photometric spectra) as parquet files (one for each).

        Parameters
        ----------
        name : str or path object
          core file name. Each file is written as <name>_<suffix>.parquet
        path : str or path object
          root path
        """
        path = pathlib.Path(path)
        fn = path.joinpath(name)
        
        # save the supernova metadata
        df = pandas.DataFrame(self.sn_data.nt).set_index('index')
        df.to_parquet(fn.with_suffix(".sn.parquet"),
                      engine='pyarrow', index=False)
        # save the lc data, if any
        if hasattr(self, 'lc_data') and self.lc_data is not None:
            df = pandas.DataFrame(self.lc_data.nt).set_index('index')
            df.to_parquet(fn.with_suffix(".lc.parquet"),
                          engine='pyarrow', index=False)
        # save the spectra, if any
        if hasattr(self, 'spec_data') and self.spec_data is not None:
            df = pandas.DataFrame(self.spec_data.nt).set_index('index')
            df.to_parquet(fn.with_suffix(".spec.parquet"),
                          engine='pyarrow', index=False)

        # save the spectrophotometric data, if available
        if hasattr(self, 'spectrophotometric_data') and \
           self.spectrophotometric_data is not None:
            df = pandas.DataFrame(self.spectrophotometric_data).set_index('index')
            df.to_parquet(fn.with_suffix(".specphot.parquet"),
                          engine='pyarrow', index=False)

        # save the basis - as a pkl file
        #        df = pandas.DataFrame({'basis': self.basis.grid})
        #        df.to_parquet(fn.with_suffix(".basis.parquet"), engine='pyarrow',
        #              index=False)
        if hasattr(self, 'basis') and self.basis is not None:
            with open(fn.with_suffix(".wlbasis.pkl"), 'wb') as f:
                pickle.dump(self.basis, f)

    @classmethod
    def read_parquet(cls, name, path='./', filterlib=None):
        """Load a TrainingDataset from parquet files

        Parameters
        ----------
        name : str or path-like object
          core file name. The function searches for parquet files
          named `<name>_<suffix>.parquet` with suffix equal to `_sn`,
          `_lc`, `_spec`, `_specphot` for each component.
        path : str or path object
          root path
        """
        path = pathlib.Path(path)
        fn = path.joinpath(name)
        sn_data = pandas.read_parquet(fn.with_suffix(".sn.parquet"))

        # light curves ?
        lc_path = fn.with_suffix(".lc.parquet")
        if lc_path.is_file():
            lc_data = pandas.read_parquet(lc_path)
        else:
            lc_data = None

        # spectra ?
        spec_path = fn.with_suffix(".spec.parquet")
        if spec_path.is_file():
            spec_data = pandas.read_parquet(spec_path)
        else:
            spec_data = None

        # spectrophotometric data ?
        # spectra ?
        specphot_path = fn.with_suffix(".specphot.parquet")
        if specphot_path.is_file():
            specphot_data = pandas.read_parquet(specphot_path)
        else:
            specphot_data = None

        # wavelength basis (if available)
        basis_path = fn.with_suffix(".wlbasis.pkl")
        if basis_path.is_file():
            with open(basis_path, 'rb') as f:
                basis = pickle.load(f)
        else:
            basis = None                

        print(basis_path, basis_path.is_file(), basis)
            
        return cls(sn_data, lc_data=lc_data, spec_data=spec_data,
                   spectrophotometric_data=specphot_data,
                   filterlib=filterlib, basis=basis)

    def to_npz(self, path, compressed=False):
        """Write the TrainingDataset instance as a numpy npz file
        """
        path = pathlib.Path(path)
        if compressed:
            np.savez_compressed(path, sn_data=self.sn_data,
                                lc_data=self.lc_data,
                                spec_data=self.spec_data)
        else:
            np.savez(path, sn_data=self.sn_data,
                     lc_data=self.lc_data,
                     spec_data=self.spec_data)

    @classmethod
    def read_npz(cls, path):
        """Load a TrainingDataset from a numpy npz file
        """
        path = pathlib.Path(path)
        f = np.load(path, allow_pickle=True)
        lc_data = f['lc_data'] if 'lc_data' in f else None
        spec_data = f['spec_data'] if 'spec_data' in f else None
        specphot_data = f['specphot_data'] if 'specphot_data' in f else None
        return cls(f['sn_data'], lc_data=lc_data, spec_data=spec_data,
                   spectrophotometric_data=specphot_data)

    def to_hdf(self, path, compressed=True):
        """Write the training dataset in a HDF5 file (binary format)
        """
        path = pathlib.Path(path)
        with pandas.HDFStore(path, complevel=9) as f:
            f.put('sn_data',
                  pandas.DataFrame(self.sn_data.nt).set_index('index'))
            if hasattr(self, 'lc_data') and self.lc_data:
                f.put('lc_data',
                      pandas.DataFrame(self.lc_data.nt).set_index('index'))
            if hasattr(self, 'spec_data') and self.spec_data:
                f.put('spec_data',
                      pandas.DataFrame(self.spec_data.nt).set_index('index'))
            if hasattr(self, 'spectrophotometric_data') and self.spectrophotometric_data:
                f.put('spectrophotometric_data',
                      pandas.DataFrame(self.spectrophotometric_data.nt).set_index('index'))
            f.put('basis',
                  pandas.DataFrame({'basis':self.basis}, index=[0]))

    @classmethod
    def read_hdf(cls, path):
        """Load a training dataset from a HDF5 file
        """
        path = pathlib.Path(path)
        with pandas.HDFStore(path) as f:
            lc_data = f.lc_data if 'lc_data' in f else None
            spec_data = f.spec_data if 'spec_data' in f else None
            spectrophotometric_data = f.spectrophotometric_data if 'spectrophotometric_data' in f else None
            basis_ = f.basis['basis'][0] if 'basis' in f else None
            return cls(f.sn_data, lc_data=lc_data, spec_data=spec_data,
                      spectrophotometric_data=spectrophotometric_data,
                      basis = basis_)

    def plot_sample(self, bins=50):
        """plot a synthetic view of the sample

        this method displays, in a single panel:
            - a histogram of the redshifts
            - histograms of X1 and color
            - the variations of X0 as a function of redshift
        """
        fig, axes = plt.subplots(2,2, figsize=(8,8))
        fig.suptitle(f'sample: size={len(self.sn_data)}')
        axes[0, 0].hist(self.sn_data.z, bins=bins, alpha=0.5)
        axes[0, 0].set_xlabel('$z$')

        axes[1, 0].semilogy(self.sn_data.z, self.sn_data.x0,
                           color='k', ls='', marker='.')
        axes[1, 0].set_xlabel('$z$')
        axes[1, 0].set_ylabel('$X_0$')

        axes[0, 1].hist(self.sn_data.x1, bins=bins, alpha=0.5)
        axes[0, 1].set_xlabel('$X_1$')
        axes[1, 1].hist(self.sn_data.col, bins=bins, alpha=0.5)
        axes[1, 1].set_xlabel('$c$')

    def plot_lcs(self, sn, model=None, pars=None,
                 color=None, cmap=None, cmap_lims=(3000., 10000.)):
        """plot the light curves of the specified SN

        Parameters:
        -----------
        sn : (int)
            unique sn id in the training dataset
        model : (SALT2Eval)
            a model eval class (the thing that compute the model a-la sncosmo)
        pars : (FitParameters)
            additional parameters for the model
        """
        idx = self.sn_data.sn == sn
        tmax = float(self.sn_data.tmax[idx])

        idx = self.lc_data.sn == sn
        lc_bands = sorted(np.unique(self.lc_data.band[idx]).tolist(),
                          key=opt_band_name_order)
        nb_bands = len(lc_bands)
        ncols = int(np.sqrt(nb_bands))
        nrows = int(nb_bands/ncols + 1)

        # color & color map
        # I am copying sncosmo's logic here
        if color is None:
            if cmap is None:
                cmap = cm.get_cmap('jet_r')

        # overploting a model
        if model is not None:
            model.set_from_tds(sn, self)
            if pars is not None:
                model.update_global_pars(pars)
            model()

        fig = plt.figure(figsize=(14, 10))
        z = np.unique(self.lc_data.z[idx])[0]
        fig.suptitle(f'SN #{sn}  [z={z}]')

        for i, b in enumerate(lc_bands):
            # axis
            p, q = int(i / ncols), i % ncols
            ax = fig.add_subplot(nrows, ncols, i+1)

            # color
            if color is None:
                wl = self.transmissions[b].wave_eff()
                bandcolor = cmap((wl-cmap_lims[0]) /
                             (cmap_lims[1] - cmap_lims[0]))
            else:
                bandcolor = color

            # plot all the LC points
            idx = (self.lc_data.sn == sn) & (self.lc_data.band == b)
            plt.plot(self.lc_data.mjd[idx], self.lc_data.flux[idx],
                    ls='', marker=',', color=bandcolor)

            # then, just the valid points
            idx = (self.lc_data.sn == sn) & (self.lc_data.band == b) & (self.lc_data.valid == 1)
            plt.errorbar(self.lc_data.mjd[idx], self.lc_data.flux[idx],
                        yerr=self.lc_data.fluxerr[idx],
                        ls='', marker='.', color=bandcolor)

            # and all the points that were killed and are no longer
            # part of the analysis
            idx_killed = (self.lc_data.sn == sn) & (self.lc_data.band == b) & (self.lc_data.valid == 0)
            plt.plot(self.lc_data.mjd[idx_killed], self.lc_data.flux[idx_killed],
                    ls='', marker='x', color=bandcolor)

            # if model requested, we plot it on top of the data
            if model:
                idx = model.tds.lc_data.band == b
                lc_data = model.tds.lc_data.nt[idx]
                ax.plot(lc_data.mjd, lc_data.flux, ls='-', color=bandcolor)
            ax.set_ylabel(f'$flux_{b}$')
            ax.axvline(tmax)

    def plot_spectra(self, sn, model=None):
        """plot all the spectra of the specified SN
        """
        idx = self.sn_data.sn == sn
        tmax = float(self.sn_data.tmax[idx])
        pass

    def plot_spectrum(self, spec, phot=False, model=None, pars=None,
                      color='b'):
        """plot the spectrum number spec
        """
        if not phot:
            spec_data = self.spec_data
        else:
            spec_data = self.spectrophotometric_data
        assert spec_data is not None

        idx = spec_data.spec == spec
        sn = spec_data.sn[idx][0]
        mjd = spec_data.mjd[idx][0]
        z = spec_data.z[idx][0]
        logging.info(f'{sn} {mjd} {z}')

        # overplotting a model
        if model is not None:
            model.set(spec_mjd=mjd)
            model.set_from_tds(sn, self)
            if pars is not None:
                model.update_global_pars(pars)
            model()

        fig = plt.figure(figsize=(14,10))
        ax = fig.add_subplot(111)
        fig.suptitle(f'spectrum {spec}' +
                     f' [SN: {sn}],' +
                     f' z={z:.3f}')
        ax.plot(spec_data.wavelength[idx], spec_data.flux[idx], 'k,')
        idx = (spec_data.spec == spec) & (spec_data.valid == 1)
        ax.errorbar(spec_data.wavelength[idx], spec_data.flux[idx],
                    yerr=spec_data.fluxerr[idx], ls='', marker='.', color='k')
        idx_killed = (spec_data.spec == spec) & (spec_data.valid==0)
        ax.plot(spec_data.wavelength[idx_killed], spec_data.flux[idx_killed],
                color='r', marker='x', ls='')

        if model:
            if not phot:
                spec_data = model.tds.spec_data.nt
            else:
                spec_data = model.tds.spectrophotometric_data.nt

            ax.plot(spec_data.wavelength, spec_data.flux,
                    ls='-', color=color)
            print(spec_data.flux)
        # if model:
        #     if self.plotter is None:
        #         self.plotter = self.init_model_plotter()
        #     sn = spec_data.sn[idx][0]
        #     mjd = spec_data.mjd[idx][0]
        #     assert np.all(spec_data.sn[idx] == sn)
        #     assert np.all(spec_data.mjd[idx] == mjd)
        #     self.plotter.load_sn_pars(sn, self, spec_mjd=mjd, pars=pars)
        #     self.plotter.plot_spectrum(ax=ax, phot=phot)

        ax.set_xlabel('$\lambda\ \ [\AA]$')
        ax.set_ylabel('flux')

    def plot_coverage(self, log=False):
        """$\lambda$-phase plane coverage
        """
        wl_bins = np.linspace(2000, 10000, 120)
        phase_bins = np.linspace(-20, 50, 40)

        # we plot things differently according to whether
        # there are two or just one spectroscopic dataset
        if self.spec_data is None and self.spectrophotometric_data is None:
            fig, axes = plt.subplots(nrows=2, ncols=2,
                                    sharex=True, sharey=True,
                                    figsize=(14,14))
            lc_axes = axes[0, 0] if self.lc_data else None
            spec_axes = axes[0, 1] if self.spec_data else None
            photspec_axes = axes[1,0] if self.spectrophotometric_data else None
            sum_axes = axes[1,1] if self.spec_data and \
                self.spectrophotometric_data else None
        else:
            fig, axes = plt.subplots(nrows=1, ncols=2,
                                    sharex=True, sharey=True,
                                    figsize=(14,7))
            lc_axes = axes[0] if self.lc_data else None
            spec_axes = axes[1] if self.spec_data else None
            photspec_axes = axes[1] if self.spectrophotometric_data else None
            sum_axes = None

        H_lc, H_spec, H_spectrophot = None, None, None

        # LC coverage
        if lc_axes is not None:
            zz = 1. + self.lc_data.z
            wl = self.lc_data.wavelength / zz
            tmax = self.sn_data.tmax[self.lc_data.isn]
            phase = (self.lc_data.mjd - tmax) / zz
            norm = matplotlib.colors.LogNorm() if log else None
            H_lc, _, _, im = lc_axes.hist2d(wl, phase,
                                            bins=(wl_bins, phase_bins),
                                            norm=norm)

            lc_axes.set_title('photometric coverage')
            lc_axes.set_xlabel('$\lambda$ [restframe, $\AA$]')
            lc_axes.set_ylabel('phase [restframe days]')
            plt.colorbar(im)

        # spectral coverage
        if spec_axes is not None:
            zz = 1. + self.spec_data.z
            wl = self.spec_data.wavelength / zz
            tmax = self.sn_data.tmax[self.spec_data.isn]
            phase = (self.spec_data.mjd - tmax) / zz
            H_spec, _, _, im = spec_axes.hist2d(wl, phase,
                                               bins=(wl_bins, phase_bins))
            spec_axes.set_title('spectral coverage')
            spec_axes.set_xlabel('$\\lambda$ [restframe, $\AA$]')
            spec_axes.set_ylabel('phase [restframe days]')
            plt.colorbar(im)

        if photspec_axes is not None:
            zz = 1. + self.spectrophotometric_data.z
            wl = self.spectrophotometric_data.wavelength / zz
            tmax = self.sn_data.tmax[self.spectrophotometric_data.isn]
            phase = (self.spectrophotometric_data.mjd - tmax) / zz
            H_spectrophot, _, _, im = photspec_axes.hist2d(wl, phase,
                                                 bins=(wl_bins, phase_bins))
            photspec_axes.set_title('photometric spectra')
            photspec_axes.set_xlabel('$\\lambda$ [restframe, $\AA$]')
            photspec_axes.set_ylabel('phase [restframe days]')
            plt.colorbar(im)

        if sum_axes is not None:
            I = sum_axes.matshow(H_spec + H_spectrophot, aspect='auto')
            sum_axes.set_title('total spectral coverage')
            sum_axes.set_xlabel('$\\lambda$ [restframe, $\AA$]')
            sum_axes.set_ylabel('phase [restframe days]')
            plt.colorbar(I)

        plt.subplots_adjust(wspace=0.1, left=0.1, right=0.95)


def _df_to_recarray(x, sort_by=None):
    """utility function to convert the data into a sorted recarray

    The TrainingDataset expects either a recarray or a dataframe. Internally,
    it uses a recarrays, because accessing their content is about factor 10
    faster than pandas.DataFrames. It also requires the recarray to be sorted
    to speed up data access and allow easy indexing of the data.

    This function (optionally) sorts the input data according to the sort_by
    argument and returns the sorted data as a numpy.recarray.

    Parameters
    ----------
    x : pandas.DataFrame | numpy.recarray
        the data
    sort_by : List[str]], optional
        sort directives, by default None

    Returns
    -------
    numpy.recarray
        the (optionally sorted) data

    Raises
    ------
    ValueError
        if the input data is neither a pandas.DataFrame or a numpy.recarray
    """
    if isinstance(x, pandas.DataFrame):
        if sort_by:
            x = x.sort_values(by=sort_by)
        return x.to_records()

    if isinstance(x, np.recarray):
        if sort_by:
            x.sort(order=sort_by)
        return x

    raise ValueError('array is neither a DataFrame nor a recarray')

class SNData:

    def __init__(self, sn_data):
        """constructor

        Parameters
        ----------
        sn_data : record
            a record that contains at least the following fields:
              - 'z', the SN redshift (float)
              - 'sn', a unique ID for the SN (int or str)
              - 'valid', int
        """
        self.data = sn_data
        self.lcs = {}
        self.spectra = []

    @property
    def sn(self):
        return self.data.sn

    @property
    def z(self):
        return self.data.z

    @property
    def valid(self):
        return self.data.valid

    def kill(self):
        """invalidate the SN and all the associated follow-up data
        """
        self.data.valid = 0
        for lc in self.lcs.values():
            lc.data.valid[:] = 0
        for sp in self.spectra:
            sp.data.valid[:] = 0

    def plot(self):
        """standard plot to present the SN data"""
        pass


class LcData:
    """A class to access the light curve data."""

    def __init__(self, sn, band, slc, lc_data):
        """Constructor

        Parameters
        ----------
        sn : int
            Index of sn.
        band : str
            Name of the Filter.
        slc : slc
            Index of the Light Curve data in the full photometric data.
        lc_data : nacl.lib.dataproxy.DataProxy
            Photometric data.
        sne : numpy.recarray
            Information of all SNe (:math:`(z, X_0, X_1, c, t_{max})`)
        """
        self.sn_info = sn
        # note: this masks the `band` field in self.lc_data
        # self.band = band
        self.slc = slc
        self.lc_data = lc_data

    def __len__(self):
        """number of light curve data points.
        """
        return len(self.lc_data.row[self.slc])

    def __getattr__(self, name):
        try:
            return self.lc_data.__dict__[name][self.slc]
        except KeyError:
            raise AttributeError(f"{type(self).__name__} has no attribute {name}")

    # @property
    # def valid(self):
    #     return self.lc_data.valid[self.slc]

    # @property
    # def mjd(self):
    #     return self.lc_data.mjd[self.slc]

    # @property
    # def flux(self):
    #     return self.lc_data.flux[self.slc]

    # @property
    # def fluxerr(self):
    #     return self.lc_data.fluxerr[self.slc]

    # @property
    # def data(self):
    #     """
    #     Return numpy.rec.array data file.
    #     """
    #     return self.lc_data[self.slc]

    # @property
    # def z(self):
    #     """redshift"""
    #     return self.lc_data.z[self.slc]

    def kill(self):
        """invalidate all the light curve measurements"""
        self.valid[:] = 0

    def plot(self, ax=None):
        """standard light curve plot"""
        plt.figure()
        x, y, ey = self.mjd, self.flux, self.fluxerr
        plt.errorbar(x, y, yerr=ey, ls='', color='k', marker='o')
        plt.xlabel('phase [days]')
        plt.ylabel('Flux')
        sn = self.sn_info.sn
        band = np.unique(self.band)[0]
        z = self.sn_info.z
        plt.title('SN#{} {} [$z={:5.3}]$'.format(sn, band, z))


class SpectrumData:
    """A class to access and plot spectra
    """
    def __init__(self, sn, spec, slc, sp_data):
        """Constructor

        Parameters
        ----------
        sn : SNData
            info about the SN
        spectrum : str or int
            Spectrum unique identifier
        slc : slc
            slice o
        sp_data : numpy.recarray or pandas.DataFrame
            spectral data
        """
        self.sn_info = sn
        self.spec = spec
        self.slc = slc
        self.sp_data = sp_data

    def __len__(self):
        """number of data points"""
        return len(self.data)

    def __getattr__(self, name):
        try:
            return self.sp_data.__dict__[name][self.slc]
        except KeyError:
            raise AttributeError(f"{type(self).__name__} has no attribute {name}")

    # @property
    # def data(self):
    #     """the spectrum data itself"""
    #     return self.sp_data[self.slc]

    # @property
    # def z(self):
    #     """Sn redshift"""
    #     return self.sn.z

    def kill(self):
        self.valid[:] = 0

    def plot(self):
        """standard control plot
        """
        plt.figure()
        x, y, ey = self.wavelength, self.flux, self.fluxerr
        plt.errorbar(x, y, yerr=ey, ls='', color='k')
        plt.xlabel(r'$\lambda [\AA]$')
        plt.ylabel('flux')
        plt.title('SN#{} [$z={:5.3}$]'.format(self.sn_info.sn, self.sn_info.z))

def _index_sne(tds):
    sne = dict([(r.sn, SNData(r)) for r in tds.sn_data.nt])
    return sne

def _index_lcs(tds, sne):
    """parse the lc_data and build the light curve index

    Parse the lc_data, build a LcData handle for each identified LC,
    and attach it to its SN

    Parameters
    ----------
    lc_data : nacl.lib.DataProxy
        the DataProxy that handles all the lightcurves
    sne : Dict[SNData]
        the index - each entry corresponds to a SN
    """
    lcs = []
    lc_data = tds.lc_data
    if not lc_data:
        return

    # we need to assume at this point that the indexes are up to date
#    if not hasattr(lc_data, 'sn_index'):
#        lc_data.make_index('sn')
#    if not hasattr(lc_data, 'band_index'):
#        lc_data.make_index('band')
    index = lc_data.sn_index * 100 + lc_data.band_index

    # detect the block edges
    i_slices = np.where(index[1:] - index[:-1])[0] + 1
    i_slices = np.hstack(([0], i_slices.repeat(2), [len(lc_data)])).reshape((-1,2))

    # now comes the slow part -- we build the handles to each lightcurve
    # logging.info(f'building the LcData handles {i_slices.shape[0]} to build')
    lc_data_nt = lc_data.nt
    for i in range(i_slices.shape[0]):
        slc = slice(*i_slices[i])
        r = lc_data_nt[slc.start]
        lcdata = LcData(sne[r.sn], r.band, slc, lc_data)
        lcs.append(lcdata)
        sne[r.sn].lcs[r.band] = lcdata
    return lcs

def _index_spectra(tds, sne):
    """parse the spec_data, identifies all the spectra

    Parameters
    ----------
    spec_data : _type_
        _description_
    sne : _type_
        _description_
    """
    spec_data = tds.spec_data
    if spec_data is None:
        return

    spectra = []

    # we need to assume at this point
    # that the indexes are up to date
    #    if not hasattr(spec_data, 'spec_index'):
    #        spec_data.make_index('spec')
    #    if not hasattr(spec_data, 'sn_index'):
    #        spec_data.make_index('sn')

    # logging.info('indexing the spectra')
    mjd = spec_data.mjd
    i_slices = np.where(mjd[1:] - mjd[:-1])[0] + 1
    i_slices = np.hstack([[0],
                          i_slices.repeat(2),
                          [len(spec_data)]]).reshape((-1,2))

    # now, indexing
    spec_data_nt = spec_data.nt
    for i in range(i_slices.shape[0]):
        slc = slice(*i_slices[i])
        r = spec_data_nt[slc.start]
        spdata = SpectrumData(sne[r.sn], r.spec, slc, spec_data)
        spectra.append(spdata)
        sne[r.sn].spectra.append(spdata)
    return spectra

def build_index(tds):
    sne = _index_sne(tds)
    lcs = _index_lcs(tds, sne)
    spectra = _index_spectra(tds, sne)
    return sne, lcs, spectra

class SimTrainingDataset(TrainingDataset):
    """simple training dataset, with one single SN and regular sampling

    Useful for plotting the model over data, or model components.
    """

    def __init__(self, bands=['SWOPE::B'],
                 phase_range=(-20., 50.), restframe_dt=1.,
                 n_spectra=1, n_phot_spectra=1, zp=30., magsys='AB', filterlib=None):
        """generate a similar dataset, with the requested bands and spectra
        """
        # sn data
        sne = np.rec.array(np.zeros(1, dtype=TrainingDataset.sn_data_dtype))
        sne['valid'] = 1

        # light curves
        if bands is not None and len(bands) > 0:
            lc_data = []
            ph_min, ph_max = phase_range
            N = int((ph_max-ph_min) / restframe_dt)
            mjd = np.linspace(ph_min, ph_max, N)
            block_size = len(mjd)
            for band in bands:
                block = np.zeros(block_size,
                                 dtype=TrainingDataset.lc_data_dtype)
                block['mjd'] = mjd
                block['band'] = band
                block['valid'] = 1
                block['magsys'] = magsys
                if type(zp) is float:
                    block['zp'] = zp
                elif type(zp) is dict:
                    block['zp'] = zp.get(band, 30.)
                else:
                    block['zp'] = 30.
                block['x'] = 1000.
                block['y'] = 1000.
                block['sensor_id'] = 12
                lc_data.append(block)
            lc_data = np.rec.array(np.hstack(lc_data))
        else:
            lc_data = None

        # copy the mjd vector
        if lc_data is not None:
            self.mjd = lc_data.mjd.copy()
        else:
            self.mjd = None

        # spectra
        spec_data = None
        if n_spectra > 0:
            spec_data = []
            for sp in range(n_spectra):
                wl = np.linspace(3000., 11000., 8000)
                block_size = len(wl)
                block = np.zeros(block_size,
                                 dtype=TrainingDataset.spec_data_dtype)
                block['wavelength'] = wl
                block['valid'] = 1
                spec_data.append(block)
            spec_data = np.rec.array(np.hstack(spec_data))

        # photometric spectra
        spectrophotometric_data = None
        if n_phot_spectra > 0:
            spectrophotometric_data = []
            for sp in range(n_phot_spectra):
                wl = np.linspace(3000., 11000., 8000)
                block_size = len(wl)
                block = np.zeros(block_size,
                                 dtype=TrainingDataset.spec_data_dtype)
                block['wavelength'] = wl
                block['valid'] = 1
                spectrophotometric_data.append(block)
            spectrophotometric_data = np.rec.array(np.hstack(spectrophotometric_data))

        super().__init__(sne, lc_data, spec_data, spectrophotometric_data, filterlib=filterlib)



class ModelPlotter:

    def __init__(self, model_type, bands,
                 phase_range=(-20., 50.),
                 wl_range=(3000., 11000.),
                 n_spectra=1, n_phot_spectra=1, magsys='AB',
                 init_from_salt2_file='salt2.npz'):
        """
        """
        self.model_type = model_type
        self.bands = bands
        self.phase_range = phase_range
        self.wl_range = wl_range
        self.n_spectra = n_spectra
        self.init_from_salt2_file = init_from_salt2_file
        self.tds = self.init_training_dataset(bands,
                                              phase_range,
                                              wl_range,
                                              n_spectra,
                                              n_phot_spectra,
                                              magsys)
        self.model_type = model_type
        # self.model = model_type(self.tds,
        #                         init_from_salt2_file=init_from_salt2_file)

    def init_training_dataset(self, band_names,
                              phase_range, wl_range,
                              n_spectra, n_phot_spectra,
                              magsys):
        """
        """
        # sn_data (1 SN)
        sne = np.rec.array(np.zeros(1, dtype=TrainingDataset.sn_data_dtype))
        sne['valid'] = 1

        # light curves
        lc_data = []
        mjd = np.linspace(phase_range[0], phase_range[1], 100)
        block_size = len(mjd)
        if band_names is not None:
            for band_name in band_names:
                block = np.zeros(block_size,
                                 dtype=TrainingDataset.lc_data_dtype)
                block['mjd'] = mjd
                block['band'] = band_name
                block['magsys'] = magsys
                block['valid'] = 1
                lc_data.append(block)
            lc_data = np.rec.array(np.hstack(lc_data))
            self.lc_mjd = lc_data['mjd'].copy()
        else:
            lc_data = None
            self.lc_mjd = None

        # spectra
        spec_data = []
        for sp in range(n_spectra):
            wl = np.linspace(3000., 11000., 8000)
            block_size = len(wl)
            block = np.zeros(block_size,
                             dtype=TrainingDataset.spec_data_dtype)
            block['wavelength'] = wl
            block['valid'] = 1
            spec_data.append(block)
        spec_data = np.rec.array(np.hstack(spec_data))

        # photometric spectra
        spectrophotometric_data = []
        for sp in range(n_phot_spectra):
            wl = np.linspace(3000., 11000., 8000)
            block_size = len(wl)
            block = np.zeros(block_size,
                             dtype=TrainingDataset.spec_data_dtype)
            block['wavelength'] = wl
            block['valid'] = 1
            spectrophotometric_data.append(block)
        spectrophotometric_data = np.rec.array(np.hstack(spectrophotometric_data))

        return TrainingDataset(sne, lc_data, spec_data, spectrophotometric_data,
                               load_filters=True)

    def __call__(self, p):
        """
        """
        vals = self.model(p)

        # split the values into phot/spec/spectrophot blocks
        # depending on what we have in the dataset
        # TODO: there should be a tds function to handle that
        phot_blksize, spec_blksize, spectrophot_blksize = 0, 0, 0
        if self.tds.lc_data is not None:
            phot_blksize = len(self.tds.lc_data.nt)
            self.phot_vals = vals[0:phot_blksize]
        if self.tds.spec_data is not None:
            spec_blksize = len(self.tds.spec_data.nt)
            if spec_blksize > 0:
                self.spec_vals = vals[phot_blksize:phot_blksize+spec_blksize]
        if self.tds.spectrophotometric_data is not None:
            spectrophot_blksize = len(self.tds.spectrophotometric_data)
            if spectrophot_blksize > 0:
                offset = phot_blksize + spec_blksize
                self.spectrophot_vals = vals[offset:]
        # self.phot_vals = vals[:n]
        # self.spec_vals = vals[n:]
        # self.spectrophot_vals = vals[]

    def set_sn_pars(self, z, x0, x1, c, tmax, spec_mjd=None):
        """
        """
        # SN local parameters
        self.tds.sn_data.nt['z'] = z
        self.tds.sn_data.nt['x0'] = x0
        self.tds.sn_data.nt['x1'] = x1
        self.tds.sn_data.nt['c'] = c
        self.tds.sn_data.nt['tmax'] = tmax

        # redshift
        if self.tds.lc_data:
            self.tds.lc_data.z[:] = z
        if self.tds.spec_data:
            self.tds.spec_data.z[:] = z
        if self.tds.spectrophotometric_data:
            self.tds.spectrophotometric_data.z[:] = z

        # mjd
        if self.tds.lc_data:
            self.tds.lc_data.nt['mjd'] = self.lc_mjd + tmax

        if spec_mjd is None:
            spec_mjd = tmax
        if self.tds.spec_data:
            self.tds.spec_data.nt['mjd'] = spec_mjd
        if self.tds.spectrophotometric_data:
            self.tds.spectrophotometric_data.nt['mjd'] = spec_mjd

    def load_sn_pars(self, sn, tds, pars=None, spec_mjd=None):
        """
        """
        idx = tds.sn_data.sn == sn
        assert idx.sum() == 1
        s = tds.sn_data.nt[idx]
        if pars is None:
            self.set_sn_pars(s.z, s.x0, s.x1, s.col, s.tmax, spec_mjd=spec_mjd)
        else:
            sn_index = tds.sn_data.sn_map[sn]
            self.set_sn_pars(s.z,
                             pars['X0'].full[sn_index],
                             pars['X1'].full[sn_index],
                             pars['c'].full[sn_index],
                             pars['tmax'].full[sn_index],
                             spec_mjd=spec_mjd)

        # load the light curve zp
        # todo: simplify this ! A tds should be able to
        # retrieve the zp of a given SN light curve.
        if self.bands is not None:
            for band in self.bands:
                idx = (tds.lc_data.sn == sn) & (tds.lc_data.band == band)
                local_idx = self.tds.lc_data.band == band
                # if the band is not in the tds
                # we set the zp to, say, 15.
                if idx.sum() == 0:
                    logging.warning(f'{band}: no data for sn#{sn}')
                    self.tds.lc_data.zp[local_idx] = 15.
                else:
                    zp = tds.lc_data.zp[idx]
                    assert np.all(zp == zp[0])
                    sel = self.tds.lc_data.band == band
                    self.tds.lc_data.zp[local_idx] = zp[0]
            self.tds.compute_photometric_norm_factors()

        # evaluate the model
        # TODO: we shouldn't have to re-instantiate the model...
        self.model = self.model_type(self.tds,
                        init_from_salt2_file=self.init_from_salt2_file)
        self.model.init_from_training_dataset()
        self(self.model.pars.free)

    def plot_lc(self, band, ax=None, **kwargs):
        """
        """
        if not ax:
            ax = plt.gca()
        idx = self.tds.lc_data.band == band
        if idx.sum() == 0:
            return
        ax.plot(self.tds.lc_data.mjd[idx], self.phot_vals[idx], **kwargs)

    def plot_spectrum(self, ax=None, phot=False, spec=0, **kwargs):
        """
        """
        spec_data, vals = None, None
        if not phot:
            spec_data = self.tds.spec_data
            vals = self.spec_vals
        else:
            spec_data = self.tds.spectrophotometric_data
            vals = self.spectrophot_vals
        assert spec_data is not None and vals is not None

        idx = spec_data.spec == spec
        if idx.sum() == 0:
            return
        ax = kwargs.get('ax', None)
        if not ax:
            ax = plt.gca()
        ax.plot(spec_data.wavelength[idx],
                vals[idx], **kwargs)
