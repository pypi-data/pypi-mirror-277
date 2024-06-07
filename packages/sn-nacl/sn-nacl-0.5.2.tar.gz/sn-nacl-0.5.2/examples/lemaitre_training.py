import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np
import pylab as pl
pl.ion()
from nacl.dataset import TrainingDataset
from nacl.train import TrainSALT2Like
from nacl.models import salt2
import pandas as pd
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from lemaitre import bandpasses

if __name__ == '__main__':
    fl = bandpasses.get_filterlib()
    tds = TrainingDataset.read_parquet('../data/lemaitre_full/lemaitre.compressed.parquet', filterlib=fl)
    
    #KEEPING ONLY HALF OF ZTF SNe
    """idx = tds.sn_data.nt['survey'] == 'ZTF'
    sn_remove = tds.sn_data.nt[idx]['name'][1500:]
    tds.kill_sne(sn_remove)
    tds.compress()
    
    
    #trainer = TrainSALT2Like(tds, variance_model='simple_snake')
    trainer = TrainSALT2Like(tds, variance_model='sn_local_snake')
    trainer.train_salt2_model()
    """
    
    #KEEPING ONLY HALF OF ZTF SNe
    # idx = tds.sn_data.nt['survey'] == 'ZTF'
    # sn_remove = tds.sn_data.nt[idx]['name'][:1500]
    # tds.kill_sne(sn_remove)
    # tds.compress()
    
    
    #trainer = TrainSALT2Like(tds, variance_model='simple_snake')
    trainer = TrainSALT2Like(tds, variance_model='sn_local_snake')
    trainer.train_salt2_model()
