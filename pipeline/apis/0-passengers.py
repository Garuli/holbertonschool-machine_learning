#!/usr/bin/env python3
"""Module that lists Star Wars ships by passenger capacity."""
import requests


def availableShips(passengerCount):
    """Return the names of ships that can hold passengerCount passengers.

    Args:
        passengerCount: the number of passengers needed.

    Returns:
        A list of ship names, or an empty list if none is available.
    """
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"
    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        for ship in data["results"]:
            passengers = ship["passengers"].replace(",", "")
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])
        url = data["next"]
    return ships
