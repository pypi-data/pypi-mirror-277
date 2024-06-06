#!/usr/bin/env python

import os
import sys
from pathlib import Path
import logging
import pickle
from argparse import ArgumentParser

import matplotlib as mpl
import numpy as np
import numpy.ma as ma
import pylab as pl
import pandas

from lemaitre import bandpasses
from nacl import TrainingDataset, LogLikelihood, Minimizer
from nacl.models import salt2
from nacl.models.salt2 import constraints
from nacl.models.salt2.regularizations import NaClSplineRegularization
from nacl.models.salt2.variancemodels import SimpleErrorSnake, LocalErrorSnake

from saunerie.robuststat import mad


_band_ordering = {'u': 0, 'U': 0, 'g': 1, 'B': 2, 'r': 3, 'r2': 3,
                  'R': 4, 'i': 5, 'i2': 5, 'I': 6, 'z': 7, 'Y': 8}

def _get_band_order(band):
    b = band.split('::')[-1]
    return _band_ordering.get(b, 100)


def order_bands(bands):
    l = bands.sort(key=_get_band_order)
    return l


def clone(tds, sn, phase_range=(-25, 51., 1.)):
    """
    """
    # sn metadata
    sn_data = tds.sn_data.nt[tds.sn_data.sn == sn]
    
    # lightcurve data
    if tds.lc_data is not None:
        lc_data = tds.lc_data.nt[tds.lc_data.sn == sn]

        tmax = float(sn_data.tmax)
        z = float(sn_data.z)
        phase = np.arange(*phase_range)
        mjd = phase * (1.+z) + tmax
        N = len(mjd)
        l = []
        for b in np.unique(lc_data.band):
            d = lc_data[lc_data.band == b]
            Z = np.full(len(mjd), d[0])
            Z['mjd'] = mjd
            Z['flux'] = 0.
            Z['fluxerr'] = 0.
            Z['valid'] = 1
            l.append(Z)
        lc_data = np.rec.array(np.hstack(l))
    else:
        lc_data = None
        
    if tds.spec_data is not None:
        spec_data = tds.spec_data.nt[tds.spec_data.sn == sn]
    else:
        spec_data = None
    if tds.spectrophotometric_data is not None:
        spectrophotometric_data = tds.spectrophotometric_data.nt[tds.spectrophotometric_data.sn == sn]
    else:
          spectrophotometric_data = None
          
    
    tds = TrainingDataset(sn_data, lc_data=lc_data,
                          spec_data=None,
                          spectrophotometric_data=None,
                          filterlib=tds.filterlib)
    
    return tds


def plot_lc(sn, tds, pars=None, model=None, phase=False, v=None, norm=1.): # was norm=8.5E-13
    """
    """
    sel = tds.lc_data.sn == sn
    bands = np.unique(tds.lc_data.band[sel]).tolist()
    bands.sort(key=_get_band_order)
    nrows = len(bands)

    sn_idx = tds.sn_data.sn == sn
    tmax = float(tds.sn_data.tmax[sn_idx])
    z = float(tds.sn_data.z[sn_idx])
    sn_index = int(tds.sn_data.sn_index[sn_idx])

    if pars is not None:
        t = clone(tds, sn)
        m = salt2.SALT2Like(t)
        p = m.init_pars()
        for nm in ['M0', 'M1', 'CL']:
            p[nm].full[:] = pars[nm].full[:]
        for nm in ['X0', 'X1', 'col', 'tmax']:
            p[nm].full[0] = pars[nm].full[sn_index]
        v_pars = m(p)
    # else:
    #     v = v[sel]

    fig, axes = pl.subplots(nrows=nrows, ncols=1,
                            figsize=(8,12),
                            sharex=True)
    for i,b in enumerate(bands):
        idx = sel & (tds.lc_data.band == b)
        wl = tds.lc_data.wavelength[idx].mean()
        color = pl.cm.jet(int((wl-2000)/(9000.-2000.) * 256))

        if phase:
            xx = (tds.lc_data.mjd[idx] - tmax) / (1. + z)
            axes[i].axvline(0., ls=':')
        else:
            xx = tds.lc_data.mjd[idx]
            axes[i].axvline(tmax, ls=':')

        axes[i].errorbar(xx, tds.lc_data.flux[idx],
                         yerr=tds.lc_data.fluxerr[idx],
                         ls='', marker='.', color=color)

        if v is not None:
            vv = v[:len(tds.lc_data)]
            axes[i].plot(xx, norm*vv[idx], color=color, ls='', marker='+')

        if pars is not None:
            iii = t.lc_data.band == b
            if phase:
                xx = (t.lc_data.mjd[iii] - tmax) / (1. + z)
            else:
                xx = t.lc_data.mjd[iii]
            axes[i].plot(xx, norm * v_pars[iii], ls=':', color=color)

        axes[i].set_ylabel(b)

    axes[-1].set_xlabel('mjd')
    pl.subplots_adjust(hspace=0.05)
    fig.suptitle(f'{sn} @ z={z:4.3}')


def recalib_spectrum(spec, tds, v):
    """
    """
    sel = tds.spec_data.spec == spec
    vv = v[len(tds.lc_data):]

    fig, axes = pl.subplots(nrows=3, ncols=1, figsize=(8, 10),
                            sharex=True)
    axes[0].errorbar(tds.spec_data.wavelength[sel], tds.spec_data.flux[sel],
                     yerr=tds.spec_data.fluxerr[sel], ls='', marker='.')
    axes[0].plot(tds.spec_data.wavelength[sel], vv[sel], marker='.', color='r')

    r = tds.spec_data.flux[sel]/vv[sel]
    axes[1].errorbar(tds.spec_data.wavelength[sel], r,
                     yerr=tds.spec_data.fluxerr[sel], ls='', marker='.')

    recal = np.median(r)
    axes[2].errorbar(tds.spec_data.wavelength[sel], tds.spec_data.flux[sel],
                     yerr=tds.spec_data.fluxerr[sel], ls='', marker='.')
    axes[2].plot(tds.spec_data.wavelength[sel], vv[sel] * recal, marker='.', color='r')

    return recal


def recalib_spectra(tds, v):
    """
    """
    vv = v[len(tds.lc_data):]
    ii = np.arange(len(vv))
    idx = np.abs(tds.spec_data.fluxerr / tds.spec_data.flux) < 1.
    zero_fluxerr = np.abs(tds.spec_data.fluxerr) <= 0.
    logging.info(f'ignoring {zero_fluxerr.sum()} points with buggy flux errs')
    idx &= ~zero_fluxerr
    neg_flux = tds.spec_data.flux <= 0.
    idx &= ~neg_flux


    fig, axes = pl.subplots(nrows=3, ncols=1, figsize=(8, 10),
                            sharex=True)
    axes[0].errorbar(ii[idx], tds.spec_data.flux[idx],
                     yerr=tds.spec_data.fluxerr[idx], ls='', marker='.')
    axes[0].plot(ii[idx], vv[idx], marker='.', color='r')

    r = np.abs(tds.spec_data.flux / vv)
    r_err = tds.spec_data.fluxerr / np.abs(vv)
    axes[1].plot(ii[idx], r[idx],
                 ls='', marker='.')

    w = 1. / r_err**2
    n = np.bincount(tds.spec_data.spec_index[idx], weights=(w*r)[idx])
    d = np.bincount(tds.spec_data.spec_index[idx], weights=w[idx])
    print(n[1700], d[1700])
    recal = n / d

    v_recal = vv * recal[tds.spec_data.spec_index]

    #axes[2].errorbar(ii[idx], tds.spec_data.flux[idx],
    #                 yerr=tds.spec_data.fluxerr[idx], ls='', marker='.')
    axes[2].plot(ii[idx], tds.spec_data.flux[idx],
                 ls='', marker='.')
    axes[2].plot(ii[idx], v_recal[idx], ls='', marker='.', color='r')

    return recal


def plot_spec(spec, tds, v=None, norm=8.5E-13):
    """
    """
    sel = tds.spec_data.spec == spec
    vv = v[len(tds.lc_data):]

    fig, axes = pl.subplots(nrows=1, ncols=1,
                            figsize=(8,8),
                            sharex=True)

    axes.errorbar(tds.spec_data.wavelength[sel], tds.spec_data.flux[sel],
                     yerr=tds.spec_data.fluxerr[sel],
                     ls='', marker='.', color='blue')

    if v is not None:
        axes.plot(tds.spec_data.wavelength[sel], vv[sel], 'r+:')

    axes.set_ylabel('flux')
    axes.set_xlabel('mjd')
    pl.subplots_adjust(hspace=0.05)
    # xfig.suptitle(f'{sn} @ z={z:4.3}')


class TrainingChi2:

    def __init__(self, tds, pars, model):
        self.tds = tds
        self.pars = pars
        self.model = model
        self._compute()

    def _compute(self):
        """Compute SN/lc/spec partial chi2's
        """
        self.v = self.model(self.pars)
        self.res = self.tds.get_all_fluxes() - self.v
        self.yerr = self.tds.get_all_fluxerr()
        self.wres = self.res / self.yerr

        self.chi2 = (self.wres**2).sum()

        # photometry
        ml = len(tds.sn_data.sn_set)
        self.phot_wres = self.wres[:len(self.tds.lc_data)]
        self.phot_chi2 = (self.phot_wres**2).sum()
        self.phot_chi2_per_sn = np.bincount(self.tds.lc_data.sn_index, weights=self.phot_wres**2, minlength=ml)
        self.phot_chi2_per_sn_count = np.bincount(self.tds.lc_data.sn_index, minlength=ml)
        self.phot_chi2_per_lc = np.bincount(self.tds.lc_data.lc_index, weights=self.phot_wres**2, minlength=ml)
        self.phot_chi2_per_lc_count = np.bincount(self.tds.lc_data.lc_index, minlength=ml)

        # spectroscopy
        # spec_wres = wres[len(tds.lc_data):len(tds.lc_data) + len(tds.spec_data)]
        # spec_chi2 =

        self.r_phot_chi2_per_sn = self.phot_chi2_per_sn / self.phot_chi2_per_sn_count
        self.r_phot_chi2_per_lc = self.phot_chi2_per_lc / self.phot_chi2_per_lc_count

    def get_sorted_list(self, sort_by='sn'):
        """
        """
        if sort_by == 'sn':
            # i = np.argsort(self.r_phot_chi2_per_sn)[::-1]
            d = pandas.DataFrame({'sn': self.tds.sn_data.sn,
                                  'sn_index': self.tds.sn_data.sn_index,
                                  'z': self.tds.sn_data.z,
                                  'rchi2': self.r_phot_chi2_per_sn[self.tds.sn_data.sn_index]})
            d = d.sort_values(by='rchi2', ascending=False)

        elif sort_by == 'lc':
            # i = np.argsort(self.r_phot_chi2_per_lc)
            d = pandas.DataFrame({'lc_index': self.tds.lc_db.lc_index,
                                  'sn': self.tds.sn_data.sn_set[self.tds.lc_db.sn_index],
                                  'band': self.tds.lc_db.band,
                                  'rchi2': self.r_phot_chi2_per_lc[self.tds.lc_db.lc_index]})
            d = d.sort_values(by='rchi2', ascending=False)

        return d


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
    # no: this version does not what we want to do
    # i_basis_max = tds.spec_data.i_basis.max()
    # idx = (tds.spec_data.i_basis < 3) | (tds.spec_data.i_basis >= (i_basis_max-3))
    #
    # we need to determine, for each spectrum, the i_basis_min and i_basis_max
    b_bins = np.arange(-0.5, tds.spec_data.i_basis.max() + 1.5, 1)
    s_bins = np.arange(-0.5, tds.spec_data.spec_index.max() + 1.5, 1)
    h, _, _ = np.histogram2d(tds.spec_data.i_basis, tds.spec_data.spec_index, bins=(b_bins, s_bins))
    bb = np.arange(0, tds.spec_data.i_basis.max() + 1, 1)
    ss = np.arange(0, tds.spec_data.spec_index.max() + 1, 1)
    bb, ss = np.meshgrid(bb, ss)
    u = bb * h.T
    mb = ma.masked_array(u, mask=u==0.)
    b_min, b_max = np.array(np.min(mb, axis=1)), np.array(np.max(mb, axis=1))
    to_kill  = np.array(b_min).astype(int)[tds.spec_data.spec_index] == tds.spec_data.i_basis
    to_kill |= np.array(b_max).astype(int)[tds.spec_data.spec_index] == tds.spec_data.i_basis

    logging.info(f'removing {to_kill.sum()} spectroscopic points outside wavelength range')
    tds.spec_data.valid[to_kill] = 0

    # remove the spectral points with an uncertainty larger than 1.E6


    # clean all SNe below 0.02
    #idx = (tds.lc_data.z < 0.01)
    #logging.info(f'removing {idx.sum()} very low redshift SNe')
    #tds.lc_data.valid[idx] = 0

    tds.compress()


def plot_all_spectra(tds):
    """
    """
    b_bins = np.arange(-0.5, tds.spec_data.i_basis.max()+1.5, 1.)
    s_bins = np.arange(-0.5, tds.spec_data.spec_index.max()+1.5, 1.)
    ttt = tds.spec_db.copy()
    u = ttt.argsort(order='z')
    k = dict([(u[i], i) for i in range(len(u))])
    pl.hist2d(tds.spec_data.i_basis, np.array([k[i] for i in tds.spec_data.spec_index]),
              weights=tds.spec_data.z,
              norm=mpl.colors.LogNorm(),
              bins=(b_bins, s_bins))
    pl.colorbar()
    pl.xlabel('i_basis')
    pl.ylabel('spectrum (ordered by redshift)')

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
    r = recalib_spectra(tds, v)
    if not lc_only:
        ll.pars['SpectrumRecalibration'].full[3::4] = np.log(r)
        pars['SpectrumRecalibration'].full[3::4] = np.log(r)

    return fl, tds, model, ll, pars, mn, v


def compare_fits(tds, pars):
    """
    """
    z = np.zeros(len(tds.sn_data))
    x0 = np.zeros(len(tds.sn_data))
    x1 = np.zeros(len(tds.sn_data))
    col = np.zeros(len(tds.sn_data))
    tmax = np.zeros(len(tds.sn_data))

    z[tds.sn_data.sn_index] = tds.sn_data.z
    x0[tds.sn_data.sn_index] = tds.sn_data.x0
    x1[tds.sn_data.sn_index] = tds.sn_data.x1
    col[tds.sn_data.sn_index] = tds.sn_data.col
    tmax[tds.sn_data.sn_index] = tds.sn_data.tmax

    pl.figure()
    pl.plot(z, x0/ll.pars['X0'].full, 'b.')
    pl.title('X0')
    pl.xlabel('z')
    pl.ylabel('$\Delta X0$')

    pl.figure()
    pl.plot(z, (x1-ll.pars['X1'].full), 'b.')
    pl.title('X1')
    pl.xlabel('z')
    pl.ylabel('$\Delta X1$')

    pl.figure()
    pl.plot(z, (col-ll.pars['col'].full), 'b.')
    pl.title('col')
    pl.xlabel('z')
    pl.ylabel('$\Delta col$')

    pl.figure()
    pl.plot(z, (tmax-ll.pars['tmax'].full), 'b.')
    pl.title('tmax')
    pl.xlabel('z')
    pl.ylabel('$\Delta tmax$')



def load_tds(fn='lemaitre.compressed.parquet',
             data_phase_range=(-20., 40.)):
    """load a training dataset
    """
    fl = bandpasses.get_filterlib()
    tds = TrainingDataset.read_parquet('lemaitre.compressed.parquet',
                                       filterlib=fl)
    clean_dataset(tds, phase_range=data_phase_range)


    # if lc_only:
    #     tds = TrainingDataset(sne=tds.sn_data.nt,
    #                           lc_data=tds.lc_data.nt,
    #                           basis=tds.basis,
    #                           filterlib=fl)
    # elif spec_only:
    #     tds = TrainingDataset(sne=tds.sn_data.nt,
    #                           spec_data=tds.spec_data.nt,
    #                           basis=tds.basis,
    #                           filterlib=fl)

    return tds


class FitRes:
    pass


def fit_local_pars(tds, model, res_init, variance_model=None, plot=False):
    """
    """
    # fl, tds, model, ll, pars, mn, v = main(lc_only=lc_only)
    ll = LogLikelihood(model, variance_model=variance_model)
    ll.pars.fix()
    ll.pars.release('X0')
    ll.pars.release('X1')
    ll.pars.release('col')
    ll.pars.release('tmax')
    ll.pars.release('SpectrumRecalibration')

    # recalibrate the spectra
    v = model(ll.pars)
    r = recalib_spectra(tds, v)
    ll.pars['SpectrumRecalibration'].full[3::4] = np.log(r)
    print(ll.pars['SpectrumRecalibration'].full[:20])

    minz = Minimizer(ll)
    p = minz.minimize_lm(ll.pars.free)
    if plot:
        minz.plot()

    res = FitRes()
    res.ll = ll
    res.minz = minz

    return res


class ModelPlotter:
    """A utility class to plot a smooth continuous (oversampled) photometric model
    """

    def __init__(self, model, sn_index, init_pars, variance_model=None):
        """Constructor - evaluate the model and error model
        """
        self.model = model
        self.tds = model.training_dataset
        self.init_pars = init_pars
        self.variance_model = variance_model
        self._init_local_pars(init_pars, sn_index)

        # evaluate model and variance model
        self.v = self.model(self.pars)
        if variance_model is not None:
            self.v_var = self.variance_model(self.pars)
        else:
            self.v_var = None

    def _init_local_pars(self, init_pars, sn_index):
        """initialize small parameter vector from many-sne one
        """
        if self.variance_model is not None:
            ll = LogLikelihood(model, variance_model=variance_model)
            self.pars = ll.pars.copy()
        else:
            self.pars = self.model.init_pars()

        for nm in ['M0', 'M1', 'CL']:
            self.pars[nm].full[:] = init_pars[nm].full[:]
        for nm in ['X0', 'X1', 'col', 'tmax']:
            self.pars[nm].full[0] = init_pars[nm].full[sn_index]
        if 'gamma' in init_pars._struct.slices:
            self.pars['gamma'].full[:] = init_pars['gamma'].full[:]
        else:
            self.pars['gamma'].full[:] = 0.

        return self.pars

    def plot(self, band, ax=None, **kwargs):
        """plotter - plot the model and error model if needed
        """
        if not ax:
            ax = pl.gca()

        phase = kwargs.get('phase', False)
        color = kwargs.get('color', 'b')
        ls = kwargs.get('ls', ':')
        label = kwargs.get('label', '')
        xlabel= kwargs.get('xlabel', None)
        ylabel= kwargs.get('ylabel', None)
        title = kwargs.get('title', None)
        alpha = kwargs.get('alpha', 0.25)
        legend = kwargs.get('legend', None)

        tmax = float(self.tds.sn_data.tmax[0])
        z = float(self.tds.sn_data.z[0])

        idx = self.tds.lc_data.band == band
        if phase:
            xx = (self.tds.lc_data.mjd - tmax) / (1. + z)
            ax.axvline(0., ls=':')
        else:
            xx = self.tds.lc_data.mjd
            ax.axvline(tmax, ls=':')

        ax.plot(xx[idx], self.v[idx], color=color, ls=ls, label=label)
        if self.variance_model is not None:
            vm = (self.v[idx] - np.sqrt(self.v_var[idx]))
            vp = (self.v[idx] + np.sqrt(self.v_var[idx]))
            ax.fill_between(xx[idx], vm, vp, alpha=0.5, color=color)

        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        if title is not None:
            ax.set_title(title)
        if legend:
            ax.legend(loc=legend)

class Trainer:

    def __init__(self, tds, model, variance_model=None):
        self.tds = tds
        self.model = model
        self.variance_model = variance_model
        self.log = []

        # recalibrate the spectra
        ll = LogLikelihood(self.model)
        self.v_init = self.model(ll.pars)
        self.spec_recal_init = recalib_spectra(self.tds, self.v_init)
        # ll.pars['SpectrumRecalibration'].full[3::4] = np.log(r)

    def fit(self, fix=None, p_init=None,
            p_init_blocks=None,
            fit_variance_model=False,
            force_spec_recalibration=False,
            max_iter=100):
        """
        """
        if fit_variance_model:
            ll = LogLikelihood(self.model, variance_model=self.variance_model)
        else:
            ll = LogLikelihood(self.model)

        if force_spec_recalibration:
            ll.pars['SpectrumRecalibration'].full[3::4] = np.log(self.spec_recal_init)

        if fix:
            for block_name in fix:
                ll.pars[block_name].fix()

        if p_init:
            for block_name in p_init._struct.slices:
                if block_name not in ll.pars._struct.slices:
                    continue
                ll.pars[block_name].full[:] = p_init[block_name].full[:]

        if p_init_blocks:
            for block_name in p_init_blocks:
                if block_name not in ll.pars._struct.slices:
                    continue
                ll.pars[block_name].full[:] = p_init_blocks[block_name]

        print(ll.pars)

        # fit
        minz = Minimizer(ll)
        p = minz.minimize_lm(ll.pars.free, max_iter=max_iter)

        res = FitRes()
        res.pars = ll.pars
        res.ll = ll
        res.minz = minz
        res.v = model(res.ll.pars, jac=0)
        res.v_var = None
        if self.variance_model is not None and fit_variance_model:
            res.v_var = self.variance_model(res.ll.pars, jac=0)

        return res

    def train(self):
        """Full model training
        """
        # initialization: PETS sncosmo/salt2 fits
        f0 = FitRes()
        f0.ll = LogLikelihood(self.model)
        f0.pars = f0.ll.pars
        f0.v = self.model(f0.pars)
        f0.var_v = None
        self.log.append(f0)

        # initialization : fit the light curves and spectra
        # no error model
        f1 = self.fit(fix=['M0', 'M1', 'CL'],
                      fit_variance_model=False,
                      force_spec_recalibration=True,
                      max_iter=10)
        self.log.append(f1)

        # fit an error model, all other pars fixed
        f2 = self.fit(fix=['M0', 'M1', 'CL', 'X0', 'X1', 'col', 'tmax', 'SpectrumRecalibration'],
                      fit_variance_model=True,
                      p_init=f1.ll.pars,
                      p_init_blocks={'gamma': -5.},
                      max_iter=10)
        self.log.append(f2)

        # refit the light curves and spectra,
        # with an error model
        f3 = self.fit(fix=['M0', 'M1', 'CL'],
                      fit_variance_model=True,
                      p_init=f2.ll.pars,
                      max_iter=10)
        self.log.append(f3)

        # train
        #f4 = self.fit(variance_model=True,
        #              p_init=f3.ll.pars)
        #self.log.append(f4)

    def _get_models_to_plot(self, numfit, pars):
        """
        """
        fits = []

        if numfit is not None:
            try:
                iter(numfit)
                fits.extend(self.log[i] for i in numfit)
            except:
                fits.append(self.log[numfit])

        if pars is not None:
            try:
                iter(pars)
                for p in pars:
                    ff = FitRes()
                    ff.pars = pars
                    ff.v = self.model(pars)
                    if self.variance_model:
                        ff.var_v = self.variance_model(pars)
                    fits.append(ff)
            except:
                ff = FitRes()
                ff.pars = pars
                ff.v = self.model(pars)
                if self.variance_model:
                    ff.var_v = self.variance_model(pars)
                fits.append(ff)

        return fits


    def plot_lc(self, sn, numfit=None, pars=None,
                phase=False, norm=1.,
                plot_variance=False):
        """plot light curve data + models

        Parameters
        ----------
        sn : (int | str)
          the supernova to plot
        numfit : int, optional
          which fit to plot (drawn from logs)
        pars : FitParameters, optional
          plot an alternate fit, not from self.log
        phase : bool, default False
          whether to plot the the light curve as a function of the phase
        plot_variance : bool, default=False
          whether to plot the error model, if available

        Returns
        -------
        None
        """
        sel = self.tds.lc_data.sn == sn
        bands = np.unique(self.tds.lc_data.band[sel]).tolist()
        bands.sort(key=_get_band_order)
        nrows = len(bands)

        sn_idx = self.tds.sn_data.sn == sn
        tmax = float(self.tds.sn_data.tmax[sn_idx])
        z = float(self.tds.sn_data.z[sn_idx])
        sn_index = int(self.tds.sn_data.sn_index[sn_idx])

        # clone the dataset
        t = clone(tds, sn)
        to_plot = self._get_models_to_plot(numfit, pars)
        m = salt2.SALT2Like(t)
        if self.variance_model is not None:
            vm = self.variance_model.__class__(m)
        else:
            vm = None
        plotters = [ModelPlotter(m, sn_index, tp.ll.pars, variance_model=vm) \
                    for tp in to_plot]

        # create a model
        # m = salt2.SALT2Like(t)
        # if self.variance_model is not None:
        #     vm = self.variance_model.__class__(m)
        # else:
        #     vm = None
        # ll = LogLikelihood(m, variance_model=vm)
        # p = ll.init_pars()

        # which models do we want to plot ?
        # to_plot = self._eval(numfit, pars, sn_index)

        # for tp in to_plot:
        #     for nm in ['M0', 'M1', 'CL']:
        #         p[nm].full[:] = tp.pars[nm].full[:]
        #     for nm in ['X0', 'X1', 'col', 'tmax']:
        #         p[nm].full[0] = tp.pars[nm].full[sn_index]
        #     if 'gamma' in tp.pars._struct.slices:
        #         p['gamma'].full[:] = tp.pars['gamma'].full[:]
        #     else:
        #         p['gamma'].full[:] = 0.
        #     v_pars = m(p)
        #     v_pars_err = vm(p) if vm is not None else None

        # plots
        fig, axes = pl.subplots(nrows=nrows, ncols=1,
                                figsize=(8,12),
                                sharex=True)
        for i,b in enumerate(bands):
            idx = sel & (tds.lc_data.band == b)
            wl = tds.lc_data.wavelength[idx].mean()
            color = pl.cm.jet(int((wl-2000)/(9000.-2000.) * 256))

            if phase:
                xx = (tds.lc_data.mjd[idx] - tmax) / (1. + z)
                axes[i].axvline(0., ls=':')
            else:
                xx = tds.lc_data.mjd[idx]
                axes[i].axvline(tmax, ls=':')

            axes[i].errorbar(xx, tds.lc_data.flux[idx],
                             yerr=tds.lc_data.fluxerr[idx],
                             ls='', marker='.', color=color)

            # plot the model
            # iii = t.lc_data.band == b
            # if phase:
            #     xx = (t.lc_data.mjd[iii] - tmax) / (1. + z)
            # else:
            #     xx = t.lc_data.mjd[iii]
            # axes[i].plot(xx, norm * v_pars[iii], ls=':', color=color)

            # # plot the variance model
            # vm = norm * (v_pars[iii] - np.sqrt(v_pars_err[iii]))
            # vp = norm * (v_pars[iii] + np.sqrt(v_pars_err[iii]))
            # axes[i].fill_between(xx, vm, vp,
            #                      color=color,
            #                      alpha=0.1)
            for p in plotters:
                p.plot(b, ax=axes[i],
                       color=color,
                       phase=phase,
                       ylabel=b)
            if phase:
                axes[-1].set_xlabel('mjd [days]')
            else:
                axes[-1].set_xlabel('phase [restframe days]')
            pl.subplots_adjust(hspace=0.05)
            fig.suptitle(f'{sn} @ z={z:4.3}')

    def plot_spec(self, spec, numfit=None, pars=None, alpha=0.5):
        """
        """
        sel = tds.spec_data.spec == spec

        fig, axes = pl.subplots(nrows=1, ncols=1,
                                figsize=(8,8),
                                sharex=True)

        axes.errorbar(tds.spec_data.wavelength[sel], tds.spec_data.flux[sel],
                      yerr=tds.spec_data.fluxerr[sel],
                      ls='', marker='.', color='blue')

        to_plot = self._get_models_to_plot(numfit, pars)
        for tp in to_plot:
            vv = tp.v[len(tds.lc_data):][sel]
            axes.plot(tds.spec_data.wavelength[sel], vv, 'r+:')
            if tp.v_var is not None:
                vv_var = tp.v_var[len(tds.lc_data):][sel]
                vmin = vv - np.sqrt(vv_var)
                vmax = vv + np.sqrt(vv_var)
                axes.fill_between(tds.spec_data.wavelength[sel],
                                  vmin, vmax,
                                  color='r', alpha=alpha)

        axes.set_ylabel('flux')
        axes.set_xlabel('mjd')

        sn = np.unique(tds.spec_data.sn[sel])
        assert len(sn) == 1
        sn = sn[0]
        z = np.unique(tds.spec_data.z[sel])
        assert len(z) == 1
        z = z[0]
        axes.set_title(f'{sn} @ z={z:4.3}')
        pl.subplots_adjust(hspace=0.05)

    def cut_lc_outliers(self, pars, nsig=10):
        """
        """
        v = self.model(pars)
        if self.variance_model is not None and 'gamma' in pars._struct.slices:
            var_v = self.variance_model(pars)
        else:
            var_v = None

        vv = v[:len(self.tds.lc_data)]
        if var_v is not None:
            var_vv = var_v[:len(self.tds.lc_data)]
        else:
            var_vv = None

        bands = np.unique(self.tds.lc_data.band)
        nbands = len(bands)

        for i,band in enumerate(bands):
            sel = self.tds.lc_data.band == band
            var = self.tds.lc_data.fluxerr**2
            if var_vv is not None:
                var += var_vv
            w = 1. / var
            res = vv - self.tds.lc_data.flux
            wres = np.sqrt(w) * res

            cut = (np.abs(wres) > nsig)
            cc = cut[sel]
            logging.info(f'cutting {cc.sum()}/{len(cc)}={100*cc.sum()/len(cc):4.3}% outliers in {band}')
            self.tds.lc_data.valid[sel] = (~cut)[sel]

            jj = (~cut)[sel]
            print(jj.sum(), self.tds.lc_data.valid[sel].sum(), len(self.tds.lc_data.valid[sel]))


    def plot_lc_training_residuals(self, pars, v=None, var_v=None,
                                   phases=False,
                                   weighted_residuals=False,
                                   hexbin=False):
        """global fit residuals
        """
        if not v:
            v = self.model(pars)
        if not var_v and self.variance_model is not None and 'gamma' in pars._struct.slices:
            var_v = self.variance_model(pars)

        vv = v[:len(tds.lc_data)]
        if var_v is not None:
            var_vv = var_v[:len(tds.lc_data)]
        else:
            var_vv = None

        tmax = pars['tmax'].full[self.tds.lc_data.sn_index]
        z = self.tds.lc_data.z

        bands = np.unique(tds.lc_data.band)
        nbands = len(bands)
        fig, axes = pl.subplots(figsize=(6,12),
                                nrows=nbands, ncols=2,
                                sharex=0, sharey=1,
                                gridspec_kw={'width_ratios': [3,1]})
        for i, band in enumerate(bands):
            sel = tds.lc_data.band == band
            wl = tds.lc_data.wavelength[sel].mean()
            color = pl.cm.jet(int((wl-2000)/(9000.-2000.) * 256))
            if phases:
                x = (self.tds.lc_data.mjd - tmax) / (1. + z)
            else:
                x = np.arange(len(sel))

            var = tds.lc_data.fluxerr**2
            if var_vv is not None:
                var += var_vv
            w = 1. / var
            res = vv - tds.lc_data.flux
            wres = np.sqrt(w) * res
            y = wres if weighted_residuals else res
            if hexbin:
                axes[i,0].hexbin(x[sel], y[sel],
                                 gridsize=(100, 500),
                                 extent=(-30, 50, -100, 100),
                                 mincnt=1)
            else:
                axes[i,0].plot(x[sel], y[sel],
                               # yerr=tds.lc_data.fluxerr[sel],
                               ls='', marker='.', color=color)
            axes[i,1].hist(y[sel], bins=500,
                           color=color,
                           density=True,
                           # orientation='vertical')
                           )
            print(band, mad(y[sel]))

            # if var_vv is not None:
            #    ii = np.argsort(x[sel])
            # axes[i].fill_between(x[sel][ii], -np.sqrt(var_vv[sel][ii]), np.sqrt(var_vv[sel][ii]),
            #                      alpha=0.25, color=color)
            axes[i,0].set_ylabel(band)
        axes[-1,0].set_xlabel('phases [days]' if phases else 'index')
        pl.subplots_adjust(hspace=0.01, wspace=0.01)

        return v, var_v


    def plot_spec_training_residuals(self, pars, v=None, var_v=None):
        """global fit residuals
        """
        if not v:
            v = self.model(pars)
        if not var_v and self.variance_model is not None and 'gamma' in pars._struct.slices:
            var_v = self.variance_model(pars)

        vv = v[len(self.tds.lc_data):]
        if var_v is not None:
            var_vv = var_v[len(self.tds.lc_data):]
        else:
            var_vv = None

        sel = self.tds.spec_data.valid

        tmax = pars['tmax'].full[self.tds.spec_data.sn_index]
        z = self.tds.spec_data.z
        phases = (self.tds.spec_data.mjd - tmax) / (1. + z)

        fig, axes = pl.subplots(nrows=1, ncols=1)
        # color = pl.cm.jet(int(phases/(50+25) * 256))
        x = self.tds.spec_data.wavelength
        ii = np.argsort(x)
        axes.errorbar(x[sel], vv[sel] - tds.spec_data.flux[sel],
                      yerr=tds.spec_data.fluxerr[sel],
                      ls='', marker=',', color='gray')
        #        if var_vv is not None:
        #            axes[i].fill_between(x[sel][ii], -np.sqrt(var_vv[sel][ii]), np.sqrt(var_vv[sel][ii]),
        #                                 alpha=0.25, color='gray')
        axes.set_xlabel('wavelength [$\AA$]')
        pl.subplots_adjust(hspace=0.05)

        return v, var_v


    def plot_lightcurves(self, pars, v=None, var_v=None, phases=False):
        """global fit residuals
        """
        if not v:
            v = self.model(pars)
        if not var_v and self.variance_model is not None and 'gamma' in pars._struct.slices:
            var_v = self.variance_model(pars)

        vv = v[:len(tds.lc_data)]
        if var_v is not None:
            var_vv = var_v[:len(tds.lc_data)]
        else:
            var_vv = None

        tmax = pars['tmax'].full[self.tds.lc_data.sn_index]
        z = self.tds.lc_data.z

        bands = np.unique(tds.lc_data.band)
        nbands = len(bands)
        fig, axes = pl.subplots(nrows=nbands, ncols=1, sharex=phases)
        for i, band in enumerate(bands):
            sel = tds.lc_data.band == band
            wl = tds.lc_data.wavelength[sel].mean()
            color = pl.cm.jet(int((wl-2000)/(9000.-2000.) * 256))
            if phases:
                x = (self.tds.lc_data.mjd - tmax) / (1. + z)
            else:
                x = self.tds.lc_data.mjd
            ii = np.argsort(x[sel])

            axes[i].errorbar(x[sel][ii], tds.lc_data.flux[sel][ii],
                             yerr=tds.lc_data.fluxerr[sel][ii],
                             ls='', marker=',', color=color)
            axes[i].plot(x[sel][ii], vv[sel][ii],
                         ls='', marker='+', color=color)

            if var_vv is not None:
                axes[i].fill_between(x[sel][ii], vv[sel]-np.sqrt(var_vv[sel][ii]), vv[sel]+np.sqrt(var_vv[sel][ii]),
                                     alpha=0.5, color=color)
            axes[i].set_ylabel(band)
        axes[-1].set_xlabel('phases [days]' if phases else 'index')
        pl.subplots_adjust(hspace=0.05)

        return v, var_v




    def save(self, fn):
        with open(fn, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, fn):
        with open(fn, 'rb') as f:
            return pickle.load(f)

    def plot(self, res):
        """
        """
        t = TrainingChi2(self.tds, res.ll.pars, res.ll.model)
        d = t.get_sorted_list(sort_by='sn')

        # plot the 5 worst SNe
        for nm in d[:5].sn:
            plot_lc(nm, self.tds, res.ll.pars, norm=1, phase=1)

        for spec in [222, 333, 444, 555, 1226, 1500, 1700]:
            plot_spec(spec, tds, res.v)




def fit_local_pars_and_error_model(tds, model, plot=False):
    """
    """
    # fl, tds, model, ll, pars, mn, v = main(lc_only=lc_only)
    error_snake = SimpleErrorSnake(model)
    ll = LogLikelihood(model, variance_model=error_snake)
    ll.pars.fix()
    ll.pars.release('X0')
    ll.pars.release('X1')
    ll.pars.release('col')
    ll.pars.release('tmax')
    ll.pars.release('SpectrumRecalibration')
    ll.pars.release('gamma')
    ll.pars['gamma'].full[:] = 0.05

    # recalibrate the spectra
    v = model(ll.pars)
    r = recalib_spectra(tds, v)
    ll.pars['SpectrumRecalibration'].full[3::4] = np.log(r)
    print(ll.pars['SpectrumRecalibration'].full[:20])

    minz = Minimizer(ll)
    p = minz.minimize_lm(ll.pars.free)
    if plot:
        minz.plot()

    res = FitRes()
    res.ll = ll
    res.minz = minz

    return res


def fit_error_model(tds, model, res_init, plot=False):
    """
    """
    # fl, tds, model, ll, pars, mn, v = main(lc_only=lc_only)
    error_snake = SimpleErrorSnake(model)
    ll = LogLikelihood(model, variance_model=error_snake)
    ll.pars.fix()
    ll.pars.release('gamma')
    ll.pars['gamma'] = 0.05

    for block_name in res_init.ll.pars._struct.slices:
        ll.pars[block_name].full[:] = res_init.ll.pars[block_name].full[:]

    minz = Minimizer(ll)
    p = minz.minimize_lm(ll.pars.free)
    if plot:
        minz.plot()

    res = FitRes()
    res.ll = ll
    res.minz = minz

    return res


def main():
    train = train = Trainer(tds, model, variance_model)
    train.train()
    train.save('training.pkl')

    # plot 5 worst and 5 best light curves and spectra
    # train.plot()


    # plot training residuals
    train.plot_lc_training_residuals()
    train.plot_spec_training_residuals()


def fit_model(tds, model, ll_init, plot=False):
    """
    """
    cons = constraints.salt2like_linear_constraints(model, mu=1.E6)
    # TODO: ll_init.pars ?  Chicken and egg problem !
    reg = NaClSplineRegularization(model, ll_init.pars, to_regularize=['M0', 'M1'], mu=1.)
    ll = LogLikelihood(model, cons=[cons], reg=[reg])

    ll.pars.full[:] = ll_init.pars[:].full
    ll.pars.fix()
    ll.pars.release('M0')
    ll.pars.release('M1')
    ll.pars.release('CL')

    minz = Minimizer(ll)
    p = minz.minimize_lm(ll.pars.free)
    if plot:
        minz.plot()

    res = FitRes()
    res.ll = ll
    res.minz = minz
    res.cons = cons
    res.reg = reg

    return res


if __name__ == '__main__':

    tds, model, variance_model = None, None, None
    ll_init = None

    parser = ArgumentParser(description='NaCl training on Lemaitre')
    parser.add_argument('--reload',
                        action='store_true',
                        help='force reloading tds and model')
    parser.add_argument('--fit-local-pars',
                        action='store_true',
                        help='fit the supernova parameters (fixed model)')
    parser.add_argument('--fit-local-pars-and-error-model',
                        action='store_true',
                        help='fit the supernova parameters with an error model (fixed model)')
    parser.add_argument('--fit-error-model',
                        action='store_true',
                        help='fit an error model (fixed local pars and model)')
    parser.add_argument('--fit-model',
                        action='store_true',
                        help='fit the model (fixed local pars)')
    parser.add_argument('--fit-model-and-error-model',
                        action='store_true',
                        help='fit the model along with an error model')
    # parser.add_argument('--fit-model-and-error-model',
    #                     action='store_true',
    #                     help='fit the model (fixed local pars) along with an error model')
    # parser.add_argument('--train',
    #                     action='store_true',
    #                     help='fit all parameters')

    args = parser.parse_args()

    if tds is None or model is None and not args.force_reload:
        tds = load_tds()
        tds.compress()
        model = salt2.SALT2Like(tds,
                                # phase_range=model_phase_range,
                                wl_grid=tds.basis.grid,
                                spectrum_recal_degree=3)
        variance_model = LocalErrorSnake(model)

#    if args.fit_local_pars:
#        res_init = fit_local_pars(tds, model)
#    #    elif args.fit_local_pars_and_error_model:
#    #        res_init = fit_local_pars_and_error_model(tds, model)

#    if args.fit_error_model:
#        res = fit_error_model(tds, model, res_init)

#    if args.fit_model:
#        if ll_init is None:
#            res_init = fit_local_pars(tds, model)
#        res = fit_model(tds, model, ll_init=res_init.ll)
#    elif args.fit_model_and_error_model:
#        res = fit_model_and_error_model(tds, model, ll_init=res_init.ll)


    # if sys.argv[1] == '2':
    #     cons = constraints.salt2like_linear_constraints(model, mu=1.E6) # was 1.E6
    #     reg = NaClSplineRegularization(model, pars, to_regularize=['M0', 'M1'], mu=1.) # was 1.E-6
    #     ll2 = LogLikelihood(model, reg=[reg])
    #     ll2.pars.full[:] = ll.pars[:].full
    #     ll2.pars.fix()
    #     ll2.pars.release('M0')
    #     ll2.pars.release('M1')
    #     ll2.pars.release('CL')
    #     mn2 = Minimizer(ll2)
    #     p = mn2.minimize_lm(ll2.pars.free)
    #     mn2.plot()

    # if sys.argv[1] == '3':
    #     ll3 = LogLikelihood(model, reg=[reg], cons=[cons]) # TODO cons make sure it is a list
    #     ll3.pars.full[:] = ll2.pars[:].full
    #     ll3.pars.release()
    #     mn3 = Minimizer(ll3)
    #     p = mn3.minimize_lm(ll3.pars.free)
    #     mn3.plot()


    #    ll.pars.release('M1')

