#!/usr/bin/env python3
"""Module that scrapes the first page of quotes from quotes.toscrape.com."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape the first page of quotes and return them as a list.

    Args:
        url: the Quotes List endpoint.

    Returns:
        A list of dicts with keys "text", "author" and "tags".
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    quotes = []
    for block in soup.find_all("div", class_="quote"):
        quotes.append({
            "text": block.find("span", class_="text").get_text(),
            "author": block.find("small", class_="author").get_text(),
            "tags": [t.get_text() for t in block.find_all("a", class_="tag")]
        })
    return quotes
