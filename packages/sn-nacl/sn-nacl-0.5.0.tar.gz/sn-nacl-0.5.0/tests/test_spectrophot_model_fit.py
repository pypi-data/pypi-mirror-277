#!/usr/bin/env python3

import logging

import numpy as np
import matplotlib.pyplot as plt

from lemaitre import bandpasses
from nacl.models import helpers
from nacl.models import salt2
from nacl.models.salt2 import lightcurves
from nacl.models.salt2 import spectra
from nacl import TrainingDataset
from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer



def load(filename='snf_projected.hd5', keep=['SNF20051003-004', 'PTF10qyz', 'PTF11kly', 'SNF20080803-000']):
    """
    """
    fl = bandpasses.get_filterlib()

    if 'hd5' in filename:
        tds = TrainingDataset.read_hdf(filename)
    else:
        tds = TrainingDataset.read_parquet(filename, filterlib=fl)

    if keep is not None:
        sne = tds.sn_data.sn_set.tolist()
        for k in keep:
            sne.remove(k)
        tds.kill_sne(sne)
        tds.compress()

    return tds


def plot_spectrum(model, pars, spec=None, spec_index=None):
    """
    """
    tds = model.training_dataset
    if spec is not None:
        idx = tds.spectrophotometric_data.spec == spec
    elif spec_index is not None:
        idx = tds.spectrophotometric_data.spec_index == spec_index
    else:
        return

    ib = tds.spectrophotometric_data.i_basis[idx]
    wl = tds.spectrophotometric_data.wavelength[idx]
    flx = tds.spectrophotometric_data.flux[idx]
    flxerr = tds.spectrophotometric_data.fluxerr[idx]

    print(flx)

    v = model(pars)

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,8), sharex=True)
    axes[0].errorbar(wl, flx, yerr=flxerr, ls='', marker='.', color='b')
    axes[0].plot(wl, v[idx], 'r+')
    axes[1].plot(wl, flx/v[idx], 'b.')
    print(np.median(flx/v[idx]))





if __name__ == '__main__':
    tds = load(keep=None)
    # quick hack
    n = len(tds.spectrophotometric_data)
    tds.spectrophotometric_data.add_field('valid', np.ones(n).astype(int))

    model = salt2.SALT2Like(tds, wl_grid=np.linspace(2000., 11000., 202))
    # pars = model.init_pars()
    # wl = np.linspace(2200., 9200., 250)
    #    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']:
    #        logging.info(f'testing: {block_name}')
    #        test_deriv(model, pars, block_name)


    ll = LogLikelihood(model)
    init_pars = ll.pars.copy()

    ll.pars.fix()
    ll.pars.release('X1')
    mm = Minimizer(ll)
    #mm.minimize(ll.pars.free)

    #plt.figure()
    #plt.plot(init_pars['X0'].full-ll.pars['X0'].full, 'k.')
