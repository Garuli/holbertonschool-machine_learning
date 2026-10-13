#!/usr/bin/env python3
"""Module that removes the rows of a DataFrame with a missing Close"""


def prune(df):
    """Removes the entries where Close has NaN values and returns the
    modified pd.DataFrame"""
    return df.dropna(subset=["Close"])
