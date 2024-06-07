#!/usr/bin/env python3

import logging
from argparse import ArgumentParser
from pathlib import Path
import glob

import numpy as np
import pandas

from nacl.dataset import TrainingDataset
from nacl.specutils import Spec, clean_and_project_spectra
from nacl.models import salt2
from lemaitre import bandpasses

bandpass_convert = {
    'MEGACAMPSF::g': 'megacam6::g',
    'MEGACAMPSF::r': 'megacam6::r',
    'MEGACAMPSF::i2': 'megacam6::i2',
    'MEGACAMPSF::z': 'megacam6::z',
    'MEGACAMPSF::i': 'MEGACAMPSF::i',

    'ztfg': 'ztf::g',
    'ztfr': 'ztf::r',
    'ztfi': 'ztf::I',

    'ztf::g': 'ztf::g',
    'ztf::r': 'ztf::r',
    'ztf::I': 'ztf::I',

    'megacam6::g': 'megacam6::g',
    'megacam6::r': 'megacam6::r',
    'megacam6::i2': 'megacam6::i2',
    'megacam6::z': 'megacam6::z',
    'megacam6::i': 'MEGACAMPSF::i',
}


def load_sample(sample='SNLS', init_sn_loc=True, input_dir='./'):
    """
    load and sanitize the SNLS data
    """
    input_dir = Path(input_dir)

    data = []
    for nm  in ['data', 'lc', 'sp']:
        path = glob.glob(str(input_dir.joinpath(f'{nm}_{sample}*parquet*')))
        assert len(path) == 1
        data.append(pandas.read_parquet(path[0]))
    sne, lc, sp = data
    # lc = pandas.read_csv(input_dir.joinpath(f'lc_{sample}.parquet.gzip'))
    # sp = pandas.read_csv(input_dir.joinpath(f'sp_{sample}.parquet.gzip'))

    # purge all the SN which could not be fitted with sncosmo
    idx = sne['x0'] != 999.9
    logging.info(f'removed {(~idx).sum()} SNe which could not be fitted with sncosmo')
    sne = sne[idx]

    # drop the index and Unnamed fields
    sne = sne
    
    # purge all the LC data taken with bandpass megacampsf::i
    idx = (lc.band == 'MEGACAMPSF::i') | (lc.band == 'megacampsf::i') | (lc.band == 'megacam6::i')
    lc = lc[~idx]
    logging.info(f'removed {(idx).sum()} LC data points taken in band megacampsf::i')
    
    # purge all the LC data with no counterpart in the SN index
    idx = lc.name.isin(sne.name)
    lc = lc[idx]
    logging.info(f'removed {(~idx).sum()} LC data points with no entry in the SN index')
    lc.sn = lc.name

    # purge all the spectra with no counterpart in the SN index
    idx = sp.name.isin(sne.name)
    sp = sp[idx]
    logging.info(f'removed {(~idx).sum()} SP data points with no entry in the SN index ')
    sp.sn = sp.name
    
    # correct the valid field
    sp.loc[sp.valid.isna(), 'valid'] = 1
    sp['valid'] = sp.valid.astype(int)
    
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
        lc['sensor_id'] = 0

    sp['i_basis'] = -1
    
    return sne, lc, sp



if __name__ == '__main__':
    parser = ArgumentParser(description='create a TrainingDataset from the PETS files')
    parser.add_argument('-o', '--output',
                        default='lemaitre',
                        help='output file name')
    parser.add_argument('--dump-uncompressed-tds',
                        action='store_true',
                        help='whether to dump the uncompressed training dataset')
    parser.add_argument('--format',
                        default='parquet',
                        help='output format: parquet or hdf5')
    parser.add_argument('-C', '--compress',
                        action='store_true',
                        help='project spectra on the model basis')
    parser.add_argument('--samples', nargs='*',
                        default=['ztf', 'SNLS'],
                        help='samples to combine')
    parser.add_argument('input_dir',
                        help='where to find the PETS results')
    args = parser.parse_args()
    
    
    #    parser.add_argument('--basis', default='',
    #                        help='project spectra on the model basis')
    
    #    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
    #                        level=logging.INFO)

    logging.info('loading the default filter lib')
    fl = bandpasses.get_filterlib()

    sne, lc, sp = [], [], []
    lc_offset = 0
    spec_offset = 0
    for sample_name in args.samples:
        logging.info(f'loading {sample_name}')
        sn_data, lc_data, sp_data = load_sample(sample_name, input_dir=args.input_dir)
        lc_data['lc'] += lc_offset
        sp_data['spec'] += spec_offset
        #        lc['lc'] = lc['lc'] + lc_offset
        #        sp['spec'] = sp['spec'] + spec_offset
        lc_offset = lc_data['lc'].max() + 1
        spec_offset = sp_data['spec'].max() + 1
        
        sne.append(sn_data)
        lc.append(lc_data)
        sp.append(sp_data)

    logging.info('building the uncompressed Training Dataset')        
    tds = TrainingDataset(pandas.concat(sne),
                          pandas.concat(lc),
                          pandas.concat(sp),
                          filterlib=fl)
    tds.compress()
    
    if args.output and args.dump_uncompressed_tds:
        p = Path(args.output)
        if 'parquet' in args.format:
            tds.to_parquet(p.with_suffix('.uncompressed.parquet'))
        elif 'hd5' in args.format or 'hdf' in args.format:
            tds.to_hdf(p.with_suffix('.uncompressed.hd5'))

    logging.info('default model')
    model = salt2.SALT2Like(tds)
    
    logging.info('compression...')
    projected_spectra, in_error = clean_and_project_spectra(tds, model.basis.bx)
    logging.info('done: in_error: {len(in_error)}')

    logging.info(f' -> {args.output}')
    ptds = TrainingDataset(tds.sn_data.nt, lc_data=tds.lc_data.nt,
                           spec_data=np.rec.array(np.hstack(projected_spectra)),
                           basis=model.basis.bx,
                           filterlib=fl)
    
    if args.output:
        p = Path(args.output)
        if 'parquet' in args.format:
            ptds.to_parquet(p.with_suffix('.compressed.parquet'))
        elif 'hd5' in args.format or 'hdf' in args.format:
            ptds.to_hdf(p.with_suffix('.compressed.hd5'))
    
