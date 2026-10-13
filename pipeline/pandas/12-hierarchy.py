#!/usr/bin/env python3
"""Module that creates a hierarchical DataFrame."""
import pandas as pd


def hierarchy(df1, df2):
    """Concatenate Bitstamp and Coinbase data in chronological order."""
    index = __import__('10-index').index

    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    df = pd.concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )

    return df.swaplevel(0, 1).sort_index()
