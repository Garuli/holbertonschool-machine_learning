#!/usr/bin/env python3
"""Module that logs in to quotes.toscrape.com and scrapes quotes."""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in with a session and scrape the protected quotes."""
    session = requests.Session()
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.find("input", {"name": "csrf_token"})["value"]

    payload = {
        "username": user,
        "password": pwd,
        "csrf_token": token
    }
    session.post(login_url, data=payload)

    page = session.get("https://quotes.toscrape.com/")
    soup = BeautifulSoup(page.text, "html.parser")

    quotes = []
    for div in soup.find_all("div", class_="quote"):
        quotes.append({
            "text": div.find("span", class_="text").get_text(),
            "author": div.find("small", class_="author").get_text(),
            "tags": [t.get_text() for t in div.find_all("a", class_="tag")]
        })
    return quotes
