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


def test_deriv(model, pars, block_name='M0'):
    """
    """
    #       pars = model.init_pars()
    pars.fix()
    pars.release(block_name)

    J, Jn = helpers.check_grad(model, pars)
    print(J.shape, Jn.shape)
    J = J.ravel()
    Jn = Jn.ravel()
    idx = (np.abs(J) > 0) | (np.abs(Jn) > 0)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
    fig.suptitle(f'derivatives: {block_name}')
    axes[0,0].plot(J[idx], Jn[idx], 'k.')
    axes[0,0].set_xlabel('$\partial_{true}$')
    axes[0,0].set_ylabel('$\partial_{num}$')

    axes[1,1].plot(J[idx] - Jn[idx], 'k.')
    axes[1,1].set_xlabel('$i$')
    axes[1,1].set_ylabel('$\partial_{true} - \partial_{num}$')

    axes[0,1].plot((J[idx] - Jn[idx])/J[idx], 'k.')
    axes[0,1].set_xlabel('i')
    axes[0,1].set_ylabel('$(\partial_{num} - \partial_{true}) / \partial_{true}$')

    axes[1,0].plot(J[idx], J[idx] - Jn[idx], 'k.')
    axes[1,0].set_xlabel('$\partial_{true}$')
    axes[1,0].set_ylabel('$\partial_{num} - \partial_{true}$')

    return J, Jn

if __name__ == '__main__':
    tds = load()
    model = salt2.SALT2Like(tds, wl_grid=np.linspace(2000., 11000., 202))
    pars = model.init_pars()
    wl = np.linspace(2200., 9200., 250)

    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']:
        logging.info(f'testing: {block_name}')
        test_deriv(model, pars, block_name)
