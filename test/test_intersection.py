# -*- coding: utf-8 -*-
#
import numpy

import dmsh


def test_intersection(h0=0.5, show=True):
    geo = dmsh.geometry.Intersection(
        [dmsh.geometry.Circle([-0.5, 0.0], 1.0), dmsh.geometry.Circle([+0.5, 0.0], 1.0)]
    )
    X, cells = dmsh.generate(geo, h0, show=show)

    print(cells)
    assert numpy.array_equal(
        cells,
        [
            [6, 8, 5],
            [9, 6, 7],
            [3, 6, 5],
            [6, 4, 7],
            [10, 8, 6],
            [9, 10, 6],
            [10, 9, 0],
            [3, 2, 6],
            [2, 4, 6],
            [2, 3, 1],
        ],
    )
    tol = 1.0e-12

    ref_norm1 = 8.08910757280533
    assert abs(numpy.linalg.norm(X.flatten(), ord=1) - ref_norm1) < tol * ref_norm1
    ref_norm2 = 2.0887854791992484
    assert abs(numpy.linalg.norm(X.flatten(), ord=2) - ref_norm2) < tol * ref_norm2
    ref_norm_inf = 0.8660254037531557
    assert (
        abs(numpy.linalg.norm(X.flatten(), ord=numpy.inf) - ref_norm_inf)
        < tol * ref_norm_inf
    )
    return


if __name__ == "__main__":
    test_intersection(0.1)