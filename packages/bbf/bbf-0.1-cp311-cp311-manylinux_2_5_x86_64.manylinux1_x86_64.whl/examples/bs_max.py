#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

from bbf.bspline import BSpline
from bbf.bspline import integ


def bs_max(bs):
    """
    """
    x = bs.grid
    grid = np.hstack((x, 0.5*(x[1:]+x[:-1])))
    grid.sort()

    J = bs.eval(grid)

    return J, grid


if __name__ == '__main__':
    # x = np.linspace(-10., 10., 25)
    x = np.random.uniform(-10., 10., 25)
    x.sort()
    bs = BSpline(x)

    x_mean = integ(bs,n=1) / integ(bs)

    xx = np.linspace(-10., 10., 1000)
    J = bs.eval(xx)
    t = np.zeros(len(bs))
    for i in range(len(t)):
        t[:] = 0.
        t[i] = 1.
        color = cm.jet(int(i * 256/len(t)))
        plt.plot(xx, J @ t, ls='-', color=color)

    for i, x in enumerate(x_mean):
        color = cm.jet(int(i * 256/len(t)))
        plt.axvline(x, ls=':', color=color)
