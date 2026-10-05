#!/usr/bin/env python3
"""Module that concatenates two numpy.ndarrays along a specific axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns a new numpy.ndarray that is the concatenation of two
    numpy.ndarrays along the given axis"""
    return np.concatenate((mat1, mat2), axis=axis)
