"""
"""

import numpy as np
from sksparse.cholmod import cholesky_AAt
from . import bspline


def is_list_of_callables(data):
    """check if the data is a list of callables
    """
    # check iterable
    try:
        iter(data)
    except:
        return False
    # check callable
    for t in data:
        if not callable(t):
            return False
    return True


def check_list(data, cond):
    """check if the data is iterable and that all elements satisfy condition cond()
    """
    try:
        iter(data)
    except:
        return False
    # check callable
    for t in data:
        if not cond(t):
            return False
    return True


def refine_grid(grid, scale=0.5):
    dx = (grid[1:] - grid[:-1]).min()
    xmin, xmax = grid.min(), grid.max()
    N = int(np.floor((xmax-xmin)/(scale * dx)))
    return np.linspace(xmin, xmax, N)


class Projector:
    """This class precomputes the projector on a spline basis

    This allows to save many repeated calls to cholesky_AAt

    """
    def __init__(self, basis, grid=None):
        """Constructor

        Build an internal basis, and an internal refinement of the basis grid.
        """
        # internal basis
        if basis is None and grid is not None:
            self.basis = bspline.BSpline(grid)
        elif basis is not None:
            self.basis = basis
        else:
            raise ValueError('no basis passed to constructor')

        # internal grid refinement (may be useful)
        gx = self.basis.grid
        gxx = np.hstack((gx, 0.5*(gx[1:]+gx[:-1])))
        gxx.sort()
        self._grid = gxx

        # compute filter for this grid refinement
        # J = basis.eval(self._grid).tocsr()
        # factor = cholesky_AAt(J.T)
        self._factor, self._J = self._get_projector(self._grid)

    def _get_projector(self, x):
        J = self.basis.eval(x).tocsr()
        factor = cholesky_AAt(J.T)
        return factor, J

    def _compatible_arrays(self, y, x):
        """check if the datset can be projected on our basis
        """
        x = np.atleast_1d(x)
        y = np.atleast_2d(y)
        if x.shape[0] == y.shape[0]:
            return y, x
        elif x.shape[0] == y.shape[1]:
            return y.T, x
        return None, None


    def __call__(self, data, x=None):
        """projects the dataset on the internal spline basis

        The data may either be:

          - a list of callables (e.g. a list of sncosmo.Bandpass objects): each
            callable is then evaluated on refinement of the basis grid, or on
            the `x` array, if specified, and the spline coefficients are derived
            through a least square fit.

          - a 2D array of shape (n,N), along with a corresponding 1D array `x`
            of shape N. Typical use case: bandpass evaluated on the same
            wavelength grid or spectral library data with all spectra sharing
            the same binning.

        """
        # either a list of callables
        if is_list_of_callables(data):
            # if a grid is explicitely specify, let's use ot
            if x is not None:
                factor, J = self._get_projector(x)
                grid = x
            # otherwise, we default to our internal grid
            else:
                factor, J, grid = self._factor, self._J, self._grid
            # evaluate our callables on the grid and project the result
            y = np.vstack([t(grid) for t in data]).T
            ret = factor(J.T @ y)
            return ret

        # or a 2D array of measurements
        yy, xx = self._compatible_arrays(data, x)
        if xx is None or yy is None:
            raise ValueError('incompatible arrays')
        factor, J = self._get_projector(xx)
        ret = factor(J.T @ yy)
        return ret
