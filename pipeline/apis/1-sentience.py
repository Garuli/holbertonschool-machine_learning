#!/usr/bin/env python3
"""Module that lists the home planets of all sentient Star Wars species."""
import requests


def sentientPlanets():
    """Return the names of the home planets of all sentient species.

    A species is sentient when "sentient" is its classification or
    its designation.

    Returns:
        A list of planet names.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"
    while url:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        for species in data["results"]:
            if (species["classification"] == "sentient" or
                    species["designation"] == "sentient"):
                homeworld = species["homeworld"]
                if homeworld:
                    planet = requests.get(homeworld, timeout=10)
                    planet.raise_for_status()
                    planets.append(planet.json()["name"])
        url = data["next"]
    return planets
