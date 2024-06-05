"""
"""

import numpy as np
import pylab as pl
from sksparse.cholmod import cholesky_AAt

import sncosmo

from .bspline import BSpline
from .splineutils import Projector, check_list


__all__ = ['SNFilterSet']


class SNFilterSet:
    """A utility class to handle blueshifted bandpasses projected on a BSpline basis
    """
    def __init__(self, basis=None):
        """Constructor. Build an internal basis and project the filters on it
        """
        # the coefficient database
        # indexed by band name and redshift
        self.db = {}

        # the original transmission db
        self.transmission_db = {}

        # instantiate the basis
        self.basis = None
        if basis is None:
            self.basis = self._default_basis()
        elif isinstance(basis, BSpline):
            self.basis = basis
        elif isinstance(basis, np.ndarray):
            self.basis = BSpline(basis)

        # instantiate the default projector
        self._grid, self._J, self._factor = self._projector(self.basis)

    @property
    def names(self):
        return [bp.name for bp in self.db]

    def __len__(self):
        return len(self.db)

    def __getitem__(self, key):
        if isinstance(key, str):
            key = (key, 0.0)
        if key not in self.db:
            raise KeyError
        return self.db[key]

    @staticmethod
    def _refine_grid(grid):
        """
        """
        gxx = np.hstack((grid, 0.5*(grid[1:]+grid[:-1])))
        gxx.sort()
        return gxx

    def _default_basis(self):
        grid = np.arange(2000., 8510., 10.)
        return BSpline(grid)

    def _compress(self, coeffs, thresh=1.E-9):
        """suppress the very small coefficients of the projection
        """
        if thresh <= 0.:
            return
        c = coeffs / coeffs.max(axis=0)
        idx = np.abs(c) < thresh
        coeffs[idx] = 0.
        return coeffs

    def __getstate__(self):
        """cholmod._factor not serializable. That's why.
        """
        return (self.basis, self.transmission_db, self.db)

    def __setstate__(self, state):
        """cholmod._factor not serializable.
        """
        self.basis, self.transmission_db, self.db = state
        self._grid, self._J, self._factor = self._projector(self.basis)

    @staticmethod
    def bandpass(self, tr):
        pass

    @staticmethod
    def _projector(basis):
        r"""
        Precompute the elements and factorization of the fit matrix

        .. math:: (J^T J)^{-1} J^T

        this saves repeated calls to cholesky_AAt when processing
        other filters.

        Parameters
        ----------
        basis : BSpline
            Spline basis.

        Returns
        -------
        gxx : np.array
            Grid, spline evaluation
        jacobian : scipy.sparse.csr_matrix
            Jacobian matrix.
        factor : sksparse.cholmod.Factor
            Result of cholesky decomposition.
        """
        # refine the basis grid
        gxx = SNFilterSet._refine_grid(basis.grid)

        # precompute the projector
        # (will save repeated calls to cholesky_AAt)
        jacobian = basis.eval(gxx).tocsr()
        factor = cholesky_AAt(jacobian.T)
        return gxx, jacobian, factor

    def insert(self, tr, z=0., x=None, y=None, sensor_id=None, basis=None):
        """Project transmission `tr` on the basis and insert it into the database

        Parameters
        ----------
        tr :
            Filter transmission.
        z : float
            SN redshift.
        x : float (pixels)
            average x-position of the measurement(s)
        y : float (pixels)
            average y-position of the measurement(s)
        sensor_id : int
            sensor_id

        Returns
        -------
        tq : numpy.array
            Transmission for grid of wavelength redshift corrected.
        """
        if basis is None:  # then, use the default basis
            grid, jacobian, factor = self._grid, self._J, self._factor
            basis = self.basis
        else:
            grid, jacobian, factor = self._projector(basis)

        if isinstance(tr, str):
            if x is None or y is None or sensor_id is None:
                tr = sncosmo.get_bandpass(tr)
            else:
                tr = sncosmo.get_bandpass(tr, x=x, y=y, sensor_id=sensor_id)
        else:
            assert isinstance(tr, sncosmo.Bandpass)

        wave = tr.wave
        trans = tr.trans

        y = tr(grid * (1.+z))
        tq = self._compress(factor(jacobian.T * y))

        full_name = tr.name
        self.db[(full_name, z)] = (tq, basis)
        return tq, basis

    def mean_wave(self):
        """return the mean wavelengh of the input filters
        """
        # if list of band passes, just call 'wave_eff' for each one
        if check_list(self.bandpasses, lambda x: hasattr(x, 'wave_eff')):
            return np.array([b.wave_eff for b in self.bandpasses])

        # if a 2D table, compute the mean wavelengths
        tr = self.bandpasses
        wl = self.wave
        return (tr * wl).sum(axis=0) / tr.sum(axis=0)

    def plot_transmissions(self, **kw):
        """plot the contents of the filter set
        """
        figsize = kw.get('figsize', (8,4.5))
        cmap = kw.get('cmap', pl.cm.jet)

        pl.figure(figsize=figsize)
        #     bands = [band_name] if band_name is not None else self.names

        wl = self.mean_wave()

        for i in range(len(self)):
            xx = self._refine_grid()
            J = self.basis.eval(xx)
            col = int(255 * (wl[i]-3000.) / (11000.-3000.))
            pl.plot(xx, J @ self.coeffs[:,i], ls='-', color=cmap(col))
        pl.xlabel('$\lambda [\AA]$')

    def plot(self, **kw):
        """plot the contents of the filter set
        """
        figsize = kw.get('figsize', (8,9))
        cmap = kw.get('cmap', pl.cm.jet)

        pl.figure(figsize=figsize)
        #     bands = [band_name] if band_name is not None else self.names
        pl.imshow(self.coeffs, aspect='auto', interpolation='nearest')
        pl.colorbar()
        pl.xlabel('band')
        pl.ylabel('$\lambda$')
