#!/usr/bin/env python3
"""Module that concatenates two DataFrames."""


def concat(df1, df2):
    """Concatenate selected Bitstamp rows above Coinbase rows."""
    index = __import__('10-index').index

    df1 = index(df1)
    df2 = index(df2)

    df2 = df2.loc[:1417411920]

    return __import__('pandas').concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )
