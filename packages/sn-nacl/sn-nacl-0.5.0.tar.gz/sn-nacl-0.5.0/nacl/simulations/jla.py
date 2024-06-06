import numpy as np
import nacl.instruments
import os 
from nacl.simulations.reindex import reindex
from nacl.dataset import TrainingDataset
import glob
import pandas as pd
from nacl.util import salt2

class Generator(object):
    r"""
    Generate JLA simulation (Betoule et al. 2014)


    We start again from the objects composing each of these training batches~: we take their redshifts,
    their SALT2 parameters (:math:`X_0`, :math:`X_1`, :math:`c`, :math:`t_{max}`) as well as the
    photometric and spectroscopic observation dates.
   
    
    Attributes
    ----------
    filespath : str
        Path to the repository containing the light curve et spectra files.
    Sne ; numpy.array
        SNe names
    lc : numpy.rec.array
        Light curves data with data_type as type.
    sp : numpy.rec.array
        Spectral data, with data_type as type.
    snInfo : numpy.rec.array
        SNe information (:math:`z`, :math:`tmax`, :math:`x1`, :math:`x0`, :math:`c`)
    data_type : list
        NaCl data type.
    snInfo_type : list
        Type of information of SNe.
    sigma_lc : numpy.array
        Dispersion of photometric data
    sigma_sp : numpy.array
        Dispersion of spectral data.
    trainingDataset : nacl.dataset.TrainingDataset
        Data set of photometric and spectroscopic observations.
    """
    def __init__(self, filespath='../data/jla',filterpath=None,x1range=None,x0range=None,crange=None):
        """
        Constructor - computes the arguments

        Parameters
        ----------
        filespath : string
           path to the repository containing the light curve et spectra files.

        """

        self.filespath = filespath
        self.filterpath = filterpath

        self.sne, self.lc, self.sp = None, None, None
        self.trainingDataset=None
        self.make_data(x1range,x0range,crange)


    def get_sample(self,x1range,x0range,crange):
        
        r"""
        Get sn parameters from all sne in published file
        
        Attributes:
        x1range : array [x1min,x1max]
        x0range : array [x0min,x0max]        
        crange : array [cmin,cmax]
        
        Returns snInfo with
        -------
        sne : list
             : name of the SNe Ia
        zhelio : list
             heliocentric redshift of K21 training sets
        x0 : list
            :math:`X_0` of JLA training sets
        x1 : list
            :math:`X_1` of JLA training sets
        color : list
            :math:`c` of JLA training sets
        tmax : list
            :math:`tmax` of JLA training sets            
        """

        lc_sum = pd.DataFrame(np.load(self.filespath + os.sep + 'jla_lc_summary.npy', allow_pickle=True))
        # their type
        lc_sum=lc_sum.rename(columns={'SN': 'sn', 'ZHelio': 'z', 'DayMax': 'tmax', 'X0': 'x0', 'X1': 'x1', 'Color': 'col', 'Surveys': 'surveys', 'MWEBV': 'mwebv'})                          
        lc_sum['valid']=(np.zeros(lc_sum['sn'].shape)+1).astype(int)
        snInfo = lc_sum[['sn','z','tmax','x1','x0','col','valid','mwebv','surveys']] 

        
        if x1range!=None:
            snInfo=snInfo[(snInfo['x1']<x1range[1]) & (snInfo['x1']>x1range[0])]
        if x0range!=None:
            snInfo=snInfo[(snInfo['x0']<x0range[1]) & (snInfo['x0']>x0range[0])]
        if crange!=None:
            snInfo=snInfo[(snInfo['col']<crange[1]) & (snInfo['col']>crange[0])]  
            
        snInfo['nbsn']=snInfo.index.values                          
        return snInfo  
        
    def get_lightcurves(self,sample):
        
        r"""
        Get light curves from published file, i.e.,
        Merge all the K21 survey training files of light curves.

        Returns 
        -------
        sample : snInfo from get_sample
             information of the sample, sne, tmax,z,x0,x1,c.


        Returns 
        -------
        lc : numpy.rec.array
             All surveys light curve file.
        lc_sum : list
             All surveys light curve summary file.
        """



        lc = pd.DataFrame(np.load(self.filespath + os.sep + 'jla_lc.npy'))
        lc_sum = pd.DataFrame(np.load(self.filespath + os.sep + 'jla_lc_summary.npy', allow_pickle=True))
        lc_sum=lc_sum.rename(columns={'SN': 'sn', 'ZHelio': 'z', 'DayMax': 'tmax', 'X0': 'x0', 'X1': 'x1', 'Color': 'col','Surveys': 'surveys', 'MWEBV': 'mwebv'})                          
        lc=lc.rename(columns={'Filter': 'band','Flux': 'flux','FluxErr': 'fluxerr','ZP': 'zp', 'Date': 'mjd','MagSys':'magsys'})                          

        lc['sn'] = reindex(lc['id'])
        lc['exptime'] = np.nan
        lc['seeing'] = np.nan
        lc['mag_sky'] = np.nan        
        lc['valid'] = 1
	
        # light curve indexation
        c = 0
        id_lc = np.ones(len(lc['flux']))  # .astype(int)
        
        for i in range(lc['sn'].iloc[-1]+1):
            idx_sn = lc['sn'] == i
            lcs = lc[idx_sn]
            _, idx = np.unique(lcs["band"], return_index=True)
            for bd_sn in lcs['band'].iloc[np.sort(idx)]:
                id_lc[(lc['sn'] == i) & (lc['band'] == bd_sn)] = c  # [c]*len(lc[lc]))
                c += 1

        id_lc = np.hstack(np.array(id_lc))
	
        lc['lc']=id_lc.astype(int)        
        lc=lc[['sn','mjd','flux','fluxerr','band','magsys','exptime','valid','lc','zp','mag_sky','seeing']]
        lc['band']=lc['band'].str.decode("utf-8")          
        lc_sum['sn_id'] = lc_sum.index
        
        #Select only the SNe from the selected sample
        lc_sum=pd.merge(lc_sum, sample, how='inner', on=['sn','z'])
        ind_lc=lc_sum.sn_id.values
        lc=lc.iloc[np.concatenate ([np.where(lc['sn']==ii)[0] for ii in ind_lc])]               
              
        return lc
        
    def get_spectra(self,sample):
        
        r"""
        Get spectra from published file, i.e.,
        Merge all the K21 survey training files of spectra.

        Returns 
        -------
        sp : numpy.rec.array
             All surveys spectra file.
        sp_sum : list
             All surveys spectra summary file.
        """

        sp = pd.DataFrame(np.load(self.filespath + os.sep + 'jla_spectra.npy'))
        sp_sum = pd.DataFrame(np.load(self.filespath + os.sep + 'jla_spectra_summary.npy', allow_pickle=True))
        
        sp_sum=sp_sum.rename(columns={'SN': 'sn', 'ZHelio': 'z', 'Date': 'mjd'})                          
        sp=sp.rename(columns={'Wavelength': 'wavelength','Flux': 'flux','FluxErr': 'fluxerr'})                          
        

        sp['spec'] = sp['id']
        sp_sum['spec'] = sp_sum.index
        sp=sp.drop(['id'], axis=1)

        #Select only the SNe from the selected sample
        sp_sum=pd.merge(sp_sum, sample, how='inner', on=['sn', 'z'])
        ind_sp=sp_sum.spec.values
        sp=sp.iloc[np.concatenate ([np.where(sp['spec']==ii)[0] for ii in ind_sp])]

        sp=pd.merge(sp, sp_sum, how='inner', on=['spec'])
        sp['exptime']=np.nan
        sp['valid']=1
        sp['sn']=sp['nbsn']


        sp=sp[['sn','mjd','wavelength','flux','fluxerr','valid','spec','exptime']]
                                   
        return sp

    def make_data(self,x1range,x0range,crange):
                      
        sne = self.get_sample(x1range,x0range,crange)
        lc= self.get_lightcurves(sne)
        sp = self.get_spectra(sne)
        sne['IAU']=sne['sn'].str.decode("utf-8")   
        sne['sn']=sne['nbsn']
        sne=sne.drop(['nbsn'], axis=1)
        self.lc=lc
        self.sp=sp
        self.sne=sne
        self.trainingDataset = TrainingDataset(self.sne,self.lc, self.sp,filterpath=self.filterpath)
        
      

