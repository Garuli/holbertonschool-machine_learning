#!/usr/bin/env python3
"""Module that cleans the missing values of a DataFrame"""


def fill(df):
    """Removes Weighted_Price and fills the missing values of the other
    columns, then returns the modified pd.DataFrame"""
    df = df.drop(columns=["Weighted_Price"])
    df["Close"] = df["Close"].ffill()
    for column in ["High", "Low", "Open"]:
        df[column] = df[column].fillna(df["Close"])
    for column in ["Volume_(BTC)", "Volume_(Currency)"]:
        df[column] = df[column].fillna(0)
    return df
