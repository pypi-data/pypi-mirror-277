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
from bbf.magsys import SpecMagsys

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

    # magsys
    ms = SpecMagsys('AB')

    # fluxes in the average bandpasses (no position information)
    logging.info(f'computing {nmeas} broadband fluxes | random bands | no positions')
    mags = ms.mag(flib, pickles, star, band)
    logging.info(f'done')

    # # fluxes in a couple of bands only, in the average bandpasses
    logging.info(f'computing {nmeas} broadband fluxes | 3 bands | no positions')
    mags = ms.mag(flib, pickles, star, ['megacam6::g', 'hsc::z', 'ztf::I'])
    logging.info(f'done')

    # fluxes at random locations
    logging.info(f'computing {nmeas} broadband fluxes | random bands | many positions')
    mags = ms.mag(flib, pickles, star, band, x, y, sensor_id)
    logging.info(f'done')

    # fluxes in a couple of bands only
    logging.info(f'computing {nmeas} broadband fluxes | 3 bands | many positions')
    idx = band == 'megacam6::g'
    mags = ms.mag(flib, pickles, star[idx], ['megacam6::g'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    idx = band == 'hsc::z'
    mags = ms.mag(flib, pickles, star[idx], ['hsc::z'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    idx = band == 'ztf::I'
    mags = ms.mag(flib, pickles, star[idx], ['ztf::I'], x=x[idx], y=y[idx], sensor_id=sensor_id[idx])
    logging.info(f'done')

    # fluxes in a couple of bands only
    # logging.info(f'computing {nmeas} broadband fluxes | 3 bands | one single position')
    # mags = ms.mag(flib, pickles, star, ['megacam6::g', 'hsc::z', 'ztf::I'], x=2., y=2., sensor_id=12)
    # logging.info(f'done')

    # ZTF-color color plot
    logging.info('ZTF color-color plot')
    mags = ms.mag(flib, pickles, star=np.arange(len(pickles)), band=['ztf::g', 'ztf::r', 'ztf::I'])
    mags = pandas.DataFrame(mags, columns=['g', 'r', 'I'])
    plt.figure()
    plt.scatter(mags.g-mags.r, mags.g-mags.I, c=mags.r, s=5)
    plt.xlabel('g-r')
    plt.ylabel('r-I')
    plt.title('ZTF')

    # MegaCam color-color plot
    logging.info('MegaCam6 color-color plot')
    mags = ms.mag(flib, pickles, star=np.arange(len(pickles)), band=['megacam6::' + b for b in ['g', 'r', 'i2', 'z']])
    mags = pandas.DataFrame(mags, columns=['g', 'r', 'i2', 'z'])
    plt.figure()
    plt.scatter(mags.g-mags.r, mags.r-mags.i2, c=mags.r, s=5)
    plt.xlabel('g-r')
    plt.ylabel('r-i2')
    plt.title('MegaCam6')

    # HSC color-color plot
    logging.info('HSC color-color plot')
    mags = ms.mag(flib, pickles, star=np.arange(len(pickles)), band=['hsc::' + b for b in ['g', 'r2', 'i2', 'z', 'Y']])
    mags = pandas.DataFrame(mags, columns=['g', 'r2', 'i2', 'z', 'Y'])
    plt.figure()
    plt.scatter(mags.g-mags.r2, mags.r2-mags.i2, c=mags.r2, s=5)
    plt.xlabel('g-r2')
    plt.ylabel('r2-i2')
    plt.title('HSC')

    # MegaCam magnitude uniformity
    logging.info('MegaCam6 mag uniformity')
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,10), sharex=True, sharey=True)
    x, y, sensor_id = bpplots.megacam_xyccd(delta=200)
    bp = flib[('megacam6::g', '*')]
    X, Y = bp.to_focalplane(x, y, sensor_id)

    star = np.full(len(x), 12)
    for i,band in enumerate(['megacam6::g', 'megacam6::r', 'megacam6::i2', 'megacam6::z']):
        logging.info(f'computing {len(x)} broadband mags')
        mags = ms.mag(flib, pickles, star=star, band=band, x=x, y=y, sensor_id=sensor_id)
        logging.info('done')
        ii, jj = int(i/2), int(i%2)
        c = axes[ii,jj].scatter(X, Y, c=mags, s=5)
        if ii == 1:
            axes[ii,jj].set_xlabel('X')
        if jj == 0:
            axes[ii,jj].set_ylabel('Y')
        plt.colorbar(c, ax=axes[ii,jj])
        axes[ii,jj].set_title(band)

    # HSC magnitude uniformity
    logging.info('HSC mag uniformity')
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12,10), sharex=True, sharey=True)
    x, y, sensor_id = bpplots.hsc_xyccd(delta=200)
    bp = flib[('hsc::g', '*')]
    X, Y = bp.to_focalplane(x, y, sensor_id)

    star = np.full(len(x), 12)
    for i,band in enumerate(['hsc::g', 'hsc::r', 'hsc::r2', 'hsc::i', 'hsc::i2', 'hsc::z', 'hsc::Y']):
        logging.info(f'computing {len(x)} broadband mags')
        mags = ms.mag(flib, pickles, star=star, band=band, x=x, y=y, sensor_id=sensor_id)
        logging.info('done')
        ii, jj = int(i/3), int(i%3)
        c = axes[ii,jj].scatter(X, Y, c=mags, s=5)
        if ii == 1:
            axes[ii,jj].set_xlabel('X')
        if jj == 0:
            axes[ii,jj].set_ylabel('Y')
        plt.colorbar(c, ax=axes[ii,jj])
        axes[ii,jj].set_title(band)

    # ZTF magnitude uniformity
    logging.info('ZTF mag uniformity')
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,10), sharex=True, sharey=True)
    x, y, sensor_id = bpplots.ztf_xyccd(delta=200)
    bp = flib[('ztf::g', 12)]
    X, Y = bp.to_focalplane(x, y, sensor_id)

    star = np.full(len(x), 12)
    for i,band in enumerate(['ztf::g', 'ztf::r', 'ztf::I']):
        logging.info(f'computing {len(x)} broadband mags')
        mags = ms.mag(flib, pickles, star=star, band=band, x=x, y=y, sensor_id=sensor_id)
        logging.info('done')
        ii, jj = int(i/2), int(i%2)
        c = axes[ii,jj].scatter(X, Y, c=mags, s=5)
        if ii == 1:
            axes[ii,jj].set_xlabel('X')
        if jj == 0:
            axes[ii,jj].set_ylabel('Y')
        plt.colorbar(c, ax=axes[ii,jj])
        axes[ii,jj].set_title(band)
