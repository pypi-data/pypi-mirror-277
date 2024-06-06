#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import pickle
from argparse import ArgumentParser

import matplotlib as mpl
import numpy as np
import numpy.ma as ma
import pylab as pl
import pandas

from lemaitre import bandpasses
from nacl import TrainingDataset, LogLikelihood, Minimizer
from nacl.models.salt2 import SALT2Like, constraints
from nacl.models.salt2.constraints import salt2like_linear_constraints, nacl_linear_constraints
from nacl.models.salt2.regularizations import NaClSplineRegularization
from nacl.models.salt2.variancemodels import SimpleErrorSnake, LocalErrorSnake
from nacl.train import TrainSALT2Like

from saunerie.robuststat import mad




if __name__ == '__main__':

    fl = bandpasses.get_filterlib()
    # tds = TrainingDataset.read_parquet('lemaitre.compressed.parquet', filterlib=fl)
    tds = TrainingDataset.read_parquet('compressed_mini_tds_blinded.parquet', filterlib=fl)

    # this phase range is very small. Find a way to extend it
    # this is mainly because we need the model predictions
    # to calibrate the spectra.
    # clean_dataset(tds, phase_range=(-20., 40.))

    model = SALT2Like(tds) # phase_grid=np.linspace(-30., 70., 30))
    salt2_cons = salt2like_linear_constraints(model)
    nacl_cons = nacl_linear_constraints(model)

    # variance_model = LocalErrorSnake(model)
    #train = TrainSALT2Like(tds, 'sn_lambda_snake')
    #train.train_salt2_model()
