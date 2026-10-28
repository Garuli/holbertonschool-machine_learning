#!/usr/bin/env python3
"""Module that scrolls an infinite-scroll page and scrapes its products."""
import time
from selenium import webdriver

CSS = "css selector"
HEIGHT = "return document.body.scrollHeight"


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to the bottom of the page and scrape all unique products.

    Args:
        url: the infinite-scroll page.
        scroll_pause: max seconds to wait for new content after a scroll.

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

        last_height = driver.execute_script(HEIGHT)
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            waited = 0.0
            new_height = last_height
            while waited < scroll_pause:
                time.sleep(0.1)
                waited += 0.1
                new_height = driver.execute_script(HEIGHT)
                if new_height > last_height:
                    break
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
