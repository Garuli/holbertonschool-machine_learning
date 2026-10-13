#!/usr/bin/env python3
"""Module that renames a column and converts timestamps to datetimes"""
import pandas as pd


def rename(df):
    """Renames the Timestamp column to Datetime, converts its values to
    datetime values and returns only the Datetime and Close columns"""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
