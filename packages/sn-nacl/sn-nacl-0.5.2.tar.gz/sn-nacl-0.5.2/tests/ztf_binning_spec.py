# Projects the flux on a 1D BSpline of order 0
# The idea is to simplify the evaluation of the model in a first place

import logging
from multiprocessing import Pool

import scipy.sparse as sparse
from sksparse import cholmod
import numpy as np
import scipy
import scipy.sparse.linalg
from scipy.interpolate import interp1d
import pylab as pl
import pandas as pd

from bbf.bspline import BSpline, BSpline2D
# from nacl.models import import salt2
from nacl.dataset import TrainingDataset
from saunerie.plottools import binplot


class Spec:

    class FitResults:
        pass

    def __init__(self, tds, spec, basis=None, error_eval_bin_width=50.,
                 bin_width=40., beta=1.E-8):
        self.tds = tds
        self.spec = spec
        self.basis = basis
        self.error_eval_bin_width = error_eval_bin_width
        self.bin_width = bin_width
        self.beta = beta

        idx = tds.spec_data.spec == spec
        self.wl = tds.spec_data.wavelength[idx]
        self.flux = tds.spec_data.flux[idx]
        self.fluxerr = tds.spec_data.fluxerr[idx]
        self.cut = (self.fluxerr < 0) | np.isnan(self.fluxerr)
        if self.cut.sum() > 0:
            logging.warning(f'{self.cut.sum()} measurement detected with negative of nan uncertainties')
        sn = tds.spec_data.sn[idx]
        assert np.all(np.equal(sn, sn[0]))
        self.idx = idx

        for field in ['sn', 'name', 'mjd', 'valid', 'spec', 'exptime']:
            setattr(self, field, self._check_field(field))

        self.fitres = []

    def _check_field(self, name):
        s = np.unique(self.tds.spec_data.nt[self.idx][name])
        assert len(s) == 1
        return s[0]

    def fit(self, x, y, yerr, bin_width, order=1, beta=None):
        """
        """
        N = len(x)
        assert (len(y) == N) and (len(yerr) == N)
        if beta is None:
            beta = self.beta

        if self.basis is None:
            grid = np.arange(x.min(), x.max()+bin_width, bin_width)
            basis = BSpline(grid, order=order)
        else:
            basis = self.basis

        J = basis.eval(x)
        w = 1. / yerr
        W = sparse.dia_matrix((w**2, 0), shape=(N,N))
        H = J.T @ W @ J
        fact = cholmod.cholesky(H.tocsc(), beta=beta)

        r = Spec.FitResults()
        r.coeffs = fact(J.T @ W @ y)
        r.res = (y - J @ r.coeffs)
        r.wres = (y - J @ r.coeffs) * w
        r.chi2 = (r.wres**2).sum()
        r.ndof = (len(y) - len(r.coeffs))
        r.rchi2 = r.chi2 / r.ndof
        r.basis = basis
        #try:
        HH = H.todense() + np.diag(np.full(len(r.coeffs), 1.E-20))
        r.coeffs_cov = np.linalg.inv(HH)
        r.coeffs_err = np.sqrt(np.array(r.coeffs_cov.diagonal()).squeeze())

            # r.coeffs_err = np.sqrt(scipy.sparse.linalg.inv(H).diagonal())
        #except:
        #    r.coeffs_err = np.zeros_like(r.coeffs)

        return r

    def recompute_error_model(self, wl, res, nbins=10):
        """
        """
        #       nbins = int((wl.max() - wl.min()) / bin_width)
        x, y, yerr = binplot(wl, res, nbins=nbins, scale=False, noplot=True)
        self.error_model = interp1d(x, yerr, kind='cubic', fill_value=(yerr[0], yerr[-1]), bounds_error=False)
        self.x_err, self.y_err = x, yerr
        return self.error_model

    def process(self):
        """
        """
        # re-eval errors
        r = self.fit(self.wl, self.flux, self.fluxerr, order=4, bin_width=self.error_eval_bin_width)
        error_model = self.recompute_error_model(self.wl, r.res, nbins=10)
        self.fitres.append(r)

        # re-fit with recomputed errors
        fluxerr = error_model(self.wl)
        r = self.fit(self.wl, self.flux, fluxerr, order=4, bin_width=self.error_eval_bin_width)
        self.fitres.append(r)

        # bin spectrum
        r = self.fit(self.wl, self.flux, fluxerr, order=1, bin_width=self.bin_width)
        self.fitres.append(r)

        self.estimated_fluxerr = fluxerr

    def get_binned_spectrum(self):
        r = self.fitres[2]
        N = len(r.coeffs)
        d = np.zeros(N, self.tds.spec_data.nt.dtype)
        d['sn'] = self.sn
        d['name'] = self.name
        d['mjd'] = self.mjd
        d['valid'] = self.valid
        d['exptime'] = self.exptime
        d['wavelength'] = 0.5 * (r.basis._grid[1:] + r.basis._grid[:-1])
        d['flux'] = r.coeffs
        d['fluxerr'] = r.coeffs_err
        return d

    def plot(self):
        """
        """
        r = self.fitres[1]
        rr = self.fitres[2]

        fig, axes = pl.subplots(nrows=4, ncols=1, figsize=(8,8), sharex=True)

        # the original spectrum
        axes[0].errorbar(self.wl[~self.cut], self.flux[~self.cut], yerr=self.estimated_fluxerr[~self.cut],
                         ls='', marker='.', label='orig')

        grid_wl = 0.5 * (rr.basis._grid[1:] + rr.basis._grid[:-1])
        # axes[0].errorbar(grid_wl, rr.coeffs, yerr=rr.coeffs_err, marker='.', ls='', color='c')
        axes[0].plot(grid_wl, rr.coeffs, marker='.', ls='', color='c')
        #        axes[0].plot(grid_wl, coeffs, 'ro', label='binned', zorder=100)
        # axes[0].plot(wl, J @ coeffs, 'r-', label='binned', zorder=100)

        axes[1].errorbar(self.wl[~self.cut], r.res[~self.cut], yerr=self.estimated_fluxerr[~self.cut],
                         ls='', marker='.', color='b')

        axes[2].plot(self.x_err, self.y_err, 'bo')
        xx = np.linspace(self.wl.min(), self.wl.max(), 100)
        axes[2].plot(xx, self.error_model(xx), 'r-')

        # the binned spectrum
        axes[3].errorbar(grid_wl, rr.coeffs, yerr=rr.coeffs_err, marker='.', ls='', color='b')
        # axes[3].errorbar(self.wl, rr.res/self.error_model(self.wl), yerr=1., ls='', marker='.', color='b')


def rebin_spectra_2(tds):
    """
    """
    spec_data = tds.spec_data
    nb_spectra = len(tds.spec_data.spec_set)
    rebinned_spectra = []
    spectra_in_error = []

    def rebin_spectrum(spec):
        logging.info(f'processing {spec}')
        try:
            s = Spec(tds, spec, bin_width=40.)
            s.process()
            rebinned_spectra.append(s.get_binned_spectrum())
        except:
            logging.error(f'unable to process {spec}')
            spectra_in_error.append(s)

    pool = Pool()
    pool.map(rebin_spectrum, tds.spec_data.spec_set)

    all_spec = np.hstack(rebinned_spectra)
    return TrainingDataset(tds.sn_data, lc_data=tds.lc_data, spec_data=tds.spec_data)

def rebin_spectra(tds):
    """
    """
    spec_data = tds.spec_data
    nb_spectra = len(tds.spec_data.spec_set)
    c = 0
    rebinned_spectra = []
    spectra_in_error = []
    for spec in tds.spec_data.spec_set:
        logging.info(f'processing {spec} {c}/{nb_spectra}')
        try:
            s = Spec(tds, spec, bin_width=40.)
            s.process()
            rebinned_spectra.append(s.get_binned_spectrum())
        except:
            logging.error(f'unable to process {spec}')
            spectra_in_error.append(s)
            continue
        c += 1

    all_spec = np.rec.array(np.hstack(rebinned_spectra))
    return TrainingDataset(tds.sn_data.nt, lc_data=tds.lc_data.nt, spec_data=all_spec)
    # return rebinned_spectra


def project_on_nacl_basis(tds, model):
    """
    """
    spec_data = tds.spec_data
    basis = model.basis.bx

    for spec in tds.spec_data.spec_set:
        try:
            s = Spec(tds, spec, basis=basis, z=None)
            s.process()
            rebinned_spectra.append(s.get_binned_spectrum())
        except:
            logging.error(f'unable to process {spec}')
            spectra_in_error.append(s)
            continue




def bin_spectrum(tds, spec,
                 error_eval_bin_with=50.,
                 bin_with=40.,
                 plot=False, beta=1.E-8):
    """A smaller rewrite of Mahmoud's original code
    """
    #    for i in tds.spec_data.spec_set:
    idx = tds.spec_data.spec == spec
    wl = tds.spec_data.wavelength[idx]
    flx = tds.spec_data.flux[idx]
    flxerr = tds.spec_data.fluxerr[idx]
    cut = (flxerr < 0) | np.isnan(flxerr)
    if cut.sum() > 0:
        logging.warning(f'{cut.sum()} measurement detected with negative of nan uncertainties')

    sn = tds.spec_data.sn[idx]
    assert np.all(np.equal(sn, sn[0]))
    N = len(sn)

    grid = np.arange(wl.min(), wl.max()+step, step)
    basis = BSpline(grid, order=4)
    # coeffs = basis.linear_fit(wl, flx, beta=1.E-10)

    # re-estimate the error bars, using an order-4 spline
    grid = np.arange(wl.min(), wl.max()+error_eval_bin_with, error_eval_bin_with)
    basis = BSpline(grid, order=4)
    J = basis.eval(wl)
    w = 1. / flxerr
    W = sparse.dia_matrix((w**2, 0), shape=(N,N))
    H = J.T @ W @ J
    fact = cholmod.cholesky(H, beta=beta)
    coeffs = fact(J.T @ W @ flx)
    res = (flx - J @ coeffs)
    x, y, yerr = binplot(wl, res, nbins=10, scale=False, noplot=True)
    wres = (flx - J @ coeffs) * w
    chi2 = (wres**2).sum()
    rchi2 = chi2 / (len(flx) - len(coeffs))

    # refit and bin
    grid = np.arange(wl.min(), wl.max()+bin_with, bin_with)
    basis = BSpline(grid, order=0)
    J = basis.eval(wl)
    w = 1. / flxerr
    W = sparse.dia_matrix((w**2, 0), shape=(N,N))
    H = J.T @ W @ J
    fact = cholmod.cholesky(H, beta=beta)
    coeffs = fact(J.T @ W @ flx)
    res = (flx - J @ coeffs)
    wres = (flx - J @ coeffs) * w
    chi2 = (wres**2).sum()
    rchi2 = chi2 / (len(flx) - len(coeffs))




    if plot:
        fig, axes = pl.subplots(nrows=4, ncols=1, figsize=(8,8), sharex=True)
        axes[0].errorbar(wl[~cut], flx[~cut], yerr=self.estimated_fluxerr[~cut],
                         ls='', marker='.', label='orig')
        grid_wl = 0.5 * (grid[1:] + grid[:-1])
        #        axes[0].plot(grid_wl, coeffs, 'ro', label='binned', zorder=100)
        axes[0].plot(wl, J @ coeffs, 'r-', label='binned', zorder=100)

        axes[1].errorbar(wl[~cut], res[~cut], yerr=flxerr[~cut], ls='', marker='.', color='b')
        x,y,yerr = binplot(wl, res, nbins=10, scale=False, ax=axes[1])
        axes[2].plot(x, yerr, 'bo')
        # p = np.polyfit(x, yerr, deg=3)
        p = interp1d(x, yerr, kind='cubic', fill_value=(yerr[0], yerr[-1]), bounds_error=False)

        xx = np.linspace(x.min(), x.max(), 100)
        axes[2].plot(xx, p(xx), 'r-')

        axes[3].errorbar(wl, res/p(wl), yerr=1., ls='', marker='.', color='b')

    return grid, coeffs, basis, fact, H, res, wres, chi2, rchi2



def tds_spec_data_binning(tds, step = 40.0):
    sn_data = tds.sn_data
    if tds.lc_data is None:
        spec_data = tds.spectrophotometric_data
    else:
        spec_data = tds.spec_data
        lc_data = tds.lc_data
    spec_index = spec_data.spec_index
    spec_flux = spec_data.flux
    spec_fluxerr = spec_data.fluxerr
    spec_wl = spec_data.wavelength
    spec_mjd = spec_data.mjd
    spec_sn = spec_data.sn
    spec_spec = spec_data.spec
    spec_valid = spec_data.valid
    
    
    SN = np.array([])
    MJD = np.array([])
    WL = np.array([])
    FLX = np.array([])
    FLXERR = np.array([])
    VALID = np.array([])
    SPEC = np.array([])
    #EXPTIME = np.array([])
    
    spec_not_inv = np.array([])
    
    for i in range( int( np.max(spec_index) ) ):
    #for i in range(1):
        idx = (spec_index == i)
        
        flux = spec_flux[idx]
        fluxerr = spec_fluxerr[idx]
        wl = spec_wl[idx]
        mjd = spec_mjd[idx]
        sn = spec_sn[idx]
        valid = spec_valid[idx]
        spec = spec_spec[idx]
        
        grid = np.arange(np.min(wl), np.max(wl)+step, step)
        wl_theta = 0.5*(grid[1:] + grid[:-1])
        try:
            base = BSpline(grid, order=1)
            
            J = base.eval(wl)
            W=sparse.dia_matrix((1./fluxerr**2, 0), shape=(len(mjd), len(mjd)))
            H = J.T @ W @ J
            f = cholmod.cholesky(H, beta=1e-10)
            theta = f(J.T @ W @ flux)
            #print(len(theta))
            #flux_new = J @ theta

            H_inv = np.linalg.inv(H.todense())
            theta_err = np.sqrt( np.diag (H_inv) )
            
            SN = np.append(SN, np.array([ sn[0] for j in range( len(theta) ) ]))
            MJD = np.append(MJD, np.array([ mjd[0] for j in range( len(theta) ) ]))
            WL = np.append(WL, wl_theta)
            FLX = np.append(FLX, theta)
            FLXERR = np.append(FLXERR, theta_err)
            VALID = np.append(VALID, np.array([ valid[0] for j in range( len(theta) ) ]))
            SPEC = np.append(SPEC, np.array([ spec[0] for j in range( len(theta) ) ]))
        except: #manual binning when fit doesn't work due to issues
            spec_not_inv = np.append(spec_not_inv, i)
            ii = np.digitize(wl, grid)-1
            grid_augment = grid[ii]
            flx_ = np.array([])
            flxerr_ = np.array([])
            wl_ = np.array([])
            for j in range(len(grid)-1):
                wave = grid[j]
                idx2 = grid_augment == wave
                flx = flux[idx2]
                if len(flx)==0:
                    continue
                else:
                    flxerr = fluxerr[idx2]
                    flux_mean = np.sum(flx/flxerr**2)/np.sum(1/flxerr**2)
                    fluxerr_mean =  np.sqrt(1/np.sum(1/flxerr**2))
                    
                    flx_ = np.append(flx_, flux_mean)
                    flxerr_ = np.append(flxerr_, fluxerr_mean)
                    wl_ = np.append(wl_, 0.5*(grid[j] + grid[j+1]))
            SN = np.append(SN, np.array([ sn[0] for j in range( len(flx_) ) ]))
            MJD = np.append(MJD, np.array([ mjd[0] for j in range( len(flx_) ) ]))
            WL = np.append(WL, wl_)
            FLX = np.append(FLX, flx_)
            FLXERR = np.append(FLXERR, flxerr_)
            VALID = np.append(VALID, np.array([ valid[0] for j in range( len(flx_) ) ]))
            SPEC = np.append(SPEC, np.array([ spec[0] for j in range( len(flx_) ) ]))
                
        
    EXPTIME = np.array([ np.nan for j in range( len(SN) ) ])
    SPEC_DATA = pd.DataFrame({'sn':SN, 'mjd':MJD,  'wavelength':WL, 'flux':FLX, 'fluxerr':FLXERR, 'valid':VALID, 'spec':SPEC, 'exptime':EXPTIME})
    SN_DATA = pd.DataFrame({'sn':sn_data.sn, 'z':sn_data.z, 'tmax':sn_data.tmax, 'x1':sn_data.x1, 'x0':sn_data.x0, 'col':sn_data.col, 'valid':sn_data.valid})
    if tds.lc_data is None:
        tds_new = TrainingDataset(SN_DATA, spectrophot_data = SPEC_DATA)
    else:
        LC_DATA = pd.DataFrame({'sn':lc_data.sn, 'mjd':lc_data.mjd, 'flux':lc_data.flux, 'fluxerr':lc_data.fluxerr, 'band':lc_data.band, 'magsys':lc_data.magsys, 'zp':lc_data.zp, 'exptime':lc_data.exptime,'valid':lc_data.valid, 'lc':lc_data.lc, 'seeing':lc_data.seeing, 'mag_sky':lc_data.mag_sky})
        tds_new = TrainingDataset(SN_DATA, lc_data = LC_DATA, spec_data = SPEC_DATA)
    return tds_new
