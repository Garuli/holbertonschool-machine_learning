#!/usr/bin/env python3
"""Module that slices a DataFrame"""


def slice(df):
    """Extracts the High, Low, Close and Volume_(BTC) columns and returns
    every 60th row as a pd.DataFrame"""
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
