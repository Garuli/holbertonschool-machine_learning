#!/usr/bin/env python3
"""Module that scrapes a single product detail page with Selenium."""
import time
from selenium import webdriver

CSS = "css selector"


def scrape_product_detail(url, delay=2.0):
    """Scrape the details of one product page.

    Args:
        url: the product detail page.
        delay: seconds to wait after opening the page.

    Returns:
        A dict with keys "title", "price", "description" and "rating".
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)
        title = driver.find_elements(CSS, ".caption h4")[1].text
        price = driver.find_element(CSS, ".caption h4.price").text
        desc = driver.find_element(CSS, ".caption p.description").text
        stars = driver.find_elements(CSS, ".ratings .ws-icon-star")
        return {
            "title": title,
            "price": price,
            "description": desc,
            "rating": len(stars)
        }
    finally:
        driver.quit()
