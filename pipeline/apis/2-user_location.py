#!/usr/bin/env python3
"""Script that prints the location of a GitHub user."""
import requests
import sys
import time


def user_location(url):
    """Print the location of the GitHub user found at url.

    Prints "Not found" if the user doesn't exist, and "Reset in X min"
    when the rate limit is exceeded.

    Args:
        url: the full GitHub API URL of the user.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset = int(response.headers["X-Ratelimit-Reset"])
        minutes = int((reset - time.time()) / 60)
        print("Reset in {} min".format(minutes))
    else:
        print(response.json()["location"])


if __name__ == '__main__':
    user_location(sys.argv[1])
