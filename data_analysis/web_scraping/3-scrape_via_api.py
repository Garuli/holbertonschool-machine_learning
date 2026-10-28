#!/usr/bin/env python3
"""Module that scrapes quotes through the quotes.toscrape.com API."""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch quotes from every page of the quotes API.

    Args:
        base_url: the root URL of the site.

    Returns:
        A list of dicts with keys "text", "author" and "tags".
    """
    quotes = []
    page = 1
    while True:
        url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        data = json.loads(fetch_html(url))
        for q in data["quotes"]:
            quotes.append({
                "text": q["text"],
                "author": q["author"]["name"],
                "tags": q["tags"]
            })
        if not data.get("has_next"):
            break
        page += 1
    return quotes