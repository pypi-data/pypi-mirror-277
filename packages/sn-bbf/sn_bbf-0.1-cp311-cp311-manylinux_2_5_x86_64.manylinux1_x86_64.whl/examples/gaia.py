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
from lemaitre import bandpasses

import bbf.stellarlib.pickles
import bbf.stellarlib.calspec
from bbf.filterlib import FilterLib
from bbf.bspline import BSpline

from saunerie.instruments import InstrumentModel, MagSys
import saunerie.spectrum

# filter lib
bands = ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]

# plots
plots = True


if __name__ == '__main__':

    x_ref = -0.
    y_ref = -0.
    sensor_id = 1

    # filters
    logging.info('loading FilterLib')
    fl = FilterLib(basis=np.arange(3000., 11000., 5.))
    for band in bands:
        fl.insert(band)

    # gaia
    logging.info('loading GAIA')
    field = "P330E"
    gaia_dir = "/home/nrl/lemaitre/pipeline/bbf/notebooks"
    gaia_spectra = pjoin(gaia_dir, f'dr3_{field}_spectra.csv')
    calibrated_spectra, sampling = calibrate(gaia_spectra)

    index = np.arange(len(calibrated_spectra))
    wave = [sampling*10 for s in calibrated_spectra['flux'][index[index != -1]]] #nm to A
    flux = [s*100 for s in calibrated_spectra['flux'][index[index != -1]]]
    data = pandas.DataFrame({'wave':wave, 'flux':flux})
    gaia = bbf.StellarLib(data, basis=np.arange(3000., 11000., 5.), project=False) # 2 nm

    logging.info('//')
    t = []
    for i in range(len(gaia.data)):
        sp = gaia.data.iloc[i]
        t.append(gaia.basis.linear_fit(sp.wave, sp.flux, beta=1.E-6))
    gaia.coeffs = np.vstack(t).T


    # comuting fluxes with saunerie
    logging.info('saunerie fluxes')
    instrument = InstrumentModel('MEGACAM6')
    magsys = MagSys("AB")
    mags_ = []
    for s in calibrated_spectra['flux'][index[index != -1]]:
        spectrum = saunerie.spectrum.Spectrum(sampling *10, s*100)
        if 0:#0at_position:
            filt = [instrument.get_efficiency(band,
                                              focal_plane_position=(star[f'xfilter_{band}'],
                                                                    star[f'yfilter_{band}']))                    for band in ['g', 'r', 'i2', 'z']]
        else:
            filt = [instrument.get_efficiency(band,focal_plane_position=(x_ref, y_ref))
                    for band in ['g', 'r', 'i2', 'z']]
        mags_.append(magsys.mag(filt, spectrum))

    saunerie_mags = np.hstack(mags_)
    logging.info('done.')

    # computing fluxes with bbf
    logging.info('bbf.fluxes')
    N = len(gaia)
    x = np.full(4*N, x_ref) # np.zeros(4 * N)
    y = np.full(4*N, y_ref) # np.zeros(4 * N)
    star = np.tile(np.arange(N), 4)
    band = np.repeat(bands, N)
    fluxes = fl.flux(gaia, star, band, x, y, filter_frame=True)
    bbf_mags = -2.5 * np.log10(fluxes)
    logging.info('done.')
    # bbf_mags.reshape((-1,4))
    bbf_mags = np.core.records.fromarrays(bbf_mags.reshape(4,-1), names=['g', 'r', 'i2', 'z'])

    if plots:
        fig, axes = plt.subplots(figsize=(16,9), nrows=2, ncols=2)
        axes[0,0].plot(saunerie_mags['g'], bbf_mags['g']-saunerie_mags['g'], 'b.')
        axes[0,0].set_title('g')
        axes[0,0].set_xlabel('$g_{saunerie}$')
        axes[0,0].set_ylabel('$g_{bbf}-g_{saunerie}$')

        axes[0,1].plot(saunerie_mags['r'], bbf_mags['r']-saunerie_mags['r'], 'g.')
        axes[0,1].set_title('r')
        axes[0,1].set_xlabel('$r_{saunerie}$')
        axes[0,1].set_ylabel('$r_{bbf}-r_{saunerie}$')

        axes[1,0].plot(saunerie_mags['i2'], bbf_mags['i2']-saunerie_mags['i2'], 'r.')
        axes[1,0].set_title('i2')
        axes[1,0].set_xlabel('$i2_{saunerie}$')
        axes[1,0].set_ylabel('$i2_{bbf}-i2_{saunerie}$')

        axes[1,1].plot(saunerie_mags['z'], bbf_mags['z']-saunerie_mags['z'], color='purple', marker='.', ls='')
        axes[1,1].set_title('z')
        axes[1,1].set_xlabel('$z_{saunerie}$')
        axes[1,1].set_ylabel('$z_{bbf}-z_{saunerie}$')

    if plots:
        fig, axes = plt.subplots(figsize=(16,9), nrows=2, ncols=2)
        dm = bbf_mags['g']-saunerie_mags['g']
        axes[0,0].plot(saunerie_mags['g']-saunerie_mags['i2'], dm-dm[~np.isnan(dm)].mean(), 'b.')
        axes[0,0].set_title('g')
        axes[0,0].set_xlabel('$g-i2$')
        axes[0,0].set_ylabel('$g_{bbf}-g_{saunerie}$')

        dm = bbf_mags['r']-saunerie_mags['r']
        axes[0,1].plot(saunerie_mags['g']-saunerie_mags['i2'], dm-dm.mean(), 'g.')
        axes[0,1].set_title('r')
        axes[0,1].set_xlabel('$g-i2$')
        axes[0,1].set_ylabel('$r_{bbf}-r_{saunerie}$')

        dm = bbf_mags['i2']-saunerie_mags['i2']
        axes[1,0].plot(saunerie_mags['g']-saunerie_mags['i2'], dm-dm.mean(), 'r.')
        axes[1,0].set_title('i2')
        axes[1,0].set_xlabel('$g-i2$')
        axes[1,0].set_ylabel('$i2_{bbf}-i2_{saunerie}$')

        dm = bbf_mags['z']-saunerie_mags['z']
        axes[1,1].plot(saunerie_mags['g']-saunerie_mags['i2'], dm-dm.mean(), color='purple', marker='.', ls='')
        axes[1,1].set_title('z')
        axes[1,1].set_xlabel('$g-i2$')
        axes[1,1].set_ylabel('$z_{bbf}-z_{saunerie}$')

        axes[0,0].set_ylim((-0.003, 0.003))
        axes[0,1].set_ylim((-0.003, 0.003))
        axes[1,0].set_ylim((-0.003, 0.003))
        axes[1,1].set_ylim((-0.003, 0.003))
