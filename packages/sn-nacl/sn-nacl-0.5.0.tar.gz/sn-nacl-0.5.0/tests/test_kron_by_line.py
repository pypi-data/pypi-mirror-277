#!/usr/bin/env python3

import numpy as np
import scipy.sparse
from bbf.bspline import BSpline
from nacl.sparseutils import kron_product_by_line


if __name__ == '__main__':

    grid = np.linspace(-10., 10., 4)
    basis = BSpline(grid)
    x = np.random.uniform(-10., 10., 4)
    J = basis.eval(x)
    F = np.random.rand(*J.shape)

    K = kron_product_by_line(J, F)
