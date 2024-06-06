"""
"""
import re
import os
import scipy
import numpy as np
from scipy.stats import norm
import matplotlib.cm as cm
import math 

import pylab as pl
import matplotlib as mpl
import matplotlib.gridspec as gridspec

from ..lib.dataproxy import DataProxy
from math import *

from nacl.models.salt import SpectrumRecalibrationPolynomials
# from nacl.models.models import ModelResiduals
from nacl.minimizers import ModelPulls
from ..lib import robuststat 
from .plottools import binplot

import seaborn as sns
#from . import models
#from . import variancemodels

def plot_parameter_init(fit, pars, save_dir = None, add_name =''):
    """
    """
    fit.model.pars.release()
    p = fit.model.pars.free.copy()
    p0 = fit.model.pars0.copy()
    
    if pars == 'CL':
        figcl = pl.figure()
        #fit.model.pars.release()
        idxcl = fit.model.pars['CL'].indexof()
        restframe_wl = np.linspace(2000, 9000, 500)
        P_cl0, J_cl = fit.model.color_law(restframe_wl, p0[idxcl], jac=False)
        P_cl, J_cl = fit.model.color_law(restframe_wl, p[idxcl], jac=False)
        gs = pl.matplotlib.gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        ax1 = figcl.add_subplot(gs[0])
        ax2 = figcl.add_subplot(gs[1])
        ax1.plot(fit.model.color_law.reduce(restframe_wl), P_cl, 'b-', label = 'rec')
        ax1.plot(fit.model.color_law.reduce(restframe_wl), P_cl0, 'r-', label = 'gen')
        ax2.plot(fit.model.color_law.reduce(restframe_wl), P_cl/P_cl0, 'k.')
        ax2.grid(1)
        ax1.grid(1)
        ax1.legend()
        
    elif (pars == 'M0') ^ (pars == 'M1'):
        figsur = pl.figure()
        surface= [pars]
        if (pars == 'M0'):
            vmin, vmax = -0.1, 0.5
        else :
            vmin, vmax = -0.01, 0.05 
        x, y, z = plot_2Dsurfacemodel(fit.model, surface, plot = False)
        #p = fit.model.pars.free.copy()
        fit.model.pars.free = p0
        x, y, z0 = plot_2Dsurfacemodel(fit.model, surface, plot = False)
        ax = figsur.add_subplot(311)
        m = ax.imshow(z, vmin=vmin, vmax=vmax)
        ax.set_title(f'{surface[0]} fit')
        pl.colorbar(m)
        ax1 =  figsur.add_subplot(312)
        m1 = ax1.imshow(z0, vmin=vmin, vmax=vmax)
        ax1.set_title(f'{surface[0]} gen')
        pl.colorbar(m1)
        ax2 =  figsur.add_subplot(313)
        m2 = ax2.imshow(z/z0, vmin=0.8, vmax=1.2)
        ax2.set_title('ratio')
        pl.colorbar(m2)
        
        # fig = pl.figure()
        # ax = fig.add_subplot(111)
        # hist(ax, (z/z0).ravel(), bins = 30)
        
    else :
        figpar = pl.figure()
        gs = pl.matplotlib.gridspec.GridSpec(3, 2, figure=figpar)
        ax = figpar.add_subplot(gs[:-1, 0])
        ax1 = figpar.add_subplot(gs[-1:, 0])

        #fit.model.pars.release()
        idx = fit.model.pars[pars].indexof()
        ppars = p[idx]
        p0pars = p0[idx]

        x = np.arange(len(idx))
        ax.plot(x, ppars, 'r.', label = 'fit')
        ax.grid()
        ax.legend()
        ax.set_title(pars)
        ax.plot(x, p0pars, 'k.', label = 'gen')
        ax1.plot(x, p0pars-ppars, 'k.')
        binplot(x, p0pars-ppars, data = False, marker = '.', markersize=20)
        ax1.grid()
        ax1.set_ylabel('dif')
        ax2 = figpar.add_subplot(gs[:, 1])
        hist(ax2, ppars, color = 'r', bins = 10)
        hist(ax2, p0pars, color ='k', bins = 10)

    fit.model.pars.free = p
    if save_dir is not None:
        name_plot = save_dir + os.sep + add_name + f"{pars}_generation.png"
        pl.savefig(name_plot)                

def plot_HD(z, mu, mu_err, mu_th, save_dir=None):
    """
    """
    idxz = z.argsort()
    fig = pl.figure()
    gs = pl.matplotlib.gridspec.GridSpec(nrows=2, ncols=6, height_ratios=[2,1])
    ax = fig.add_subplot(gs[0, :-1])
    ax.plot(z[idxz], mu_th[idxz], 'r-')
    ax.errorbar(z[idxz], mu[idxz], yerr =  mu_err[idxz],
                ls = '', marker= '.', color = 'b')
    ax.grid(1)
    ax.set_ylabel(r'$\mu$')
    ax.set_xlabel(r'z')
    ax1 = fig.add_subplot(gs[1, :-1], sharex=ax)
    ax1.errorbar(z[idxz], mu[idxz] - mu_th[idxz],
                 yerr =  mu_err[idxz], ls = '',
                 color = 'b', marker= '.')
    ax1.grid(1)
    ax1.set_xlabel('z')
    ax1.set_ylabel(r'$\mu-\mu_{th}$')
    binplot(z[idxz], mu[idxz] - mu_th[idxz], weights=1/mu_err[idxz]**2 ,
            data = False, color = 'r')

    ax2 = fig.add_subplot(gs[1, -1])
    hist(ax2, mu[idxz] - mu_th[idxz], histtype='step', orientation='horizontal')
    ax2.grid(1)

    if save_dir is not None:
        pl.savefig(save_dir + os.sep + f'distance_modulus.png')

    
def plot_lc(model, idx_lc, variance_model = False, save_dir = None,
            add_name = f'', plot=True, sigma = None):
    """
    LC reconstruction od the Nth first SN.
    N : int, Nth first SN LC recosntruction;
    unique : bool, just the Nth SN,
    variance_model : Variance model, if error snake wanted.
    """
    model.pars.release()

    idx = model.training_dataset.lc_data['lc_id'] == idx_lc 
    lc =  model.training_dataset.lc_data[idx]
    snInfo = model.training_dataset.sne
    
    
    z = lc['ZHelio'][0]
    band = lc['Filter'][0]
    tr = model.filter_db.transmission_db[band.decode('UTF-8')]
    tqz, _ = model.filter_db.insert(tr, z=z)
    tqz[(np.abs(tqz)/tqz.max() < 1e-10)] = 0.
    
    sne = lc['sn_id'][0]
    x0 = model.pars['X0'].full[sne]
    tmax = model.pars['tmax'].full[sne]
    x1 = model.pars['X1'].full[sne]
    c = model.pars['c'].full[sne]
    eta = model.pars['eta_calib'].full[lc['band_id'][0]]
    kappa = model.pars['kappa_color'].full[idx_lc]
    print(kappa)

    if sigma is not None:
        x0_err = sigma[model.pars['X0'].indexof()][sne]
        tmax_err = sigma[model.pars['tmax'].indexof()][sne]
        x1_err = sigma[model.pars['X1'].indexof()][sne]
        c_err = sigma[model.pars['c'].indexof()][sne]
        
    
    ph_basis_size = len(model.basis.by)
    M0 = model.pars['M0'].full.reshape(ph_basis_size, -1)
    M1 = model.pars['M1'].full.reshape(ph_basis_size, -1)
    cl_pars = model.pars['CL'].full
    P_cl, _ = model.color_law(model.Leff.data, cl_pars, jac=False)
    P_cl = scipy.sparse.csr_matrix((P_cl, (model.Leff.row, model.Leff.col)), shape=model.Leff.shape)
    
    phase = (lc['Date']- tmax)/(1+z)
    phase100 = np.linspace(phase[0], phase[-1], 100)

    P = model.basis.by.eval(phase100 + model.delta_phase).tocsr()
    cl  = np.power(10., 0.4 * c * P_cl.data)
    CC  = scipy.sparse.csr_matrix((cl, (model.Leff.row, model.Leff.col)), shape=model.Leff.shape)
    G = model.G.multiply(CC)
    I0 = P.dot(M0.dot(G.dot(tqz)))
    I1 = P.dot(M1.dot(G.dot(tqz)))

    flux100 = model.norm * (1+z) * x0 * (I0 + x1*I1) * (1+eta) * (1+kappa)

    if plot : 
        fig = pl.figure(figsize=(10,8))
        gs = fig.add_gridspec(nrows=4,ncols=1)
        ax = fig.add_subplot(gs[:3,0])

        label0 = 'data' + f" X0 :  {snInfo['x0'][sne] : .5f} " + f" X1 :  {snInfo['x1'][sne] : .3f} " + f"\n tmax :  {snInfo['tmax'][sne] : .3f} " + f" c :  {snInfo['c'][sne] : .3f} "  #+ f" eta :  {0. : .3f}"
        if sigma is not None:
            label = 'data' + f" X0 :  {x0 : .5f} $\pm$ {x0_err : .5f}  " + f" X1 :  {x1 : .3f}  $\pm$ {x1_err : .3f}" + f"\n tmax :  {tmax : .3f} $\pm$ {tmax_err : .3f}" + f" c :  {c : .3f} $\pm$ {c_err : .3f}"  #+ f" eta :  {0. : .3f}"
        else :
            label = 'data' + f" X0 :  {x0 : .5f}   " + f" X1 :  {x1 : .3f}" + f"\n tmax :  {tmax : .3f}" + f" c :  {c : .3f}" 
            
        try : 
            ax.errorbar(phase, lc['Flux'], yerr = lc['FluxErr'], label = label0,
                        color = 'k', marker = '.', ls = '', alpha = 0.75)                    
        except :
            ax.errorbar(phase, lc['Flux'], yerr = lc['FluxErr'], color = 'k', marker = '.', ls = '')

        ax.plot(phase100, flux100, color = 'r', ls = '-', label = label) #'model'  + f" X0 :  {x0 : .5f}  " + f" X1 :  {x1 : .3f}  " +  f"\n tmax :  {tmax : .3f}  " + f" c :  {c : .3f}  ") #+ f" eta :  {eta : .3f}  "+ f" kappa :  {kappa : .3f}  ")

    if variance_model :
        spline_lc100 = variance_model.basis.eval(lc['Wavelength'][0]*np.ones_like(phase100), phase100)
        spline_lc = variance_model.basis.eval(lc['Wavelength'][0]*np.ones_like(phase), phase)

        ss_lc100 = (spline_lc100 * variance_model.pars['gamma'].full)
        ss_lc = (spline_lc * variance_model.pars['gamma'].full)

        siglc100 = ss_lc100 * flux100
        siglc = ss_lc * lc['Flux']

        if plot: 
            ax.plot(phase100, flux100 + siglc100, color = 'b', ls ='--')
            ax.plot(phase100, flux100 - siglc100, color = 'b', ls ='--')
            ax.fill_between(phase100, flux100 - siglc100, flux100 + siglc100, color = 'b', alpha=0.25)
    if plot: 
        idxmax = np.where(lc['Flux'] == lc['Flux'].max())[0]
        idxmin = np.where(lc['Flux'] == lc['Flux'].min())[0]
        ax.set_ylim((lc['Flux']- 3 * lc['FluxErr'])[idxmin], (lc['Flux']+ 3 * lc['FluxErr'])[idxmax])
        ax.set_ylabel('Flux')
        ax.grid(True)
        pl.title(f"{band}  z={snInfo['z'][sne] : .4f}")
    
        res = fig.add_subplot(gs[3,0], sharex = ax)

    val = model(model.pars.free, plotting = True, ilc_plot = idx_lc)
    RES = (lc['Flux'] - val)#[lc['i']])
    if plot :
        res.errorbar(phase, RES, lc['FluxErr'], 
                     color = 'r', marker = '+',ls = '',
                     label = 'Measurement Error')
                
        if variance_model :
            mod_res_minus = 0. - siglc#/val0[idx]
            mod_res_plus = 0. + siglc#/val0[idx]
            res.plot(phase100,  -siglc100 , color = 'b', ls ='--')
            res.plot(phase100,  siglc100, color = 'b', ls ='--')
            res.fill_between(phase100, -siglc100, siglc100, color = 'b', alpha=0.25)
            res.errorbar(phase, RES, siglc, color = 'k', marker = '+',ls = '', label= 'Error Model')
            
        res.grid(True)
        res.legend()
        res.set_ylabel('y-mod')
        res.set_xlabel('Date since maximum')
        res.set_ylim(-10 * max(np.abs(RES.max()),np.abs(RES.min())),
                     10 * max(np.abs(RES.max()),np.abs(RES.min())))
        # if variance_model :
            
        #     ax.errorbar(phase,
        #                 lc['Flux'],
        #                 yerr = siglc, elinewidth = 2.5,
        #                 color = 'darkorange', marker = '',
        #                 ls = '', label = r'$\sigma_X$')
        
        #     ax.errorbar(phase, lc['Flux'],
        #                 yerr = np.sqrt(siglc**2+lc['FluxErr']**2),
        #                 elinewidth = 1.,
        #                 color = 'green', marker = '',
        #                 ls = '', label = r'$\sigma$')
        
        ax.legend(ncol=1)
    
        if save_dir is not None:
            name_plot = save_dir + os.sep + add_name + f"{sne}_{band.decode('UTF-8')}_lc.png"
            pl.savefig(name_plot)
        
        return fig
    if variance_model==False :
        siglc, siglc100 = np.zeros_like(phase), np.zeros_like(phase100)
    return phase, val, siglc, phase100, flux100, siglc100 

def plot_hist_variancemodelparameter(fit):
    """
    """
    g_gen = fit.g0
    g_init = fit.variance_model.pars0
    g = fit.variance_model.pars.full

    fig = pl.figure()
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    idxg = fit.variance_model.pars['gamma'].indexof()
    idxk = fit.variance_model.pars['kappa'].indexof()
    hist(ax, (g/g_gen)[idxg], color = 'b', histtype='step')
    hist(ax, (g_init/g_gen)[idxg], color = 'c', histtype='step')
    ax.set_title(r'$\gamma$')
    hist(ax2, (g/g_gen)[idxk], color = 'r', histtype='step')
    hist(ax2, (g_init/g_gen)[idxk], color = 'orange', histtype='step')
    ax2.set_title(r'$\kappa$')


def plot_tw0models(model, pars, p, p0, labelp, labelp0, sigma_pars, sigma_pars0):

    if (pars == 'CL'):
        figcl = pl.figure()
        idxcl = model.pars['CL'].indexof()
        bas = model.basis.bx.range
        restframe_wl = np.linspace(bas[0], bas[1], 500)
        P_cl0, J_cl = model.color_law(restframe_wl, p0[idxcl], jac=False)
        P_cl, J_cl = model.color_law(restframe_wl, p[idxcl], jac=False)
        gs = pl.matplotlib.gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        ax1 = figcl.add_subplot(gs[0])
        ax2 = figcl.add_subplot(gs[1])
        ax1.plot(model.color_law.reduce(restframe_wl), P_cl, 'b-', label=labelp)
        ax1.plot(model.color_law.reduce(restframe_wl), P_cl0, 'r-', label=labelp0)
        ax2.plot(model.color_law.reduce(restframe_wl), P_cl/P_cl0, 'k.')
        ax2.set_ylabel('ratio')
        ax1.set_ylabel('CL')
        ax2.grid(1)
        ax1.grid(1)
        ax1.legend()
        ax2.set_xlabel(r'$\lambda_{red}^*$')
        
    elif (pars == 'M0') ^ (pars == 'M1'):
        figsur = pl.figure()
        surface= [pars]
        if (pars == 'M0'):
            vmin, vmax = -0.1, 0.5
        else :
            vmin, vmax = -0.01, 0.05
        model.pars.free = p
        x, y, z = plot_2Dsurfacemodel(model, surface, plot = False)
        model.pars.free = p0
        x, y, z0 = plot_2Dsurfacemodel(model, surface, plot = False)
        ax = figsur.add_subplot(311)
        extent = np.min(x), np.max(x), np.min(y), np.max(y)
        m = ax.imshow(z, vmin=vmin, vmax=vmax, origin="lower", extent=extent, aspect='auto')
        ax.set_title(f'{labelp} : {surface[0]}')
        pl.colorbar(m)

        
        ax1 =  figsur.add_subplot(312)
        m1 = ax1.imshow(z0, vmin=vmin, vmax=vmax, origin="lower", extent=extent, aspect='auto')
        ax1.set_title(f'{labelp0} : {surface[0]} gen')
        pl.colorbar(m1)
        ax2 =  figsur.add_subplot(313)
        m2 = ax2.imshow(z/z0, vmin=0.5, vmax=1.5, origin="lower", extent=extent, aspect='auto')
        ax2.set_title('ratio')
        pl.colorbar(m2)
        
    else :
        figpar = pl.figure()
        gs = pl.matplotlib.gridspec.GridSpec(3, 2, figure=figpar)
        ax = figpar.add_subplot(gs[:-1, 0])
        ax1 = figpar.add_subplot(gs[-1:, 0])

        idx = model.pars[pars].indexof()
        ppars = p[idx]
        p0pars = p0[idx]

        if pars in ['X0', 'X1', 'tmax', 'c']:
            z = model.training_dataset.sne['z']
            idxz = z.argsort()
            
            x = z[idxz]
            ppars = ppars[idxz]
            p0pars = p0pars[idxz]

            sig = sigma_pars[idx][idxz]
            sig0 = sigma_pars0[idx][idxz]
            
        else : 
            x = np.arange(len(idx))
            sig = 0
            sig0 = 0
            
        ax.errorbar(x, ppars, yerr = sig, color ='r', marker ='.', ls = '', label = f'{labelp}')
        ax.grid()
        
        
        ax.set_title(pars)
        ax.errorbar(x, p0pars, yerr = sig0, color ='k', marker ='.', ls = '', label = f'{labelp0}')
        #ax.plot(x, p0pars, 'k.', label = f'{labelp0}')
        ax1.set_xlabel('redshift')
        ax.legend()
        
        if pars == 'X0':
            ax1.plot(x, p0pars/ppars, 'k.')
            binplot(x, p0pars/ppars, data = False, marker = '.', markersize=20)
            ax1.grid()
            ax1.set_ylabel('ratio')

            ax3 = figpar.add_subplot(gs[-1:, 1])
            hist(ax3, p0pars/ppars, color = 'k', bins = 10, orientation='horizontal')


            ax.set_yscale('log')
            MIN, MAX = 1e-11, 1e-5
            bins = 10 ** np.linspace(np.log10(MIN), np.log10(MAX), 10)

            ax2 = figpar.add_subplot(gs[:-1, 1], sharey = ax)
            hist(ax2, ppars, color = 'r', bins = bins, orientation='horizontal')
            hist(ax2, p0pars, color ='k', bins = bins, orientation='horizontal')
            ax2.set_yscale("log")

            

            
        else :
            
            ax1.plot(x, p0pars-ppars, 'k.')
            binplot(x, p0pars-ppars, data = False, marker = '.', markersize=20)
            ax1.grid()
            ax1.set_ylabel('difference')

            ax2 = figpar.add_subplot(gs[:-1, 1])
            hist(ax2, ppars, color = 'r', bins = 10, orientation='horizontal')
            hist(ax2, p0pars, color ='k', bins = 10, orientation='horizontal')

            ax3 = figpar.add_subplot(gs[-1:, 1])
            hist(ax3, p0pars-ppars, color = 'k', bins = 10, orientation='horizontal')


def plot_calibration_zp(model, eta_covmatrix, pars_generation = None, dir_plot = None, k21=False):
    """
    """
    idx_photo_calibration = model.pars['eta_calib'].indexof()
    fig = pl.figure(figsize=(8,8))
    ax = fig.add_subplot(131)
    bands = model.bands
    eta = model.pars.full[idx_photo_calibration]
    ax.plot(eta, bands, ls = '', marker = '+', color='DarkRed', label = 'reconstruction')

    if pars_generation is not None:
        ax.plot(pars_generation[idx_photo_calibration], bands, 'k*', label = 'generation')

    ax.grid(1)
    ax.legend()
    

    ax1 = fig.add_subplot(132)
    if k21:
        survey = np.array([bd.split('::')[1].split('-')[0] for bd in bands.astype(str)])
    else : 
        survey = np.array([bd.split('::')[0] for bd in bands.astype(str)])
    zp_sur = []
    for isur in survey:
        idx = np.where(survey == isur)
        zp_sur.append(eta[idx].mean())
    ax1.plot(zp_sur, survey, ls = '', marker = '+', color='DarkGreen')#, label = '')
    ax1.grid(1)
    
    lc = model.lc_data
    m_wl = []
    ax2 = fig.add_subplot(133)
    for ib in bands:
        idx = lc['Filter'] == ib
        m_wl.append(np.mean(np.unique(lc['Wavelength'][idx])))#/(1+lc['ZHelio'][idx]))))
        #print(ib, np.unique(lc['Wavelength'][idx]))#/(1+lc['ZHelio'][idx])))
    m_wl = np.array(m_wl)
    idx_lw = m_wl.argsort()
    ax2.plot(eta[m_wl.argsort()], bands[idx_lw], ls = '', marker = '+', color='DarkBlue')
    ax2.grid(1)

    if type(eta_covmatrix) == float :
        sig = np.sqrt(eta_covmatrix)
        ax.axvline(sig, color ='r', ls = '--', alpha = 0.5)
        ax.axvline(-sig, color ='r',ls = '--', alpha = 0.5)

        ax1.axvline(sig, color ='r', ls = '--', alpha = 0.5)
        ax1.axvline(-sig, color ='r',ls = '--', alpha = 0.5)

        ax2.axvline(sig, color ='r', ls = '--', alpha = 0.5)
        ax2.axvline(-sig, color ='r',ls = '--', alpha = 0.5)
        
    else :
        sig = np.sqrt(eta_covmatrix)#np.diag(eta_covmatrix))
        #ax.plot(sig, bands, 'k+')
        #ax.plot(-sig, bands, 'k+')
        
        ax.plot(sig,bands,  color ='r', ls = '--', alpha = 0.5)
        ax.plot(-sig,bands,  color ='r',ls = '--', alpha = 0.5)

        ax2.plot(sig[idx_lw], bands[idx_lw],  color ='r', ls = '--', alpha = 0.5)
        ax2.plot(-sig[idx_lw], bands[idx_lw],  color ='r',ls = '--', alpha = 0.5)

    import matplotlib.ticker as ticker
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
    ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.4f'))
        
    print(r'eta < 1 $\sigma$ : ', (np.abs(eta) < sig).sum()/len(eta))
    print(r'eta < 2 $\sigma$ : ', (np.abs(eta) < 2*sig).sum()/len(eta))
    print(r'eta < 3 $\sigma$ : ', (np.abs(eta) < 3*sig).sum()/len(eta))
    ax.set_title(f'sigma : {sig}')
    if dir_plot is not None: 
        dir_plot 
        pl.savefig(dir_plot)
        
    

def plot_spec(model, idx_spec, variance_model = False, save_dir = None, add_name = f"", plot=True, sigma = None):
    """
    """
    model.pars.release()    
    idx = model.training_dataset.spec_data['spec_id'] == idx_spec 
    sp =  model.training_dataset.spec_data[idx]
    snInfo = model.training_dataset.sne

    z = sp['ZHelio'][0]
    
    sne = sp['sn_id'][0]
    x0 = model.pars['X0'].full[sne]
    tmax = model.pars['tmax'].full[sne]
    x1 = model.pars['X1'].full[sne]
    c = model.pars['c'].full[sne]
    ph_basis_size = len(model.basis.by)
    M0 = model.pars['M0'].full
    M1 = model.pars['M1'].full
    cl_pars = model.pars['CL'].full

    if sigma is not None:
        x0_err = sigma[model.pars['X0'].indexof()][sne]
        tmax_err = sigma[model.pars['tmax'].indexof()][sne]
        x1_err = sigma[model.pars['X1'].indexof()][sne]
        c_err = sigma[model.pars['c'].indexof()][sne]
 
    
    phase = (sp['Date']- tmax)/(1+z)
    restframe_wl = sp['Wavelength']/(1+z)
    
    J = model.basis.eval(restframe_wl, phase + model.delta_phase).tocsr()
    V0  = J.dot(M0)
    V1  = J.dot(M1)
    P_cl, J_cl = model.color_law(restframe_wl, cl_pars, jac=False)
    CL  = np.power(10., 0.4*c*P_cl)
    zz = 1. + z
    
    recal_func = SpectrumRecalibrationPolynomials(model.training_dataset, model,
                                                  model.recalibration_degree)
    recal, J_recal = recal_func(jac=False)
    M = (V0 + x1 * V1)
    flux = M * CL * recal[idx] / zz

    if plot :
        fig = pl.figure(figsize=(10,8))
        gs = fig.add_gridspec(nrows=4,ncols=1)
        ax = fig.add_subplot(gs[:3,0])

        label0 = 'data' + f" X0 :  {snInfo['x0'][sne] : .5f} " + f" X1 :  {snInfo['x1'][sne] : .3f} " + f"\n tmax :  {snInfo['tmax'][sne] : .3f} " + f" c :  {snInfo['c'][sne] : .3f} "  #+ f" eta :  {0. : .3f}"
        if sigma is not None:
            label = 'data' + f" X0 :  {x0 : .5f} $\pm$ {x0_err : .5f}  " + f" X1 :  {x1 : .3f}  $\pm$ {x1_err : .3f}" + f"\n tmax :  {tmax : .3f} $\pm$ {tmax_err : .3f}" + f" c :  {c : .3f} $\pm$ {c_err : .3f}"  #+ f" eta :  {0. : .3f}"
        else :
            label = 'data' + f" X0 :  {x0 : .5f}   " + f" X1 :  {x1 : .3f}" + f"\n tmax :  {tmax : .3f}" + f" c :  {c : .3f}" 
 


        try : 
            ax.errorbar(restframe_wl, sp['Flux'], yerr = sp['FluxErr'],
                        color = 'k', marker = '.', ls = '',
                        label = label0)#'data' + f" X0 :  {snInfo['x0'][sne] : .5f}  " + f" X1 :  {snInfo['x1'][sne] : .3f}  " + f"\n tmax :  {snInfo['tmax'][sne] : .3f}" + f" c :  {snInfo['c'][sne] : .3f}"+ f' rec_sp', alpha = 0.4)                    
        except :
            ax.errorbar(restframe_wl, sp['Flux'], yerr = sp['FluxErr'], color = 'k', marker = '.', ls = '')

        ax.plot(restframe_wl, flux, color = 'r', ls = '-',
                label = label)#'model'  + f" X0 :  {x0 : .5f}  " + f" X1 :  {x1 : .3f}  " +  f"\n tmax :  {tmax : .3f}  " + f" c :  {c : .3f}  "+ f" rec_sp  ", alpha = 0.4)        
        idxmax = np.where(sp['Flux'] == sp['Flux'].max())[0]
        idxmin = np.where(sp['Flux'] == sp['Flux'].min())[0]
        ax.set_ylim((sp['Flux']- 3 * sp['FluxErr'])[idxmin], (sp['Flux']+ 3 * sp['FluxErr'])[idxmax])

        ax.set_ylabel('Flux')
        ax.grid(True)
        pl.title(f"{sne} {idx_spec} phase : {phase[0] :.3f}  z={snInfo['z'][sne] : .4f}")
        res = fig.add_subplot(gs[3,0], sharex = ax)

    
    if variance_model :
        spline_sp = variance_model.basis.eval(restframe_wl, phase)
        ss_sp = (spline_sp * variance_model.pars['gamma'].full)
        sigsp = ss_sp * sp['Flux']
        if plot :
            ax.plot(restframe_wl, flux + sigsp, color = 'b', ls ='--')
            ax.plot(restframe_wl, flux - sigsp, color = 'b', ls ='--')
            ax.fill_between(restframe_wl, flux - sigsp, flux + sigsp, color = 'b', alpha=0.25)
    
    val = model(model.pars.free, plotting = True, spec_plot = True)
    RES = (sp['Flux'] - val[sp['i'] - len(model.training_dataset.lc_data)])
    if plot :
        res.errorbar(restframe_wl, RES, sp['FluxErr'], 
                     color = 'r', marker = '+',ls = '',
                     label = 'Measurement Error')
                
        if variance_model :
            mod_res_minus = 0. - sigsp#/val0[idx]
            mod_res_plus = 0. + sigsp#/val0[idx]
            res.plot(restframe_wl,  mod_res_minus , color = 'b', ls ='--')
            res.plot(restframe_wl,  mod_res_plus, color = 'b', ls ='--')
            res.fill_between(restframe_wl, mod_res_minus,mod_res_plus, color = 'b', alpha=0.25)
            res.errorbar(restframe_wl, RES, sigsp, color = 'k', marker = '+',ls = '',
                         label= 'Error Model')
        res.grid(True)
        res.legend()
        res.set_ylabel('y-mod')
        res.set_xlabel('Wavelength')
        res.set_ylim(-10 * max(np.abs(RES.max()),np.abs(RES.min())),
                    10 * max(np.abs(RES.max()),np.abs(RES.min())))


        # if variance_model :

        #     ax.errorbar(restframe_wl,
        #                 sp['Flux'],
        #                 yerr = sigsp, elinewidth = 2.5,
        #                 color = 'darkorange', marker = '',
        #                 ls = '', label = r'$\sigma_X$')

        #     ax.errorbar(restframe_wl, sp['Flux'],
        #                 yerr = np.sqrt(sigsp**2+sp['FluxErr']**2),
        #                 elinewidth = 1.,
        #                 color = 'green', marker = '',
        #                 ls = '', label = r'$\sigma$')

        ax.legend(ncol=1)

        if save_dir is not None:
            name_plot = save_dir + os.sep +  add_name + f"{sne}_{idx_spec}_sp.png"
            pl.savefig(name_plot)
        return fig
    if variance_model == False:
        sigsp = np.zeros_like(flux)
    val0 = val[sp['i'] - len(model.training_dataset.lc_data)]
    print('vla,flux', (val0==flux).sum()/len(flux))
    return restframe_wl, flux, val0, sigsp

def plot_coverage_diagram(specimen, model, vmin = 0, vmax = 200, xbin = 50):
    """
    Plot the coverage diagram of the model for Lc or spectra
    """
    range0 = [model.wl_range, model.phase_range]
    if specimen == 'lc':
        data = model.training_dataset.lc_data
        zz = data['ZHelio']+1

        Y_sp = (data['Date']-model.training_dataset.sne['tmax'][data['sn_id']]) / zz
        X_sp = data['Wavelength']/zz
        xbin = xbin
        
    elif specimen == 'spec':
        #data = model.training_dataset.spec_data
        #zz = data['ZHelio']+1
        Y_sp = []
        X_sp = []
        xbin = 10
        bins = np.arange(range0[0][0], range0[0][1], xbin)
        
        #for sp in model.training_dataset.spectra:
        for isp in range(model.training_dataset.nb_spectra()):
            sp = model.training_dataset.spec_data[model.training_dataset.spec_data['spec_id']==isp]
            
            x_sp = sp['Wavelength']/(1+sp['ZHelio'])
            y_sp = (sp['Date'] - model.training_dataset.sne['tmax'][sp['sn_id']])/(1+sp['ZHelio'])
            idx_bins = np.where((x_sp.min() < bins) & (x_sp.max() > bins))
            X_sp.append(bins[idx_bins])
            Y_sp.append(y_sp[0] * np.ones_like(idx_bins[0]))

        
        X_sp = np.hstack(X_sp)
        Y_sp = np.hstack(Y_sp)
        
    else:
        print("specimen should be 'lc' or 'spec'")
        

    pl.figure()
    cmap = pl.cm.jet
    norm = pl.matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    Z = pl.hist2d(X_sp, Y_sp, bins=[int((range0[0][1]-range0[0][0])/xbin),
                                    int((range0[1][1]-range0[1][0])/2)],
                  range=range0, cmap = cmap, norm = norm)
    pl.colorbar()
    #pl.ylim()
    #pl.xlim(2000,9000)
    pl.xlabel(r'$\lambda \; [\AA]$')
    pl.ylabel('Phase [days]')
    #pl.title(f'{specimen} Coverage Diagram')
    pl.show()
    return Z
    
    


def plot_2Dsurfacemodel(model, surfaces, vmin = 0, vmax = 0.01, ddd = True,
                        init_unit = False, plot = True, theta_init = None,
                        save_dir = None, add_name = '',
                        cmap = pl.cm.jet):
    """
    """
    x = np.linspace(model.basis.bx.range[0], model.basis.bx.range[1]-1,
                    model.basis.bx.nj)        
    y = np.linspace(model.basis.by.range[0], model.basis.by.range[1]-1,
                    model.basis.by.nj)

    for pars in surfaces:
        idx = model.pars[pars].indexof()
        theta = model.pars.full[idx]

        X, Y = np.meshgrid(x, y)
        ZZ = (model.basis.eval(x=X.ravel(), y = Y.ravel()) * theta).reshape(X.shape)
        if init_unit:
            theta0 = model.pars0[idx]
            ZZ0 = (model.basis.eval(x=X.ravel(), y = Y.ravel()) * theta0).reshape(X.shape)
            zz = ZZ0
        else:
            zz = ZZ
            
        if plot :
            if init_unit == False:
                fig = pl.figure()
                if ddd:
                    ax = fig.gca(projection='3d')
                    surf = ax.plot_surface(X, Y, ZZ, cmap = pl.cm.coolwarm, vmin = vmin, vmax=vmax,
                                           linewidth=0, antialiased=False)
                    ax.set_zlabel('Flux')
                    ax.text2D(0., 1., f'{pars}', transform=ax.transAxes)
                    fig.colorbar(surf, shrink=0.5, aspect=5)

                else :
                    extent = np.min(x), np.max(x), np.min(y), np.max(y)
                    ax = fig.add_subplot(111)
                    pl.imshow(ZZ, origin="lower", extent = extent, aspect = 'auto',
                              vmin = vmin, vmax = vmax)
                    ax.set_title(f'{pars}')
                    pl.colorbar()

                ax.set_ylabel('Phase')
                ax.set_xlabel('Wavelenght')
                pl.show()
                
            if init_unit:
                fig = pl.figure(figsize = (4,3))

                cmap, mi, ma = pl.cm.ocean, 0.25, 0.9
                new_cmap = pl.matplotlib.colors.LinearSegmentedColormap.from_list(
                    'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap, a=mi, b=ma),
                    cmap(np.linspace(mi, ma, 30)))

                
                extent = np.min(x), np.max(x), np.min(y), np.max(y)
                ax = fig.add_subplot(111)
                pl.imshow(ZZ/ZZ0, origin="lower", extent=extent, aspect='auto',
                          vmin=vmin, vmax=vmax, cmap=new_cmap)
                ax.set_title(f'{pars}/{pars}_generation')
                if pars == 'gamma':
                    ax.set_title(r'$\gamma$ / $\gamma_{generation}$')
                pl.colorbar()
                ax.set_xlabel(r'$\lambda \; [\AA]$')
                ax.set_ylabel('Phase [days]')

                #ax.set_ylabel('Phase')
                #ax.set_xlabel('Wavelenght')
                if save_dir is not None:
                    name_plot = save_dir + os.sep + add_name + f"{pars}_surface.png"
                    pl.savefig(name_plot)                

                if theta_init is not None:
                    ZZ_init = (model.basis.eval(x=X.ravel(),
                                                y = Y.ravel()) * theta_init).reshape(X.shape)

                    fig = pl.figure(figsize = (4,3))
                    axh = fig.add_subplot(111)
                    ratio = (ZZ/ZZ0).ravel()
                    ratio_init = (ZZ_init/ZZ0).ravel()

                    ratio[np.isnan(ratio)] = 1e10
                    ratio_init[np.isnan(ratio_init)] = 1e10

                    # from robuststat import mad
                    # ratio = ratio[np.abs(ratio - np.median(ratio)) < 0.2]# 1 * mad(ratio)]
                    # ratio_init = ratio_init[np.abs(ratio_init-np.median(ratio_init))<1*mad(ratio_init)]
                    
                    lcs = model.lc
                    sps = model.sp
                    ph_sp = model.model.get_restframe_phases(sps)
                    ph_lc = model.model.get_restframe_phases(lcs)
                    wl_sp = sps['Wavelength']/(1 + sps['ZHelio'])
                    wl_lc = lcs['Wavelength']/(1 + lcs['ZHelio'])
                    X = np.hstack((wl_sp,wl_lc))
                    Y = np.hstack((ph_sp,ph_lc))
                    jj = model.basis.eval(X, Y)
                    idx = np.where(np.bincount(np.sort(jj.col))/(len(X))*100/16 > 1.5)
                    ratio = ratio[idx]
                    ratio_init = ratio_init[idx]


                    
                    axh.hist(ratio, bins = 'auto',
                             label = f'parameters rec/gen : m {ratio.mean() : .3f} , sig {ratio.std() : .3f}',
                             histtype='step')
                    axh.hist(ratio_init, bins = 'auto', label = f'parameters init/gen : m {ratio_init.mean() : .3f} , sig {ratio_init.std() : .3f}',
                             histtype='step')
                    axh.legend()
                    axh.grid(1)
                    axh.grid('minor', ls = '--', alpha = 0.5)
                    if save_dir is not None:
                        name_plot = save_dir + os.sep +  os.sep +  add_name + f"{pars}_histograms_parameters.png"
                        pl.savefig(name_plot)                

        return X, Y, zz
 

def plot_hist_partvariance(variance_model):
    var = variance_model(variance_model.pars.free, variance_model.model.pars.free)
    flux_err = np.hstack((variance_model.lc['FluxErr'], sp['FluxErr']))
    sig = np.sqrt(var - flux_err**2)      

    res = sig/flux_err
    lc = res[variance_model.model.lc['i']]
    sp = res[variance_model.model.sp['i']]
    idxlc = lc <= lc.max() #np.abs(lc)<3*robuststat.mad(lc)
    idxsp = sp <= sp.max() #np.abs(sp)<3*robuststat.mad(sp)

    fig = pl.figure()

    axlc = fig.add_subplot(121)
    axlc.hist(lc[idxlc], bins = 'auto', density = True,
              label = f'mu = {lc[idxlc].mean() : .3} , sigma = {lc[idxlc].std() : .3}')
    axlc.legend(loc='best')
    axlc.set_ylabel(r'$ \frac{\sigma_X}{\sigma_{flux}}$')
    axlc.set_title(f'lc : pts in : {idxlc.sum()/len(lc) : .1%}')
    axlc.grid(1)

    axsp = fig.add_subplot(122)
    axsp.hist(sp[idxsp], bins = 'auto', density = True,
              label = f'mu = {sp[idxsp].mean() : .3} , sigma = {sp[idxsp].std() : .3}')
    axsp.legend(loc='best')
    axsp.set_title(f'sp : pts in : {idxsp.sum()/len(sp) : .1%}')
    axsp.grid(1)

def plot_kappa_CS(model, CS, sigma_init, kappa_init, save_dir = None, add_name =f''):

    fig = pl.figure(figsize=(20,10))
    sig = np.hstack((CS.sigma_blue, CS.sigma_red))
    s = CS(sig)
    lambda_c_red = CS.WL
    sr = CS(sigma_init.ravel())
    k = model.pars['kappa_color'].full.copy()

    gs = pl.matplotlib.gridspec.GridSpec(3, 1, height_ratios=[1, 3, 1])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    idx = lambda_c_red.argsort()
    ax2.plot(lambda_c_red[idx], kappa_init[idx], 'kp', label = r'$\kappa$ init')
    ax2.plot(lambda_c_red[idx], k[idx], 'r.', label = r'$\kappa$')
    ax2.plot(lambda_c_red[idx], s[idx], 'r-', label = r'$\sigma$' + f' : {sig}')
    ax2.plot(lambda_c_red[idx], sr[idx], 'k--', label = r'$\sigma$ init'+f' : {sigma_init.ravel()}')
    ax2.plot(lambda_c_red[idx], -s[idx], 'r-')
    ax2.plot(lambda_c_red[idx], -sr[idx], 'k--')
    ax2.grid()
    ax2.legend(loc='lower right')
    ax2.set_ylabel(r'$\kappa$')
    ax3 = fig.add_subplot(gs[2])
    ax3.plot(lambda_c_red[idx], kappa_init[idx]-k[idx], 'k.')
    binplot(lambda_c_red[idx], kappa_init[idx]-k[idx],data = False,marker = '.', markersize=20)
    ax3.grid()
    ax3.set_xlabel(r'$\lambda_{red}^*$')
    ax3.set_ylabel(r'$\kappa - \kappa_{gen}$')
    ax1.hist(lambda_c_red[idx], bins='auto')
    ax1.grid(1)
    
    
def plot_kappa_sigma(model, gkappa, lambda_c_red, sigma_init, kappa_init, bins = None,
                     sigs = None, sigp = None, save_dir = None, add_name =f'', bins_vals = True):

    fig = pl.figure(figsize=(20,10))
    s = np.polyval(gkappa, lambda_c_red) #* lambda_c_red ###ICI 
    sr = np.polyval(sigma_init, lambda_c_red) #* lambda_c_red ### ICI 
    k = model.pars['kappa_color'].full.copy()

    gs = pl.matplotlib.gridspec.GridSpec(3, 1, height_ratios=[1, 3, 1])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    idx = lambda_c_red.argsort()
    ax2.plot(lambda_c_red[idx], kappa_init[idx], 'kp', label = r'$\kappa$ init')
    ax2.plot(lambda_c_red[idx], k[idx], 'r.', label = r'$\kappa$')
    ax2.plot(lambda_c_red[idx], s[idx], 'r-', label = r'$\sigma$' + f' : {np.round(gkappa,3)}')
    ax2.plot(lambda_c_red[idx], sr[idx], 'k--', label = r'$\sigma$ init'+f' : {sigma_init}')
    ax2.plot(lambda_c_red[idx], -s[idx], 'r-')
    ax2.plot(lambda_c_red[idx], -sr[idx], 'k--')
    ax2.grid()
    ax2.legend(loc='lower right')
    ax2.set_ylabel(r'$\kappa$')

    if sigs is not None:
        ax2.plot(lambda_c_red, -sigs, marker ='.',color = 'purple', ls = '' )
        ax2.plot(lambda_c_red, sigs, marker = '.', color = 'purple', ls = '',
                 label ='covariance simulation')

    if sigp is not None:
        ax2.plot(lambda_c_red, -sigp, 'b+')
        ax2.plot(lambda_c_red, sigp, 'b+',  label ='covariance propagation')

    if bins_vals :
        xrange = np.linspace(lambda_c_red.min(),lambda_c_red.max(), 10)
        dx = np.diff(xrange).mean()
        for i in range(len(xrange) - 1):
            idxr = np.where((lambda_c_red < xrange[i+1]) & (lambda_c_red > xrange[i]))

            ax2.text(xrange[i] + dx/2 , sr.max(),
                     f'{(np.abs(k)[idxr]<np.abs(s)[idxr]).sum()/len(s[idxr]) : .3f}')

            ax2.text(xrange[i] + dx/2, -sr.max(),               
                     f'{(np.abs(kappa_init)[idxr]<np.abs(sr)[idxr]).sum()/len(sr[idxr]) : .3f}',
                     alpha = 0.4)

            ax2.axvline(xrange[i], alpha = 0.15, color = 'k', ls = '--')
            ax2.axvline(xrange[i+1], alpha = 0.15, color = 'k', ls = '--')
        
    binplot(lambda_c_red[idx], k[idx], data = False, bins = bins, marker = '.', markersize=20)
    ax3 = fig.add_subplot(gs[2])
    ax3.plot(lambda_c_red[idx], kappa_init[idx]-k[idx], 'k.')
    binplot(lambda_c_red[idx], kappa_init[idx]-k[idx],data = False,marker = '.', markersize=20)
    ax3.grid()
    ax3.set_xlabel(r'$\lambda_{red}^*$')
    ax3.set_ylabel(r'$\kappa - \kappa_{gen}$')
    ax1.hist(lambda_c_red[idx], bins='auto')
    ax1.grid(1)

    if save_dir is not None:
        name_plot = save_dir + os.sep + add_name + os.sep + f"kappa_reconstruction.png"
        pl.savefig(name_plot)                
    
    return fig
     

def binning_residuals(model, variance_model = None, save_dir = None, add_name = f"", pull=True):
    """
    """
    mod = model(model.pars.free)

    lc = model.training_dataset.lc_data
    modlc = mod[lc['i']]
    phaselc = model.get_restframe_phases(lc)
    reslc = lc["Flux"] - modlc 

    sp = model.training_dataset.spec_data  
    modsp = mod[sp['i']]
    phasesp = model.get_restframe_phases(sp)
    ressp = sp["Flux"] - modsp

    if variance_model is not None:
        var = variance_model(variance_model.pars.free, model.pars.free)
        sigerr = np.sqrt(var)
        sigerrlc = sigerr[lc['i']]
        sigerrsp = sigerr[sp['i']]
    else :
        sigerrlc = lc['FluxErr']
        sigerrsp = sp['FluxErr']

    if pull :
        reslc /= sigerrlc
        ressp /= sigerrsp
        ylabel = r'Y - Mod/$\sigma$'
    else :
        ylabel = 'Y - Mod'
    #binning per surveys:
    split_term = '::'
    surveys = np.unique(np.array(([bd.split(split_term)[0] for bd in model.bands.astype(str)])))

    if surveys[0] == 'K21':
        split_term = '-'
        surveys = np.unique(np.array(([bd.split(split_term)[0] for bd in model.bands.astype(str)])))

    def onpicklc(event):
        ax = event.inaxes
        bd = dict_plot[ax]
        idx_bd = lc['Filter'] == bd
        x, y = event.xdata, event.ydata
        print(x, y)
        difx = (phaselc[idx_bd] - event.xdata)**2#np.abs(phaselc - event.xdata)[idx_bd]**2
        dify = (reslc[idx_bd] - event.ydata)**2#np.abs(reslc - event.ydata)[idx_bd]**2
        dif = np.sqrt(difx + dify)
        idxpt = lc[idx_bd][np.where(dif == dif.min())][0]
        print(idxpt)
        lc_id = idxpt['lc_id']
        #for dataind in [lc_id] : 
        plot_lc(model, lc_id, variance_model)
        return True

    dict_plot = {}
    for survey in surveys:
        survey_bands = np.array([bd for bd in model.bands if bd.decode('UTF_8').split(split_term)[0] == survey])
        
        col = 2
        lcfig, lcaxes = pl.subplots(nrows = ceil((len(survey_bands) / col)),
                                    ncols = col, figsize=(12,10))
        lcaxes = lcaxes.ravel()
        lcfig.dpi = 100
        lcfig.suptitle(f'{survey}', fontsize=16)
        for i, bd in enumerate(survey_bands):
            idx = lc["band_id"] == i
            x, y = phaselc[idx], reslc[idx]
            mu, sig = y.mean(), y.std()

            vmax = np.abs(y).max()
            print(survey_bands, vmax)
            line = lcaxes[i].errorbar(x, y, yerr=sigerrlc[idx], marker=".",ls="", alpha=0.15,
                                      picker=True,
                                      label = f'$\mu$ : {mu : .5f}, $\sigma$ : {sig : .5f}')
            
            lcaxes[i].set_title(bd)
            lcaxes[i].grid(1)
            lcaxes[i].legend()
            lcaxes[i].set_ylim(-vmax*1.2, 1.2*vmax)
            xbin, ybin, yerrbin = binplot(x, y, color="r", data=False, noplot=True)
            lcaxes[i].set_ylabel(ylabel, picker=True)
            lcaxes[i].set_xlabel('phase', picker=True)
            lcaxes[i].errorbar(xbin, ybin, yerr=yerrbin, color="r", ls="", marker="o")#, picker=5)
            lcaxes[i].set_picker(True)
            dict_plot[lcaxes[i]] = bd
        #lcfig.canvas.mpl_connect('button_press_event', #'pick_event',
        #                         onpicklc)
        
            
        pl.subplots_adjust(wspace=0.2, hspace=0.35)
        if save_dir is not None:
            pl.savefig(save_dir + os.sep + survey +'_lcbinned_residuals.png')


    def onpickspec(event):
        print(event.inaxes)
        ax = event.inaxes
        wlx, resy = dict_plot_sp[ax]
        x = event.xdata,
        y = event.ydata
        print(x, y)
        print(wlx.shape, resy.shape)
        difx = (wlx - event.xdata)**2
        dify = (resy - event.ydata)**2        
        dist = np.sqrt(difx+dify)
        idxx = np.where(dist == dist.min())
        print(idxx)#,idxy)
        print(resy[idxx[0]], wlx[idxx[0]])
        idxpt = sp[(ressp == resy[idxx[0]][0]) & (wl == wlx[idxx[0]][0])]
        spec_id = idxpt['spec_id']
        print(spec_id)
        for dataind in spec_id : 
            plot_spec(model, spec_id, variance_model)
        return True

            
    n_bins = 8
    spfig, spaxes = pl.subplots(nrows = round(n_bins / 2), ncols = 2, figsize=(12,10))    
    bins = np.linspace(model.basis.by.grid[0], model.basis.by.grid[-1], n_bins+1)
    spaxes = spaxes.ravel()
    wl = sp['Wavelength']/(1+sp['ZHelio'])
    dict_plot_sp = {}
    spfig.dpi = 100

    for i in range(n_bins):
        lowerval, upperval = bins[i], bins[i+1]
        idx = (phasesp < upperval) & (phasesp > lowerval)
        x, y = wl[idx], ressp[idx]
        mu, sig = y.mean(), y.std()
        dict_plot_sp[spaxes[i]] = (wl[idx], ressp[idx])
        line = spaxes[i].errorbar(x, y, yerr=sigerrsp[idx], color="k", marker=".", ls="", alpha=0.05,
        picker = True, label = f'$\mu$ : {mu : .5f}, $\sigma$ : {sig : .5f}')
        spaxes[i].set_ylim(mu- 5*sig,#5*mu,
                           mu+ 5*sig)#5*mu)
        spaxes[i].set_xlim(3100,#5*mu,
                           9000)#5*mu)

        #if len(y) != 0:
        #    vmax = np.abs(y).max()
        #    print(i, vmax)
        #    spaxes[i].set_ylim(-vmax*1.2, 1.2*vmax)

        spaxes[i].set_title(f'{lowerval : .1f}, < phase < {upperval : .1f}')
        spaxes[i].grid(1)
        spaxes[i].legend()
        try: 
            xbin, ybin, yerrbin = binplot(x, y, color="r", weights= 1/sigerrsp[idx]**2,
                                          data=False, noplot=True, nbins = 15)
        except :
            xbin, ybin, yerrbin = np.zeros(1), np.zeros(1), np.zeros(1)
        spaxes[i].errorbar(xbin, ybin, yerr=yerrbin, color="r", ls="", marker="o")
        
        spaxes[i].set_ylabel(ylabel, #'y - model',
                             picker=True)
        if (i == 6) ^ ( i == 7) :
            spaxes[i].set_xlabel(r'$\lambda^{\star}$', #'restframe Wavelength',
                                 picker=True)
     
    pl.subplots_adjust(wspace=0.2, hspace=0.35)
    #spfig.canvas.mpl_connect('button_press_event', 
    #                             onpickspec)
    if save_dir is not None:
        pl.savefig(save_dir + os.sep +  add_name + 'specbinned_residuals.png')
    




        

def plot_seaborn_2dist(x, y0, y1 = None, save_name = None):
    """
    """
    sns.set_style('whitegrid')
    if y1 is not None:
        y = np.hstack((y0, y1))
        hue = np.hstack((np.zeros_like(x), np.ones_like(x)))
        x = np.tile(x, 2)
    else :
        y = y0
        hue = np.zeros_like(x)
    g = sns.jointplot(x=x, y=y, hue=hue)
    if save_name:
        pl.savefig(save_name)
    pl.matplotlib.rc_file_defaults()

    
def plot_scatter(x, y):
    def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
        ax_histx.tick_params(axis="x", labelbottom=False)
        ax_histy.tick_params(axis="y", labelleft=False)
        ax.scatter(x, y)
        #binwidth = 0.025
        xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
        xymin = min(np.min(np.abs(x)), np.min(np.abs(y)))
        
        binwidth = (xymax - xymin)/30  #2* xymax/50
        #lim = (int(xymax/binwidth) + 1) * binwidth
        bins = np.arange(xymin,xymax+ binwidth, binwidth) #np.arange(-lim, lim + binwidth, binwidth)
        hist(ax_histx, x, bins=bins)
        hist(ax_histy, y, bins=bins, orientation='horizontal')
        #4(6)
    fig = pl.figure(figsize=(8, 8))
    gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.05, hspace=0.05)
    ax = fig.add_subplot(gs[1, 0])
    ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
    ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
    ax.grid()
    ax_histx.grid()
    ax_histy.grid()
    scatter_hist(x, y, ax, ax_histx, ax_histy)
    pl.show()

    
    
def residual_histogram(model, N_fit, variance_model=None, chi2_normalization=1, save_dir=None,
                       data_selection = False, add_name = f"", outsigma=3, name=None):
    """
    """
    
    f = ModelPulls(model, variance_model=variance_model,
                       chi2_normalization=chi2_normalization)
    pl.matplotlib.rcParams.update({'font.size': 15})
    fig = pl.figure(figsize=(5,4))
    allpl = fig.add_subplot(131)
    lcpl  = fig.add_subplot(132)
    sppl  = fig.add_subplot(133)
    
    lc = model.training_dataset.lc_data
    sp = model.training_dataset.spec_data
    x = model.pars.free
    if variance_model is not None:
        g = variance_model.pars.free
        #    ylabel = r'$\frac{data - model}{(VarMod)^{1/2}}$'
    else :
        g = []
    ylabel = r'$\frac{data - model}{\sigma}$'

    res,_ = f(x, g, jac = False)
    
    reslc = res[lc['i']]
    ressp = res[sp['i']]
        
    color = ['g', 'r', 'b', 'k']
    if data_selection :
        res = res[np.abs(res) < outsigma *  robuststat.mad(res)] 
        reslc = reslc[np.abs(reslc) < outsigma * robuststat.mad(reslc)]
        ressp = ressp[np.abs(ressp) < outsigma * robuststat.mad(ressp)]
        
    hist(allpl, res, title = 'All',histtype ='step', color = color[N_fit])
    dlc = (reslc.max() - reslc.min())/0.5
    hist(lcpl, reslc, title ='Light Curves ',histtype ='step', color = color[N_fit])
    hist(sppl, ressp, title ='Spectra',histtype ='step', color = color[N_fit])
    allpl.set_ylabel(ylabel)

    allpl.grid(1)
    lcpl.grid(1)
    sppl.grid(1)
    if name is None:
        fig.suptitle(f'Fit number {N_fit}')
    else :
         fig.suptitle(name)
    if save_dir is not None:
        pl.savefig(save_dir + os.sep + add_name + f'histogramme_residual_fitN{N_fit}.png')
    return fig

def hist(ax, res, title = '', histtype = 'bar', color = 'b',
         addlegend ='', bins = 'auto', gauss = True, moy = False, orientation = 'vertical'):
    n, bins, patches = ax.hist(res, bins = bins, density=True, histtype=histtype, color=color,
                               orientation=orientation)
    if moy :
        mu = res.mean()
        sigma = res.std()
        gauss = False
    else :
        mu, sigma = scipy.stats.norm.fit(res)
        #mu, sigma = np.median(res), robuststat.mad(res)
    y = scipy.stats.norm.pdf(bins, mu, sigma)
    xl = True
    if orientation =='horizontal':
        y,bins = bins, y
        xl = False
    if gauss:
        l = ax.plot(bins, y, '--',linewidth=1., color=color,
                    label= addlegend + r' $\mu$ :'+f'{mu: .3f}, '+ r'$\sigma$ : '+f'{sigma: .3f}')
        if xl :
            ax.set_xlim(mu - 5 * sigma,mu + 5 * sigma)
        else :
            print('')
    else :
        l = ax.plot(bins, y, '--',linewidth=0., color=color,
                    label= addlegend + r' $\mu$ :'+f'{mu: .3f}, '+ r'$\sigma$ : '+f'{sigma: .3f}')
    ax.legend(fontsize='x-small', loc='upper right')
    if title != '':
        ax.set_title(title)


def hist_pull_mod(f, save_title = '', title = '', ylabel = ''):
    """
    """
    fig = pl.figure(12,10)
    all = fig.add_subplot(131)
    lc  = fig.add_subplot(132)
    sp  = fig.add_subplot(133)
    try :
        g = f.VarianceModel.pars.free
    except :
        g = None
    res = f(f.model.pars.free, g, jac = False)

    hist(all, res[np.abs(res) < 3 * np.std(res)], title = 'all')
    hist(lc,res[f.model.lc_idx][np.abs(res[f.model.lc_idx])<3*np.std(res[f.model.lc_idx])],title ='lc')
    hist(sp,res[f.model.sp_idx][np.abs(res[f.model.sp_idx])<3*np.std(res[f.model.sp_idx])],title ='sp')
    all.set_ylabel(r'$\frac{flux_{data} - model}{(VarMod)^{1/2}}$')
    if title !='':
        fig.suptitle(title)
        if save_title !='' :
            pl.savefig('images/' + save_title + '.png')





            


def spectra_residuation_per_phase_bin(model, nbin = 10):
    """
    """
    rg = model.basis.bx.range
    range_phase = np.arange(rg[0], rg[1], nbin)
    sp = model.sp
    
    #mod = model(model.pars.free, data = sp)
    f = models.VarModelResiduals(model.data, model,
                                 NN = model.NN)
    res = f(f.model.pars.free, jac= False)
    wl = sp.wavelength/(1. + sp.zhelio)
    ph = (sp.date-model.pars['tmax'].full[sp.sn])/(1+sp.zhelio)
    fig = pl.figure(figsize=(12,8))
    gs = fig.add_gridspec(nrows=len(range_phase), ncols=1)
    
    for i in range(len(range_phase)-1):
        ax = fig.add_subplot(gs[i,0])
        idx = (ph > range_phase[i]) & (ph <= range_phase[i+1])
        print(f'\n {range_phase[i] : .3f} < phase < {range_phase[i+1] : .3f} : {len(np.unique(sp.obs_id[idx]))} spectra') 
        ax.errorbar(wl[idx], res[model.sp_idx][idx], yerr = sp.flux_err[idx],
                    #color = [ i for i in np.random.choice(range(256), size=3)],
                    ls = '', marker = '.')
        ax.set_title(f'{range_phase[i] : .3f} < phase < {range_phase[i+1] : .3f}')
        pl.grid(1)
        

def chi2_model2D(model, variance_model = None):
    """
    """
    val = model(model.pars.free)
    lc = model.training_dataset.lc_data
    sp = model.training_dataset.spec_data
    
    data = np.hstack((lc['Flux'], sp['Flux']))
    err = np.hstack((lc['FluxErr'], sp['FluxErr']))
    
    if variance_model is not None:
        var = variance_model(variance_model.pars.free, model.pars.free)
    else :
        var = err**2

    chi2_sp = []
    Npars_sp = 3 + model.spectrum_recal_degree #int(len(model.recal_poly.cp)/len(np.unique(model.sp.obs_id)))
    for isp in range(model.training_dataset.nb_spectra()):
        idx_sp = sp['spec_id'] == isp
        sp0 = sp[idx_sp]
        val0 = val[sp[idx_sp]['i']]
        
        den = idx_sp.sum() - Npars_sp
        cc = ((val0 - sp0['Flux'])**2/var[sp[idx_sp]['i']]).sum()/den
        chi2_sp.append(cc)

    chi2_lc = []
    Npars_lc = 6
    #name = []
    for ilc in range(model.training_dataset.nb_lcs()):
        idx_bd = lc['lc_id'] == ilc
        #fil = np.unique(model.data.band[idx_sn])
        #for bd in fil[1:] :
        #    idx_bd = (model.data.sn == ilc) & (model.data.band == bd)
        lc0 = lc[idx_bd]
        val0 = val[lc[idx_bd]['i']]
        den = idx_bd.sum() - Npars_lc
        cc = ((val0 - lc0['Flux'])**2/var[lc[idx_bd]['i']]).sum()/den
        #name.append(f"{ilc};;{bd.decode('UTF-8')}")
        chi2_lc.append(cc)
    chi2_sp = np.array(chi2_sp)
    chi2_lc = np.array(chi2_lc)
    #name = np.array(name)
    
    id_ordsp = chi2_sp.argsort()

    fig = pl.figure()
    pl.title('spectra')
    ax = fig.add_subplot(111)
    y = [str(i) for i in np.arange(model.training_dataset.nb_spectra())[id_ordsp]]
    line, = ax.plot(chi2_sp[id_ordsp], y, 'b+', picker=5)

    def onpick(event):
        N = len(event.ind)
        for subplotnum, dataind in enumerate(event.ind):
            NN = np.arange(model.training_dataset.nb_spectra())[id_ordsp[dataind]]
            if variance_model is not None:
                plot_spec(model, NN, variance_model=variance_model)
                #model.sp_reconstruction(N=NN, variance_model=variance_model, unique=True)
            else :
                plot_spec(model, NN)
                #model.sp_reconstruction(N=NN, unique=True)
        return True
    fig.canvas.mpl_connect('pick_event', onpick)
    
    id_ordlc = chi2_lc.argsort()
    fig0 = pl.figure()
    pl.title('light curves')
    ax0 = fig0.add_subplot(111)
    name = np.arange(model.training_dataset.nb_lcs())
    line, = ax0.plot(chi2_lc[id_ordlc], name[id_ordlc], 'b+', picker=5)
    def onpick(event):
        N = len(event.ind)
        print(N)
        for subplotnum, dataind in enumerate(event.ind):            
            ilc = name[id_ordlc][dataind]
            print(ilc)
            #sn, band = int(nam.split(';;')[0]), nam.split(';;')[1].encode('UTF-8')
            #NN = np.unique(model.lc.sn)[sn]
            #print(sn, band, NN)
            if variance_model is not None:
                #model.lc_reconstruction(N = NN, unique = True, band = band,
                #                        variance_model = variance_model)
                plot_lc(model, ilc, variance_model=variance_model)
            else :
                plot_lc(model, ilc)
                #model.lc_reconstruction(N = NN, unique = True, band = band)
        return True
    fig0.canvas.mpl_connect('pick_event', onpick)

    
    return chi2_sp, chi2_lc, name

def plot_gamma_parameters(bands_unique, variance_model):
    n = len(bands_unique)
    fig = pl.figure(figsize = (10, 8))
    gs = fig.add_gridspec(nrows= ceil(n/2), ncols=2)


    for i_bd in range(n):
        if i_bd < ceil(n/2):
            ax = fig.add_subplot(gs[i_bd,0])
        else :
            ax = fig.add_subplot(gs[i_bd-ceil(n/2),1])

        bd = bands_unique[i_bd].decode('UTF-8')
        XX = variance_model.pars[f'v_{bd}'].full
        a, b, c = pl.hist(XX, bins = 'auto')
        mm, ss = scipy.stats.norm.fit(XX)
        ax.text(mm, a.max(), r'$\mu = %.3f, \sigma = %.3f$' %(mm, ss))
        ax.set_title(bd)
        ax.grid(1)
    
    
def get_xdata_for_model_evaluation(nsn, tmax, bands, npoints=200):
    """
    """
    xdata = []
    block = np.zeros(npoints, dtype=[('date', float), ('sn', int), ('band', '|S13')])
    for sn in range(nsn):
        t = np.linspace(tmax[sn]-50., tmax[sn]+50., npoints)
        for band in bands:
            x = block.copy()
            x['sn'] = sn
            x['band'] = band
            x['date'] = t
            xdata.append(x)
    xdata = np.hstack(xdata)
    dp = DataProxy(xdata, date='date', sn='sn', band='band')
    dp.make_index('sn')
    dp.make_index('band')
    return dp







########################################################################################
############################### Model 2D ###############################################
########################################################################################

def plot_spline_B_model2D(m, leff = None, local = True):
    """                                                                         
    """
    X = m.basis.bx.grid
    I = m.basis.bx.eval(X)
    if local :
        if leff is None:
            leff = np.array([4650.])#m.filterset.mean_wavelength(['SWOPE::B'])
        else :
            leff = leff
        G = m.basis.by.eval(leff)

        mm = m.pars['M0'].full.reshape(m.basis.bx.nj,
                                       m.basis.by.nj)
        proj = I * mm * G.T
        pl.figure()
        pl.plot(X, proj, 'k.')
        pl.title(f'{leff}')
        pl.grid(1)
    else:
        G, Fz = m.get_fz(z = 0, band = np.array(['SWOPE::B']))
        mm = m.pars['M0'].full.reshape(m.basis.bx.nj,
                                       m.basis.by.nj)
        #try: 
        proj = (I * mm * Fz.T.squeeze()).sum(axis=1)
        #except :
        #    proj = I.dot(mm.dot(Fz.T.squeeze()))
        pl.figure()
        pl.plot(X, proj, 'k.')
        pl.title('SWOPE::B')
        pl.grid(1)

def plot_monochromatic_lc_model2D(lambda0, model):
    """
    """
    leff = np.array([lambda0])
    X = model.basis.bx.grid()
    I = model.basis.bx.eval(X).toarray()
    G = model.basis.by.eval(leff).toarray()
    JJ0 = np.outer(I.squeeze(),G.squeeze())
    #JJ = JJ0.reshape((len(model.pars['M0'].free)))#,len(model))

    pl.figure()
    pl.plot(X, JJ0 * model.pars['M0'].full, 'k.')
    pl.figure(str(lambda0))
    
    #self.H = coo_matrix(self.JJ).tocsr() 

def plot_param_recons_model2D(m, pars = []):#, norm = True, tmax = True, s= True):
    """
    """
    fig = pl.figure()
    if pars == []:
        pars = ['X0', 'tmax', 'X1', 'c', 'M0', 'M1', 'CL', 'rec_sp']

    res = (m.pars.free - m.pars0)/m.pars0 
    for i in range(len(pars)):
        pp = pars[i]
        ax = fig.add_subplot(2, 4, i+1)
        idx = m.pars[pp].indexof()
        if pp in ['M0', 'M1']:
            rr = res[idx][np.abs(res[idx]) < robuststat.mad(res[idx])*3]
        else :
            rr = res[idx]
        hist(ax, rr, title = pp, gauss = False)
        if i > 3:
            ax.set_xlabel(r'$\frac{p_{rec} - p_{imp}}{p_{imp}}$')


def plot_param_comparaison_model2D(m, m0):#, norm = True, tmax = True, s= True):
    """
    """
    fig = pl.figure()
    gs = fig.add_gridspec(2, 2)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    
    norm = (m.pars['X0'].full - m.snInfo['norm'])/m.snInfo['norm']#*100
    tmax = (m.pars['tmax'].full - m.snInfo['tmax'])/m.snInfo['tmax']#*100
    x1 = (m.pars['X1'].full - m.snInfo['sig'])/m.snInfo['sig']#*100
    c = (m.pars['c'].full - m.snInfo['c'])/m.snInfo['c']

    norm0 = (m0.pars['X0'].full - m0.snInfo['norm'])/m0.snInfo['norm']#*100
    tmax0 = (m0.pars['tmax'].full - m0.snInfo['tmax'])/m0.snInfo['tmax']#*100
    x10 = (m0.pars['X1'].full - m0.snInfo['sig'])/m0.snInfo['sig']#*100
    c0 = (m0.pars['c'].full - m0.snInfo['c'])/m0.snInfo['c']

    
    ax1.hist(norm, bins = 'auto', label = f" m : {norm.mean() : .5f},\n s : {norm.std() : .5f}")
    ax2.hist(tmax, bins = 'auto', label = f" m : {tmax.mean() : .5f},\n s : {tmax.std() : .5f}")
    ax3.hist(x1, bins = 'auto', label = f" m : {x1.mean() : .5f},\n s : {x1.std() : .5f}")
    ax4.hist(c, bins = 'auto', label = f" m : {c.mean() : .5f},\n s : {c.std() : .5f}")

    ax1.hist(norm0, bins = 'auto', label = f" m : {norm0.mean() : .5f},\n s : {norm0.std() : .5f}")
    ax2.hist(tmax0, bins = 'auto', label = f" m : {tmax0.mean() : .5f},\n s : {tmax0.std() : .5f}")
    ax3.hist(x10, bins = 'auto', label = f" m : {x10.mean() : .5f},\n s : {x10.std() : .5f}")
    ax4.hist(c0, bins = 'auto', label = f" m : {c0.mean() : .5f},\n s : {c0.std() : .5f}")
    
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()

    
    ax1.set_title('X0')
    ax2.set_title('tmax')
    ax3.set_title('X1')
    ax4.set_title('c')
    ax3.set_xlabel(r'$\frac{p_{rec} - p_{imp}}{p_{imp}}$')
    ax4.set_xlabel(r'$\frac{p_{rec} - p_{imp}}{p_{imp}}$')

    fig = pl.figure()
    ax = fig.gca(projection='3d')

    fig0 = pl.figure()
    ax0 = fig0.gca(projection='3d')
    
    X = np.linspace(m.basis.bx.range[0], m.basis.bx.range[1], m.basis.bx.nj)
    Y = np.linspace(m.basis.by.range[0], m.basis.by.range[1], m.basis.by.nj)
    X, Y = np.meshgrid(X, Y)
    nx = m.basis.bx.nj
    ny = m.basis.by.nj

    Z = m.basis.eval(x=X.ravel(), y = Y.ravel()) * m.pars['M0'].full.reshape(nx,ny).T.ravel()
    Z = Z.reshape(X.shape)
    Z0 = m.basis.eval(x=X.ravel(), y = Y.ravel()) * m0.pars['M0'].full.reshape(nx,ny).T.ravel()
    Z0 = Z0.reshape(X.shape)

    ZZ = m.basis.eval(x=X.ravel(), y = Y.ravel()) * m.pars['M1'].full.reshape(nx,ny).T.ravel()
    ZZ = ZZ.reshape(X.shape)
    ZZ0 = m.basis.eval(x=X.ravel(), y = Y.ravel()) * m0.pars['M1'].full.reshape(nx,ny).T.ravel()
    ZZ0 = ZZ0.reshape(X.shape)
    
    surf = ax.plot_surface(X, Y, Z-Z0, cmap = pl.cm.coolwarm,linewidth=0, antialiased=False)
    ax.set_xlabel('Phase')
    ax.set_ylabel('Wavelenght')
    ax.set_zlabel('Difference of M0')
    ax.text2D(0., 1., "mean spectral surface", transform=ax.transAxes)
    fig.colorbar(surf, shrink=0.5, aspect=5)

    surf0 = ax0.plot_surface(X, Y, ZZ-ZZ0, cmap = pl.cm.coolwarm, linewidth=0, antialiased=False)
    ax0.set_xlabel('Phase')
    ax0.set_ylabel('Wavelenght')
    ax0.set_zlabel('Difference of M1')
    ax0.text2D(0., 1., "first variability surface", transform=ax0.transAxes)
    fig0.colorbar(surf0, shrink=0.5, aspect=5)
    #pl.show()

    pl.figure()
    x = m.basis.by.grid
    y = m.CL(x, color = 1., p = m.pars)
    y = 1/0.4 * np.log10(y)
    pl.plot(x, y, 'b--')
    y0 = m0.CL(x, color = 1., p = m0.pars)
    y0 = 1/0.4 * np.log10(y0)
    pl.plot(x, y0, 'r--', label = 'with spectra recalibration')
    
    pl.hlines(0., x.min(), x.max(), color = 'r', ls ='--', alpha = 0.3)
    pl.hlines(1, x.min(), x.max(), color = 'r', ls ='--', alpha = 0.3)
    pl.vlines(m.CL.WAVELENGTH["B"], y.min(), y.max(), color = 'r', ls ='--', alpha = 0.3)
    pl.vlines(m.CL.WAVELENGTH["V"], y.min(), y.max(), color = 'r', ls ='--', alpha = 0.3)
    #pl.title(f'c = {c}')
    pl.xlabel(r'$\lambda$')
    pl.ylabel(r'$c \,  CL(\lambda)$')
    pl.grid()
    pl.legend()
    return m, m0



########################################################################################
################################### End Model 2D #######################################


def array_lc_model2D(model, sn_id, band, variance_model=None):
    """
    Return evaluated model, data and evaluated model on large phase range 
    for plotting a ligth curves.
    if variance model, return variance model total and part off additional model.
    """
    lc = DataProxy(model.training_dataset.lc_data, date='Date', flux='Flux',
                   flux_err='FluxErr',wavelength = 'Wavelength',
		   band='Filter', magsys='MagSys',
                   sn='id', zhelio= 'ZHelio', obs_id = 'obs_id')

    idx = (lc.sn == sn_id) & (lc.band == band) 
    #lc = lc.nt[idx]
    lc = DataProxy(lc, date='Date',flux='Flux',flux_err='FluxErr',sn='id',
                   wavelength='Wavelength',band='Filter',zhelio= 'ZHelio',obs_id='obs_id')
    dp_fit = create_array(d = lc.date, z = lc.zhelio[0], sn_id = sn_id, band = band, N = 100)
    dp_lc = create_array(d = lc.date, z = lc.zhelio[0], sn_id = sn_id, band = band, N = None)

    val_fit = model(model.pars.free, data = dp_fit, only_lc = True)
    val_lc = model(model.pars.free, data = dp_lc, only_lc = True)
    dp_fit.flux = val_fit
    dp_lc.flux = val_lc
    dp_fit.nt['Flux'] = val_fit
    dp_lc.nt['Flux'] = val_lc 
    dp_lc.nt['FluxErr'] = lc.flux_err
    print(dp_lc.flux_err)
    dp_lc.flux_err = lc.flux_err
    print(dp_lc.flux_err)
    if variance_model is not None:
        sig = variance_model(variance_model.pars.free, model.pars.free, data = dp_lc)

        sig_x = np.sqrt(sig - lc.flux_err**2)
        sig = np.sqrt(sig)

        sig_fit = variance_model(variance_model.pars.free, model.pars.free, data = dp_fit)
        #sig_x_fit = np.sqrt(sig_fit - dp_fit.flux_err**2)
        sig_fit = np.sqrt(sig_fit)

    lc.date = (lc.date - model.pars['tmax'].full[sn_id]) /(1 + lc.zhelio[0])
    dp_fit.date = (dp_fit.date - model.pars['tmax'].full[sn_id]) /(1 + lc.zhelio[0])
    dp_lc.date = (dp_lc.date - model.pars['tmax'].full[sn_id]) /(1 + lc.zhelio[0])
    if variance_model is not None:
        return lc, dp_lc, dp_fit, sig, sig_x, sig_fit#, sig_x_fit
    return lc, dp_lc, dp_fit


def array_sp_model2D(model, obs_id, variance_model=None):
    """
    Return evaluated model and data for plotting a spectra.
    if variance model, return variance model total.
    """
    sp = DataProxy(model.training_dataset.spec_data, date='Date', flux='Flux',
                   flux_err='FluxErr',wavelength = 'Wavelength',
		   band='Filter', magsys='MagSys',
                   sn='id', zhelio= 'ZHelio', obs_id = 'obs_id')

    idx = sp.obs_id == obs_id
    dp_sp = DataProxy(sp.nt[idx], date='Date', flux='Flux',flux_err='FluxErr',sn='id',
                      wavelength='Wavelength',band='Filter', zhelio= 'ZHelio', obs_id='obs_id')    
    
    val = model(model.pars.free, data = dp_sp)
    
    if variance_model is not None:
        sig = variance_model(variance_model.pars.free, model.pars.free, data = dp_sp)
        sig_x = np.sqrt(sig - dp_sp.flux_err**2)
        sig = np.sqrt(sig)

    dp_sp.date = (dp_sp.date - model.pars['tmax'].full[dp_sp.sn[0]]) /(1 + dp_sp.zhelio[0])
    dp_sp.wavelength /=(1 + dp_sp.zhelio[0])
    if variance_model is not None:
        return dp_sp,  val, sig, sig_x
    return dp_sp,  val

def plot_SNparameters_bias_res(m, D, pull = False):
    """
    M is the hessian
    D = np.sqrt(np.diag(scipy.linalg.inv(M.todense())))
    """
    z = m.training_dataset.sne['z']
    dist_pars = m.pars.full - m.pars0
    cr = m.training_dataset.sne['c']
    x1r = m.training_dataset.sne['x1']
    x0r = m.training_dataset.sne['x0']
    tmaxr = m.training_dataset.sne['tmax']

    idxx0 = m.pars.indexof('X0')
    idxx1 = m.pars.indexof('X1')
    idxc = m.pars.indexof('c')
    idxtmax = m.pars.indexof('tmax')

    biai_x0 = dist_pars[idxx0]
    biai_x1 = dist_pars[idxx1]
    biai_c = dist_pars[idxc]
    biai_tmax = dist_pars[idxtmax]
    
    #c_offset = c.mean()
    #x1_offset = x1.mean()
    #dist_pars[m.pars.indexof('c')] += c_offset
    #dist_pars[m.pars.indexof('X1')] += x1_offset

    addname = ''
    if pull :
        dist_pars /= D[:len(dist_pars)]
        addname = '/err'
    
    x0 = m.pars.full[idxx0]
    x1 = m.pars.full[idxx1]
    c = m.pars.full[idxc]
    tmax = m.pars.full[idxtmax]

    x0_err = D[idxx0]
    tmax_err = D[idxtmax]
    x1_err = D[idxx1]
    c_err = D[idxc]

    fig = pl.figure()
    gs = pl.matplotlib.gridspec.GridSpec(2, 4, height_ratios=[4, 1])

    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])

    ax1.plot(z, x0r, 'k.')
    ax1.errorbar(z, x0, yerr=x0_err, ls = '', marker = '.')
    ax1.set_title('x0')
    ax2.plot(z, x1r, 'k.')
    ax2.errorbar(z, x1, yerr=x1_err, ls = '', marker = '.')
    ax2.set_title('x1')
    ax3.plot(z, cr, 'k.')
    ax3.errorbar(z, c, yerr=c_err, ls = '', marker = '.')
    ax3.set_title('c')
    ax4.plot(z, tmaxr, 'k.')
    ax4.errorbar(z, tmax, yerr=tmax_err, ls = '', marker = '.')
    ax4.set_title('tmax')
    
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)
    ax5 = fig.add_subplot(gs[4])
    ax5.errorbar(z, biai_x0, yerr=x0_err, ls = '', marker = '.')
    binplot(z, biai_x0, data = False, marker = '.', markersize=5, color = 'r')
    ax5.grid(True)
    ax5.set_xlabel('z')
    
    ax6 = fig.add_subplot(gs[5])
    ax6.errorbar(z, biai_x1, yerr=x1_err, ls = '', marker = '.')
    binplot(z, biai_x1, data = False, marker = '.', markersize=5, color = 'r')
    ax6.grid(True)
    ax6.set_xlabel('z')
        
    ax7 = fig.add_subplot(gs[6])
    ax7.errorbar(z, biai_c, yerr=c_err, ls = '', marker = '.')
    ax7.grid(1)
    binplot(z, biai_c, data = False, marker = '.', markersize=5, color = 'r')
    ax7.set_xlabel('z')
    
    ax8 = fig.add_subplot(gs[7])
    ax8.errorbar(z, biai_tmax, yerr=tmax_err, ls = '', marker = '.')
    ax8.grid(1)
    binplot(z, biai_tmax, data = False, marker = '.', markersize=5, color = 'r')
    ax8.set_xlabel('z')



def plot_SNparameters_bias_with_error(m, D, name = 'jla', pull = False):
    """
    M is the hessian
    D = np.sqrt(np.diag(scipy.linalg.inv(M.todense())))
    """
    dist_pars = m.pars.full - m.pars0
    c = m.training_dataset.sne['c']
    x1 = m.training_dataset.sne['x1']
    x0 = m.training_dataset.sne['x0']
    tmax =m.training_dataset.sne['tmax']

    c_offset = c.mean()
    x1_offset = x1.mean()
    dist_pars[m.pars.indexof('c')] += c_offset
    dist_pars[m.pars.indexof('X1')] += x1_offset

    addname = ''
    if pull :
        dist_pars /= D[:len(dist_pars)]
        addname = '/err'
    
    biai_x0 = dist_pars[m.pars.indexof('X0')]
    biai_x1 = dist_pars[m.pars.indexof('X1')]
    biai_c = dist_pars[m.pars.indexof('c')]
    biai_tmax = dist_pars[m.pars.indexof('tmax')]

    x0_err = D[m.pars.indexof('X0')]
    tmax_err = D[m.pars.indexof('tmax')]
    x1_err = D[m.pars.indexof('X1')]
    c_err = D[m.pars.indexof('c')]
    
    cmap = pl.matplotlib.cm.jet #get_cmap('cividis')
    norm = pl.matplotlib.colors.Normalize(vmin=-0.5, vmax=0.5)

    EW = 0.75
    AL = 0.75
    
    fig, axes = pl.subplots(4,4, constrained_layout=True, figsize=(15,15))#, sharex=True)
    [[ax1, ax2,ax3, ax4], [ax5, ax6,ax7, ax8],
          [ax9, ax10, ax11, ax12], [ax13, ax14,ax15, ax16]] = axes
    pl.title(name)
    #ax1.hist(biai_x0, bins = 500, orientation='horizontal',
    #         label = f'm : {biai_x0.mean() : 0.3}, s : {biai_x0.std() : 0.3}')
    hist(ax1, biai_x0, bins = 500, orientation='horizontal',
             )#label = f'm : {biai_x0.mean() : 0.3}, s : {biai_x0.std() : 0.3}')
    ax1.legend()

    ax2.errorbar(biai_tmax, biai_x0, yerr = x0_err,#np.sqrt(x0_err),
                 xerr = tmax_err,#np.sqrt(tmax_err),
                 marker = '', ls = '', ecolor = cmap(norm(c)),
                 elinewidth = EW, alpha = AL) 
    ax2.scatter(biai_tmax,biai_x0, c= cmap(norm(c)), s = 5)
    ax2.set_ylabel('x0_rec - x0_gen'+addname)
    ax2.set_xlabel('tmax_rec - tmax_gen'+addname)
    ax2.grid(1)
    ax3.errorbar(biai_c, biai_x0, xerr = c_err,#np.sqrt(c_err),
                 yerr = x0_err,#np.sqrt(x0_err),
                 marker = '', ls = '', ecolor = cmap(norm(c)),
                 elinewidth = EW, alpha = AL) 
    ax3.scatter(biai_c,biai_x0, c= cmap(norm(c)), s = 5)
    ax3.set_ylabel('x0_rec - x0_gen'+addname)
    ax3.set_xlabel('c_rec - c_gen'+addname)
    ax3.grid(1)

    ax4.errorbar(biai_x1, biai_x0, xerr = x1_err,#np.sqrt(x1_err),
                 yerr = x0_err,#np.sqrt(x0_err),
                 marker = '', ls = '', ecolor = cmap(norm(c)),
                 elinewidth = EW, alpha = AL)#,color=cmap(norm(c)))
    ax4.scatter(biai_x1,biai_x0, c= cmap(norm(c)), s = 5)
    ax4.set_xlabel('x1_rec - x1_gen'+addname)
    ax4.set_ylabel('x0_rec - x0_gen'+addname)
    ax4.grid(1)

    hist(ax6, biai_tmax, bins = 30)#, label = f'm : {biai_tmax.mean():0.3}, s : {biai_tmax.std():0.3}')
    #ax6.hist(biai_tmax, bins = 30, label = f'm : {biai_tmax.mean():0.3}, s : {biai_tmax.std():0.3}')
    ax6.legend()
    ax8.errorbar(biai_x1,biai_tmax,  xerr = x1_err,#np.sqrt(x1_err),
                 yerr = tmax_err,#np.sqrt(tmax_err),
                 marker = '', ls = '', ecolor = cmap(norm(c)),
                 elinewidth = EW, alpha = AL)#, color = cmap(norm(c)))
    ax8.scatter(biai_x1,biai_tmax, c= cmap(norm(c)), s = 5)
    ax8.set_ylabel('tmax_rec - tmax_gen'+addname)
    ax8.set_xlabel('x1_rec - x1_gen'+addname)
    ax8.grid(1)

    ax7.errorbar(biai_c, biai_tmax, xerr = c_err,#np.sqrt(c_err),
                 yerr = tmax_err,#np.sqrt(tmax_err),
                 marker = '', ls = '', ecolor = cmap(norm(c)),
                 elinewidth = EW, alpha = AL)
    ax7.scatter(biai_c,biai_tmax, c= cmap(norm(c)), s = 5)
    ax7.set_xlabel('c_rec - c_gen'+addname)
    ax7.set_ylabel('tmax_rec - tmax_gen'+addname)
    ax7.grid(1)

    #ax11.hist(biai_c, bins = 30, label = f'm : {biai_c.mean() : 0.3}, s : {biai_c.std() : 0.3}')
    hist(ax11, biai_c, bins = 30)#, label = f'm : {biai_c.mean() : 0.3}, s : {biai_c.std() : 0.3}')
    ax11.legend()

    hist(ax16, biai_x1, bins = 30)#, label = f'm : {biai_x1.mean() : 0.3}, s : {biai_x1.std() : 0.3}')
    #    ax16.hist(biai_x1, bins = 30, label = f'm : {biai_x1.mean() : 0.3}, s : {biai_x1.std() : 0.3}')
    ax16.legend()
    ax12.errorbar(biai_x1, biai_c,  yerr = c_err,#np.sqrt(c_err),
                  xerr = x1_err,#np.sqrt(x1_err),
                  marker = '', ls = '', ecolor = cmap(norm(c)),
                  elinewidth = EW, alpha = AL)#,color=cmap(norm(c)))
    im = ax12.scatter(biai_x1, biai_c, c= cmap(norm(c)), s = 5)
    ax12.set_ylabel('c_rec - c_gen'+addname)
    ax12.set_xlabel('x1_rec - x1_gen'+addname)
    ax12.grid(1)

    from matplotlib.cm import ScalarMappable
    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])

    cbar = fig.colorbar(sm, ax=axes[:,1])
    cbar.ax.set_title("color")

    ax1.sharey(ax2)
    ax2.sharey(ax4)
    ax3.sharey(ax4)
    ax2.sharex(ax6)
    ax4.sharex(ax8)
    ax8.sharex(ax12)
    ax12.sharex(ax16)
    ax3.sharex(ax7)
    ax7.sharex(ax11)

    
    # x0_err = np.sqrt(x0_err)
    # tmax_err = np.sqrt(tmax_err)
    # x1_err = np.sqrt(x1_err)
    # c_err=np.sqrt(c_err)
    # np.savez(f'{name}_bias.npz', biai_x0=biai_x0, biai_tmax=biai_tmax,
    #          biai_x1=biai_x1, biai_c=biai_c,
    #          x0_err=x0_err, tmax_err=tmax_err, x1_err=x1_err, c_err=c_err,
    #          c=c, tmax=tmax, x1 = x1, x0=x0)


    # import pandas as pd
    # import seaborn as sns
    
    # dist_pars = dist_pars/D[:len(dist_pars)]
    
    # biai_x0 = dist_pars[m.pars.indexof('X0')]
    # biai_x1 = dist_pars[m.pars.indexof('X1')]
    # biai_c = dist_pars[m.pars.indexof('c')]
    # biai_tmax = dist_pars[m.pars.indexof('tmax')]

    # df=pd.DataFrame(np.array([biai_x0,biai_tmax,biai_c,biai_x1]).T, columns=['x0', 'tmax', 'c', 'x1'])
    # sns.pairplot(df)
    # # return df



def plot_model_control(model, p0, p1):
    """
    """

    model.pars.free = p0
    X, Y, Z0_M0 = model.plotsurface('M0',  plot =False)
    X, Y, Z0_M1 = model.plotsurface('M1',  plot =False)

    model.pars.free = p1
    X, Y, Z1_M0= model.plotsurface('M0',  plot =False)
    X, Y, Z1_M1= model.plotsurface('M1',  plot =False)

    fig = pl.figure()
    z0 = Z0_M0/Z1_M0
    extent = np.min(X), np.max(X), np.min(Y), np.max(Y)
    ax = fig.add_subplot(111)
    pl.imshow(z0, origin="lower", extent = extent, aspect = 'auto', vmin = 0.8, vmax = 1.2)
    ax.set_title(f'M0')
    pl.colorbar()
    ax.set_xlabel('Phase')
    ax.set_ylabel('Wavelenght')
    pl.show()

    fig = pl.figure()
    z1 = Z0_M1/Z1_M1
    extent = np.min(X), np.max(X), np.min(Y), np.max(Y)
    ax = fig.add_subplot(111)
    pl.imshow(z1, origin="lower", extent = extent, aspect = 'auto', vmin = 0.5, vmax = 1.5)
    ax.set_title(f'M1')
    pl.colorbar()
    ax.set_xlabel('Phase')
    ax.set_ylabel('Wavelenght')
    pl.show()

    xx = model.basis.by.grid
    model.pars.free = p0
    y0 = model.CL(xx, 1.0, p = model.pars)
    model.pars.free = p1
    y1 = model.CL(xx, 1.0, p = model.pars)

    fig = pl.figure()
    ax = pl.subplot(111)
    ax.grid()
    ax.set_xlabel(r'$\lambda$')
    ax.set_ylabel('CL(c = 1, pars = y0) - CL(c = 1, pars = y1)')
    ax.plot(xx, y0-y1, 'b-')
    pl.show()

    idx_x0 = model.pars['X0'].indexof()
    idx_c = model.pars['c'].indexof()
    idx_x1 = model.pars['X1'].indexof()

    dp = p0 - p1
    
    fig = pl.figure()
    gs = fig.add_gridspec(3,1)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0])
    axc = fig.add_subplot(gs[2, 0])

    ax0.plot(model.z, p0[idx_x0]/p1[idx_x0], 'k.', label = 'X0_p0/X0_p1')
    ax0.grid(1)
    ax0.legend()

    ax1.plot(model.z, dp[idx_x1], 'k.', label = 'X1_p0 - X1_p1')
    ax1.grid(1)
    ax1.legend()

    axc.plot(model.z, dp[idx_c], 'k.', label = 'c_p0 - c_p1')
    axc.grid(1)
    axc.legend()
    fig.show()

    MB = -19.0906
    ALPHA = 0.13
    BETA = 3.0

    mb0 = -2.5 * np.log(p0[idx_x0])
    mu0 = mb0 - MB + ALPHA * p0[idx_x1] - BETA * p0[idx_c]

    mb1 = -2.5 * np.log(p1[idx_x0])
    mu1 = mb1 - MB + ALPHA * p1[idx_x1] - BETA * p1[idx_c]

    fig = pl.figure(constrained_layout=True)
    gs = fig.add_gridspec(4,1)
    f0 = fig.add_subplot(gs[:3, 0])
    f1 = fig.add_subplot(gs[3, 0])

    f0.plot(model.z, mu0, label = 'mu(p0)', color = 'r', ls = '', marker = '.')
    f0.plot(model.z, mu1, label = 'mu(p1)', color = 'b', ls = '', marker = '.')
    f0.grid(1)
    f0.set_ylabel(r'$\mu = m_b - M_b + \alpha * x1 - \beta * c$') 
    f0.legend()

    f1.plot(model.z, mu1-mu0, label = 'mu(p1)-mu(p0)', color = 'k', ls = '', marker = '.')
    f1.grid(1)
    f1.set_xlabel('z')
    f1.set_ylabel('mu(p1)-mu(p0)')
    f1.legend()


    
    fig = pl.figure()
    gs = fig.add_gridspec(4,2)
    ax0 = fig.add_subplot(gs[:3, 0])
    ax5 = fig.add_subplot(gs[:3,1])
    
    res0 = fig.add_subplot(gs[3, 0])
    res5 = fig.add_subplot(gs[3, 1])
    
    wl = np.linspace(2000, 8999, 500)
    phase0 = np.zeros_like(wl)
    phase5 = phase0.copy() + 5
    idx_m0 = model.pars.indexof('M0')
    splines0 = model.basis.eval(phase0,wl)
    splines5 = model.basis.eval(phase5,wl)

    sp0_x0 = splines0 @ p0[idx_m0].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()
    sp0_x1 = splines0 @ p1[idx_m0].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()

    sp5_x0 = splines5 @ p0[idx_m0].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()
    sp5_x1 = splines5 @ p1[idx_m0].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()

    ax0.set_title('M0 cut phase = 0')
    ax5.set_title('M0 cut phase = 5')

    ax0.set_xlabel(r'$\lambda$')
    ax5.set_xlabel(r'$\lambda$')
    ax0.set_ylabel(r'S($\lambda$, p)')

    ax0.plot(wl, sp0_x0, color = 'r', label = 'spectra from p0')
    ax0.plot(wl, sp0_x1, color = 'b', label = 'spectra from p1')

    ax5.plot(wl, sp5_x0, color = 'r', label = 'spectra from p0')
    ax5.plot(wl, sp5_x1, color = 'b', label = 'spectra from p1')

    res0.plot(wl, sp0_x0/sp0_x1, 'k--')
    res5.plot(wl, sp5_x0/sp5_x1, 'k--')
    ax5.grid()
    res5.grid()
    res0.grid()
    ax0.grid()
    res5.set_ylim(0.5, 1.5)
    res0.set_ylim(0.5, 1.5)
    res5.set_xlabel(r'$\lambda$')
    res0.set_xlabel(r'$\lambda$')
    res0.set_ylabel(r'sp_p0 / sp0_p1')


    
    fig = pl.figure()
    gs = fig.add_gridspec(4,2)
    ax0 = fig.add_subplot(gs[:3, 0])
    ax5 = fig.add_subplot(gs[:3,1])
    
    res0 = fig.add_subplot(gs[3, 0])
    res5 = fig.add_subplot(gs[3, 1])
    
    idx_m1 = model.pars.indexof('M1')
    
    sp0_x0 = splines0 @ p0[idx_m1].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()
    sp0_x1 = splines0 @ p1[idx_m1].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()

    sp5_x0 = splines5 @ p0[idx_m1].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()
    sp5_x1 = splines5 @ p1[idx_m1].reshape(model.basis.bx.nj, model.basis.by.nj).T.ravel()

    ax0.set_title('M1 cut phase = 0')
    ax5.set_title('M1 cut phase = 5')

    ax0.set_xlabel(r'$\lambda$')
    ax5.set_xlabel(r'$\lambda$')
    ax0.set_ylabel(r'S($\lambda$, p)')

    ax0.plot(wl, sp0_x0, color = 'r', label = 'spectra from p0')
    ax0.plot(wl, sp0_x1, color = 'b', label = 'spectra from p1')

    ax5.plot(wl, sp5_x0, color = 'r', label = 'spectra from p0')
    ax5.plot(wl, sp5_x1, color = 'b', label = 'spectra from p1')

    res0.plot(wl, sp0_x0/sp0_x1, 'k--')
    res5.plot(wl, sp5_x0/sp5_x1, 'k--')
    ax5.grid()
    res5.grid()
    res0.grid()
    ax0.grid()
    res5.set_ylim(0.5, 1.5)
    res0.set_ylim(0.5, 1.5)
    res5.set_xlabel(r'$\lambda$')
    res0.set_xlabel(r'$\lambda$')
    res0.set_ylabel(r'sp_p0 / sp0_p1')

    
allbands = ['SWOPE::u',
            '4SHOOTER2::Us',
            'KEPLERCAM::Us',
            'STANDARD::U',
            'SWOPE2::u',
            'SDSS::u', 
            'K21::Bessell-U/U',
            'K21::CFA3K-U/f',
            'K21::CFA3S-U/a',
            'K21::CSP-u/t',
            'K21::SDSS-u',
            'LSST::u',
            
            'SWOPE::B',
            '4SHOOTER2::B',
            'KEPLERCAM::B',
            'STANDARD::B',
            'SWOPE2::B',
            'K21::Bessell-B/B',
            'K21::CFA3K-B/h',
            'K21::CFA3S-B/b',
            'K21::CFA41-B',
            'K21::CSP-B/v'
            'K21::CSP-B/u',
            
         
            'MEGACAMPSF::g',
            'SDSS::g',
            'K21::CSP-g/A',
            'K21::CSP-g/y',
            'K21::DES-g',
            'K21::PS1-g',
            'K21::SDSS-g',
            'K21::SNLS-g',
            'LSST::g',
            
            'SWOPE::V',
            '4SHOOTER2::V',
            'KEPLERCAM::V',
            'STANDARD::V',
            'SWOPE2::V',
            'K21::Bessell-V/V',
            'K21::CFA3K-V/j',
            'K21::CFA3S-V/c',
            'K21::CFA41-V',
            'K21::CSP-m/w',
            'K21::CSP-n/x',
            'K21::CSP-o/v',
            'K21::CSP-o/y',

            'LSST::r',
            'MEGACAMPSF::r',
            'SWOPE::r',
            'SDSS::r',
            'SWOPE2::r',
            'KEPLERCAM::r',
            'K21::CFA3K-r/k',
            'K21::CFA41-r',
            'K21::CSP-r/B',
            'K21::CSP-r/z',
            'K21::DES-r',
            'K21::PS1-r',
            'K21::SDSS-r',
            'K21::SNLS-r',
            
            
            '4SHOOTER2::R',
            'STANDARD::R',
            'K21::Bessell-R/R',
            'K21::CFA3S-R/d',
            
            'KEPLERCAM::i',
            'MEGACAMPSF::i',
            'SDSS::i',
            'SWOPE2::i',
            'K21::CFA3K-i/l',
            'K21::CFA41-i',
            'K21::CSP-i/A',
            'K21::CSP-i/C',
            'K21::DES-i',
            'K21::PS1-i',
            'K21::SDSS-i',
            'K21::SNLS-i',
            'LSST::i',
            
            '4SHOOTER2::I',
            'STANDARD::I',
            'K21::Bessell-I/I',
            'K21::CFA3S-I/e',
            
            'SDSS::z',
            'K21::DES-z',
            'K21::PS1-z',
            'K21::SDSS-z',
            'K21::SNLS-z',
            'LSST::z',
            'MEGACAMPSF::z']

colors = iter(cm.jet(np.linspace(0, 1, len(allbands))))
dict_color = {}
for bd in allbands:
    dict_color[bd] = next(colors)


    
def plot_all_lcsp_model2D(model, sn, variance_model = None, name = None):
    """
    """

    sp = DataProxy(model.training_dataset.spec_data, date='Date', flux='Flux',
                   flux_err='FluxErr',wavelength = 'Wavelength',
		   band='Filter', magsys='MagSys',
                   sn_id='sn_id', sp_id = 'spec_id', lc_id='lc_id',
                   zhelio= 'ZHelio')

    lc = DataProxy(model.training_dataset.lc_data, date='Date', flux='Flux',
                   flux_err='FluxErr',wavelength = 'Wavelength',
		   band='Filter', magsys='MagSys',
                   sn_id='sn_id', sp_id = 'spec_id', lc_id='lc_id',
                   zhelio= 'ZHelio')

    
    fig = pl.figure() 
    obs_id = np.unique(sp.sp_id[sp.sn_id == sn])
    if len(obs_id) == 0:
        gs = fig.add_gridspec(nrows= 4, ncols=1)
        pllc = fig.add_subplot(gs[:3,0])
        reslc = fig.add_subplot(gs[3,0])
            
    else:
        gs = fig.add_gridspec(nrows= 4, ncols=2)

        plsp = fig.add_subplot(gs[:3,0])
        ressp = fig.add_subplot(gs[3,0], sharex = plsp)
       
        pllc = fig.add_subplot(gs[:3,1])
        reslc = fig.add_subplot(gs[3,1], sharex = pllc)
        
        
        fm = [sp.flux[sp.sp_id == oi].max() for oi in obs_id]
        idx = np.array(fm).argsort()
        
        colors = iter(cm.jet(np.linspace(0, 1, len(obs_id))))
        compt = 0
        for i in range(len(obs_id)):
            oi = obs_id[idx][i]
            sp0 = sp.nt[sp.sp_id == oi]
            # if variance_model is not None:
            #     d = array_sp_model2D(model, oi,
            #                          variance_model = variance_model)
            # else:
            #     d = array_sp_model2D(model, oi)
            if variance_model is not None:
                restframe_wl, flux, val0, sigsp = plot_spec(model, oi,
                                                            variance_model=variance_model,
                                                            plot=False)
            else:
                restframe_wl, flux, val0, sigsp = plot_spec(model, oi,
                                                            variance_model=False,
                                                            plot=False)

            date = sp0['Date'][0]/(1+sp0[0]['ZHelio']) #d[0].date[0]
            c = next(colors)
                
            nf = 1
            plsp.plot(restframe_wl, (compt + flux)/nf, ls = '-', color = c, lw = 1.)
            plsp.errorbar(restframe_wl, (compt + sp0['Flux'])/nf,
                        yerr = (sp0['FluxErr'])/nf,
                        marker = '.', ls = '', markersize=3,
                        elinewidth=0.5,label = f'phase : {date :.3}',
                        color = c, alpha = 0.5)
            if variance_model is not None:
                plsp.plot(restframe_wl, (compt + flux + sigsp)/nf, ls = '-',
                        color = c, lw = 0.5, alpha = 0.5)
                plsp.plot(restframe_wl, (compt + flux - sigsp)/nf, ls = '-',
                color = c, lw = 0.5, alpha = 0.5)
                plsp.fill_between(restframe_wl,
                                (compt + flux + sigsp)/nf,
                                (compt + flux - sigsp)/nf, color = c, alpha=0.25)
                
            compt += sp0['Flux'].mean()/4*3
            plsp.set_ylabel('Flux + offset')
            plsp.set_title(f'Spectra')
            #sp.set_xlabel(r'Wavelength ($\AA$)')
            plsp.grid(1)
            plsp.legend(loc = 'upper right')

            ressp.errorbar(restframe_wl, (sp0['Flux'] - flux),
                        yerr = (sp0['FluxErr']),
                        marker = '.', ls = '', markersize=3,
                        elinewidth=0.5, #label = f'phase : {date :.3}',
                        color = c, alpha = 0.5)
            if variance_model is not None:
                ressp.plot(restframe_wl, sigsp, ls = '-',
                        color = c, lw = 0.5, alpha = 0.5)
                ressp.plot(restframe_wl, -sigsp, ls = '-',
                           color = c, lw = 0.5, alpha = 0.5)
                ressp.fill_between(restframe_wl, +sigsp, -sigsp, color = c, alpha=0.25)
            ressp.set_ylabel('Residuals')
            ressp.set_xlabel(r'Wavelength ($\AA$)')
            ressp.grid(1)
            #sp.legend()

            

            
    compt = 0
    bands = np.unique(lc.band[lc.sn_id == sn])
    lc_id = np.unique(lc.lc_id[lc.sn_id == sn])
    bds = np.array([i.decode('UTF-8') for i in bands])
    idx = np.array([np.where(np.array(allbands) == i) for i in bds]).squeeze()
    bands = bands[idx.argsort()]

        
    for ilc in lc_id:
        i = lc.band[lc.lc_id ==ilc ]
        #bd = i.decode('UTF-8')
        bd = i.astype('str')[0]
        c = dict_color[bd]
        lc0 = lc.nt[lc.lc_id == ilc] 
        # if variance_model is not None:
        #     d = array_lc_model2D(model, sn, i, variance_model = variance_model)
        # else:
        #     d = array_lc_model2D(model, sn, i)
        if variance_model : 
            phase, val, siglc, phase100, flux100, siglc100 = plot_lc(model,ilc,
                                                                     variance_model=variance_model,
                                                                     plot=False)
        else:
            phase, val, siglc, phase100, flux100, siglc100 = plot_lc(model,ilc,
                                                                     variance_model=False,
                                                                     plot=False)
        
        pllc.plot(phase100, compt + flux100, ls = '-', color = c, lw = 0.5)
        pllc.errorbar(phase, compt + lc0['Flux'], yerr = lc0['FluxErr'], marker = '.',
                    ls = '', label = bd, color = c)
        if variance_model is not None:
            pllc.plot(phase100, compt + flux100 + siglc100, ls = '-', color = c, lw = 0.5, alpha = 0.5)
            pllc.plot(phase100, compt + flux100 - siglc100, ls = '-', color = c, lw = 0.5, alpha = 0.5)
            pllc.fill_between(phase100,
                            compt + flux100 + siglc100,
                            compt + flux100 - siglc100, color = c, alpha=0.25)

        pllc.set_ylabel('Flux + offset')
        pllc.set_title(f'Light curves')
        pllc.grid(1)
        pllc.legend()
        
        reslc.errorbar(phase, (lc0['Flux'] - val),
                       yerr = (lc0['FluxErr']),
                       marker = '.', ls = '', markersize=10,
                       elinewidth=1.5, #label = f'phase : {date :.3}',
                       color = c, alpha = 0.5)
        if variance_model is not None:
            reslc.plot(phase100, siglc100, ls = '-',
                       color = c, lw = 1.5, alpha = 0.5)
            reslc.plot(phase100, - siglc100, ls = '-',
                       color = c, lw = 1.5, alpha = 0.5)
            reslc.fill_between(phase100, + siglc100, -siglc100, color = c, alpha=0.25)
        reslc.set_ylabel('Residuals')
        reslc.set_xlabel(r'Phase (days)')
        reslc.grid(1)
        
        compt += lc0['Flux'].max()/4*3


    fig.suptitle(f"z : {lc0['ZHelio'][0] : .3}")
    if name is not None:
        fig.suptitle(name + f' z : {lc0["ZHelio"][0] : .3}')    
    return fig

    
def plot_distance_bias(m, M, ALPHA = 0.13 , beta =30, MB = -19.0906, pull = False,
                       return_biai=False, give_inv =False, add_gen_limits=False,
                       figsize = (10,10), dpi = 100):
    """
    M is the hessian
    M = np.diag(scipy.linalg.inv(M.todense())))
    """
    z = m.training_dataset.sne['z']
    idxz = z.argsort()
    mm = m.pars.full[:].copy()
    dist_pars = m.pars.full - m.pars0
    

    idxx0 = m.pars.indexof('X0')
    idxx1 = m.pars.indexof('X1')
    idxc = m.pars.indexof('c')

    cr = m.training_dataset.sne['c']    #[idxz]
    x1r = m.training_dataset.sne['x1']  #[idxz]
    x0r = m.training_dataset.sne['x0']  #[idxz]

    x0 = m.pars.full[idxx0]  #[idxz]
    x1 = m.pars.full[idxx1]  #[idxz]
    c = m.pars.full[idxc]    #[idxz]


    if give_inv :
        invM = M.todense().copy()
    else :
        M = 1/2 * M
        invM = scipy.linalg.inv(M.todense())
        
        
    import nacl.distance as distance
    distances = distance.DistancesModulus(m)
    z, mu, mu_err, cov, invM = distances.propagated_error(invM, give_inv=True)
           
    #z, mu, mu_err, cov = distance.calculate_distance_modulus(m, M, plot=False, return_dist=True, give_inv=give_inv)
    #m.pars.full[:] = m.pars0
    distances.model.pars.full[:] = m.pars0
    z, mur, mur_err, covr, invM = distances.propagated_error(invM, give_inv=True)
    
    #z, mur, mur_err, covr = distance.calculate_distance_modulus(m, M, plot=False, return_dist=True, give_inv=give_inv)
    #m.pars.full[:] = mm


    
    D = np.sqrt(np.diag(invM))
    x0_err = D[idxx0]
    x1_err = D[idxx1]
    c_err = D[idxc]

    parameters = {'axes.labelsize': 15,
                  'axes.titlesize': 15}
    pl.rcParams.update(parameters)
    
    fig = pl.figure(figsize=figsize, dpi = dpi)
    gs = pl.matplotlib.gridspec.GridSpec(4, 2, width_ratios=[4, 1])


    dmb, dx1, dc, dmu = -2.5 * np.log10(x0r) + 2.5 * np.log10(x0), x1r-x1, cr-c, mur-mu
    
    # calcul erreure de X0 sur mB
    nsn = len(x0)
    i, j, v = [], [], []
    dmb_dx0 = 2.5 * 1/(x0* np.log(10))
    i = np.arange(nsn)
    j = idxx0
    v = dmb_dx0
    Jmb = scipy.sparse.coo_matrix((v, (i,j)), shape=(nsn,nsn))
    Cmb = invM[:nsn, :nsn]
    mb_err = np.sqrt(np.diag(Jmb @ Cmb @ Jmb))


    dmb, dx1, dc, dmu =  dmb[idxz], dx1[idxz], dc[idxz], dmu[idxz]
    mb_err, x1_err, c_err, mu_err = mb_err[idxz], x1_err[idxz], c_err[idxz], mu_err[idxz]
    z = z[idxz]
    
    colors = iter(pl.matplotlib.cm.Blues(np.linspace(0.5, 1, 4)))
    markersize = 15
    maker = 'o'
    alpha = 0.3

    bincolor = 'DarkRed'
    
    c = next(colors)
    ax1 = fig.add_subplot(gs[0])
    ax1.errorbar(z, dmb, yerr=mb_err, ls = '', marker =maker, alpha=alpha, color=c)
    ax1.set_ylabel(r'$\Delta m_B^{\star}$')
    binplot(z, dmb, data = False, marker = '.', markersize=markersize, color=bincolor)

    drmb = droite(z, dmb, mb_err, 1, 0)
    ax1.plot(z, drmb(drmb.pars.free), color=bincolor, ls = '--', alpha = 0.5,
             label = drmb.legend) #f'a : {drmb.pars.free[0]  : .3f}, b :{drmb.pars.free[1] : .3f}')

    a = drmb.pars.full[0]
    aerr = drmb.err[0]
    b = drmb.pars.full[1]
    berr = drmb.err[1]
    ax1.fill_between(z, (a-aerr)*z+(b-berr), (a+aerr)*z+(b+berr), color=bincolor, alpha = 0.3)
    ax1.fill_between(z, (a-2*aerr)*z+(b-2*berr), (a+2*aerr)*z+(b+2*berr), color=bincolor, alpha = 0.2)
    ax1.fill_between(z, (a-3*aerr)*z+(b-3*berr), (a+3*aerr)*z+(b+3*berr), color=bincolor, alpha = 0.1)
    
    ax1.grid(True)
    ax1.legend()
    ax2 = fig.add_subplot(gs[1], sharey=ax1)
    hist(ax2, dmb, orientation ='horizontal', color=c)
    ax2.grid(True)
    
    c =	next(colors)
    ax3 = fig.add_subplot(gs[2], sharex=ax1)    
    ax3.errorbar(z, dx1, yerr=x1_err, ls = '', marker =maker, alpha=alpha, color=c)
    ax3.set_ylabel(r'$\Delta X_1$')
    binplot(z, dx1, data = False, marker = '.', markersize=markersize, color= bincolor)
    dr1 = droite(z, dx1, x1_err, 1, 0)
    if add_gen_limits:
        x1_gen = m.training_dataset.sne['x1'].mean()
        ax3.axhline(x1_gen.mean(), color = 'k', alpha = 0.5, label = 'mean in training sample')
    ax3.plot(z, dr1(dr1.pars.free), color=bincolor, ls = '--', alpha = 0.5,
             label = dr1.legend) 

    a = dr1.pars.full[0]
    aerr = dr1.err[0]
    b = dr1.pars.full[1]
    berr = dr1.err[1]
    ax3.fill_between(z, (a-aerr)*z+(b-berr), (a+aerr)*z+(b+berr), color=bincolor, alpha = 0.3)
    ax3.fill_between(z, (a-2*aerr)*z+(b-2*berr), (a+2*aerr)*z+(b+2*berr), color=bincolor, alpha = 0.2)
    ax3.fill_between(z, (a-3*aerr)*z+(b-3*berr), (a+3*aerr)*z+(b+3*berr), color=bincolor, alpha = 0.1)

    ax3.grid(True)
    ax3.legend()
    
    ax4 = fig.add_subplot(gs[3], sharey=ax3)
    hist(ax4, dx1, orientation ='horizontal', color=c)
    ax4.grid(True)

    c =	next(colors)
    ax5 = fig.add_subplot(gs[4], sharex=ax1)        
    ax5.errorbar(z, dc, yerr=c_err, ls = '', marker =maker, alpha=alpha, color=c )
    ax5.set_ylabel(r'$\Delta c$')
    binplot(z, dc, data = False, marker = '.', markersize=markersize, color=bincolor)
    ax5.grid(True)
    
    
    drc = droite(z, dc, c_err, 1, 0)
    ax5.plot(z, drc(drc.pars.free), color=bincolor, ls = '--', alpha = 0.5,
             label = drc.legend) 
    if add_gen_limits:
        c_gen = m.training_dataset.sne['c'].mean()
        ax5.axhline(c_gen.mean(), color = 'k', alpha = 0.5, label = 'mean in training sample')

    a = drc.pars.full[0]
    aerr = drc.err[0]
    b = drc.pars.full[1]
    berr = drc.err[1]
    ax5.fill_between(z, (a-aerr)*z+(b-berr), (a+aerr)*z+(b+berr), color=bincolor, alpha = 0.3)
    ax5.fill_between(z, (a-2*aerr)*z+(b-2*berr), (a+2*aerr)*z+(b+2*berr), color=bincolor, alpha = 0.2)
    ax5.fill_between(z, (a-3*aerr)*z+(b-3*berr), (a+3*aerr)*z+(b+3*berr), color=bincolor, alpha = 0.1)

    ax5.grid(True)
   
    ax5.legend()
    ax6 = fig.add_subplot(gs[5], sharey=ax5)
    hist(ax6, dc, orientation ='horizontal', color=c)
    ax6.grid(True)
    
    c = next(colors)
    ax7 = fig.add_subplot(gs[6], sharex=ax1)    
    ax7.errorbar(z, dmu, yerr=mu_err, ls = '', marker =maker, alpha=alpha, color=c)
    binplot(z, dmu, data = False, marker = '.', markersize=markersize, color=bincolor)
    ax7.set_ylabel(r'$\Delta \mu$')
    ax7.grid(True)
    ax7.set_xlabel('redshift')
    drm = droite(z, dmu, mu_err, 1, 0)
    ax7.plot(z, drm(drm.pars.free), color=bincolor, ls = '--', alpha = 0.5,
             label = drm.legend) 

    a = drm.pars.full[0]
    aerr = drm.err[0]
    b = drm.pars.full[1]
    berr = drm.err[1]
    ax7.fill_between(z, (a-aerr)*z+(b-berr), (a+aerr)*z+(b+berr), color=bincolor, alpha = 0.3)
    ax7.fill_between(z, (a-2*aerr)*z+(b-2*berr), (a+2*aerr)*z+(b+2*berr), color=bincolor, alpha = 0.2)
    ax7.fill_between(z, (a-3*aerr)*z+(b-3*berr), (a+3*aerr)*z+(b+3*berr), color=bincolor, alpha = 0.1)

    ax7.grid(True)
    ax7.legend()

    ax7.legend()
    
    ax8 = fig.add_subplot(gs[7], sharey=ax7)
    hist(ax8, dmu, orientation ='horizontal', color=c)
    ax8.grid(True)

    if return_biai:
        return {'dmb': dmb, 'dx1' : dx1, 'dc' : dc, 'dmu' : dmu, 'mu_err':mu_err, 'z':z}
    return fig




from scipy.sparse import coo_matrix
from ..lib.fitparameters import FitParameters
from sksparse import cholmod

class droite(object):
    """
    """
    def __init__(self, x, y, yerr, a, b):

        data = np.rec.fromarrays((x, y, yerr, [0]*len(x)),
                           dtype=[('Date', '<f8'),('Flux', '<f8'),
                                  ('FluxErr', '<f8'), ('id', '<i4')])
        self.lambda_c = self.lambda_c_red = 1
        self.data = data
        self.nlc = len(np.unique(data['id']))
        self.pars = self.init_pars(a, b)
        self.droite_minimization()
        
    def init_pars(self, a, b):
        fp = FitParameters([('a', 1), ('b', 1)])
        fp['a'].full[:] = a
        fp['b'].full[:] = b 
        return fp
    
    def __call__(self, p, jac = False):
        self.pars.free = p
        data = self.data
        
        a = self.pars['a'].full[:]
        b = self.pars['b'].full[:]
        val = a * data['Date'] + b
        if jac :
            J = coo_matrix(np.vstack((data['Date'],
                                      np.ones_like(data['Date']))))
            return val, J.T
        return val


    def get_chi2(self, data, val, sig):
        rr = (data-val)/sig
        chi2 = rr.T @ rr
        return chi2

    
    def droite_minimization(self):

        dchi2 = 1000
        iteration = 0
        x = self.data['Date']
        data = self.data['Flux']
        flux_err = self.data['FluxErr']

        p = self.pars.free
        
        while dchi2 > 1e-5:
            sig =  flux_err
            
            W = coo_matrix(np.diag(1/sig**2))
            val, J = self(p, jac =True)
            res = data - val

            chi2 = self.get_chi2(data, val, sig)
            hess = 2*J.T @ W @ J
            grad = - 2*J.T @ W @ res

            fact = cholmod.cholesky(coo_matrix(hess))
            dx = fact( -1 * grad)

            p += dx
            val, J = self(p, jac =True)

            chi22 = self.get_chi2(data, val, sig)
            dchi2 = chi2 - chi22
            if dchi2 < 0 :
                p -= dx[0]
            
            if iteration > 200:
                break
            iteration += 1
        self.chi2_red = chi2/(len(self.data)-len(p))
        self.err = np.sqrt(np.diag(np.linalg.inv(1/2*hess.toarray())))
        self.legend = f'a : {p[0]  : .3f} $\pm$ {self.err[0] : .3f}, b :{p[1] : .3f} $\pm$ {self.err[1] : .3f}, ' \
                      f'$\chi^2/dof$: {self.chi2_red : .3f}'
        print(self.legend)
        return p
