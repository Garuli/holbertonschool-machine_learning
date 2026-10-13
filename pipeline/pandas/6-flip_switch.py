#!/usr/bin/env python3
"""Module that sorts a DataFrame in reverse chronological order and
transposes it"""


def flip_switch(df):
    """Sorts the data in reverse chronological order, transposes the
    sorted DataFrame and returns it"""
    return df.sort_values("Timestamp", ascending=False).T
