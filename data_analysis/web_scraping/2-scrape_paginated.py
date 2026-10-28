#!/usr/bin/env python3
"""Module that scrapes all pages of quotes by following Next links."""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape every page of quotes and return them as one list.

    Args:
        base_url: the URL of the first page.

    Returns:
        A list of quote dicts from all pages.
    """
    results = []
    url = base_url
    while url:
        results.extend(scrape_basic(url))

        html = fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        next_li = soup.find("li", class_="next")
        if next_li is None:
            break

        href = next_li.find("a")["href"]
        url = parse.urljoin(url, href)
        time.sleep(1)
    return results