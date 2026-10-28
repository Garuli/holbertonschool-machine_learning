#!/usr/bin/env python3
"""Module that scrapes static product pages with Selenium."""
import time
from selenium import webdriver

CSS = "css selector"


def scrape_products_list(url):
    """Scrape the products of a static category page.

    Args:
        url: the product category page.

    Returns:
        A list of dicts with keys "title", "price", "description"
        and "rating".
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    products = []
    try:
        driver.get(url)
        time.sleep(1)
        cards = driver.find_elements(CSS, ".thumbnail")
        for card in cards:
            link = card.find_element(CSS, "a.title")
            price = card.find_element(CSS, "h4.price")
            desc = card.find_element(CSS, "p.description")
            stars = card.find_element(CSS, ".ratings p[data-rating]")
            products.append({
                "title": link.get_attribute("title"),
                "price": price.text,
                "description": desc.text,
                "rating": int(stars.get_attribute("data-rating"))
            })
    finally:
        driver.quit()
    return products


scrape_products = scrape_products_list