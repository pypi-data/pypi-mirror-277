import numpy as np
import pylab as pl
pl.ion()
import sncosmo
from nacl.models.salt2.salt import SALT2Like
from nacl.dataset import SimTrainingDataset
source = sncosmo.get_source('salt2', version='2.4')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from lemaitre import bandpasses

def NaCl_vs_sncosmo_simple(bands = ['ztf::g'], params = [{'x0':1, 'x1':0, 'c':0}], dt=0.27, zp=30., zp_band=1.):
    """
    This function compares NaCl lightcurve prediction with sncosmo in a single band with a set of given parameters
    and calculates the relative difference.
    """
    fl = bandpasses.get_filterlib()
    model_sncosmo = sncosmo.Model(source=source)
    t = np.arange(-20, 50, 1)
    for band in bands:
        tds_sim = SimTrainingDataset( [band], n_spectra=0, n_phot_spectra=0, zp=zp, filterlib=fl )
        model_sim = SALT2Like(tds_sim, basis_knots=[700,70])
        pars = model_sim.init_pars()
        for p in params:
            model_sncosmo.set(x0=p['x0'], x1=p['x1'], c=p['c'])
            print(p)
            pars['X0'].full += p['x0']
            pars['X1'].full += p['x1'] + 0.13
            pars['c'].full += p['c']
            
            #model_sim.renorm()
            
            ms = sncosmo.get_magsystem('ab')
            bd = sncosmo.get_bandpass(band)
            
            mm = model_sim(pars)
            nn = model_sncosmo.bandflux(band, t+dt, zp=zp, zpsys='ab')[20]/mm[20]
            print(nn) 
            
            pl.figure()
            pl.plot(t, model_sncosmo.bandflux(band, t+dt, zp=zp, zpsys='ab'), label='sncosmo')
            pl.plot(t, mm*nn, label = 'NaCl * norm')
            pl.xlabel('phase')
            pl.ylabel('flux')
            pl.title(band+', X0=1, X1=c=0  norm ' + str(nn))
            pl.legend()
            pl.show()
            
            pl.figure()
            pl.plot(t, np.abs(mm[:len(t)]*nn-model_sncosmo.bandflux(band, t+dt, zp=zp, zpsys='ab'))/model_sncosmo.bandflux(band, t+dt, zp=zp, zpsys='ab'), label='relative difference')
            pl.xlabel('phase')
            pl.ylabel('flux')
            pl.title(band+', relative difference')
            pl.legend()
            pl.show()
    return tds_sim
        
    #pl.figure()
    #pl.plot(t, np.abs((model_sncosmo.bandflux('standard::b', t) - mm[:len(t)]*nn)/model_sncosmo.bandflux('standard::b', t)), label='sncosmo')
    #pl.xlabel('phase')
    #pl.ylabel('flux diff %')
    #pl.title('Diff Standard B, X0=1, X1=c=0')
    #pl.legend()
    #pl.show()
    
    #return model_sim
