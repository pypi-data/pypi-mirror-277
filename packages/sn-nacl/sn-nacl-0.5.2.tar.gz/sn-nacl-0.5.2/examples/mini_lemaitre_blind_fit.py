import numpy as np
import pylab as pl
pl.ion()
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)
from nacl.dataset import TrainingDataset
from nacl.train import TrainSALT2Like
from nacl.models import salt2
import pandas as pd
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from lemaitre import bandpasses
import release

#will be removed from the full fit
from nacl.specutils import Spec, clean_and_project_spectra

if __name__ == '__main__':
    fl = bandpasses.get_filterlib()  #Initialise filters
    tds = release.dataset_release('lemaitre_light') # Uncompressed dataset
    model_ = salt2.get_model(tds)
    
    #will be removed later : Compression should be done beforehand
    #I am leaving it here because the compression takes 2 seconds here
    logging.info('compression...')
    projected_spectra, in_error = clean_and_project_spectra(tds, model_.basis.bx)
    logging.info('done: in_error: {len(in_error)}')

    ptds = TrainingDataset(tds.sn_data.nt, lc_data=tds.lc_data.nt,
                           spec_data=np.rec.array(np.hstack(projected_spectra)),
                           basis=model_.basis.bx,
                           filterlib=fl)
    
    #TRAINING
    trainer = TrainSALT2Like(ptds, variance_model='simple_snake')  #Initialise with an error model
    #trainer = TrainSALT2Like(ptds, variance_model='local_snake')
    #trainer = TrainSALT2Like(ptds, variance_model='sn_lambda_snake')
    #trainer = TrainSALT2Like(ptds, variance_model='sn_local_snake')
    trainer.train_salt2_model(save=True, path='test_mini')  #train
    
    
    #RESULTS
    pars_trained = trainer.log[-1].pars  #parameters
    v_trained = trainer.log[-1].v  #model prediction
    #cov_matrix = trainer.log[-1].minz.get_cov_matrix()[0] #full covariance matrix (this can take a few minutes)
    
    #PLOTS
    trainer.plot_lc('ZTF18aapsedq', numfit=3, plot_variance=True)
