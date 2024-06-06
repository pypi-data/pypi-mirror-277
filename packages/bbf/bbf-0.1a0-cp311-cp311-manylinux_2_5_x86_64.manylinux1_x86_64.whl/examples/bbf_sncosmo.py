#!/usr/bin/env python3

import numpy as np
import pandas
from matplotlib import pyplot as plt

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

from astropy.table import Table
from gaiaxpy import calibrate

import sncosmo
from sncosmo import specmodel

from lemaitre import bandpasses

import bbf.stellarlib.pickles
import bbf.stellarlib.calspec
from bbf.filterlib import FilterLib
from bbf.bspline import BSpline



# filter lib
bands = ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]

# plots
plots = True


if __name__ == '__main__':

    nmeas = 10000
    nbands = len(bands)
    x_ref = 11.2
    y_ref = -1.2

    logging.info('filterlib')
    fl = FilterLib(basis=np.arange(3000., 11010., 10.))
    fl.insert('megacam6::g', xy_size=40, xy_order=4)
    fl.insert('megacam6::r', xy_size=20, xy_order=2)
    fl.insert('megacam6::i2', xy_size=20, xy_order=2)
    fl.insert('megacam6::z', xy_size=20, xy_order=2)

    logging.info('pickles')
    pickles = bbf.stellarlib.pickles.fetch(basis=BSpline(np.arange(3000., 11010., 10.)))
    # pickles = bbf.stellarlib.calspec.fetch(basis=BSpline(np.arange(3000., 11010., 10.)))

    # bbf fluxes
    logging.info('bbf fluxes')
    star = np.tile(np.arange(len(pickles)), nbands)
    x = np.tile(np.full(len(pickles), x_ref), nbands)
    y = np.tile(np.full(len(pickles), y_ref), nbands)
    band_names = np.repeat(bands, len(pickles))

    flx = fl.flux(pickles, star, band_names, x, y, filter_frame=True)
    flx = flx.reshape((nbands,-1)).T
    logging.info('done.')


    # sncosmo fluxes
    logging.info('sncosmo fluxes')
    sncosmo_bands = dict([(bn, sncosmo.get_bandpass(bn,
                           x=x_ref, y=y_ref, sensor_id=1,
                           filter_frame=True)) for bn in bands])
    sncosmo_fluxes = dict([bn, []] for bn in bands)
    for index, d in pickles.data.iterrows():
        sp = sncosmo.specmodel.SpectrumModel(d.wave, d.flux)
        m_b = {}
        for bn,b in sncosmo_bands.items():
            try:
                m_b[bn] = -2.5 * np.log10(sp.bandflux(b))
            except:
                m_b[bn] = 0.
        for bn in sncosmo_bands:
            sncosmo_fluxes[bn].append(m_b[bn])
    logging.info('done')

    # dataframe
    df = pandas.DataFrame(sncosmo_fluxes)
    df['bbf_g'] = -2.5 * np.log10(flx[:,0])
    df['bbf_r'] = -2.5 * np.log10(flx[:,1])
    df['bbf_i2'] = -2.5 * np.log10(flx[:,2])
    df['bbf_z'] = -2.5 * np.log10(flx[:,3])

    idx = df['megacam6::g'] == 0.
    df = df[~idx]

    # plots
    fig, axes = plt.subplots(figsize=(8,8), nrows=2, ncols=2,
                             sharex=True, sharey=True)
    axes[0,0].plot(df['bbf_g'] - df['megacam6::g'], 'b.')
    axes[0,0].set_ylabel('$\delta g$')
    axes[0,1].plot(df['bbf_r'] - df['megacam6::r'], 'g.')
    axes[0,1].set_ylabel('$\delta r$')
    axes[1,0].plot(df['bbf_i2'] - df['megacam6::i2'], 'r.')
    axes[1,0].set_ylabel('$\delta i2$')
    axes[1,0].set_xlabel('star')
    axes[1,1].plot(df['bbf_z'] - df['megacam6::z'], marker='.', color='purple', ls='')
    axes[1,1].set_ylabel('$\delta z$')
    axes[1,1].set_xlabel('star')
    fig.suptitle('$\Delta m$ [bbf-sncosmo] vs star index')

    fig, axes = plt.subplots(figsize=(8,8), nrows=2, ncols=2,
                             sharex=True, sharey=True)
    col = df['megacam6::g'] - df['megacam6::i2']
    dm = df['bbf_g'] - df['megacam6::g']
    axes[0,0].plot(col, dm - dm.mean(), 'b.')
    axes[0,0].set_ylabel('$\delta g$')
    dm = df['bbf_r'] - df['megacam6::r']
    axes[0,1].plot(col, dm - dm.mean(), 'g.')
    axes[0,1].set_ylabel('$\delta r$')
    dm = df['bbf_i2'] - df['megacam6::i2']
    axes[1,0].plot(col, dm - dm.mean(), 'r.')
    axes[1,0].set_ylabel('$\delta i2$')
    dm = df['bbf_z'] - df['megacam6::z']
    axes[1,0].set_xlabel('$g-i$')
    axes[1,1].plot(col, dm - dm.mean(), marker='.', color='purple', ls='')
    axes[1,1].set_ylabel('$\delta z$')
    axes[1,1].set_xlabel('$g-i$')
    fig.suptitle('$\Delta m$ [bbf-sncosmo] vs $g-i$')
