#!/usr/bin/env python3
import os
import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)
import pandas
import glob
import nacl
from nacl.dataset import TrainingDataset
from lemaitre import bandpasses

bandpass_convert = {
    'MEGACAMPSF::g': 'megacam6::g',
    'MEGACAMPSF::r': 'megacam6::r',
    'MEGACAMPSF::i2': 'megacam6::i2',
    'MEGACAMPSF::z': 'megacam6::z',
    'MEGACAMPSF::i': 'megacampsf::i',

    'megacam6::g': 'megacam6::g',
    'megacam6::r': 'megacam6::r',
    'megacam6::i2': 'megacam6::i2',
    'megacam6::z': 'megacam6::z',
    'megacam6::i': 'megacampsf::i',

    'ztfg': 'ztf::g',
    'ztfr': 'ztf::r',
    'ztfi': 'ztf::I',

    'ztf::g': 'ztf::g',
    'ztf::r': 'ztf::r',
    'ztf::I': 'ztf::I',
}


def load_sample(path, sample='SNLS', init_sn_loc=True, extension="parquet.gzip"):
    """
    load and sanitize the SNLS data

    Examples
    --------
    >>> sne, lc, sp = load_sample(path="data/test_datasets/", sample="SNLS")
    """
    if "parquet" in extension:
        logging.info(f'Loading {sample} from\n'+"\n".join(glob.glob(os.path.join(path, f"*_{sample}_blind.parquet.gzip"))))
        sne = pandas.read_parquet(os.path.join(path, f'data_{sample}_blind.parquet.gzip'))
        lc = pandas.read_parquet(os.path.join(path, f'lc_{sample}_blind.parquet.gzip'))
        sp = pandas.read_parquet(os.path.join(path, f'sp_{sample}_blind.parquet.gzip'))
    elif "csv" in extension:
        logging.info(f'Loading {sample} from\n'+"\n".join(glob.glob(os.path.join(path, f"*_{sample}_blind.csv"))))
        sne = pandas.read_csv(os.path.join(path, f'data_{sample}_blind.csv'))
        lc = pandas.read_csv(os.path.join(path, f'lc_{sample}_blind.csv'))
        sp = pandas.read_csv(os.path.join(path, f'sp_{sample}_blind.csv'))
    else:
        raise ValueError(f"Unknown extension: {extension}. Must be either 'parquet' or 'csv'")

    # purge all the SN which could not be fitted with sncosmo
    idx = sne['x0'] != 999.9
    logging.info(f'removed {(~idx).sum()} SNe which could not be fitted with sncosmo')
    sne = sne[idx]

    # purge all the LC data with no counterpart in the SN index
    idx = lc.name.isin(sne.name)
    lc = lc[idx]
    logging.info(f'removed {(~idx).sum()} LC data points with no entry in the SN index')
    lc.sn = lc.name

    # purge all the LC data taken with bandpass megacampsf::i
    idx = (lc.band == 'MEGACAMPSF::i') | (lc.band == 'megacampsf::i') | (lc.band == 'megacam6::i')
    lc = lc[~idx]
    logging.info(f'removed {(idx).sum()} LC data points taken in band megacampsf::i')

    # get rid of AB_B12 magsys
    # we assume that the light curves will be recalibrated
    #    idx = lc.magsys == 'AB_B12'
    #    lc.loc[idx, 'magsys'] = 'AB'
    #    logging.info(f'hacked the magsys of {idx.sum()} measurements from AB_B12 to AB')

    # purge all the spectra with no counterpart in the SN index
    idx = sp.name.isin(sne.name)
    sp = sp[idx]
    logging.info(f'removed {(~idx).sum()} SP data points with no entry in the SN index ')
    sp.sn = sp.name

    # correct the valid field
    sp.loc[sp.valid.isna(), 'valid'] = 1
    sp['valid'] = sp.valid.astype(int)

    # add a i_basis field
    sp['i_basis'] = 0

    # we use names to identify the SNe
    sne.sn = sne.name
    lc.sn = lc.name
    sp.sn = sp.name

    # update the bandpass names
    lc['band'] = [bandpass_convert[b] for b in lc.band]
    if 'survey' not in sne.columns:
        lc['survey'] = sample

    if init_sn_loc:
        lc['x'] = 0.
        lc['y'] = 0.
        lc['ccd'] = 0
        lc['amp'] = 0

    return sne, lc, sp


def dataset_release(path):
    """
    Build a TrainingDataset from an existing path

    :param path: str
    :return: nacl.dataset.TrainingDataset

    Examples
    --------
    >>> tds = dataset_release("../../../data/lemaitre_light/")
    >>> assert isinstance(tds, nacl.dataset.TrainingDataset)
    """
    sne_ztf, lc_ztf, sp_ztf = load_sample(path, 'ztf')
    lc_ztf['x'] = 1000.
    lc_ztf['y'] = 1000.
    lc_ztf['sensor_id'] = 12

    sne_SNLS, lc_SNLS, sp_SNLS = load_sample(path, 'SNLS')
    lc_SNLS['x'] = 1000.
    lc_SNLS['y'] = 1000.
    lc_SNLS['sensor_id'] = 12
    lc_offset = lc_ztf.lc.max() + 1
    lc_SNLS['lc'] = lc_SNLS['lc'] + lc_offset
    spec_offset = sp_ztf.spec.max() + 1
    sp_SNLS['spec'] = sp_SNLS['spec'] + spec_offset

    flib = bandpasses.get_filterlib(rebuild=False)
    tds = TrainingDataset(pandas.concat([sne_ztf, sne_SNLS]),
                          pandas.concat([lc_ztf, lc_SNLS]),
                          pandas.concat([sp_ztf, sp_SNLS]),
                          filterlib=flib)
    return tds
