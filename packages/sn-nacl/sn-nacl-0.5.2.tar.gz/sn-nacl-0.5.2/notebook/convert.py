#!/usr/bin/env python3

import numpy as np
import pandas
import pylab as pl
from lemaitre import bandpasses
from nacl import TrainingDataset
from nacl.models.salt2 import SALT2Like


if __name__ == '__main__':

    fl = bandpasses.get_filterlib()

    sn_data = pandas.read_parquet('sn_data.parquet',
                                  columns=['z', 'x0', 'x1', 'c', 't0', 'ra', 'dec'],
                                  ).rename(columns={'t0': 'tmax'})
    #sn_data = sn_data_orig[[]]
    #sn_data.rename(columns={'t0': 'tmax'}, inplace=True)
    sn_data['sn'] = sn_data.index
    sn_data['mwebv'] = 0.
    sn_data['survey'] = ''
    sn_data['valid'] = 1

    lc_data = pandas.read_parquet('lc_data.parquet',
                                  columns=['z', 'mjd', 'band'])
    #lc_data = lc_data_orig[['snname', 'z', 'mjd', 'band']]
    #lc_data.rename(columns={'snname': 'sn'}, inplace=True)
    lc_data['sn'] = lc_data.index
    lc_data['exptime'] = 0.
    lc_data['valid'] = 1
    lc_data['flux'] = 0.
    lc_data['fluxerr'] = 0.
    lc_data['magsys'] = 0.
    lc_data['lc'] = lc_data['sn'].astype(str) + '-' + lc_data['band']
    lc_data['seeing'] = 0.
    lc_data['zp'] = 0.
    lc_data['mag_sky'] = 0.
    lc_data['x'] = 0.
    lc_data['y'] = 0.
    # lc_data['ccd'] = 0.
    # lc_data['amp'] = 0.
    lc_data['sensor_id'] = 0

    print('training dataset...')
    tds = TrainingDataset(sne=sn_data.to_records(),
                          lc_data=lc_data.to_records(),
                          filterlib=fl)
    tds.plot_sample()
