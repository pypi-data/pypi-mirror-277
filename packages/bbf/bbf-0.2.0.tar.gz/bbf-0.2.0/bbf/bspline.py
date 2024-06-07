"""
Implementation of 1-D and 2-D B-spline bases.


.. note: on the grids on which the B-Splines are defined
      -----+------+--- ... --+-----+--- ... -----+-----+--
          -k    -k+1         0     1             N    
                             [ specified by user ]
           [       internal, extended grid       ]

.. examples:




"""

import ctypes
import os 
import os.path as op
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse import csr_matrix, coo_matrix
import scipy.sparse as sparse
import scipy.sparse.linalg
try:
    from scipy.special import comb
except:
    from scipy.misc import comb

try:
    from sksparse.cholmod import cholesky_AAt
except ImportError:
    from scikits.sparse.cholmod import cholesky_AAt



# from . import linearmodels as lm
#from exceptions import LookupError, NotImplementedError

# from IPython import embed 

_lib = np.ctypeslib.load_library('_libbbf', op.dirname(op.abspath(__file__)))
_blossom = _lib.blossom
_blossom.restype = None
_blossom.argtypes = [
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous, writeable'),
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous, writeable'),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int]

_binary_search_with_guess = _lib.binary_search_with_guess
_binary_search_with_guess.restype = np.int32
_binary_search_with_guess.argtypes = [
    ctypes.c_double,
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    ctypes.c_int]

_binary_search = _lib.binary_search
_binary_search.restype = None
_binary_search.argtypes = [
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int]

_blossom_grid = _lib.blossom_grid
_blossom_grid.restype = None
_blossom_grid.argtypes = [
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int]

_deriv_grid = _lib.deriv_grid
_deriv_grid.restype = None
_deriv_grid.argtypes = [
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(np.int32, ndim=1, flags='aligned, contiguous'),
    np.ctypeslib.ndpointer(np.double, ndim=1, flags='aligned, contiguous'),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int]


class BSpline(object):
    """1-dimensional B-Spline basis
    
    Implements a 1D-BSpline basis, of arbitrary order, defined on an
    arbitrary grid.
    """
    def __init__(self, grid, order=4):
        self.order=order
        assert self._monotonic_grid(grid)        
        # n_knots is misleading - this should be called n_edges
        # or we could use n_intervals = len(grid) - 1
        self.n_knots = len(grid)
        # if we had n_invervals, then 
        #        self.nj = self.n_intervals + self.order - 1
        # with n_knots, we have:
        self.nj = self.n_knots + self.order - 2
        self.range = grid.min(), grid.max()
        # internally, the grid must be extended
        self._grid = self._extend_grid(grid)
        
    def _monotonic_grid(self, grid):
        d = grid[1:]-grid[:-1]
        if np.sum(d<0) > 0:
            return False
        return True
        
    def _extend_grid(self, grid):
        dx = grid[1]-grid[0]
        p = np.arange(1., self.order)
        pre = -p[::-1] * dx + grid[0]
        dx = grid[-1] - grid[-2]
        post = p * dx + grid[-1]
        return np.hstack((pre, grid, post))

    @property
    def grid(self):
        """the spline intervals, as seen by the user of the class
        """
        return self._grid[self.order-1:-self.order+1]
        
    def __len__(self):
        return self.nj

    def eval(self, x):
        """evaluate the value of the basis functions for each element of x

        Evaluate the 
        
        Args:
            x (ndarray of floats): the values of x

        Returns:
            scipy.sparse.coo_matrix: a sparse, N x p jacobian matrix 
            [N=len(x), p=len(self)] containing the basis values 
            :math:`B_{ij} = B_j(x_i)`

        .. note:  The jacobian matrix triplets are sorted as follows:
            [i=0   j=p      B_p(x_0)      ]  p, lowest integer / B_p(x_i) > 0
            [i=0   j=p+1    B_{p+1}(x_0)  ]
            [i=0   j=p+deg  B_{p+deg}(x_0)]
            [i=1   j=q      B_q(x_1)      ]
                ...    
            The BSpline2.eval function (in fact. BSpline2._cross)
            assumes that order to compute the tensor product of the 1D
            basis elements.
          
            Note also that the old, pure python version of
            CardinalBSpline.eval also returns ordered triplets, but
            the ordering was different.
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N, dtype=np.float64)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        _blossom_grid(self._grid, len(self._grid), 
                      x, nx, 
                      i, j, B, N, 
                      self.order, self.order, self.nj)
        return coo_matrix((B, (i,j)), shape=(nx, self.nj))
    
    def deriv(self, x, dtype=np.float64):
        """
        evaluate the first derivative of the basis functions for each element of x
        
        Args:
           x: (ndarray of floats) 
       
        Returns:
           a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
           (contains the values of the derivatives)
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N, dtype=np.float64)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        _blossom_grid(self._grid, len(self._grid), 
                      x, nx, 
                      i, j, B, N, 
                      self.order-1, self.order, self.nj)
        _deriv_grid(self._grid, len(self._grid),
                    i, j, B, N,
                    nx, self.order)        
        return coo_matrix((B, (i,j)), shape=(nx, self.nj))
        

    def deriv_m(self, x, m=2, dtype=np.float64):
        """
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N, dtype=dtype)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        if (self.order - m) <= 0:
            return coo_matrix((B, (i,j)), shape=(nx, self.nj))
        _blossom_grid(self._grid, len(self._grid), 
                      x, nx, 
                      i, j, B, N, 
                      self.order-m, self.order, self.nj)
        # _deriv_basis derives B once, need to derive it m times
        # formula in book differentiates the spline in it's entirety but not just the basis
        return coo_matrix((B, (i,j)), shape=(nx, self.nj))
        #pass
    
    def gram(self, dtype=np.float64):
        """Compute the gramian matrix of the base elements. 

        The gramian is defined by:
        :math:`G_{ij} = \int B_i(x) B_j(x) dx`

        Args:
           dtype: Gramian dtype (np.float32 or np.float64)

        Returns:
           scipy.sparse.coo_matrix: a sparse p x p matrix [p=len(self)]
                                   containing the gramian values
        """
        p, w = leggauss(self.order)
        g = self._grid
        # linear transform grid-elements -> [-1,1]
        ak = np.repeat(0.5 * (g[1:]-g[:-1]), self.order)
        bk = np.repeat(0.5 * (g[1:]+g[:-1]), self.order)
        # integration grid 
        nk = len(g) - 1
        pp = np.tile(p, nk)
        pp = ak*pp+bk
        # weights
        ww = np.tile(w, nk)
        N = len(ww)
        i = np.arange(N)
        W = coo_matrix((ak*ww, (i,i)), shape=(N,N))
        B = self.eval(pp)
        return B.T * W * B

    def __call__(self, x, p, deriv=0):
        if deriv == 0:
            B = self.eval(x)
        elif deriv == 1:
            B = self.deriv(x)
        else:
            B = self.deriv_m(x, m=deriv)
        return B * p

    def linear_fit(self, x, y, w=None, beta=None):
        # we now use cholmod, since it behaves much better than
        # scipy.sr parse.linalg.spsolve when the size of the basis increases
        # this is especially important in 2D (see below)
        J = self.eval(x).tocsr()
        if w is not None:
            J.data *= w[J.row]
            yy = w * y
        else:
            yy = y
        factor = cholesky_AAt(J.T, beta=beta)
        return factor(J.T * yy)


class BSpline2D(object):
    """
    2D BSpline basis of arbitrary order, 
    defined on an arbitrary grid

    The basis is the cross-product of two 1D BSpline bases, along x and y:

    .. math::
       B_{ij} = B_i(x) \\times B_j(y)
    """
    def __init__(self, gx, gy, x_order=4, y_order=4):
        self.bx = BSpline(gx, order=x_order)
        self.by = BSpline(gy, order=y_order)
        self.nj = self.bx.nj * self.by.nj
        
    def __len__(self):
        """
        return the size of the basis
        """
        return self.nj

    def _cross(self, N, ix, jx, vx, iy, jy, vy):
        """
        compute the cross-product: 

        .. math::
           B_{ij}(x,y) = B_i(x) \times B_j(y)

        Args:
          N: (int) 
             number of points (N=len(x))
          i: ndarray of ints 
             a ndarray containing the row-indices in the jacobian matrix
          jx: ndarray of ints 
              the column indices in the matrix returned by the x-basis 
          vx: ndarray of floats, 
              the values B_j(x)
          jy: ndarray of ints 
              the column indices in the matrix returned by the y-basis 
          vy: ndarray of floats
              the values B_j(y)

        Returns:
          J: (scipy.sparse.coo_matrix) 
              the values of the cross-product as a (N,n) sparse jacobian matrix, 
              [N is the number of points, n the size of the 2D-basis]

        Note:
          This implementation makes an assumption on how the return value 
          of ``BSpline.eval'' is sorted internally.  
          See the documentation of this routine above.           

        TODO: 
          One could gain ~ a factor 2 in execution time, by implementing 
          the tile's and repeat's in C.
        """
        
        xo, yo = self.bx.order, self.by.order
        
        i_   = ix.reshape(-1,xo).repeat(yo,axis=1).ravel()
        jx_  = jx.reshape(-1,xo).repeat(yo,axis=1).ravel()
        vx_  = vx.reshape(-1,xo).repeat(yo,axis=1).ravel()
        jy_  = np.tile(jy.reshape(-1,yo), (1,xo)).ravel()
        vy_  = np.tile(vy.reshape(-1,yo), (1,xo)).ravel()        
        data_ = vx_ * vy_
        j_ = jy_ * self.bx.nj + jx_
        return coo_matrix((data_, (i_,j_)),
                          shape=(N,self.nj))
    
    def eval(self, x, y):
        """
        evaluate and return the values of the basis functions for (x,y)
        
        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          B: (scipy.sparse.coo_matrix)
              a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
              containing the basis values: B_{ij} = B_j(x_i)
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        Jx = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jy = self.by.eval(y)        
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None        
        #        embed()
        r = self._cross(N, ix, jx, vx, iy, jy, vy)
        return r
        
    def gradient(self, x, y):
        """
        evaluate and return the derivatives vs. x and y of the basis functions for (x,y)
        
        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          dvdx: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j'(x_i) * B_j(y_i)
          dvdy: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j(x_i) * B_j'(y_i)
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        
        Jxp = self.bx.deriv(x)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy  = self.by.eval(y)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx = self._cross(N, ix, jx, vx, iy, jy, vy)
        
        ix = jx = vx = None
        iy = jy = vy = None
        
        Jx  = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jyp = self.by.deriv(y)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy = self._cross(N, ix, jx, vx, iy, jy, vy)
        
        return ddx, ddy        
        
    def hessian(self, x, y, dtype=np.float32):
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        
        Jxp = self.bx.deriv_m(x, m=2, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy  = self.by.eval(y, dtype=dtype)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        ix = jx = vx = None
        iy = jy = vy = None
        
        Jx = self.bx.eval(x, dtype=dtype)
        ix, jx, vx = Jx.row, Jx.col, Jx.data 
        Jx = None
        Jyp = self.by.deriv_m(y, m=2, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)

        ix = jx = vx = None
        iy = jy = vy = None
        
        Jxp = self.bx.deriv_m(x, m=1, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jyp = self.by.deriv_m(y, m=1, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddxy = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        return ddx2, ddy2, ddxy

        #raise NotImplementedError('BSpline2D.hessian not implemented (yet)')

    def laplacian(self, x, y):
        raise NotImplementedError('BSpline2D.hessian not implemented (yet)')

    def __call__(self, x, y, p, deriv=0):
        if deriv == 0:
            B = self.eval(x,y)
        elif deriv == 1:
            B = self.gradient(x,y)
        else:
            raise exceptions.NotImplementedError('m>1 derivatives not implemented')
        return B * p

    def linear_fit(self, x, y, v, w=None):
        """fit the basis coefficients on the data passed in argument

        Perform a least square fit of the basic coefficients. 

        Args:
            x (ndarray of floats): x coordinates
            y (ndarray of floats): y coordinates
            v (ndarray of floats): values

        Returns:
            ndarray of floats: fit solution, i.e. basis coefficients

        .. note: ~ 12 seconds on a Intel(R) Core(TM) i5-2540M CPU @ 2.60GHz
                 for 10^6 values and a 10x10 basis. Dominated by the cholesky
                 factorization.
        """
        J = self.eval(x,y)
        if w is not None:
            J.data *= w[J.row]
            vv = w * v
        else:
            vv = v
        factor = cholesky_AAt(J.T)
        return factor(J.T * vv)


class CardinalBSplineC(object):
    """
    New CardinalBSpline basis, with a blossoming 
    function implemented in C. 
    
    (Simpler, and faster in most cases)
    """
    def __init__(self, n=10, x_range=(0., 1.), order = 4):
        self.order = order 
        self.n_knots = n
        self.nj = self.n_knots + self.order - 1
        self.range = x_range
        self.dx = (x_range[1]-x_range[0]) / n 
        
    def __len__(self):
        return self.nj 

    @property
    def grid(self):
        r = np.arange(self.range[0], self.range[1]+0.5*self.dx, self.dx)
        return r
    
    def _int_grid(self, x):
        """
        return a copy of the x' array, 
        scaled so that the knots are at integer locations 
        """
        return (x-self.range[0]) / self.dx + self.order - 1.
    
    def eval(self, x):
        """
        evaluate the value of the basis functions for each element of x
        
        Args:
          x : (ndarray of floats) 
              the x-values 
       
        Returns:
          B: (scipy.sparse.coo_matrix) 
                a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                containing the basis values: B_{ij} = B_j(x_i)        
                
        TODO: 
          add a float32 version (?)
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N, dtype=np.float64)
        xi = self._int_grid(x)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        _blossom(xi, nx, i, j, B, N, self.order, self.order, self.nj)
        return coo_matrix((B, (i,j)), shape=(nx, self.nj))
            
    def deriv(self, x):
        """
        evaluate the first derivative of the basis functions for each element of x
        
        Args:
           x: (ndarray of floats) 
       
         Returns:
            a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N)
        xi = self._int_grid(x)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        _blossom(xi, nx, i, j, B, N, self.order-1, self.order, self.nj)
        B[:-1] -= B[1:]
        return coo_matrix((B, (i,j)), shape=(nx, self.nj)) / self.dx

    def deriv_m(self, x, m=2, dtype=np.float64):
        """
        evaluate the m-th first derivative of the basis functions for each element of x
        
        Args:
           x: (ndarray of floats) 
       
         Returns:
            a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)
        """
        nx = len(x)
        N = self.order * nx
        B = np.zeros(N, dtype=dtype)
        xi = self._int_grid(x)
        i, j = np.zeros(N, dtype=np.int32), np.zeros(N, dtype=np.int32)
        if (self.order - m) <= 0:
            return coo_matrix((B, (i,j)), shape=(nx,self.nj)) / self.dx
        _blossom(xi, nx, i, j, B, N, self.order-m, self.order, self.nj)
        d = np.arange(1,m+1) # was m+1
        Cmp = comb(m, d)
        Cmp[::2] *= -1.
        BB = B.copy()
        for d,c in zip(d,Cmp):
            BB[:-d] += c * B[d:]
        return coo_matrix((BB, (i,j)), shape=(nx,self.nj)) / self.dx

    def gram(self):
        """
        Compute the gramian matrix of the base elements:
        
        .. math::
             G_{ij} = \int B_i(x) B_j(x) dx

        """
        nk = self.n_knots
        N = self.order * (self.n_knots+1)
        p, w = leggauss(self.order)
        # I am here ... 
        grid = np.linspace(self.range[0], self.range[1], self.n_knots+1)
        _integ()
        W = coo_matrix((W, (i,i)), shape=(N,N))
        B = self.eval(pp)
        return B.T * W * B        
    
    # def __call__(self, x, p, deriv=0):
    #     if deriv == 0:
    #         B = self.eval(x)
    #     elif deriv == 1:
    #         B = self.deriv(x)
    #     else:
    #         B = self.deriv_m(x, m=deriv)
    #     return B * p
    
    def linear_fit(self, x, y):
        J = self.eval(x)
        JtJ = J.T.dot(J)
        return scipy.sparse.linalg.spsolve(JtJ, J.T.dot(y))


class CardinalBSpline(object):
    """
    Implements a 1D-BSpline basis of arbitrary order, 
    defined on a grid of evenly spaced knots.
    """
    def __init__(self, n=10, x_range=(0.,1.), order=4):
        """
        By default, compute cardinal BSplines of order 4 
        (i.e. CubicBSplines)
        """
        self.order = order 
        self.n_knots = n
        self.nj = self.n_knots + self.order - 1
        self.range = x_range
        self.dx = (x_range[1]-x_range[0]) / n 

    def __len__(self):
        """
        return the size of the basis
        """
        return self.nj

    @property
    def grid(self):
        r = np.arange(self.range[0], self.range[1]+0.5*self.dx, self.dx)
        return r                 
    
    def _start(self, xi, dtype):
        """
        compute the 1-st order splines given the xi (step functions)
        
        Args:
          xi: (ndarray)
              array of x's, rescaled so that the knots are at integer positions. 

        Returns:
          a tuple (k, xi, i, j, b, om) where 
            - k is the order of the spline (1) 
            - xi are the rescaled x's (reference to the arguments)
            - i  are the line indexes of the jacobian matrix (i = arange(len(x)))
            - j  are the column indexes of the jacobian matrix 
            - b  are the spline values 
            - om are the recursion coefficients: \omega_{j,k+1} = (x - j) / k
        """
        N = len(xi)
        i = np.arange(N)
        j = np.floor(xi)
        b = np.ones(N)
        om = (xi - j).astype(dtype)
        return [(1, xi, i, j, b, om)]    
    
    def _merge(self, xxx_todo_changeme):
        """
        auxiliary function, called while blossoming up. 
        
        compute the B^k spline from a pair of adjacent B^{k-1}
        splines. The recursion formula is:
        
        .. math::
             B^k_{j}(x) = \omega^k_j(x) B^{k-1}_{j}(x) + (1-\omega^{k}_{j+1}) B^{k-1}_{j+1}(x)

        with 

        .. math::
             \omega^k_j(x) = \frac{x-t_j}{t_{j+k-1}-t_{j}}
             
        Args:
            left (tuple or None):  (k, xi, i,m j, b, om)
            right (tuple or None): (k, xi, i,m j, b, om)
              
        Returns:
            new tuple, of the form (k+1, xi, i, j, b, om) of order k+1
        """
        (left, right) = xxx_todo_changeme
        if right is None:
            k, xi, i, j, b, om = left
            b = b * om
            om = (xi - j) / (k+1.)
            return (k+1, xi, i, j, b, om)
        elif left is None:
            k, xi, i, j, b, om = right
            b = b * (1.-om)
            om = (xi - j + 1.) / (k+1.)
            return (k+1, xi, i, j-1, b, om)
        k_l, xi, i, j_l, b_l, om_l = left
        k_r, xi, i, j_r, b_r, om_r = right
        b = om_l*b_l + (1.-om_r)*b_r
        om = (xi-j_l) / (k_l + 1.)
        return (k_l+1, xi, i, j_l, b, om)
    
    def _blossom(self, bvlist):
        """
        blossom: compute recursively the k-th order splines from the (k-1)-th order splines.
        """
        l = [None] + bvlist + [None]
        l = list(zip(l[:-1], l[1:]))
        return [self._merge(b) for b in l]
    
    def get_xi(self, x):
        """
        return a copy of the x' array, 
        scaled so that the knots are at integer locations 

        The spline corresponding to the first node is at location i=0.
        This means that x.min() is at location i=(order-1).
        """
        return (x-self.range[0]) / self.dx + self.order - 1.
    
    def eval(self, x, dtype=np.float32):
        """
        evaluate the value of the basis functions for each element of x
        
        Args:
          x : (ndarray of floats) 
              the x-values 
       
        Returns:
          B: (scipy.sparse.coo_matrix) 
                a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                containing the basis values: B_{ij} = B_j(x_i)
                
        Note:
          This method is used by the 2D-version of the CardinalBSplines, which 
          assumes that the triplets (i,j,v) are sorted like they are here, i.e.: 
 
                [i=0, j=0, B_0(x0)]
                [i=1, j=0, B_0(x1)]
                      ...
                [i=0, j=1, B_1(x0)]
                      ...          
        """
        xi = (x-self.range[0]) / self.dx + self.order - 1.
        s = self._start(xi, dtype)
        for i in range(1,self.order):
            s = self._blossom(s)
        i = np.hstack([b[2] for b in s])
        j = np.hstack([b[3] for b in s])
        v = np.hstack([b[-2] for b in s])
        J = coo_matrix((v, (i,j)), dtype=dtype, shape=(len(x), self.nj))
        return J
    
    def deriv(self, x, dtype=np.float32):
        """
        evaluate the derivatives of the basis functions for each element of x
        
        Args:
           x: (ndarray of floats) 
       
         Returns:
            a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)        
        """
        xi = (x-self.range[0]) / self.dx + self.order - 1.

        # lower order splines (k-1)
        s = self._start(xi, dtype)
        for i in range(1,self.order-1):
            s = self._blossom(s)
            
        # add 
        N = len(x) ; z = np.zeros(N)
        k0, xi, i, j0, b0, om0 = s[0]
        k1, xi, i, j1, b1, om1 = s[-1]
        s = [(k0, xi, i, j0-1, z, z)] + s + [(k1, xi, i, j1+1, z, z)]
            
        # and compute the differences B_j^k-1 - B_j+1^k-1
        l = list(zip(s[0:-1], s[1:]))
        s = []
        for low, high in l:
            kl, xi, i, jl, bl, oml = low
            kh, xi, i, jh, bh, omh = high
            s.append((kl, xi, i, jl, bl-bh, oml))
            
        i = np.hstack([b[2] for b in s])
        j = np.hstack([b[3] for b in s])
        v = np.hstack([b[-2] for b in s])
        J = coo_matrix((v, (i,j)), dtype=dtype, shape=(N, self.nj))
        # checked with numerical derivative that the self.dx is really needed
        return J / self.dx  

    def deriv_m(self, x, m=2, dtype=np.float32):
        """
        evaluate the m-th derivatives of the basis functions for each element of x
        
         Args:
          x: (ndarray of floats) 
       
         Returns:
           a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
            (contains the values of the derivatives)        
        """
        xi = (x-self.range[0]) / self.dx + self.order - 1.

        # splines of order k-m 
        s = self._start(xi, dtype)
        for i in range(1,self.order-m):
            s = self._blossom(s)
            
        # add m zero elements before and after the structure 
        N = len(x) ; z = np.zeros(N)
        k0, xi, i, j0, b0, om0 = s[0]
        k1, xi, i, j1, b1, om1 = s[-1]
        s_pre = []
        s_post = []
        for q in range(m):
            s_pre.append([k0, xi, i, j0-m+q, z, z])
            s_post.append([k0, xi, i, j1+q+1, z, z])
        s = s_pre + s + s_post
        #        s = [(k0, xi, i, j0-1, z, z)]*m + s + [(k1, xi, i, j1+1, z, z)]*m # BUG !

        # now, we want to compute  \sum_p=0^m f[p] B_{j+p,k-m}(x)
        # with f[p] = (-1)^p C_m^p 
        # First, we compute the bvfilter f[p] itself 
        f = comb(m, np.arange(m+1))
        f[1::2] *= -1. 
        # then, we stack the basis values into one single array 
        l = []
        bvalues = np.vstack([u[-2] for u in s]).T
        for k in range(len(s)-m):
            kl, xi, i, jl, bl, oml = s[k]
            bv = np.sum(f * bvalues[:,k:k+m+1], axis=1)
            l.append((kl, xi, i, jl, bv, oml))
            
        i = np.hstack([b[2] for b in l])
        j = np.hstack([b[3] for b in l])
        v = np.hstack([b[-2] for b in l])
        J = coo_matrix((v, (i,j)), dtype=dtype, shape=(N, self.nj))
        return J / self.dx

    def gram(self, dtype=np.float64):
        """
        Compute the gramian matrix of the base elements:

        .. math::
            G_{ij} = \int B_i(x) B_j(x) dx
        """
        nk = self.n_knots        
        # Gaussian quadrature points and weights
        p, w = leggauss(self.order) 
                
        # points
        #        x = np.arange(self.range[0], self.range[1]+self.dx, self.dx)
        x = np.linspace(self.range[0], self.range[1], self.n_knots+1)
        ak = np.repeat(0.5*(x[1:]-x[:-1]), self.order)
        bk = np.repeat(0.5*(x[1:]+x[:-1]), self.order)
        pp = np.tile(p, nk)
        pp = ak*pp+bk
        
        # weights
        ww = np.tile(w, nk)
        N = len(ww)
        i = np.arange(N)
        W = coo_matrix((ak*ww, (i,i)), shape=(N,N))
        
        B = self.eval(pp, dtype=dtype)
        return B.T * W * B
                
    def integral(self, x):
        """
        Also have a look at this: 
        http://www.sciencedirect.com/science/article/pii/S009630030500189X
        http://imamat.oxfordjournals.org/content/17/1/37.abstract
        """
        pass

    def __call__(self, x, b, deriv=0, dtype=np.float32):
        """
        Syntaxic sugar so that if bs is a bspline
        bs(x, b) returns the evaluated spline function on the grid x
        with spline parameters b
        
        deriv: set it to the degree of the derivation you expect.
        deriv=0 is similar default and returns the spline       
        """
        if deriv == 0:
            A = self.eval(x, dtype=dtype)
        elif deriv == 1:
            A = self.deriv(x, dtype=dtype)
        else:
            A = self.deriv_m(x, m=deriv, dtype=dtype )

        return (A * b)

    def linear_fit(self, x, y):
        """
        Makes a linear fit of the spline 
        
        x is the list of abscissa (not necessarily ordered)
        y is the corresponding list of data

        Make sure that all x values are within the bounds of the bspline you defined.        

        FIXME: add the weights
        """
        # essential to have float64, otherwise the solver complains
        J = self.eval(x, dtype=np.float64)
        JtJ = J.T.dot(J)
        return sparse.linalg.spsolve(JtJ, J.T.dot(y))
        #        return np.linalg.solve((A.T * A).todense(), A.T * y)
        

def gram(basis1, basis2, dtype=np.float64):
    """
    Compute the gramian matrix of elements of the two (different) bases
    ``basis1`` and ``basis2``. 
    
    .. math::  G_{ij} = \int B_i(x) C_j(x) dx

    where B_i and C_j are elements of the two bases. 
    """
    # Gaussian quadrature points and weights
    deg = basis1.order + basis2.order
    p, w = leggauss(deg)
    
    # points -- use the basis grids ! 
    x1 = np.linspace(basis1.range[0], basis1.range[1], basis1.n_knots+1)
    x2 = np.linspace(basis2.range[0], basis2.range[1], basis2.n_knots+1)
    x = np.hstack((x1,x2)) ; x.sort() ; x = np.unique(x)
    nk = len(x)-1
    ak = np.repeat(0.5*(x[1:]-x[:-1]), deg)
    bk = np.repeat(0.5*(x[1:]+x[:-1]), deg)
    pp = np.tile(p, nk)
    pp = ak*pp+bk
    
    # weights
    ww = np.tile(w, nk)
    N = len(ww)
    i = np.arange(N)
    W = coo_matrix((ak*ww, (i,i)), shape=(N,N))
    
    # some bases accept dtypes, other not...
    # TODO: uniformize this (ban np.float32 and remove dtype options ?)
    B1 = basis1.eval(pp)
    B2 = basis2.eval(pp)
    return B1.T * W * B2


def lgram(spectrum_basis, filter_basis, **keys):
    """Compute the :math:`\\lambda-`Gramian of both bases.

    When computing broadband fluxes, using transmission functions as
    spectra developed on spline bases, one needs to compute the
    following quantities:

    .. math::
         G_{ij} = \\int B_i(\\lambda) B_j(\\lambda) \\lambda d\\lambda
     
    This function computes the G-matrix above, and returns it as a
    sparse matrix. The spectrum basis may be shifted by a factor
    (1+z), for example:

    .. math::
         G_{ij} = \\int B_i(\\lambda) B_j(\\lambda / (1+z)) \\lambda d\\lambda

    """
    # Gaussian quadrature points and weights
    deg = spectrum_basis.order + filter_basis.order
    p, w = leggauss(deg)
    
    z = keys.get('z', 0.)
    to_photons = keys.get('to_photons', False)
    lambda_power = keys.get('lambda_power', 1)
    
    # points -- use the basis grids ! 
    if z > 0.:
        x1 = spectrum_basis.grid * (1.+z)
    else:
        x1 = spectrum_basis.grid / (1.-z)
    x2 = filter_basis.grid
    x = np.hstack((x1,x2)) ; x.sort() ; x = np.unique(x)
    nk = len(x)-1
    ak = np.repeat(0.5*(x[1:]-x[:-1]), deg)
    bk = np.repeat(0.5*(x[1:]+x[:-1]), deg)
    pp = np.tile(p, nk)
    pp = ak*pp+bk
    
    # weights
    ww = np.tile(w, nk)
    N = len(ww)
    i = np.arange(N)
    
    A_hc = 50341170.081942275 / (1.+z) ** 2 
    W = coo_matrix((ak * ww * A_hc * np.power(pp, lambda_power), (i,i)), 
                   shape=(N,N))
    
    if z > 0.:
        B1 = spectrum_basis.eval(pp / (1.+z))
    else:
        B1 = spectrum_basis.eval(pp / (1.-z))
    B2 = filter_basis.eval(pp)
    return B1.T * W * B2


_leggauss_cache = {}

def integ(basis, n=0):
    """
    Compute the integral (of n-th moments) of the spline basis functions.
    
    .. math::
       I_i^{[n]} = \int x^n B_i(x) dx
    
    Args:
      basis (bspline basis): 1-D bspline basis to integrate 
      n (int): moment order 

    Returns:
      a vector of length `len(basis)` containing the n-th moment of each function.      
    """
    global _leggauss_cache
    g = basis.grid
    aa = np.matrix(0.5 * (g[1:]-g[:-1]))
    bb = np.matrix(0.5 * (g[1:]+g[:-1]))
    nk = len(g) - 1

    deg = basis.order + n
    if deg in _leggauss_cache:
        x,w = _leggauss_cache[deg]
    else:
        x,w = leggauss(basis.order + n)
        _leggauss_cache[deg] = x,w
        
    xx = np.array(np.dot(aa.T, np.matrix(x)) + bb.T).flatten().squeeze()
    dx = np.array(np.dot(aa.T, np.matrix(np.ones(len(x))))).flatten().squeeze()
    
    J = basis.eval(xx)
    w = np.tile(w, nk) * xx**n * dx
    i,j = np.zeros(len(w)), np.arange(len(w))
    W = coo_matrix((w,(i,j)), shape=(1,len(w)))

    I = (W * J).tocoo()

    return I.data[I.col]



class CardinalBSpline2D(object):
    """
    2D-BSpline basis of arbitrary order, 
    defined on a grid of evenly spaced knots.
    
    The basis is the cross-product of two BSpline bases, along x and y:
    
    .. math::
      B_{ij}(x,y) = B_i(x) \times B_j(y)
      
    """
    def __init__(self, 
                 nx=10, x_range=(0.,1.), x_order=4,
                 ny=10, y_range=(0.,1.), y_order=4):
        self.bx = CardinalBSpline(n=nx, x_range=x_range, order=x_order)
        self.by = CardinalBSpline(n=ny, x_range=y_range, order=y_order) # there is a bug here, no ? 
        self.nj = self.bx.nj * self.by.nj

    def __len__(self):
        """
        return the size of the basis
        """
        return self.nj

    def _cross(self, N, i, jx, vx, jy, vy, dtype=np.float32):
        """
        compute the cross-product: B_{ij}(x,y) = B_i(x) \times B_j(y)

        Args:
          N: (int) 
             number of points (N=len(x))
          j: ndarray of ints 
             a ndarray containing the row-indices in the jacobian matrix
          jx: ndarray of ints 
              the column indices in the matrix returned by the x-basis 
          vx: ndarray of floats, 
              the values B_j(x)
          jy: ndarray of ints 
              the column indices in the matrix returned by the y-basis 
          vy: ndarray of floats
              the values B_j(y)

        Returns:
          J: (scipy.sparse.coo_matrix) 
              the values of the cross-product as a (N,n) sparse jacobian matrix, 
              [N is the number of points, n the size of the 2D-basis]

        Note:
          This implementation makes an assumption on how the return value 
          of ``CardinalBSpline.eval'' is sorted internally.  
          See the documentation of this routine above.           
        """
        i  = i.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        jx = jx.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        vx = vx.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        jy = np.tile(jy.reshape(-1,N).T, (1,self.by.order))
        vy = np.tile(vy.reshape(-1,N).T, (1,self.by.order))
        
        data = vx * vy
        i = i.ravel()
        j = jy.ravel()*self.bx.nj + jx.ravel()
        
        return coo_matrix((data.ravel(), (i,j)), 
                          shape=(N,self.nj), dtype=dtype)        

    def eval(self, x, y, dtype=np.float32):
        """
        evaluate and return the values of the basis functions for (x,y)
        
        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          B: (scipy.sparse.coo_matrix)
              a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
              containing the basis values: B_{ij} = B_j(x_i)
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        Jx = self.bx.eval(x, dtype=dtype)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jy = self.by.eval(y, dtype=dtype)        
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        #        embed()
        return self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)


    def gradient(self, x, y, dtype=np.float32):
        """
        evaluate and return the derivatives vs. x and y of the basis functions for (x,y)
        
        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          dvdx: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j'(x_i) * B_j(y_i)
          dvdy: (scipy.sparse.coo_matrix)
                 a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
                 containing the values: B_{ij} = B_j(x_i) * B_j'(y_i)
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        
        Jxp = self.bx.deriv(x, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy  = self.by.eval(y, dtype=dtype)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        ix = jx = vx = None
        iy = jy = vy = None
        
        Jx  = self.bx.eval(x, dtype=dtype)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        Jyp = self.by.deriv(y, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        return ddx, ddy        

    def hessian(self, x, y, dtype=np.float32):
        """
        evaluate and return the partial second derivatives of the
        basis functions.

        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          d2Bdx2, d2Bdy2, d2Bdxy : (scipy.sparse.coo_matrix)
              a tuple of 3 sparse, N x p jacobian matrices [N=len(x), p=len(self)]
              containing second derivatives of the basis values.
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        
        Jxp = self.bx.deriv_m(x, m=2, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy  = self.by.eval(y, dtype=dtype)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        ix = jx = vx = None
        iy = jy = vy = None
        
        Jx = self.bx.eval(x, dtype=dtype)
        ix, jx, vx = Jx.row, Jx.col, Jx.data 
        Jx = None
        Jyp = self.by.deriv_m(y, m=2, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)

        ix = jx = vx = None
        iy = jy = vy = None
        
        Jxp = self.bx.deriv_m(x, m=1, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jyp = self.by.deriv_m(y, m=1, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddxy = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        return ddx2, ddy2, ddxy
                

    def laplacian(self, x, y, dtype=np.float32):
        """
        evaluate and return the laplacian of the basis functions. 

        Args:
          x: (ndarray of floats) 
              x-coordinates of the entry points
          y: (ndarray of floats) 
              y-coordinates of the entry points

        Returns:
          L : (scipy.sparse.coo_matrix)
              a sparse, N x p jacobian matrix [N=len(x), p=len(self)]
              containing the laplacian of basis values: L_{ij} = \Delta B_j(x_i)
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        
        Jxp = self.bx.deriv_m(x, m=2, dtype=dtype)
        ix, jx, vx = Jxp.row, Jxp.col, Jxp.data
        Jxp = None
        Jy  = self.by.eval(y, dtype=dtype)
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        ddx2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        ix = jx = vx = None
        iy = jy = vy = None
        
        Jx = self.bx.eval(x, dtype=dtype)
        ix, jx, vx = Jx.row, Jx.col, Jx.data 
        Jx = None
        Jyp = self.by.deriv_m(y, m=2, dtype=dtype)
        iy, jy, vy = Jyp.row, Jyp.col, Jyp.data
        Jyp = None
        ddy2 = self._cross(N, ix, jx, vx, jy, vy, dtype=dtype)
        
        return ddx2 + ddy2    
    
    def eval_old(self, x, y):
        """
        Still here, but deprecated. Will disappear soon. 
        """
        if len(x) != len(y): 
            raise ValueError('x and y should have the same length')        
        N = len(x)
        Jx = self.bx.eval(x)
        ix, jx, vx = Jx.row, Jx.col, Jx.data
        Jx = None
        ix = ix.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        jx = jx.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        vx = vx.reshape(-1,N).T.repeat(self.bx.order,axis=1)
        
        Jy = self.by.eval(y)        
        iy, jy, vy = Jy.row, Jy.col, Jy.data
        Jy = None
        #        iy = np.tile(iy.reshape(-1,N).T, (1,4))
        jy = np.tile(jy.reshape(-1,N).T, (1,self.by.order))
        vy = np.tile(vy.reshape(-1,N).T, (1,self.by.order))
        
        data = vx * vy
        i = ix.ravel()
        j = jy.ravel()*self.bx.nj + jx.ravel()

        return coo_matrix((data.ravel(), (i,j)), 
                          shape=(N,self.nj), dtype=np.float32)


class CubicBSpline:
    """Define a basis of (h+4)) uniform cubic B-splines on a
    segment [0,Lx]
    """
    def __init__(self, N=1, Lx=1.0, Ly=1.0):
        self.Lx = Lx
        self.N = N + 3
        self.dx = float(Lx) / N
        self.tx = np.arange(-3 * self.dx, Lx + 4 * self.dx, self.dx)
        self.compute_weights()

    def compute_weights(self):
        self.w = np.ones(5)
        self.ti = np.arange(5)
        for i in range(5):
            for j in range(5):
                if j != i:
                    self.w[i] = self.w[i] * (self.ti[j] - self.ti[i])
        self.w = 1.0 / self.w

    def b3(self, t):
        b = np.zeros(t.shape)
        for i in range(5):
            cond = t >= self.ti[i]
            _t = t[cond] - self.ti[i]
            _t *= _t * _t
            b[cond] += self.w[i] * _t
        return b

    def b3_eval(self, t):
        i = np.vstack([np.floor(t).astype('int') + e for e in range(0, 4)])
        val = np.vstack([self.b3(t - i[e, :] + 3) for e in range(4)])
        return i, val

    def _eval(self, x):
        i, M = self.b3_eval(x / self.dx)
        return i, M

    def sparse_mat(self, x, factor=None):
        Ncell = len(x)
        i, val = self._eval(x)
        index_x = np.tile(np.arange(Ncell), 4)
        index_y = i.flatten()
        if factor is not None:
            val *= factor
        index = index_y < self.N
        return index_x[index], index_y[index], val.flatten()[index]

    def eval(self, pars, x):
        from scipy import sparse as sp
        index_x, index_y, val = self.sparse_mat(x.flatten())
        A = sp.coo_matrix((val, (index_x, index_y)),
                          #shape=(index_x.max() + 1, len(self.tx) - 1)).tocsr()
                          ).tocsr()
        return x, np.reshape(A * pars, x.shape)

    # def fit(self, x, y, w=None, full_output=False):
    #     M = lm.LinearSparseModel()
    #     M.models = {"pars": lambda: self.sparse_mat(x)}
    #     if w is not None:
    #         M.w = w
    #     M.B = y
    #     if full_output:
    #         return M.solve(), M
    #     else:
    #         return M.solve()

class BicubicBSpline(CubicBSpline):
    """Define a basis of (h+4)(k+4) uniform bicubic B-splines on a
    rectangle [0,Lx]x[0,Ly].
    """
    def __init__(self, M=1, N=1, Lx=1.0, Ly=1.0):
        self.Lx = Lx
        self.Ly = Ly
        self.dx, self.dy = float(Lx) / M, float(Ly) / N
        self.tx = np.arange(-3 * self.dx, Lx + 4 * self.dx, self.dx)
        self.ty = np.arange(-3 * self.dy, Ly + 4 * self.dy, self.dy)
        self.compute_weights()

    def eval(self, x, y):
        if len(x) != len(y):
            raise ValueError('x and y should have same length')
        i, M = self.b3_eval(x / self.dx)
        j, N = self.b3_eval(y / self.dy)
        _m, _n = np.mgrid[0:4, 0:4]
        _n = _n.flatten()
        _m = _m.flatten()
        val = M[_m, :] * N[_n, :]
        return i[_m, :], j[_n, :], val

    def sparse_mat(self, x, y, factor=None):
        Ncell = len(x)
        i, j, val = self.eval(x, y)
        if factor is not None:
            val *= factor
        index_x = np.tile(np.arange(Ncell), 16)
        index_y = i.flatten() + j.flatten() * (len(self.tx) - 4)
        return index_x, index_y, val.flatten()

    def show(self, pars, res=[100j, 100j], xy=None):
        from scipy import sparse as sp
        #import pylab
        if xy is None:
            _x = np.linspace(0, self.Lx - 1, abs(res[0]) + 2)[1:-1]
            _y = np.linspace(0, self.Ly - 1, abs(res[1]) + 2)[1:-1]
        #x,y=np.mgrid[0:self.Lx-1:res[0],0:self.Ly-1:res[1]]
            x, y = np.meshgrid(_x, _y)
        else:
            x, y = xy
        index_x, index_y, val = self.sparse_mat(x.flatten(), y.flatten())
        A = sp.coo_matrix((val, (index_x, index_y))).tocsr()
        return x, y, np.reshape(A * pars, x.shape)
        #pylab.imshow(np.reshape(A*pars,(100,100)))
        #pylab.colorbar()

    # def b3_integral(self, a, b):
    #      return 0.25*(self.w*((b-self.ti)**4*(b>=self.ti) - (a-self.ti)**4*(a>=self.ti))).sum()

    # def integral(self, i, j, quad):
    #     a,b,c,d= quad
    #     i1 = self.dx*self.b3_integral((a-self.tx[i])/self.dx, (b-self.tx[i])/self.dx)
    #     i2 = self.dy*self.b3_integral((c-self.ty[j])/self.dy, (d-self.ty[j])/self.dy)
    #     return i1*i2



    # def plot_debug(self, x, y):
    #     import pylab as pl 
    #     pl.figure()        
    #     Jx = self.bx.eval(x)
    #     p = np.random.choice([0.,1.], size=len(self.bx))
    #     pl.plot(x, Jx * p, 'r.')
        
    #     pl.figure()
    #     Jy = self.by.eval(y)
    #     p = np.random.choice([0.,1.], size=len(self.by))
    #     pl.plot(y, Jy * p, 'r.')        

    #     pl.figure()
    #     ax = pl.subplot(221)
    #     pl.plot(x, 'r.')
    #     ay = pl.subplot(222)
    #     pl.plot(y, 'b.')
    #     pl.subplot(223, sharex=ax)
    #     pl.plot(Jx.col, 'r.')
    #     pl.subplot(224, sharex=ay)
    #     pl.plot(Jy.col, 'b.')
        
    #     pl.figure()
        
    #     ix = Jx.row.reshape(-1,N).T.repeat(self.by.order,axis=1)
    #     jx = np.repeat(Jx.col, self.by.order)
    #     vx = np.repeat(Jx.data, self.by.order)

    #     iy = np.tile(Jy.row, self.bx.order)
    #     jy = np.tile(Jy.col, self.bx.order)
    #     vy = np.tile(Jy.data, self.bx.order)

    #     j = jx * self.by.nj + jy
    #     #        j = jy * self.bx.nj + jx
    #     N,n = len(x), self.nj
    #     J = coo_matrix((vx*vy, (ix,j)), shape=(N,n))
        
    #     pl.subplot(421)
    #     pl.plot(x, 'r.')
    #     pl.subplot(422)
    #     pl.plot(y, 'b.')
    #     pl.subplot(423)
    #     pl.plot(ix, 'r.')
    #     pl.subplot(424)
    #     pl.plot(iy, 'b.')
    #     pl.subplot(425)  
    #     pl.plot(jx, 'r.')      
    #     pl.subplot(426)  
    #     pl.plot(jy, 'b.')      
    #     pl.subplot(427)  
    #     pl.plot(vx, 'r.')      
    #     pl.subplot(428)  
    #     pl.plot(vy, 'b.')      
    #     return J
