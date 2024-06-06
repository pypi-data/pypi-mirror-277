import numpy as np
import nacl.instruments
import os 
from nacl.simulations.reindex import reindex
from nacl.dataset import TrainingDataset
import glob
import pandas as pd

class Generator(object):
    r"""
    Data generator using light curves, spectra and redshift from Kenworthy et al. 21
    CSP, CfA3,4, SDSS,SNLS, Pan Starrs, DES, and historical low-z SNe Ia.


    We start again from the objects composing each of these training batches~: we take their redshifts,
    their SALT2 parameters (:math:`X_0`, :math:`X_1`, :math:`c`, :math:`t_{max}`) as well as the
    photometric and spectroscopic observation dates.
   
    
    OUTPUTS:
    
    trainingDataset : nacl.dataset.TrainingDataset
        Data set of photometric and spectroscopic observations.
    """
    
    def __init__(self, filespath='../data/k21/Data_reshape/',
                 filterpath='../data/k21/filters',zppath='../data/k21/MagSys',parspath='../data/k21/SALT3TRAIN_K21_PUBLIC/',x1range=None,x0range=None,crange=None):
        """
        Constructor - computes the arguments

        Parameters
        ----------
        filespath : string
           path to the repository containing the light curve et spectra files.
        filterpath : string
           path to the filters files repository in nacl.dev/data/           
        parspath : string
            path to the SALT3 parameters (x0,X1,c) and SNe information from K21
           
        """

        self.filespath = filespath
        self.zppath=zppath
        self.filterpath = filterpath
        self.parspath = parspath
        self.Sne, self.snInfo, self.lc, self.sp = None, None, None, None
        self.trainingDataset = None
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
            :math:`X_0` of K21 training sets
        x1 : list
            :math:`X_1` of K21 training sets
        color : list
            :math:`c` of K21 training sets
        """

        # all the outputs
        snInfo= None
                            
        pars=self.parspath+os.sep+'SALT3_PARS_INIT.LIST'
        tmax=self.parspath+os.sep+'SALT3_PKMJD_INIT.LIST'                                        
        salt3_pars = np.recfromtxt(pars) #SNID zHelio x0 x1 c
        salt3_tmax = np.recfromtxt(tmax) #Tmax
        sne,zhel,tmax,x0, x1, color = [], [], [], [], [], []
        for i in range(len(salt3_pars)):
            sne.append(salt3_pars['f0'][i])
            zhel.append(salt3_pars['f1'][i])
            x0.append(salt3_pars['f2'][i])
            x1.append(salt3_pars['f3'][i])
            color.append(salt3_pars['f4'][i])
            ind_Tmax=np.where(salt3_tmax['f0']==salt3_pars['f0'][i])[0]
            if np.size(ind_Tmax)>0:            
                tmax.append(salt3_tmax['f1'][ind_Tmax[0]])
            else:
                tmax.append(999.9)
        snInfo=pd.DataFrame()
        snInfo['sn']=np.array(sne)
        snInfo['z']=np.array(zhel)
        snInfo['tmax']=np.array(tmax) 
        snInfo['x1']=np.array(x1)
        snInfo['x0']=np.array(x0)                               
        snInfo['col']=np.array(color)
        snInfo['valid']=1

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

        surveys = glob.glob(self.filespath + os.sep + '*_lc.npy')
        surveys = [i.split('/')[-1].split('_')[0] for i in surveys]
        lc ,lc_sum= [],[]

        zp = {}
        with open(self.zppath + os.sep + 'k21_zp2.txt') as f:
            for line in f:
                (key,band, val) = line.split()
                zp[key+'::'+band] = float(val)
        for sur in surveys:
            lc_sur = pd.DataFrame(np.load(self.filespath + os.sep + f'{sur}_lc.npy'))
            lc_sum_sur = pd.DataFrame(np.load(self.filespath + os.sep + f'{sur}_lc_summary.npy',allow_pickle=True))        
            try:
                lc_id_offset = lc.iloc[-1]['id']+1
            except:
                lc_id_offset = 0
   
            lc_sur['id'] += lc_id_offset
            

            if np.where(np.array(surveys) == sur)[0][0] == 0:
                lc = lc_sur
                lc_sum = lc_sum_sur                

            else:
                lc = pd.concat([lc, lc_sur])
                lc_sum = pd.concat([lc_sum, lc_sum_sur])
                
        lc_sum=lc_sum.reset_index() 
        lc['sn'] = lc['id']
        lc['seeing'] = np.nan
        lc['mag_sky'] = np.nan
        lc['exptime'] = np.nan                
        lc['valid'] = 1
        lc_sum=lc_sum.rename(columns={'SN': 'sn', 'ZHelio': 'z', 'Date': 'mjd'})

        lc_sum['sn']=[ind.strip() for ind in lc_sum['sn'].values]                
        
        lc=lc.rename(columns={'Date': 'mjd', 'Flux': 'flux', 'FluxErr': 'fluxerr','Filter':'band','MagSys':'magsys'})
        
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
        lc=lc[['sn','mjd','flux','fluxerr','band','magsys','exptime','valid','lc','mag_sky','seeing']]
        lc_sum=lc_sum.drop(['index'], axis=1)        
        lc_sum['sn_id'] = lc_sum.index
        lc['sn_id'] = lc['sn']
        #Select only the SNe from the selected sample
        lc_sum=pd.merge(lc_sum, sample, how='inner', on=['sn'],suffixes=('', '_y'))
        lc=pd.merge(lc, lc_sum[['sn_id','nbsn']], how='inner', on=['sn_id'])
        lc=lc.drop(['sn','sn_id'], axis=1)  
        lc=lc.rename(columns={'nbsn': 'sn'})  
        lc['band']=lc['band'].str.decode("utf-8")   
        
        zp_lc=np.zeros(lc['sn'].shape)
        for filt in np.unique(lc.band):
            zp_lc[lc.band==filt]=zp[filt]
        lc['zp']=zp_lc               
        return lc,lc_sum
        
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

        surveys = glob.glob(self.filespath + os.sep + '*_lc.npy')
        surveys = [i.split('/')[-1].split('_')[0] for i in surveys]
        sp,sp_sum= [],[]
               
        for sur in surveys:
            try:
                sp_sur = pd.DataFrame(np.load(self.filespath + os.sep + f'{sur}_spectra.npy'))
                sp_sur_sum =  pd.DataFrame(np.load(self.filespath + os.sep + f'{sur}_spectra_summary.npy',allow_pickle=True))
            except FileNotFoundError:
                print('No spectra for %s'%sur)                
                sp_sur=None
            try:
                sp_id_offset = sp.iloc[-1]['id']+1
            except:
                sp_id_offset = 0
                
            if sp_sur is not None:
                sp_sur['id'] += sp_id_offset
            

            if np.where(np.array(surveys) == sur)[0][0] == 0:
                if sp_sur is not None:            
                    sp = sp_sur
                    sp_sum= sp_sur_sum
            else:
                if sp_sur is not None:            
                    sp = pd.concat((sp, sp_sur))
                    sp_sum = pd.concat((sp_sum, sp_sur_sum))                                   

        sp=sp.rename(columns={'Wavelength': 'wavelength', 'Flux': 'flux', 'FluxErr': 'fluxerr','SPECFLAG':'valid'})
        sp_sum=sp_sum.rename(columns={'SN': 'sn', 'ZHelio': 'z', 'Date': 'mjd'})

        sp['spec'] = sp['id'].astype(int)
        sp=sp.drop(['id'], axis=1)   
        sp_sum=sp_sum.reset_index()                     
        sp_sum['spec'] = sp_sum.index                    
                    
        #Select only the SNe from the selected sample
        sp_sum['sn']=[ind.strip() for ind in sp_sum['sn'].values]                
        sp_sum=pd.merge(sp_sum, sample, how='inner', on=['sn'])

        sp=pd.merge(sp, sp_sum[['spec','mjd','nbsn']], how='inner', on=['spec'])
        sp=sp.rename(columns={'nbsn': 'sn'})  

        sp['exptime']=np.nan
        sp['valid']=1
        sp=sp[['sn','mjd','wavelength','flux','fluxerr','valid','spec','exptime']]
                                   
        return sp


    def make_data(self,x1range,x0range,crange):
                      
        sne = self.get_sample(x1range,x0range,crange)
        lc,lc_sum= self.get_lightcurves(sne)
        sne=lc_sum[['sn','z','tmax','x1','x0','col','valid','nbsn']]
        sp = self.get_spectra(sne)
        sne['IAU']=sne['sn'].str.decode("utf-8")   
        sne['sn']=sne['nbsn']
        sne=sne.drop(['nbsn'], axis=1)

        self.lc=lc
        self.sp=sp
        self.sne=sne
        self.trainingDataset = TrainingDataset(self.lc, self.sp, self.sne,filterpath=self.filterpath)
        

