#!/usr/bin/env python3

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

import numpy as np

from lemaitre import bandpasses
import sncosmo
import bbf.stellarlib.pickles
import bbf.stellarlib.calspec
from bbf.filterlib import FilterLib
from bbf.bspline import BSpline



if __name__ == '__main__':

    nmeas = 100_000 # 1_000_000
    bands = ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]
    bands += ['ztf::' + b for b in ['g', 'r', 'I']]
    bands += ['hsc::' + b for b in ['g', 'r', 'r2', 'i', 'i2', 'z', 'Y']]

    # filters
    fl = FilterLib(bands=bands)
    # for band in bands:
    #    fl.insert(band)
    print(fl)

    # pickles and calspec
    pickles = bbf.stellarlib.pickles.fetch(basis=BSpline(np.arange(3000., 10010, 10.)))
    calspec = bbf.stellarlib.calspec.fetch(basis=BSpline(np.arange(3000., 10010, 10.)))

    # computes broadband fluxes in one band (XY variations)
    if 0:
        logging.info('pickles in megacam6::g')
        star = np.random.randint(len(pickles), size=nmeas)
        x = np.random.uniform(-12., 12, size=nmeas)
        y = np.random.uniform(-12., 12., size=nmeas)
        megacam_g_flx = fl['megacam6::g'].flux(pickles, star, x, y, filter_frame=True)

    # compute broadband fluxes in a radially variable band
    if 0:
        logging.info('pickles in hsc::g')#
        star = np.random.randint(len(pickles), size=nmeas)
        x = np.random.uniform(-12., 12, size=nmeas)
        y = np.random.uniform(-12., 12., size=nmeas)
        hsc_g_flx = fl['hsc::g'].flux(pickles, star, x, y, filter_frame=True)

    # compute broadband fluxes (many bands)
    if 1:
        logging.info('pickles -- all bands')
        star = np.random.randint(len(pickles), size=nmeas)
        x = np.random.uniform(-12., 12, size=nmeas)
        y = np.random.uniform(-12., 12., size=nmeas)
        band = np.random.choice(bands, size=nmeas)
        pickles_all_bands = fl.flux(pickles, star, band, x, y, sensor_id=None, filter_frame=True)
        logging.info('done')

    # calspec
    if 1:
        logging.info('calspec -- all bands')
        star = np.random.randint(len(calspec), size=nmeas)
        x = np.random.uniform(-12., 12, size=nmeas)
        y = np.random.uniform(-12., 12., size=nmeas)
        band = np.random.choice(bands, size=nmeas)
        calspec_all_bands_flx = fl.flux(calspec, star, band, x, y, sensor_id=None, filter_frame=True)
        logging.info('done')
