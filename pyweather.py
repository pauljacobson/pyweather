#!/usr/bin/env python3

"""
Get weather data from OpenWeatherMap.org
and expose it to other scripts.
"""

import json

import requests


def api_key_gen():
    """
    Generate an API key for OpenWeatherMap.org.
    """
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)
        api_key = secrets['openweathermap_api_key']
        return api_key


def main(city):
    """
    Get weather data from OpenWeatherMap.org
    and return it as a dictionary.
    """
    api_key = api_key_gen()
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    url = base_url.format(city, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data


if __name__ == "__main__":
    main('Modiin')
