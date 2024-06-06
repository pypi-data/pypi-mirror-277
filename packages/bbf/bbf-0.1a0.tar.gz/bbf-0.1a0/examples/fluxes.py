#!/usr/bin/env python3


from os.path import join as pjoin

import numpy as np
import pandas
from matplotlib import pyplot as plt

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

from lemaitre import bandpasses
from lemaitre.bandpasses import plots as bpplots

import bbf.stellarlib.pickles
import bbf.stellarlib.calspec
from bbf.filterlib import FilterLib
from bbf.bspline import BSpline

try:
    from saunerie.instruments import InstrumentModel, MagSys
    import saunerie.spectrum
    compare_with_saunerie = True
except:
    logging.info('saunerie is not installed - no saunerie-bbf comparison')
    compare_with_saunerie = False

# filter lib
megacam_bands = ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]
ztf_bands = ['ztf::' + b for b in ['g', 'r', 'I']]
hsc_bands = ['hsc::' + b for b in ['g', 'r', 'r2', 'i', 'i2', 'z', 'Y']]

# plots
plots = True


def random_obs(slib, nmeas):
    """
    """
    star = np.random.randint(len(slib), size=nmeas)
    band = np.random.choice(megacam_bands + ztf_bands + hsc_bands, size=nmeas)
    sensor_id = np.zeros(nmeas).astype(int)
    x = np.zeros(nmeas).astype(float)
    y = np.zeros(nmeas).astype(float)

    for b in np.unique(band):
        idx = band == b
        nobs = idx.sum()
        if 'megacam6' in b:
            sensor_id[idx] = np.random.choice(np.arange(0, 36), nobs)
            x[idx] = np.random.uniform(0., 2048, nobs)
            y[idx] = np.random.uniform(0., 4600., nobs)
        if 'hsc' in b:
            a = list(range(0, 104))
            a.remove(9)
            sensor_id[idx] = np.random.choice(a, nobs)
            x[idx] = np.random.uniform(0., 2048, nobs)
            y[idx] = np.random.uniform(0., 4100., nobs)
        if 'ztf' in b:
            sensor_id[idx] = np.random.choice(np.arange(1, 65), nobs)
            x[idx] = np.random.uniform(0., 3072, nobs)
            y[idx] = np.random.uniform(0., 3080., nobs)

    return star, band, x, y, sensor_id


if __name__ == '__main__':

    # should take about 2-3 seconds
    nmeas = 100_000

    # get the filterlib
    flib = bandpasses.get_filterlib()

    # load the pickles library
    pickles = bbf.stellarlib.pickles.fetch()

    # random locations, random bands
    star, band, x, y, sensor_id = random_obs(pickles, nmeas)

    # fluxes in the average bandpasses (no position information)
    logging.info(f'computing {nmeas} broadband fluxes | random bands | no positions')
    flux = flib.flux(pickles, star, band)
    logging.info(f'done')

    # fluxes in a couple of bands only, in the average bandpasses
    logging.info(f'computing {nmeas} broadband fluxes | 3 bands | no positions')
    flux = flib.flux(pickles, star, ['megacam6::g', 'hsc::z', 'ztf::I'])
    logging.info(f'done')

    # fluxes at random locations
    logging.info(f'computing {nmeas} broadband fluxes | random bands | many positions')
    flux = flib.flux(pickles, star, band, x, y, sensor_id)
    logging.info(f'done')

    # fluxes in a couple of bands only
    logging.info(f'computing {nmeas} broadband fluxes | 3 bands | many positions')
    idx = band == 'megacam6::g'
    flux = flib.flux(pickles, star[idx], ['megacam6::g'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    idx = band == 'hsc::z'
    flux = flib.flux(pickles, star[idx], ['hsc::z'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    idx = band == 'ztf::I'
    flux = flib.flux(pickles, star[idx], ['ztf::I'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    logging.info(f'done')

    # fluxes in a couple of bands only
    logging.info(f'computing {nmeas} broadband fluxes | 3 bands | one single position')
    flux = flib.flux(pickles, star, ['megacam6::g', 'hsc::z', 'ztf::I'], x=2., y=2., sensor_id=12)
    logging.info(f'done')

    # fluxes of the first star only,
    logging.info(f'computing {nmeas} broadband fluxes | random bands | no positions | one star')
    flux = flib.flux(pickles, [0], band)
    logging.info(f'done')
