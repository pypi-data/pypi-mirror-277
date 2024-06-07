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


def load(filename='tds_test_deriv', keep=None):
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


def test_kron(filename='compressed_lm2'):

    tds = load(filename)
    model = salt2.SALT2Like(tds)
    pars = model.init_pars()
    ll = lightcurves.LightcurveEvalUnit(model)
    F = ll.meas_filter_projections
    restframe_phase = (tds.lc_data.mjd - pars['tmax'].full[tds.lc_data.sn_index]) / (1. + tds.lc_data.z)
    ph_basis = ll.model.basis.by
    J = ph_basis.eval(restframe_phase)

    return J, F


def test_deriv(model, pars, block_name='M0'):
    """
    """
    #       pars = model.init_pars()
    pars.fix()
    pars.release(block_name)

    J, Jn = helpers.check_grad(model, pars, dx=1.E-7)
    print(J.shape, Jn.shape)
    J = J.ravel()
    Jn = Jn.ravel()
    idx = (np.abs(J) > 0) | (np.abs(Jn) > 0)

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
    fig.suptitle(f'derivatives: {block_name}')
    axes[0,0].plot(J[idx], Jn[idx], 'k.')
    axes[0,0].set_xlabel('$\partial_{true}$')
    axes[0,0].set_ylabel('$\partial_{num}$')

    axes[0,1].plot((J[idx] - Jn[idx])/Jn[idx], 'k.')
    axes[0,1].set_xlabel('i')
    axes[0,1].set_ylabel('$(\partial_{true} - \partial_{num}) / \partial_{num}$')

    axes[1,0].plot(J[idx], (J[idx] - Jn[idx])/Jn[idx], 'k.')
    axes[1,0].set_xlabel('$\partial_{true}$')
    axes[1,0].set_ylabel('$(\partial_{num} - \partial_{true})/\partial_{num}$')

    axes[1,1].plot(J[idx] - Jn[idx], 'k.')
    axes[1,1].set_xlabel('$i$')
    axes[1,1].set_ylabel('$\partial_{true} - \partial_{num}$')

    return J, Jn


if __name__ == '__main__':
    tds = load()
    model = salt2.SALT2Like(tds)
    pars = model.init_pars()
    # wl = np.linspace(2200., 9200., 250)

    ll = lightcurves.LightcurveEvalUnit(model)

    for block_name in ['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']:
        logging.info(f'testing: {block_name}')
        test_deriv(ll, pars, block_name)

    pars.fix()
    pars.release('M0')
    J, Jn = helpers.check_grad(ll, pars, dx=1.E-7)
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16,5),
                             sharex=True, sharey=True)
    fig.suptitle('M0')
    axes[0].imshow(J, aspect='auto', vmin=-0.1, vmax=0.1)
    axes[0].set_title('analytical')
    axes[1].imshow(Jn, aspect='auto', vmin=-0.1, vmax=0.1)
    axes[1].set_title('numerical')
    c = axes[2].imshow((J-Jn)/Jn, aspect='auto', vmin=-1., vmax=1.)
    plt.colorbar(c)
    axes[2].set_title('(J-Jn)/Jn')

    pars.fix()
    pars.release('M1')
    J, Jn = helpers.check_grad(ll, pars)
    fig.suptitle('M1')
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16,5),
                             sharex=True, sharey=True)
    axes[0].imshow(J, aspect='auto', vmin=-0.1, vmax=0.1)
    axes[0].set_title('analytical')
    axes[1].imshow(Jn, aspect='auto', vmin=-0.1, vmax=0.1)
    axes[1].set_title('numerical')
    c = axes[2].imshow((J-Jn)/Jn, aspect='auto', vmin=-1., vmax=1.)
    plt.colorbar(c)
    axes[2].set_title('(J-Jn)/Jn')
