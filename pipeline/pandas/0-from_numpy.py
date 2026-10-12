#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a numpy ndarray"""
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray, with the columns labeled
    A, B, C... in alphabetical order"""
    columns = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
