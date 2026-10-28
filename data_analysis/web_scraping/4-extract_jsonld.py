#!/usr/bin/env python3
"""Module that extracts quotes from JSON-LD blocks embedded in a page."""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quotes from the JSON-LD scripts of a page.

    Args:
        url: the page to fetch.

    Returns:
        A list of dicts with keys "text", "author" and "tags".
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    quotes = []
    scripts = soup.find_all("script", type="application/ld+json")
    for script in scripts:
        try:
            data = json.loads(script.get_text())
        except json.JSONDecodeError:
            continue

        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict) or item.get("@type") != "Quote":
                continue

            tags = item.get("keywords", [])
            if isinstance(tags, str):
                tags = [t.strip() for t in tags.split(",") if t.strip()]

            quotes.append({
                "text": item.get("text"),
                "author": item.get("author", {}).get("name"),
                "tags": tags
            })
    return quotes
