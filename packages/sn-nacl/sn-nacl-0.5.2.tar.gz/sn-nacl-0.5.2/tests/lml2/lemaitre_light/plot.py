#!/usr/bin/env python3

import os
import os.path as op
import sys

import numpy as np
import pandas

from lemaitre import bandpasses
from nacl import TrainingDataset
from nacl.train import ModelTrainer
from nacl.models.salt2 import SALT2Like



if __name__ == '__main__':
    """
    """
    fl = bandpasses.get_filterlib()
    tds = TrainingDataset.read_parquet('lml.compressed.parquet', filterlib=fl)
    model = SALT2Like(tds)
    train = ModelTrainer(tds, model)

    # sne_ztf = pandas.read_parquet('data_ztf_blind.parquet.gzip')
    # sne_ztf['col'] = sne_ztf['c']
    # lc_ztf = pandas.read_parquet('lc_SNLS_blind.parquet.gzip')
    # lc_ztf['x'] = 0.
    # lc_ztf['y'] = 0.
    # lc_ztf['sensor_id'] = 12
    # sp_ztf = pandas.read_parquet('sp_SNLS_blind.parquet.gzip')
    # sp_ztf['i_basis'] = 0

    # sne_snls = pandas.read_parquet('data_SNLS_blind.parquet.gzip')
    # sne_snls['col'] = sne_snls['c']
    # lc_snls = pandas.read_parquet('lc_SNLS_blind.parquet.gzip')
    # lc_snls['x'] = 0.
    # lc_snls['y'] = 0.
    # lc_snls['sensor_id'] = 12
    # sp_snls = pandas.read_parquet('sp_SNLS_blind.parquet.gzip')
    # sp_snls['i_basis'] = 0

    # lc_snls.lc += lc_ztf.lc.max() + 1
    # sp_snls.spec += sp_ztf.spec.max() + 1

    # tds = TrainingDataset(pandas.concat([sne_ztf, sne_snls]),
    #                       pandas.concat([lc_ztf, lc_snls]),
    #                       pandas.concat([sp_ztf, sp_snls]),
    #                       filterlib=fl)
