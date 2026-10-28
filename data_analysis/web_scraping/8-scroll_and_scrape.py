#!/usr/bin/env python3
"""Module that scrolls an infinite-scroll page and scrapes its products."""
import time
from selenium import webdriver

CSS = "css selector"


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to the bottom of the page and scrape all unique products.

    Args:
        url: the infinite-scroll page.
        scroll_pause: seconds to wait after each scroll.

    Returns:
        A list of unique dicts with keys "title", "price", "description"
        and "rating".
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    products = []
    seen = set()
    try:
        driver.get(url)
        time.sleep(scroll_pause)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height <= last_height:
                break
            last_height = new_height

        cards = driver.find_elements(CSS, "div.thumbnail")
        for card in cards:
            title = card.find_element(CSS, "a.title").get_attribute("title")
            price = card.find_element(CSS, "h4.price").text
            if (title, price) in seen:
                continue
            seen.add((title, price))
            desc = card.find_element(CSS, "p.description").text
            stars = card.find_elements(CSS, ".ratings .ws-icon-star")
            products.append({
                "title": title,
                "price": price,
                "description": desc,
                "rating": len(stars)
            })
    finally:
        driver.quit()
    return products
