#!/usr/bin/env python3
"""Module that lists the starships able to hold a number of passengers."""
import requests


def availableShips(passengerCount):
    """Return the names of ships that can hold passengerCount passengers.

    Follows the API pagination until there is no next page. Ships whose
    passenger value is not a number (e.g. "n/a", "unknown") are skipped.
    Returns an empty list if no ship is available.
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []
    while url:
        response = requests.get(url)
        data = response.json()
        for ship in data.get("results", []):
            passengers = ship.get("passengers", "").replace(",", "")
            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship.get("name"))
            except ValueError:
                continue
        url = data.get("next")
    return ships
