#!/usr/bin/env python3

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import matplotlib.pyplot as plt

import numpy as np
from bbf import FilterLib, SpecMagsys
import bbf.stellarlib.pickles
import bbf.stellarlib.calspec
from lemaitre import bandpasses


if __name__ == '__main__':

    nmeas = 100_000
    pickles = bbf.stellarlib.pickles.fetch()
    calspec = bbf.stellarlib.calspec.fetch()

    flib = bandpasses.get_filterlib()

    # megacam6, pickles, filter_frame
    if True:
        logging.info('megacam6 mags of pickle stars')
        star = np.random.randint(len(pickles), size=nmeas)
        bands = np.full(nmeas, 'megacam6::g')
        x = np.random.uniform(-110., 110., size=nmeas)
        y = np.random.uniform(-110., 110., size=nmeas)
        sensor_id = np.full(nmeas, 20)
        ms = SpecMagsys()
        pickles_mags = ms.mag(pickles, flib, star, bands, x, y, sensor_id, filter_frame=True)
        logging.info('done')

    # megacam6, calspec, filter_frame
    if True:
        logging.info('megacam6 mags of calspec stars')
        star = np.random.randint(len(calspec), size=nmeas)
        bands = np.full(nmeas, 'megacam6::g')
        x = np.random.uniform(-110., 110., size=nmeas)
        y = np.random.uniform(-110., 110., size=nmeas)
        sensor_id = np.full(nmeas, 20)
        ms = SpecMagsys()
        calspec_mags = ms.mag(calspec, flib, star, bands, x, y, sensor_id, filter_frame=True)
        logging.info('done')

    # megacam6, ccd frame
    if False:
        bands = np.random.choice(list(filter(lambda x: 'megacam6' in x, flib.bandpasses.keys())), size=nmeas)
        x = np.random.uniform(0., 2000, size=nmeas)
        y = np.random.uniform(0., 2000, size=nmeas)
        sensor_id = np.random.randint(1, 36, size=nmeas)

        ms = SpecMagsys()
        mags = ms.mag(pickles, flib, star, bands, x, y, sensor_id, filter_frame=False)

    # plot the magsys zero points
    if True:
        x, y = np.meshgrid(np.linspace(-121., 121., 100), np.linspace(-121., 121., 100))
        x, y = x.ravel(), y.ravel()
        sensor_id = np.full(len(x), 12)
        ms = SpecMagsys()

        for band_name in ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]:
            band = np.full(len(x), band_name)
            ref_zp = ms.zero_points(flib, band, x, y, sensor_id, filter_frame=1)

            plt.figure(figsize=(6, 4.5))
            plt.scatter(x, y, c=ref_zp-ref_zp.mean(), s=10)
            plt.xlabel('$X_{filt} [mm]$')
            plt.ylabel('$Y_{filt} [mm]$')
            plt.colorbar()
            plt.title(f'{band_name}')

    if True:
        N = 100
        x = np.linspace(-120., 120., N)
        y = np.linspace(-120., 120., N)
        sensor_id = np.full(len(x), 12)
        ms = SpecMagsys()

        for band_name in ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]:
            band = np.full(len(x), band_name)
            ref_zp_x = ms.zero_points(flib, band, x, np.zeros(N),
                                      sensor_id, filter_frame=1)
            ref_zp_y = ms.zero_points(flib, band, np.zeros(N), y,
                                      sensor_id, filter_frame=1)
            plt.figure(figsize=(6, 4.5))
            plt.plot(x, ref_zp_x-ref_zp_x.mean(), 'r.-', label='along_x')
            plt.plot(y, ref_zp_y-ref_zp_y.mean(), 'b.-', label='along_y')
            plt.xlabel('$X/Y_{filt} [mm]$')
            plt.ylabel('$zp$')
            plt.title(f'{band_name}')
            plt.legend(loc='best')
