#!/usr/bin/env python3

import numpy as np
import pylab as pl

from nacl.models.toy1d import lightcurves as lc1d
from nacl.models.toy2d import lightcurves as lc2d
from nacl.loglikelihood import LogLikelihood
from nacl.minimize import Minimizer

from nacl.models.helpers import check_grad, check_deriv_old
from nacl.lib.fitparameters import FitParameters
from scipy.optimize import curve_fit

from sksparse import cholmod


def constant(x, c):
    return c

def test_new_noise(n=10,nsn=200, npts=20, nbands=3,
                       release=['x0', 'stretch', 'color', 'tmax', 'eta'],
                       gen_error_pedestal=0., gen_error_snake=0.1,
                       gamma_init=0.):
    gen = lc1d.ToyModelGenerator(nbands=nbands, nsn=nsn, npts=npts, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
        
    dp = gen.generate()
    idx = dp.sn_index == 0
    
    pl.figure(figsize=(10,7))
    
    for i in range(n):
        
        pl.errorbar(dp.x[idx], dp.y[idx], yerr = dp.yerr[idx], ls='', marker='.', elinewidth = 2) 
        
        gen.change_noise(dp)
    pl.scatter(dp.x[idx], dp.y_true[idx], color = 'r', marker='x', zorder=n+1, label='y_true')
    pl.xlabel('x')
    pl.ylabel('y')
    pl.legend()
    pl.title('1st LC simulated ' + str(n) + ' times with different noise')
    
    
def bias_1d(n=50,nsn=100, npts=20, nbands=3,
                           release=['x0', 'stretch', 'color', 'tmax', 'eta'],
                           gen_error_pedestal=0., gen_error_snake=0.1,
                           gamma_init=0.05):
    
    x0 = []
    stretch = []
    color = []
    
    gen = lc1d.ToyModelGenerator(nbands=nbands, nsn=nsn, npts=npts, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
        
    dp = gen.generate()
    
    for i in range(n):        
        model = lc1d.LightCurveModel1DWithCalibScatter(dp)
        reg = lc1d.Regularization(block_name='theta')
        cons = lc1d.cons(model, mu=1.E6, s=True)
        snake = lc1d.SimpleErrorSnake(model)
        V_calib = np.diag(np.full(nbands, 0.005**2))
        calib_prior = lc1d.CalibPrior(V_calib)
        ll = LogLikelihood(model,
                           reg=[reg], cons=[cons],
                           priors=[calib_prior],
                           data=dp)
        # fit initialization
        for block_name in ['x0', 'stretch', 'color', 'tmax']:
            ll.pars[block_name].full[:] = dp.sample[block_name]
            ll.pars[block_name].fix()

        for block_name in release:
            ll.pars[block_name].release()

        # first fit with model only
        minz = Minimizer(ll)
        r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6, dchi2=10., max_iter=10)

        # second fit, with model and error modelfull )
        ll = LogLikelihood(model, variance_model=snake,
                           reg=[reg], cons=[cons],
                           priors=[calib_prior],
                           data=dp)
        for block_name in ['x0', 'tmax', 'stretch', 'color', 'theta']:
            ll.pars[block_name].full[:] = r['pars'][block_name].full[:]
        ll.pars['gamma'].full[:] = gamma_init
        minz = Minimizer(ll)
        r = minz.minimize_lm(p_init=ll.pars.free, lamb=1.E-6)

        minz.gen = gen
        
        x0.append( minz.log_likelihood.pars['x0'].full )
        stretch.append( minz.log_likelihood.pars['stretch'].full )
        color.append( minz.log_likelihood.pars['color'].full )
        
        gen.change_noise(dp)
    # PLOTS and VARIANCES
    x0 = np.vstack(x0)
    stretch = np.vstack(stretch)
    color = np.vstack(color)
    
    mean_x0 = np.mean(x0, axis=0)
    mean_stretch = np.mean(stretch, axis=0)
    mean_color = np.mean(color, axis=0)
    
    var_x0 = np.var(x0, axis=0)/n
    var_stretch = np.var(stretch, axis=0)/n
    var_color = np.var(color, axis=0)/n
    
    x = np.arange(len(mean_x0))
    
    #empirical covariance
    V_x0_emp = (x0 - mean_x0).T @ (x0 - mean_x0) / (n-1)
    V_stretch_emp = (stretch - mean_stretch).T @ (stretch - mean_stretch) / (n-1)
    V_color_emp = (color - mean_color).T @ (color - mean_color) / (n-1)
    
    #fisher covariance
    free_pars = ['x0', 'stretch', 'color']
    V, err_of_interest, corr = minz.get_cov_matrix(free_pars, corr=True, plot=False)
    idx_x0 = minz.log_likelihood.pars.indexof('x0')
    idx_stretch = minz.log_likelihood.pars.indexof('stretch')
    idx_color = minz.log_likelihood.pars.indexof('color')
    
    V_x0_fisher = V.toarray()[idx_x0][:,idx_x0]
    V_stretch_fisher = V.toarray()[idx_stretch][:,idx_stretch]
    V_color_fisher = V.toarray()[idx_color][:,idx_color]
    
    #fit the bias
    popt_x0, pcov_x0 = curve_fit(constant, x,  dp.sample['x0'] - mean_x0)
    popt_stretch, pcov_stretch = curve_fit(constant, x,  dp.sample['stretch'] - mean_stretch)
    popt_color, pcov_color = curve_fit(constant, x,  dp.sample['color'] - mean_color)
    
    
    #plot true vs fit differences and pulls
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].errorbar(x, dp.sample['x0'] - mean_x0, np.sqrt(var_x0), marker = '.', color ='k', ls='')
    axes[0].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[0].plot(x, np.linspace(popt_x0[0], popt_x0[0], len(x)), 'g--', label='bias fit')
    axes[0].fill_between(x, np.linspace(popt_x0[0]-np.sqrt(pcov_x0[0][0]), popt_x0[0]-np.sqrt(pcov_x0[0][0]), 
                         len(x)), np.linspace(popt_x0[0]+np.sqrt(pcov_x0[0][0]), popt_x0[0]+np.sqrt(pcov_x0[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[0].set_title('x0 true - x0 fit')
    axes[0].set_ylabel(r'$x0_{true}$ - $x0_{fit}$')
    axes[0].legend()
    
    axes[1].errorbar(x, dp.sample['stretch'] - mean_stretch, np.sqrt(var_stretch), marker = '.', color ='k', ls='')
    axes[1].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[1].plot(x, np.linspace(popt_stretch[0], popt_stretch[0], len(x)), 'g--', label='bias fit')
    axes[1].fill_between(x, np.linspace(popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), 
                         len(x)), np.linspace(popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[1].set_title('stretch true - stretch fit')
    axes[1].set_ylabel(r'$stretch_{true}$ - $stretch_{fit}$')
    axes[1].legend()
    
    axes[2].errorbar(x, dp.sample['color'] - mean_color, np.sqrt(var_color), marker = '.', color ='k', ls='')
    axes[2].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[2].plot(x, np.linspace(popt_color[0], popt_color[0], len(x)), 'g--', label='bias fit')
    axes[2].fill_between(x, np.linspace(popt_color[0]-np.sqrt(pcov_color[0][0]), popt_color[0]-np.sqrt(pcov_color[0][0]), 
                         len(x)), np.linspace(popt_color[0]+np.sqrt(pcov_color[0][0]), popt_color[0]+np.sqrt(pcov_color[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[2].set_title('color true - color fit')
    axes[2].set_ylabel(r'$color_{true}$ vs $color_{fit}$')
    axes[2].legend()
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x, np.sqrt(var_x0) - np.sqrt(np.diag(V_x0_fisher)), 'r.')
    axes[0].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[0].set_title('err_x0 empirical - err_x0 fisher')
    axes[0].set_ylabel(r'err_$x0_{empirical}$ - err_$x0_{fisher}$')
    
    axes[1].plot(x, np.sqrt(var_stretch) - np.sqrt(np.diag(V_stretch_fisher)), 'g.')
    axes[1].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[1].set_title('err_stretch empirical - err_stretch fisher')
    axes[1].set_ylabel(r'err_$stretch_{empirical}$ - err_$stretch_{fisher}$')
    
    axes[2].plot(x, np.sqrt(var_color) - np.sqrt(np.diag(V_color_fisher)), 'b.')
    axes[2].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[2].set_title('err_color empirical - err_color fisher')
    axes[2].set_ylabel(r'err_$color_{empirical}$ - err_$color_{fisher}$')
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x, np.abs(dp.sample['x0'] - mean_x0)/np.sqrt(var_x0), 'k.')
    axes[0].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[0].set_title('x0 pull')
    axes[0].set_ylabel(r'|$x0_{true}$ - $x0_{fit}$|/err_x0')
    
    axes[1].plot(x, np.abs(dp.sample['stretch'] - mean_stretch)/np.sqrt(var_stretch), 'k.')
    axes[1].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[1].set_title('stretch pull')
    axes[1].set_ylabel(r'|$stretch_{true}$ - $stretch_{fit}$|/err_stretch')
    
    axes[2].plot(x, np.abs(dp.sample['color'] - mean_color)/np.sqrt(var_color), 'k.')
    axes[2].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[2].set_title('color pull')
    axes[2].set_ylabel(r'|$color_{true}$ - $color_{fit}$|/err_color')
    
    
    #remove outliers
    idx_x0_1 = dp.sample['x0'] - mean_x0 - np.sqrt(var_x0) < np.linspace(popt_x0[0], popt_x0[0], len(x)) + np.linspace(np.sqrt(pcov_x0[0][0]), np.sqrt(pcov_x0[0][0]), len(x))
    idx_x0_2 = dp.sample['x0'][idx_x0_1] - mean_x0[idx_x0_1] + np.sqrt(var_x0)[idx_x0_1] > np.linspace(popt_x0[0], popt_x0[0], len(x))[idx_x0_1] - np.linspace(np.sqrt(pcov_x0[0][0]), np.sqrt(pcov_x0[0][0]), len(x))[idx_x0_1]
    idx_x0_3 = np.abs(dp.sample['x0'][idx_x0_1][idx_x0_2] - mean_x0[idx_x0_1][idx_x0_2])<1
    
    idx_stretch_1 = dp.sample['stretch'] - mean_stretch - np.sqrt(var_stretch) < np.linspace(popt_stretch[0], popt_stretch[0], len(x)) + np.linspace(np.sqrt(pcov_stretch[0][0]), np.sqrt(pcov_stretch[0][0]), len(x))
    idx_stretch_2 = dp.sample['stretch'][idx_stretch_1] - mean_stretch[idx_stretch_1] + np.sqrt(var_stretch)[idx_stretch_1] > np.linspace(popt_stretch[0], popt_stretch[0], len(x))[idx_stretch_1] - np.linspace(np.sqrt(pcov_stretch[0][0]), np.sqrt(pcov_stretch[0][0]), len(x))[idx_stretch_1]
    idx_stretch_3 = np.abs(dp.sample['stretch'][idx_stretch_1][idx_stretch_2] - mean_stretch[idx_stretch_1][idx_stretch_2])<0.05

    idx_color_1 = dp.sample['color'] - mean_color - np.sqrt(var_color) < np.linspace(popt_color[0], popt_color[0], len(x)) + np.linspace(np.sqrt(pcov_color[0][0]), np.sqrt(pcov_color[0][0]), len(x))
    idx_color_2 = dp.sample['color'][idx_color_1] - mean_color[idx_color_1] + np.sqrt(var_color)[idx_color_1] > np.linspace(popt_color[0], popt_color[0], len(x))[idx_color_1] - np.linspace(np.sqrt(pcov_color[0][0]), np.sqrt(pcov_color[0][0]), len(x))[idx_color_1]
    idx_color_3 = np.abs(dp.sample['color'][idx_color_1][idx_color_2] - mean_color[idx_color_1][idx_color_2])<1
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].errorbar(x[idx_x0_1][idx_x0_2][idx_x0_3], dp.sample['x0'][idx_x0_1][idx_x0_2][idx_x0_3] - mean_x0[idx_x0_1][idx_x0_2][idx_x0_3], np.sqrt(var_x0)[idx_x0_1][idx_x0_2][idx_x0_3], marker = '.', color ='k', ls='')
    axes[0].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[0].plot(x, np.linspace(popt_x0[0], popt_x0[0], len(x)), 'g--', label='bias fit')
    axes[0].fill_between(x, np.linspace(popt_x0[0]-np.sqrt(pcov_x0[0][0]), popt_x0[0]-np.sqrt(pcov_x0[0][0]), 
                         len(x)), np.linspace(popt_x0[0]+np.sqrt(pcov_x0[0][0]), popt_x0[0]+np.sqrt(pcov_x0[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[0].set_title('x0 true - x0 fit no outliers')
    axes[0].set_ylabel(r'$x0_{true}$ - $x0_{fit}$')
    axes[0].legend()
    
    axes[1].errorbar(x[idx_stretch_1][idx_stretch_2][idx_stretch_3], dp.sample['stretch'][idx_stretch_1][idx_stretch_2][idx_stretch_3] - mean_stretch[idx_stretch_1][idx_stretch_2][idx_stretch_3], np.sqrt(var_stretch)[idx_stretch_1][idx_stretch_2][idx_stretch_3], marker = '.', color ='k', ls='')
    axes[1].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[1].plot(x, np.linspace(popt_stretch[0], popt_stretch[0], len(x)), 'g--', label='bias fit')
    axes[1].fill_between(x, np.linspace(popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), 
                         len(x)), np.linspace(popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[1].set_title('stretch true - stretch fit no outliers')
    axes[1].set_ylabel(r'$stretch_{true}$ - $stretch_{fit}$')
    axes[1].legend()
    
    axes[2].errorbar(x[idx_color_1][idx_color_2][idx_color_3], dp.sample['color'][idx_color_1][idx_color_2][idx_color_3] - mean_color[idx_color_1][idx_color_2][idx_color_3], np.sqrt(var_color)[idx_color_1][idx_color_2][idx_color_3], marker = '.', color ='k', ls='')
    axes[2].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[2].plot(x, np.linspace(popt_color[0], popt_color[0], len(x)), 'g--', label='bias fit')
    axes[2].fill_between(x, np.linspace(popt_color[0]-np.sqrt(pcov_color[0][0]), popt_color[0]-np.sqrt(pcov_color[0][0]), 
                        len(x)), np.linspace(popt_color[0]+np.sqrt(pcov_color[0][0]), popt_color[0]+np.sqrt(pcov_color[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[2].set_title('color true - color fit no outliers')
    axes[2].set_ylabel(r'$color_{true}$ - $color_{fit}$')
    axes[2].legend()
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x[idx_x0_1][idx_x0_2][idx_x0_3], np.sqrt(var_x0[idx_x0_1][idx_x0_2][idx_x0_3]) - np.sqrt(np.diag(V_x0_fisher))[idx_x0_1][idx_x0_2][idx_x0_3], 'r.')
    axes[0].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[0].set_title('err_x0 empirical - err_x0 fisher no outliers')
    axes[0].set_ylabel(r'err_$x0_{empirical}$ - err_$x0_{fisher}$')
    
    axes[1].plot(x[idx_stretch_1][idx_stretch_2][idx_stretch_3], np.sqrt(var_stretch[idx_stretch_1][idx_stretch_2][idx_stretch_3]) - np.sqrt(np.diag(V_stretch_fisher)[idx_stretch_1][idx_stretch_2][idx_stretch_3]), 'g.')
    axes[1].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[1].set_title('err_stretch empirical - err_stretch fisher no outliers')
    axes[1].set_ylabel(r'err_$stretch_{empirical}$ - err_$stretch_{fisher}$')
    
    axes[2].plot(x[idx_color_1][idx_color_2][idx_color_3], np.sqrt(var_color[idx_color_1][idx_color_2][idx_color_3]) - np.sqrt(np.diag(V_color_fisher)[idx_color_1][idx_color_2][idx_color_3]), 'b.')
    axes[2].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[2].set_title('err_color empirical - err_color fisher no outliers')
    axes[2].set_ylabel(r'err_$color_{empirical}$ - err_$color_{fisher}$')
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x[idx_x0_1][idx_x0_2][idx_x0_3], np.abs(dp.sample['x0'][idx_x0_1][idx_x0_2][idx_x0_3] - mean_x0[idx_x0_1][idx_x0_2][idx_x0_3])/np.sqrt(var_x0[idx_x0_1][idx_x0_2][idx_x0_3]), 'k.')
    axes[0].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[0].set_title('x0 pull outliers')
    axes[0].set_ylabel(r'|$x0_{true}$ - $x0_{fit}$|/err_x0')
    
    axes[1].plot(x[idx_stretch_1][idx_stretch_2][idx_stretch_3], np.abs(dp.sample['stretch'][idx_stretch_1][idx_stretch_2][idx_stretch_3] - mean_stretch[idx_stretch_1][idx_stretch_2][idx_stretch_3])/np.sqrt(var_stretch[idx_stretch_1][idx_stretch_2][idx_stretch_3]), 'k.')
    axes[1].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[1].set_title('stretch pull no outliers')
    axes[1].set_ylabel(r'|$stretch_{true}$ - $stretch_{fit}$|/err_stretch')
    
    axes[2].plot(x[idx_color_1][idx_color_2][idx_color_3], np.abs(dp.sample['color'][idx_color_1][idx_color_2][idx_color_3] - mean_color[idx_color_1][idx_color_2][idx_color_3])/np.sqrt(var_color[idx_color_1][idx_color_2][idx_color_3]), 'k.')
    axes[2].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[2].set_title('color pull no outliers')
    axes[2].set_ylabel(r'|$color_{true}$ - $color_{fit}$|/err_color')
    #empirical correlation matrix
    v_x0 = np.diag(V_x0_emp)
    i = np.arange(len(v_x0))
    ii = np.vstack([i for k in range( len(v_x0) )])
    v1_x0 = v_x0[ii]
    v2_x0 = v1_x0.T
    vii_jj_x0 = v1_x0 * v2_x0
    vii_jj_x0 = np.sqrt(vii_jj_x0)
    corr_x0_emp = V_x0_emp/vii_jj_x0   
    
    v_stretch = np.diag(V_stretch_emp)
    i = np.arange(len(v_stretch))
    ii = np.vstack([i for k in range( len(v_stretch) )])
    v1_stretch = v_stretch[ii]
    v2_stretch = v1_stretch.T
    vii_jj_stretch = v1_stretch * v2_stretch
    vii_jj_stretch = np.sqrt(vii_jj_stretch)
    corr_stretch_emp = V_stretch_emp/vii_jj_stretch   
    
    v_color = np.diag(V_color_emp)
    i = np.arange(len(v_color))
    ii = np.vstack([i for k in range( len(v_color) )])
    v1_color = v_color[ii]
    v2_color = v1_color.T
    vii_jj_color = v1_color * v2_color
    vii_jj_color = np.sqrt(vii_jj_color)
    corr_color_emp = V_color_emp/vii_jj_color
    
    #fisher correlation matrix
    v_x0 = np.diag(V_x0_fisher)
    i = np.arange(len(v_x0))
    ii = np.vstack([i for k in range( len(v_x0) )])
    v1_x0 = v_x0[ii]
    v2_x0 = v1_x0.T
    vii_jj_x0 = v1_x0 * v2_x0
    vii_jj_x0 = np.sqrt(vii_jj_x0)
    corr_x0_fisher = V_x0_fisher/vii_jj_x0   
    
    v_stretch = np.diag(V_stretch_fisher)
    i = np.arange(len(v_stretch))
    ii = np.vstack([i for k in range( len(v_stretch) )])
    v1_stretch = v_stretch[ii]
    v2_stretch = v1_stretch.T
    vii_jj_stretch = v1_stretch * v2_stretch
    vii_jj_stretch = np.sqrt(vii_jj_stretch)
    corr_stretch_fisher = V_stretch_fisher/vii_jj_stretch   
    
    v_color = np.diag(V_color_fisher)
    i = np.arange(len(v_color))
    ii = np.vstack([i for k in range( len(v_color) )])
    v1_color = v_color[ii]
    v2_color = v1_color.T
    vii_jj_color = v1_color * v2_color
    vii_jj_color = np.sqrt(vii_jj_color)
    corr_color_fisher = V_color_fisher/vii_jj_color
    
    #without outliers
    
    #plot covariance matrix
    fig, axes = pl.subplots(figsize=(10,10), nrows=3, ncols=2)
    
    A = axes[0,0].imshow(V_x0_emp)
    pl.colorbar(A)
    axes[0,0].set_title('Covariance matrix x0 empirical')
    
    A = axes[0,1].imshow(V_x0_fisher)
    pl.colorbar(A)
    axes[0,1].set_title('Covariance matrix x0 fisher')
    
    B = axes[1,0].imshow(V_stretch_emp)
    pl.colorbar(B)
    axes[1,0].set_title('Covariance matrix stretch empirical')
    
    B = axes[1,1].imshow(V_stretch_fisher)
    pl.colorbar(B)
    axes[1,1].set_title('Covariance matrix stretch fisher')
    
    C = axes[2,0].imshow(V_color_emp)
    pl.colorbar(C)
    axes[2,0].set_title('Covariance matrix color empirical')
    
    C = axes[2,1].imshow(V_color_fisher)
    pl.colorbar(C)
    axes[2,1].set_title('Covariance matrix color fisher')
    
    #plot correlation matrix
    fig, axes = pl.subplots(figsize=(10,10), nrows=3, ncols=2)
    
    A = axes[0,0].imshow(corr_x0_emp)
    pl.colorbar(A)
    axes[0,0].set_title('Correlation matrix x0 empirical')
    
    A = axes[0,1].imshow(corr_x0_fisher)
    pl.colorbar(A)
    axes[0,1].set_title('Correlation matrix x0 fisher')
    
    B = axes[1,0].imshow(corr_stretch_emp)
    pl.colorbar(B)
    axes[1,0].set_title('Correlation matrix stretch empirical')
    
    B = axes[1,1].imshow(corr_stretch_fisher)
    pl.colorbar(B)
    axes[1,1].set_title('Correlation matrix stretch fisher')
    
    C = axes[2,0].imshow(corr_color_emp)
    pl.colorbar(C)
    axes[2,0].set_title('Correlation matrix color empirical')
    
    C = axes[2,1].imshow(corr_color_fisher)
    pl.colorbar(C)
    axes[2,1].set_title('Correlation matrix color fisher')
    
    
def bias_2d(n=100, nsn=50, nbands=3, npts1=20, npts2=15, release=['x0', 'tmax', 'stretch', 'eta', 'color'], 
                                 gen_error_pedestal=None, gen_error_snake=0.05, gamma_init=0.05):
    
    x0 = []
    stretch = []
    color = []
    
    gen = lc2d.ToyModelGenerator(nbands=nbands, nsn=nsn, npts1=npts1, npts2=npts2, yerr=0.01,
                                        error_pedestal=gen_error_pedestal,
                                        error_snake=gen_error_snake)
    dp = gen.generate()
    for i in range(n):
        model = lc2d.LightCurve2DCalibScatter(dp)
        reg = lc2d.Regularization(block_name='theta')
      
        cons = lc2d.cons(model, mu=1.E6, color='True')
        snake = lc2d.SimpleErrorSnake(model)
        V_calib = np.diag(np.full(nbands, 0.005**2))
        calib_prior = lc2d.CalibPrior(V_calib)
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
        minz.gen = gen
        
        x0.append( minz.log_likelihood.pars['x0'].full )
        stretch.append( minz.log_likelihood.pars['stretch'].full )
        color.append( minz.log_likelihood.pars['color'].full )
        
        gen.change_noise(dp)
    
    # PLOTS and VARIANCES
    x0 = np.vstack(x0)
    stretch = np.vstack(stretch)
    color = np.vstack(color)
    
    mean_x0 = np.mean(x0, axis=0)
    mean_stretch = np.mean(stretch, axis=0)
    mean_color = np.mean(color, axis=0)
    
    var_x0 = np.var(x0, axis=0)/n
    var_stretch = np.var(stretch, axis=0)/n
    var_color = np.var(color, axis=0)/n
    
    x = np.arange(len(mean_x0))
    
    #empirical covariance
    V_x0_emp = (x0 - mean_x0).T @ (x0 - mean_x0) / (n-1)
    V_stretch_emp = (stretch - mean_stretch).T @ (stretch - mean_stretch) / (n-1)
    V_color_emp = (color - mean_color).T @ (color - mean_color) / (n-1)
    
    #fisher covariance
    free_pars = ['x0', 'stretch', 'color']
    V, err_of_interest, corr = minz.get_cov_matrix(free_pars, corr=True, plot=False)
    idx_x0 = minz.log_likelihood.pars.indexof('x0')
    idx_stretch = minz.log_likelihood.pars.indexof('stretch')
    idx_color = minz.log_likelihood.pars.indexof('color')
    
    V_x0_fisher = V.toarray()[idx_x0][:,idx_x0]
    V_stretch_fisher = V.toarray()[idx_stretch][:,idx_stretch]
    V_color_fisher = V.toarray()[idx_color][:,idx_color]
    
    #fit the bias
    popt_x0, pcov_x0 = curve_fit(constant, x,  dp.sample['x0'] - mean_x0, sigma = np.sqrt(var_x0))
    popt_stretch, pcov_stretch = curve_fit(constant, x,  dp.sample['stretch'] - mean_stretch, sigma = np.sqrt(var_stretch))
    popt_color, pcov_color = curve_fit(constant, x,  dp.sample['color'] - mean_color, sigma = np.sqrt(var_color))
    
    #plot true vs fit differences and pulls
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].errorbar(x, dp.sample['x0'] - mean_x0, np.sqrt(var_x0), marker = '.', color ='k', ls='')
    axes[0].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[0].plot(x, np.linspace(popt_x0[0], popt_x0[0], len(x)), 'g--', label='bias fit')
    axes[0].fill_between(x, np.linspace(popt_x0[0]-np.sqrt(pcov_x0[0][0]), popt_x0[0]-np.sqrt(pcov_x0[0][0]), 
                         len(x)), np.linspace(popt_x0[0]+np.sqrt(pcov_x0[0][0]), popt_x0[0]+np.sqrt(pcov_x0[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[0].set_title('x0 true - x0 fit')
    axes[0].set_ylabel(r'$x0_{true}$ - $x0_{fit}$')
    axes[0].legend()
    
    axes[1].errorbar(x, dp.sample['stretch'] - mean_stretch, np.sqrt(var_stretch), marker = '.', color ='k', ls='')
    axes[1].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[1].plot(x, np.linspace(popt_stretch[0], popt_stretch[0], len(x)), 'g--', label='bias fit')
    axes[1].fill_between(x, np.linspace(popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), popt_stretch[0]-np.sqrt(pcov_stretch[0][0]), 
                         len(x)), np.linspace(popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), popt_stretch[0]+np.sqrt(pcov_stretch[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[1].set_title('stretch true - stretch fit')
    axes[1].set_ylabel(r'$stretch_{true}$ - $stretch_{fit}$')
    axes[1].legend()
    
    axes[2].errorbar(x, dp.sample['color'] - mean_color, np.sqrt(var_color), marker = '.', color ='k', ls='')
    axes[2].plot(x, np.linspace(0,0,len(x)), 'r')
    axes[2].plot(x, np.linspace(popt_color[0], popt_color[0], len(x)), 'g--', label='bias fit')
    axes[2].fill_between(x, np.linspace(popt_color[0]-np.sqrt(pcov_color[0][0]), popt_color[0]-np.sqrt(pcov_color[0][0]), 
                         len(x)), np.linspace(popt_color[0]+np.sqrt(pcov_color[0][0]), popt_color[0]+np.sqrt(pcov_color[0][0]), len(x)), color = 'g',alpha = 0.5)
    axes[2].set_title('color true - color fit')
    axes[2].set_ylabel(r'$color_{true}$ vs $color_{fit}$')
    axes[2].legend()
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x, np.sqrt(var_x0) - np.sqrt(np.diag(V_x0_fisher)), 'r.')
    axes[0].set_title('err_x0 empirical - err_x0 fisher')
    axes[0].set_ylabel(r'err_$x0_{empirical}$ - err_$x0_{fisher}$')
    
    axes[1].plot(x, np.sqrt(var_stretch) - np.sqrt(np.diag(V_stretch_fisher)), 'g.')
    axes[1].set_title('err_stretch empirical - err_stretch fisher')
    axes[1].set_ylabel(r'err_$stretch_{empirical}$ - err_$stretch_{fisher}$')
    
    axes[2].plot(x, np.sqrt(var_color) - np.sqrt(np.diag(V_color_fisher)), 'b.')
    axes[2].set_title('err_color empirical - err_color fisher')
    axes[2].set_ylabel(r'err_$color_{empirical}$ - err_$color_{fisher}$')
    
    fig, axes = pl.subplots(figsize=(7,10), nrows=3, ncols=1)
    
    axes[0].plot(x, np.abs(dp.sample['x0'] - mean_x0)/np.sqrt(var_x0), 'k.')
    axes[0].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[0].set_title('x0 pull')
    axes[0].set_ylabel(r'|$x0_{true}$ - $x0_{fit}$|/err_x0')
    
    axes[1].plot(x, np.abs(dp.sample['stretch'] - mean_stretch)/np.sqrt(var_stretch), 'k.')
    axes[1].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[1].set_title('stretch pull')
    axes[1].set_ylabel(r'|$stretch_{true}$ - $stretch_{fit}$|/err_stretch')
    
    axes[2].plot(x, np.abs(dp.sample['color'] - mean_color)/np.sqrt(var_color), 'k.')
    axes[2].plot(x, np.linspace(1, 1, len(x)), 'g--')
    axes[2].set_title('color pull')
    axes[2].set_ylabel(r'|$color_{true}$ - $color_{fit}$|/err_color')
    
    
    #empirical correlation matrix
    v_x0 = np.diag(V_x0_emp)
    i = np.arange(len(v_x0))
    ii = np.vstack([i for k in range( len(v_x0) )])
    v1_x0 = v_x0[ii]
    v2_x0 = v1_x0.T
    vii_jj_x0 = v1_x0 * v2_x0
    vii_jj_x0 = np.sqrt(vii_jj_x0)
    corr_x0_emp = V_x0_emp/vii_jj_x0   
    
    v_stretch = np.diag(V_stretch_emp)
    i = np.arange(len(v_stretch))
    ii = np.vstack([i for k in range( len(v_stretch) )])
    v1_stretch = v_stretch[ii]
    v2_stretch = v1_stretch.T
    vii_jj_stretch = v1_stretch * v2_stretch
    vii_jj_stretch = np.sqrt(vii_jj_stretch)
    corr_stretch_emp = V_stretch_emp/vii_jj_stretch   
    
    v_color = np.diag(V_color_emp)
    i = np.arange(len(v_color))
    ii = np.vstack([i for k in range( len(v_color) )])
    v1_color = v_color[ii]
    v2_color = v1_color.T
    vii_jj_color = v1_color * v2_color
    vii_jj_color = np.sqrt(vii_jj_color)
    corr_color_emp = V_color_emp/vii_jj_color   
    
    #fisher correlation matrix
    v_x0 = np.diag(V_x0_fisher)
    i = np.arange(len(v_x0))
    ii = np.vstack([i for k in range( len(v_x0) )])
    v1_x0 = v_x0[ii]
    v2_x0 = v1_x0.T
    vii_jj_x0 = v1_x0 * v2_x0
    vii_jj_x0 = np.sqrt(vii_jj_x0)
    corr_x0_fisher = V_x0_fisher/vii_jj_x0   
    
    v_stretch = np.diag(V_stretch_fisher)
    i = np.arange(len(v_stretch))
    ii = np.vstack([i for k in range( len(v_stretch) )])
    v1_stretch = v_stretch[ii]
    v2_stretch = v1_stretch.T
    vii_jj_stretch = v1_stretch * v2_stretch
    vii_jj_stretch = np.sqrt(vii_jj_stretch)
    corr_stretch_fisher = V_stretch_fisher/vii_jj_stretch   
    
    v_color = np.diag(V_color_fisher)
    i = np.arange(len(v_color))
    ii = np.vstack([i for k in range( len(v_color) )])
    v1_color = v_color[ii]
    v2_color = v1_color.T
    vii_jj_color = v1_color * v2_color
    vii_jj_color = np.sqrt(vii_jj_color)
    corr_color_fisher = V_color_fisher/vii_jj_color
    
    #plot covariance matrix
    fig, axes = pl.subplots(figsize=(10,10), nrows=3, ncols=2)
    
    A = axes[0,0].imshow(V_x0_emp)
    pl.colorbar(A)
    axes[0,0].set_title('Covariance matrix x0 empirical')
    
    A = axes[0,1].imshow(V_x0_fisher)
    pl.colorbar(A)
    axes[0,1].set_title('Covariance matrix x0 fisher')
    
    B = axes[1,0].imshow(V_stretch_emp)
    pl.colorbar(B)
    axes[1,0].set_title('Covariance matrix stretch empirical')
    
    B = axes[1,1].imshow(V_stretch_fisher)
    pl.colorbar(B)
    axes[1,1].set_title('Covariance matrix stretch fisher')
    
    C = axes[2,0].imshow(V_color_emp)
    pl.colorbar(C)
    axes[2,0].set_title('Covariance matrix color empirical')
    
    C = axes[2,1].imshow(V_color_fisher)
    pl.colorbar(C)
    axes[2,1].set_title('Covariance matrix color fisher')
    
    #plot correlation matrix
    fig, axes = pl.subplots(figsize=(10,10), nrows=3, ncols=2)
    
    A = axes[0,0].imshow(corr_x0_emp)
    pl.colorbar(A)
    axes[0,0].set_title('Correlation matrix x0 empirical')
    
    A = axes[0,1].imshow(corr_x0_fisher)
    pl.colorbar(A)
    axes[0,1].set_title('Correlation matrix x0 fisher')
    
    B = axes[1,0].imshow(corr_stretch_emp)
    pl.colorbar(B)
    axes[1,0].set_title('Correlation matrix stretch empirical')
    
    B = axes[1,1].imshow(corr_stretch_fisher)
    pl.colorbar(B)
    axes[1,1].set_title('Correlation matrix stretch fisher')
    
    C = axes[2,0].imshow(corr_color_emp)
    pl.colorbar(C)
    axes[2,0].set_title('Correlation matrix color empirical')
    
    C = axes[2,1].imshow(corr_color_fisher)
    pl.colorbar(C)
    axes[2,1].set_title('Correlation matrix color fisher')
