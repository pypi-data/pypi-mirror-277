"""
"""

import collections.abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Protocol, Tuple, Union

import astropy.cosmology
import numpy as np
import pandas
import pylab as pl

from ...dataset import TrainingDataset
from . import cadences as cads
from ..randutils import draw_from_hist

# class SnSurvey(ABC):
#     """A base class for SnSurveys 
    
#     SnSurveys are given a SN sample and an observing 
#     log and generate a supernova training sample from that.
    
#     """
#     @abstractmethod
#     def observe(self):
#         """Determine the observation log for each SN
#         """
#         pass

#     def model(self):
#         pass
    
#     def add_noise(self):
#         pass

    
# class SimpleSNSurvey:
#     """
#     """
#     def __init__(self, sample, obslog, model):
#         """
#         """
#         self.sample = sample
#         self.obslog = obslog
#         self.model = model

#     def observe(self):
#         """Generate an observation log for all supernovae in the sample
#         """
#         pass
        
    
# class FieldSNSurvey(SnSurvey):
    
#     def __init_(self, sample, obslog, model):
#         self.sample = sample
#         self.obslog = obslog
#         self.model = model
        
#     def observe(self):
#         pass
    

# class HealpixSNSurvey(SnSurvey):

#     def __init__(self, sample, obslog, model):
#         self.sample = sample
#         self.obslog = obslog
#         self.model = model

        
if __name__ == '__main__':
    """
    """
    # first, we need a SN sample
    gen = DVDzSNFactory(nsn=5000)
    sample = gen.generate_sample()
    
    # then, we need a cadence
    cad = cads.MetronomicCadenceFactory(specs = {
        'LSST::g': cads.CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22., delta_t_band=0.00), 
        'LSST::r': cads.CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22., delta_t_band=0.30), 
        'LSST::i': cads.CadenceSpecs(delta_t=2., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22., delta_t_band=0.2), 
        'LSST::z': cads.CadenceSpecs(delta_t=2., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22., delta_t_band=1.00), 
        'LSST::y': cads.CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22., delta_t_band=1.03), 
    })
    obslog = cad()

    # then, we need a cadence
    cad2 = cads.RandomCadenceFactory(specs = {
        'LSST::g': cads.CadenceSpecs(delta_t=4., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22.), 
        'LSST::r': cads.CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22.), 
        'LSST::i': cads.CadenceSpecs(delta_t=2., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22.), 
        'LSST::z': cads.CadenceSpecs(delta_t=2., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22.), 
        'LSST::y': cads.CadenceSpecs(delta_t=3., seeing=(0.8,1.), airmass=1., exptime=200., mag_sky=22.), 
    })
    obslog2 = cad2()
    

    mjd_min = 9
    mjd_max = 12220
    cad3 = np.linspace(mjd_min, mjd_max, 100)

    
    

                                
