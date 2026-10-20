#!/usr/bin/env python3
fetch_html = __import__('0-fetch_html').fetch_html
html0 = fetch_html("https://quotes.toscrape.com/",
                   headers={"User-Agent": "test-agent"}, timeout=5)
print("Test 0:\n", html0[:209])
try:
    fetch_html("https://quote.toscrape.com/")
except Exception as e:
    print("Test 1:\n", e)
