#!/usr/bin/env python3

import numpy as np
import pylab as pl

from nacl.models.toy2d import lightcurves
from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer
from matplotlib.gridspec import GridSpec
from nacl.lib.fitparameters import FitParameters

from nacl.models.helpers import check_grad, check_deriv_old

from scipy import sparse




def main(release=['x0', 'tmax'], error_pedestal=0.05):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nsn = 10, nbands=1, npts1=20, npts2=30, yerr=0.01, error_pedestal=error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.Model(dp)
    reg = lightcurves.Regularization(block_name='theta')
    cons = lightcurves.cons(model, mu=1.E6)
    snake = lightcurves.SimplePedestalModel(model)
    ll = LogLikelihood(model, variance_model=snake, reg=[reg], cons=[cons], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch']:
        ll.pars[block_name] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # fit
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)

    minz.plot()
    v = model(ll.pars, jac=0)

    pl.figure()
    pl.plot(dp.y, v, 'r.')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y, zerr=dp.yerr, color='k', ls='', marker='.')
    ax.plot(dp.x1, dp.x2, v, 'r+')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y-v, zerr=dp.yerr, color='k', ls='', marker='.')

    return minz
    
def main_snake(release=['x0', 'tmax','stretch'], error_pedestal=0.05):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nsn = 100, nbands=1, npts1=20, npts2=30, yerr=0.01, error_pedestal=error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.Model(dp)
    reg = lightcurves.Regularization(block_name='theta')
    cons = lightcurves.cons(model, mu=1.E6)
    snake = lightcurves.SimpleErrorSnake_new(model)
    ll = LogLikelihood(model, variance_model=snake, reg=[reg], cons=[cons], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch']:
        ll.pars[block_name] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # fit
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)

    minz.plot()
    v = model(ll.pars, jac=0)

    pl.figure()
    pl.plot(dp.y, v, 'r.')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y, zerr=dp.yerr, color='k', ls='', marker='.')
    ax.plot(dp.x1, dp.x2, v, 'r+')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y-v, zerr=dp.yerr, color='k', ls='', marker='.')
    
    minz.gen = gen

    return minz
    
def main_error_pedestal(release=['x0', 'tmax'], gen_error_pedestal=0.05, gen_error_snake=None, gamma_init=0.):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nsn = 50, nbands=1, npts1=20, npts2=30, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
    print(gen.error_snake, gen.error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.Model(dp)
    reg = lightcurves.Regularization(block_name='theta')
    cons = lightcurves.cons(model, mu=1.E6)
    snake = lightcurves.SimplePedestalModel(model)
    # snake = lightcurves.SimpleErrorSnake(model)
    ll = LogLikelihood(model, variance_model=snake, reg=[reg], cons=[cons], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch']:
        ll.pars[block_name].full[:] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # fit
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)

    minz.plot()
    v = model(ll.pars, jac=0)

    pl.figure()
    pl.plot(dp.y, v, 'r.')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y, zerr=dp.yerr, color='k', ls='', marker='.')
    ax.plot(dp.x1, dp.x2, v, 'r+')

    ax = pl.figure().add_subplot(projection='3d')
    ax.errorbar(dp.x1, dp.x2, dp.y-v, zerr=dp.yerr, color='k', ls='', marker='.')
    
    minz.gen = gen

    return minz



def main_error_snake(nsn=50, npts1=20, npts2=15, release=['x0', 'tmax'], gen_error_pedestal=None, gen_error_snake=0.05, gamma_init=0.05):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nbands=1, nsn=nsn, npts1=npts1, npts2=npts2, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
    print(gen.error_snake, gen.error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.Model(dp)
    reg = lightcurves.Regularization(block_name='theta')
    cons = lightcurves.cons(model, mu=1.E6)
    snake = lightcurves.SimpleErrorSnake(model)
    ll = LogLikelihood(model, reg=[reg], cons=[cons], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch']:
        ll.pars[block_name].full[:] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # first fit with model only
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6, dchi2=10., max_iter=10)
    minz.plot()

    # second fit, with model and error model
    ll = LogLikelihood(model, variance_model=snake, reg=[reg], cons=[cons], data=dp)
    for block_name in ['x0', 'tmax', 'stretch', 'theta']:
        ll.pars[block_name].full[:] = r['pars'][block_name].full[:]
    ll.pars['gamma'].full[:] = gamma_init
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)
    minz.plot()

    minz.gen = gen

    return minz

def main_error_snake_calib_prior(nsn=50, nbands=3, npts1=20, npts2=15, release=['x0', 'tmax', 'stretch', 'eta'], gen_error_pedestal=None, gen_error_snake=0.05, gamma_init=0.05):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nbands=nbands, nsn=nsn, npts1=npts1, npts2=npts2, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
    print(gen.error_snake, gen.error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.ModelwithCalibScatter(dp)
    reg = lightcurves.Regularization(block_name='theta')
  
    cons = lightcurves.cons(model, mu=1.E6)
    snake = lightcurves.SimpleErrorSnake(model)
    V_calib = np.diag(np.full(nbands, 0.005**2))
    calib_prior = lightcurves.CalibPrior(V_calib)
    ll = LogLikelihood(model, reg=[reg], cons=[cons], priors=[calib_prior], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch']:
        ll.pars[block_name].full[:] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # first fit with model only
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6, dchi2=10., max_iter=10)
    minz.plot()

    # second fit, with model and error model
    ll = LogLikelihood(model, variance_model=snake, reg=[reg], cons=[cons], data=dp)
    for block_name in ['x0', 'tmax', 'stretch', 'theta']:
        ll.pars[block_name].full[:] = r['pars'][block_name].full[:]
    ll.pars['gamma'].full[:] = gamma_init
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)
    minz.plot()

    minz.gen = gen

    return minz

def main_lc_error_snake_calib_prior(nsn=50, nbands=3, npts1=20, npts2=15, release=['x0', 'tmax', 'stretch', 'eta', 'color'], 
                                 gen_error_pedestal=None, gen_error_snake=0.05, gamma_init=0.05):
    # generate dataset
    gen = lightcurves.ToyModelGenerator(nbands=nbands, nsn=nsn, npts1=npts1, npts2=npts2, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
    print(gen.error_snake, gen.error_pedestal)
    dp = gen.generate()

    # build a model and a log-likelihood
    model = lightcurves.LightCurve2DCalibScatter(dp)
    reg = lightcurves.Regularization(block_name='theta')
  
    cons = lightcurves.cons(model, mu=1.E6, color='True')
    snake = lightcurves.SimpleErrorSnake(model)
    V_calib = np.diag(np.full(nbands, 0.005**2))
    calib_prior = lightcurves.CalibPrior(V_calib)
    ll = LogLikelihood(model, reg=[reg], cons=[cons], priors=[calib_prior], data=dp)

    # fit initialization
    for block_name in ['x0', 'tmax', 'stretch', 'color']:
        ll.pars[block_name].full[:] = dp.sample[block_name]
        ll.pars[block_name].fix()

    for block_name in release:
        ll.pars[block_name].release()

    # first fit with model only
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6, dchi2=10., max_iter=10)
    minz.plot()

    # second fit, with model and error model
    ll = LogLikelihood(model, variance_model=snake,
                       reg=[reg], cons=[cons],
                       priors=[calib_prior],
                       data=dp)
    for block_name in ['x0', 'tmax', 'stretch', 'color','theta']:
        ll.pars[block_name].full[:] = r['pars'][block_name].full[:]
    ll.pars['gamma'].full[:] = gamma_init
    minz = Minimizer(ll)
    r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)
    minz.plot()

    minz.gen = gen

    return minz


def plot_fit_summary(minz, nsn_to_draw=3, band_to_draw=1):
    """
    """
    ll = minz.log_likelihood
    model = ll.model
    snake = ll.variance_model
    pars = ll.pars
    dp = ll.data
    gen = minz.gen

    x0 = pars['x0'].full
    tmax = pars['tmax'].full
    stretch = pars['stretch'].full
    nsn = len(x0)

    v = model(pars, jac=0)
    var = snake(pars, jac=0)
    
    fig = pl.figure()
    gs = GridSpec(4, 3)
    idx = dp.sn < nsn_to_draw
    ax00 = fig.add_subplot(gs[0], projection='3d')
    ax00.errorbar(dp.x1[idx], dp.x2[idx], dp.y[idx], zerr=np.sqrt(dp.yerr**2 + var)[idx], color='gray', ls='', marker=',', alpha=0.25)
    _dp = gen.gen_fine_grid()
    _model = lightcurves.Model(_dp)
    if snake is not None:
        _snake = snake.__class__(_model)
        _pars = FitParameters(_model.get_struct() + _snake.get_struct())
        _model.init_pars(_pars)
        _snake.init_pars(_pars)
        _pars['gamma'].full[:] = pars['gamma'].full[:]
    else:
        _snake = None
        _pars = _model.init_pars()
    _pars['theta'].full[:] = pars['theta'].full[:]
    for isn in range(3):
        for blk in ['x0', 'tmax', 'stretch']:
            _pars[blk].full[0] = pars[blk].full[isn]
        if 'color' in _pars._struct:
            _pars['color'].full[0] = pars['color'].full[isn]
        vv = _model(_pars, jac=False)
        
        _v = _model(_pars, jac=False)
        _ev = np.sqrt(_snake(_pars, jac=False))
        
        color = pl.cm.jet(int(isn / nsn_to_draw * 256))
        #idx = dp.sn_index == isn
        idx = (dp.sn_index == isn) & (dp.band == band_to_draw)
        ax00.errorbar(dp.x1[idx], dp.x2[idx], dp.y[idx], zerr=dp.yerr[idx], color=color, ls='', marker='.', elinewidth=2)
        idx = _dp.band == band_to_draw
        ax00.plot(_dp.x1[idx], _dp.x2[idx], _v[idx], ls='-', color=color, alpha=0.25, zorder=10)
        ax00.plot(_dp.x1, _dp.x2, vv, ls='-', color=color, alpha=0.25, zorder=10)
        #ax00.fill_between(_dp.x1[idx], _dp.x2[idx], (_v-_ev)[idx], (_v+_ev)[idx], color=color, alpha=0.7)

    ax00.set_xlabel('x1')
    ax00.set_ylabel('x2')
    ax00.set_zlabel('data & model')
    
    idx = (dp.sn_index == isn) & (dp.band == band_to_draw)
    phase1 = (dp.x1[idx]-tmax[dp.sn_index][idx]) * (1. + stretch[dp.sn_index][idx])
    phase2 = (dp.x2[idx]-tmax[dp.sn_index][idx]) * (1. + stretch[dp.sn_index][idx])
    yy = dp.y[idx] / x0[dp.sn_index][idx]
    eyy = dp.yerr[idx] / np.abs(x0[dp.sn_index][idx])
    ax01 = fig.add_subplot(gs[1], projection = '3d')
    ax01.errorbar(phase1, phase2, yy, zerr=eyy, color='k', ls='', marker='.', label='fit')
    xx = np.linspace(phase1.min(), phase1.max(), 30)
    yy = np.linspace(phase2.min(), phase2.max(), 30)
    XX, YY = np.meshgrid(xx, yy)
    J = model.basis.eval(XX.ravel(), YY.ravel())
    ax01.plot(XX.ravel(), YY.ravel(), J @ pars['theta'].full, color='red', linewidth=2, zorder=100, label='model')
    ax01.set_xlabel('phase')
    ax01.set_ylabel('data & model')
    pl.legend(loc='best')

    ax02 = fig.add_subplot(gs[2])
    ax02.plot(dp.var**2, var, color='brown', marker='.', ls='')
    xx = np.linspace(0., var.max(), 100)
    ax02.plot(xx, xx, 'b--')
    ax02.set_xlabel('$V_{true}$')
    ax02.set_ylabel('$V_{reco}$')
    
    ax10 = fig.add_subplot(gs[3])
    ax10.errorbar(dp.x1[idx], dp.y[idx]-v[idx], yerr=np.sqrt(dp.yerr[idx]**2 + var[idx]), color='brown', marker=',', ls='')
    ax10.errorbar(dp.x1[idx], dp.y[idx]-v[idx], yerr=dp.yerr[idx], color='k', marker='.', ls='', elinewidth=2)
    ax10.set_xlabel('x1')
    ax10.set_ylabel('residuals[idx]')
    
    ax11 = fig.add_subplot(gs[4])
    ax11.errorbar(phase1, dp.y[idx]-v[idx], yerr=np.sqrt(dp.yerr[idx]**2 + var[idx]), color='brown', marker=',', ls='')
    ax11.errorbar(phase1, dp.y[idx]-v[idx], yerr=dp.yerr[idx]**2, color='k', marker='.', ls='')
    ax11.set_xlabel('phase1')
    ax11.set_ylabel('residuals[idx]')
    
    ax12 = fig.add_subplot(gs[5])
    ax12.plot(phase1, dp.var[idx]-var[idx], color='brown', marker='.', ls='')
    ax12.set_xlabel('phase')
    ax12.set_ylabel('$V-V_{true}$')
    
    
    ax20 = fig.add_subplot(gs[6])
    ax21 = fig.add_subplot(gs[7])
    ax22 = fig.add_subplot(gs[8])
    ax20.plot(dp.sample.x0, pars['x0'].full, 'b.')
    ax20.set_xlabel('$X_0$ [true]')
    ax20.set_ylabel('$X_0$ [reco]')
    ax21.plot(dp.sample.tmax, pars['tmax'].full, 'b.')
    ax21.set_xlabel('$x_{peak}$ [true]')
    ax21.set_ylabel('$x_{peak}$ [reco]')
    ax22.plot(dp.sample.stretch, pars['stretch'].full, 'b.')
    ax22.set_xlabel('$s$ [true]')
    ax22.set_ylabel('$s$ [reco]')
    
    free_pars = ['x0', 'tmax', 'stretch', 'gamma']
    if 'color' in pars._struct:
        ax30 = fig.add_subplot(gs[9])
        free_pars.append('color')
        ax30.plot(dp.sample.color, pars['color'].full, 'b.')
        ax30.set_xlabel('$color$ [true]')
        ax30.set_ylabel('$color$ [reco]')
    
    ax31 = fig.add_subplot(gs[10])
    ax31.plot(phase1, (dp.y[idx]-v[idx]) / np.sqrt(dp.yerr[idx]**2 + var[idx]), color='k', marker='.', ls='')
    ax31.set_xlabel('phase1')
    ax31.set_ylabel('pulls[idx]')
    
    V, err_of_interest, corr = minz.get_cov_matrix(free_pars, corr=True, plot=True)
