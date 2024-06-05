#!/usr/bin/env python3



from os.path import join as pjoin

import numpy as np
import pandas
from matplotlib import pyplot as plt

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

from astropy.table import Table
from gaiaxpy import calibrate

import sncosmo
from sncosmo.bandpasses import _BANDPASS_INTERPOLATORS
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


def get_color(wl):
    i = int(256 * (wl-3000.)/(10000.-3000.))
    return plt.cm.jet(i)


def draw_average_bandpasses(band_names):
    """
    """
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,8), sharex=True)

    flib = bandpasses.get_filterlib()
    wl = np.arange(3000., 11000., 10.)
    for band_name in band_names:
        bp = flib[band_name]
        tr = bp(wl)
        wl_eff = (tr*wl).sum() / tr.sum()
        axes[0].plot(wl, bp(wl), ls='-', marker='.', color=get_color(wl_eff), label=f'{band_name} [bbf]')
        sncosmo_bp = sncosmo.get_bandpass(band_name)
        axes[0].plot(wl, sncosmo_bp(wl), ls=':', marker='', color='gray', label=f'{band_name} [sncosmo]')
        axes[0].legend(loc='best')
        axes[1].plot(wl, tr-sncosmo_bp(wl), ls='-', marker='.', color=get_color(wl_eff), label=f'$\Delta{band_name}$ [bbf-sncosmo]')
    axes[1].set_xlabel('$\lambda [nm]$')


def draw_bandpass_mean_wavelength(band_name):
    """
    """
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16,4), sharey=True)

    flib = bandpasses.get_filterlib()
    wl = np.arange(3000., 11000., 10.)

    if 'ztf' in band_name:
        x, y, sensor_id = bpplots.ztf_xyccd(delta=100)
        bp = flib[('ztf::g', 1)]
        X, Y = bp.to_focalplane(x, y, sensor_id)
    elif 'hsc' in band_name:
        x, y, sensor_id = bpplots.hsc_xyccd(delta=100)
        bp = flib[('hsc::g', '*')]
        X, Y = bp.to_focalplane(x, y, sensor_id)
    elif 'megacam' in band_name:
        x, y, sensor_id = bpplots.megacam_xyccd(delta=100)
        bp = flib[('megacam6::g', '*')]
        X, Y = bp.to_focalplane(x, y, sensor_id)

    flib_tr = sncosmo.get_bandpass(band_name, x=x, y=y, sensor_id=sensor_id, wave=wl)
    bbf_wave_eff = (flib_tr * wl).sum(axis=1) / flib_tr.sum(axis=1)
    c = axes[0].scatter(X, Y, c=bbf_wave_eff, s=1)
    axes[0].set_title(f'{band_name} [bbf]')
    plt.colorbar(c, ax=axes[0])

    sncosmo_tr = sncosmo.get_bandpass(band_name, x=x, y=y, sensor_id=sensor_id, wave=wl)
    sncosmo_wave_eff = (sncosmo_tr * wl).sum(axis=1) / sncosmo_tr.sum(axis=1)
    c = axes[1].scatter(X, Y, c=sncosmo_wave_eff, s=1)
    axes[1].set_title(f'{band_name} [sncosmo]')
    plt.colorbar(c, ax=axes[1])

    sncosmo_tr = sncosmo.get_bandpass(band_name, x=x, y=y, sensor_id=sensor_id, wave=wl)
    wave_eff = (sncosmo_tr * wl).sum(axis=1) / sncosmo_tr.sum(axis=1)
    c = axes[2].scatter(X, Y, c=bbf_wave_eff-sncosmo_wave_eff, s=1)
    axes[2].set_title(f'{band_name} [bbf-sncosmo]')
    plt.colorbar(c, ax=axes[2])



# if __name__ == '__main__':

#     flib = bandpasses.get_filterlib()


#     x, y, sensor_id = -12.,  11., 12
#     x, y, sensor_id =   0.,   0., 12
#     x, y, sensor_id =   8., -10., 12

#     # filters
#     logging.info('loading FilterLib')
#     fl = FilterLib(basis=np.arange(3000., 11000., 5.))
#     fl.insert('megacam6::g', xy_size=40, xy_order=4)
#     fl.insert('megacam6::r', xy_size=20, xy_order=2)
#     fl.insert('megacam6::i2', xy_size=20, xy_order=2)
#     fl.insert('megacam6::z', xy_size=20, xy_order=2)
#     #    for band in bands:
#     #        fl.insert(band)
#     logging.info('done.')


#     # comuting fluxes with saunerie
#     logging.info('saunerie fluxes')
#     instrument = InstrumentModel('MEGACAM6')
#     filt = [instrument.get_efficiency(band, focal_plane_position=(x, y))
#             for band in ['g', 'r', 'i2', 'z']]

#     if plots:
#         wl = np.arange(3000., 11000., 1.)
#         fig, axes = plt.subplots(figsize=(12,8), nrows=3, ncols=1, sharex=True)

#         tr_g_saunerie = filt[0](wl)
#         interp_g_sncosmo = _BANDPASS_INTERPOLATORS.retrieve('megacam6::g')
#         tr_g_sncosmo = interp_g_sncosmo.eval_at(x, y, sensor_id, wl=wl, filter_frame=1).squeeze()
#         tr_g_bbf = fl['megacam6::g'](x, y, wl)
#         axes[0].plot(wl, tr_g_saunerie, 'b--', label='saunerie')
#         axes[0].plot(wl, tr_g_bbf, 'k.', label='bbf')
#         axes[0].plot(wl, tr_g_sncosmo, 'b-.', label='sncosmo')
#         axes[0].legend(loc='best')
#         axes[1].plot(wl, tr_g_bbf-tr_g_saunerie, 'b.', label='bbf-saunerie')
#         axes[1].legend(loc='best')
#         axes[2].plot(wl, tr_g_bbf-tr_g_sncosmo, 'b.', label='bbf-sncosmo')
#         axes[2].legend(loc='best')

#         tr_r_saunerie = filt[1](wl)
#         interp_r_sncosmo = _BANDPASS_INTERPOLATORS.retrieve('megacam6::r')
#         tr_r_sncosmo = interp_r_sncosmo.eval_at(x, y, sensor_id, wl=wl, filter_frame=1).squeeze()
#         tr_r_bbf = fl['megacam6::r'](x, y, wl)
#         axes[0].plot(wl, tr_r_saunerie, 'g--')
#         axes[0].plot(wl, tr_r_sncosmo, 'g-.')
#         axes[0].plot(wl, tr_r_bbf, 'k.')
#         axes[1].plot(wl, tr_r_bbf-tr_r_saunerie, 'g.')
#         axes[2].plot(wl, tr_r_bbf-tr_r_sncosmo, 'g.')

#         tr_i2_saunerie = filt[2](wl)
#         interp_i2_sncosmo = _BANDPASS_INTERPOLATORS.retrieve('megacam6::i2')
#         tr_i2_sncosmo = interp_i2_sncosmo.eval_at(x, y, sensor_id, wl=wl, filter_frame=1).squeeze()
#         tr_i2_bbf = fl['megacam6::i2'](x, y, wl)
#         axes[0].plot(wl, tr_i2_saunerie, 'r--')
#         axes[0].plot(wl, tr_i2_sncosmo, 'r-.')
#         axes[0].plot(wl, tr_i2_bbf, 'k.')
#         axes[1].plot(wl, tr_i2_bbf-tr_i2_saunerie, 'r.')
#         axes[2].plot(wl, tr_i2_bbf-tr_i2_sncosmo, 'r.')

#         tr_z_saunerie = filt[3](wl)
#         interp_z_sncosmo = _BANDPASS_INTERPOLATORS.retrieve('megacam6::z')
#         tr_z_sncosmo = interp_z_sncosmo.eval_at(x, y, sensor_id, wl=wl, filter_frame=1).squeeze()
#         tr_z_bbf = fl['megacam6::z'](x, y, wl)
#         axes[0].plot(wl, tr_z_saunerie, ls='--', color='purple')
#         axes[0].plot(wl, tr_z_sncosmo, ls='-.', color='purple')
#         axes[0].plot(wl, tr_z_bbf, 'k.')
#         axes[1].plot(wl, tr_z_bbf-tr_z_saunerie, marker='.', color='purple')
#         axes[2].plot(wl, tr_z_bbf-tr_z_sncosmo, marker='.', color='purple')

#         plt.subplots_adjust(hspace=0.05)
#         axes[2].set_xlabel('$\lambda\ \ [\AA]$')
#         axes[0].set_ylabel('$T(\lambda)$')
#         axes[1].set_ylabel('$\Delta T(\lambda)$ [bbf-saunerie]')
#         axes[2].set_ylabel('$\Delta T(\lambda)$ [bbf-sncosmo]')
#         axes[1].sharey(axes[2])
