"""Simple cadence generators for simple survey simulations

"""

from dataclasses import dataclass
from typing import Dict, Protocol, Tuple, Union

import numpy as np
import pandas

# cadence specifications
@dataclass
class CadenceSpecs:
    delta_t: float = 3.
    delta_t_band: float = 0.
    airmass: Union[float, Tuple[float,float]] = 1.
    seeing: Union[float, Tuple[float,float]] = 0.8
    exptime: float = 100.
    mag_sky: Union[float, Tuple[float,float]] = 20.5

lsst_ddf_ideal = {
    'LSST::g': CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=600., mag_sky=22., delta_t_band=0.00),
    'LSST::r': CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=600., mag_sky=21.2, delta_t_band=0.30),
    'LSST::i': CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=600., mag_sky=20.5, delta_t_band=0.2),
    'LSST::z': CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=600., mag_sky=19.6, delta_t_band=1.00),
    'LSST::y4': CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=600., mag_sky=18.6, delta_t_band=1.03),}

lsst_wfd_ideal = {
    'LSST::g': CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=30., mag_sky=22., delta_t_band=0.00),
    'LSST::r': CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=30., mag_sky=21.2, delta_t_band=0.30),
    'LSST::i': CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=30., mag_sky=20.5, delta_t_band=0.2),
    'LSST::z': CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=30., mag_sky=19.6, delta_t_band=1.00),
    'LSST::y4': CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=30., mag_sky=18.6, delta_t_band=1.03),}

ztf_ideal = {
    'ZTF::g': CadenceSpecs(delta_t=3., seeing=(2.,4.), airmass=1., exptime=30., mag_sky=22., delta_t_band=0.00),
    'ZTF::r': CadenceSpecs(delta_t=3., seeing=(2.,4.), airmass=1., exptime=30., mag_sky=21.2, delta_t_band=0.30),
    'ZTF::I': CadenceSpecs(delta_t=3., seeing=(2.,4.), airmass=1., exptime=30., mag_sky=19.6, delta_t_band=0.2),
}


def _range(x):
    """return a range from either a scalar or a tuple
    """
    if hasattr(x, '__len__') and len(x) == 2:
        return x
    elif isinstance(x, (int, float)):
        return (x,x)
    else:
        raise ValueError(f'{x} is neither a scalar nor a range definition')


class CadenceFactory(Protocol):
    def __call__(self):
        ...


class MetronomicCadenceFactory:
    """Regular sampling in all listed bands.

    following the specifications passed in argument.
    """
    def __init__(self, specs: Dict[str,CadenceSpecs], mjd_range=(0,150), n_fields=1):
        """Constructor

        Parameters
        ----------
        specs: Dict[str,CadenceSpecs]
          cadence specifications
        mjd_range: Tuple[float,float]
          mjd_range (beginning/end of the survey)
        """
        self.specs = specs
        self.mjd_range = mjd_range
        self.n_fields = n_fields
        self.obslog = None

    def __call__(self):
        """Generate the observation log

        The observation log is returned as a DataFrame, sorted by
        field and mjd.

        .. todo::
          add field index to make it easy to access all the data
          for a given field.
        """
        blocks = []
        mjd_min, mjd_max = self.mjd_range

        for band_name in self.specs:
            specs = self.specs[band_name]
            mjd = np.arange(mjd_min, mjd_max, specs.delta_t)
            N = len(mjd)
            mjd += specs.delta_t_band

            blk = {
                'mjd': mjd,
                'band': band_name,
                'airmass': np.random.uniform(*_range(specs.airmass), size=N),
                'seeing': np.random.uniform(*_range(specs.seeing), size=N),
                'exptime': specs.exptime,
                'mag_sky': np.random.uniform(*_range(specs.mag_sky), size=N),
                'zp': 0.,
                'ra': 0.,
                'dec': 0.,
                'field': 0,
                }
            blocks.append(pandas.DataFrame(blk))
        obslog = pandas.concat(blocks).sort_values(by=['field', 'mjd'])

        # if more than one field is requested
        # (the justifiation for this cadence would be just performance evaluation)
        # then, duplicate the obslog as many times as requested
        i = np.tile(np.arange(len(obslog)), self.n_fields)
        field_id = np.repeat(np.arange(self.n_fields), len(obslog))

        self.obslog = obslog.iloc[i].copy()
        self.obslog.loc[:,'field'] = field_id

        return self.obslog


class RandomCadenceFactory:
    """Same as above, with random (uniform) observation dates
    """

    def __init__(self, specs: Dict[str,CadenceSpecs], mjd_range=(0., 150.), n_fields=1):
        """Constructor

        Parameters
        ----------
        specs: Dict[str,CadenceSpecs]
          cadence specification
        mjd_range: Tuple[float,float]
          mjd_range (beginning/end of the survey)
        """
        self.specs = specs
        self.mjd_range = mjd_range
        self.n_fields = n_fields

    def __call__(self):
        """generate the observation log
        """
        blocks = []
        mjd_min, mjd_max = self.mjd_range

        for field in range(self.n_fields):
            for band_name in self.specs:
                specs = self.specs[band_name]
                N = int(np.floor((mjd_max-mjd_min) / specs.delta_t))
                mjd = np.random.uniform(mjd_min, mjd_max, size=N)
                mjd.sort()

                blk = {
                    'mjd': mjd,
                    'band': band_name,
                    'airmass': np.random.uniform(*_range(specs.airmass), size=N),
                    'seeing': np.random.uniform(*_range(specs.seeing), size=N),
                    'exptime': specs.exptime,
                    'mag_sky': np.random.uniform(*_range(specs.mag_sky), size=N),
                    'field': field,
                    }
                blocks.append(pandas.DataFrame(blk))

        self.obslog = pandas.concat(blocks).sort_values(by=['field', 'mjd'])

        return self.obslog


class RealCadenceFactory:
    def __init__(self, name, version=None):
        """Constructor - initialize the

        Parameters
        ----------
        name : str
            the generic cadence name -- e.g. `baseline`, `kraken`
        version : str, optional
            version , by default None
            a given cadence may have been released several times.
        """
        self.name = name
        self.version = version
        self.obslog = self._load(name, version)

    def _load(self, name, version):
        pass

    def __call__(self):
        return self.obslog


