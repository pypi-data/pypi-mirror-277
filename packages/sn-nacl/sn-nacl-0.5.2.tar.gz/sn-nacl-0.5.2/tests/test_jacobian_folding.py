#!/usr/bin/env python

import os
import sys
import time
from pathlib import Path
import logging
import pandas

import numpy as np
import pylab as pl

from sparse_dot_mkl import dot_product_mkl

from lemaitre import bandpasses
from nacl import TrainingDataset, LogLikelihood, Minimizer
from nacl.models import salt2
from nacl.models.salt2 import constraints
from nacl.models.salt2.regularizations import NaClSplineRegularization



def clean_dataset(tds, phase_range=(-25., +80.)):
    """
    """
    # clean ZTF19adcecwu
    idx = (tds.lc_data.sn == 'ZTF19adcecwu') & (tds.lc_data.mjd > 58840) & (tds.lc_data.flux<10000.)
    logging.info(f'removing {idx.sum()} outliers identified on ZTF19adcecwu g- and r- DR2 lightcurves')
    tds.lc_data.valid[idx] = 0

    # phase range (photometric data)
    tmax = np.zeros(len(tds.sn_data))
    tmax[tds.sn_data.sn_index] = tds.sn_data.tmax
    phot_tmax = tmax[tds.lc_data.sn_index]
    phase = (tds.lc_data.mjd - phot_tmax) / (1. + tds.lc_data.z)
    print(phase)
    print(phase_range)
    idx = (phase<phase_range[0]) | (phase>phase_range[1])
    logging.info(f'removing {idx.sum()} photometric points outside phase range')
    tds.lc_data.valid[idx] = 0

    # phase range (spectra)
    spec_tmax = tmax[tds.spec_data.sn_index]
    phase = (tds.spec_data.mjd - spec_tmax) / (1. + tds.spec_data.z)
    idx = (phase<phase_range[0]) | (phase>phase_range[1])
    logging.info(f'removing {idx.sum()} spectroscopic points outside phase range')
    tds.spec_data.valid[idx] = 0

    # points of the edge of the wavelength basis
    i_basis_max = tds.spec_data.i_basis.max()
    idx = (tds.spec_data.i_basis < 2) | (tds.spec_data.i_basis >= (i_basis_max-2))
    logging.info(f'removing {idx.sum()} spectroscopic points outside wavelength range')
    tds.spec_data.valid[idx] = 0

    # clean all SNe below 0.02
    #idx = (tds.lc_data.z < 0.01)
    #logging.info(f'removing {idx.sum()} very low redshift SNe')
    #tds.lc_data.valid[idx] = 0

    tds.compress()




def main(lc_only=False, spec_only=False,
         model_phase_range=(-20., +50.),
         data_phase_range=(-20., +40.)):
    # trainin dataset
    fl = bandpasses.get_filterlib()
    tds = TrainingDataset.read_parquet('lemaitre.compressed.parquet',
                                       filterlib=fl)
    clean_dataset(tds, phase_range=data_phase_range)

    if lc_only:
        tds = TrainingDataset(sne=tds.sn_data.nt,
                              lc_data=tds.lc_data.nt,
                              basis=tds.basis,
                              filterlib=fl)
    elif spec_only:
        tds = TrainingDataset(sne=tds.sn_data.nt,
                              spec_data=tds.spec_data.nt,
                              basis=tds.basis,
                              filterlib=fl)

    # model 
    model = salt2.SALT2Like(tds,
                            # phase_range=model_phase_range,
                            wl_grid=tds.basis.grid,
                            spectrum_recal_degree=3)
    
    # likelihood 
    ll = LogLikelihood(model)
    pars = model.init_pars()


    # minimizer
    mn = Minimizer(ll)
    
    # preliminary control plots : how does the model compare with the data ?
    v = model(pars)

    # recalibrate the spectra
    # r = recalib_spectra(tds, v)
    # if not lc_only:
    #    ll.pars['SpectrumRecalibration'].full[3::4] = np.log(r)
    #    pars['SpectrumRecalibration'].full[3::4] = np.log(r)

    return fl, tds, model, ll, pars, mn, v



if __name__ == '__main__':

    fl, tds, model, ll, pars, mn, v = main(lc_only=False)
    v, J = model(ll.pars, jac=1)
    J = J.tocsr()

    # use mkl
    t_start = time.perf_counter()
    H = dot_product_mkl(J.T, J, reorder_output=True)
    t_end = time.perf_counter()
    print(f'MKL: {t_end-t_start}, {H.shape}')

