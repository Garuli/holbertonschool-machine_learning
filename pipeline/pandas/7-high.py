#!/usr/bin/env python3
"""Module that sorts a DataFrame by the High price"""


def high(df):
    """Sorts a pd.DataFrame by the High price in descending order and
    returns the sorted pd.DataFrame"""
    return df.sort_values("High", ascending=False)
