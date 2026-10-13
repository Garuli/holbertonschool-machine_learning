#!/usr/bin/env python3
"""Module that sets the Timestamp column as the index."""


def index(df):
    """Set Timestamp as the DataFrame index and return the DataFrame."""
    return df.set_index("Timestamp")
