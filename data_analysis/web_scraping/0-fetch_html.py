#!/usr/bin/env python3
"""Module that fetches the HTML of a web page."""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a web page and return its HTML as text.

    Args:
        url: the page to retrieve.
        headers: optional dict of HTTP headers.
        timeout: seconds to wait before aborting.

    Returns:
        The full HTML of the response as a string.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text