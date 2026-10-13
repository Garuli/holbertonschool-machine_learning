#!/usr/bin/env python3
"""Module that computes descriptive statistics."""


def analyze(df):
    """Return descriptive statistics excluding the Timestamp column."""
    return df.drop(columns=['Timestamp']).describe()
