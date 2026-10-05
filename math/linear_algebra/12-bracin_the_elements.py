#!/usr/bin/env python3
"""Module that performs element-wise operations on numpy.ndarrays"""


def np_elementwise(mat1, mat2):
    """Returns a tuple with the element-wise sum, difference, product
    and quotient of two numpy.ndarrays (or an array and a scalar)"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
