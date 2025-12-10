"""
Ingest weather advisory data from the PAGASA-DOST website.

This module provides functions to extract key information from the
weather advisory page, including:

- Weather advisory source URL or content

All extracted data is saved as a JSON file in the
`data/raw/weather_advisory/` subdirectory on the local machine.
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/weather_advisory` subdirectory to store JSON files.

    This subdirectory holds the weather advisory data from the PAGASA-DOST website.
    """
    # Create the data/raw/weather_advisory/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/weather_advisory'):
        os.makedirs('data/raw/weather_advisory')

def extract_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Extract the BeautifulSoup object from the weather advisory page.

    :param url: URL of the PAGASA-DOST weather advisory page.
    :type url: str

    :return: BeautifulSoup object for navigating the page, or None if extraction fails
    :rtype: BeautifulSoup | None
    """
    response = requests.get(url)

    # We need to check if the status code of the response for the request is unsuccessful
    if response.status_code != 200:
        return None

    # Parse as a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_weather_advisory(
        soup: BeautifulSoup | None
) -> str:
    """
    Extract the weather advisory source URL or content from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Weather advisory source URL or content
    :rtype: str
    """
    weather_advisory = ''

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return weather_advisory

    # Extract HTML tags for weather advisory
    div_tag_with_row_marine_class = soup.find('div', attrs={'class': 'row marine'})
    weather_advisory_tag = div_tag_with_row_marine_class.find(
        'div',
        attrs={
            'class': 'weekly-content-adv'
        }
    )
    iframe_tag = weather_advisory_tag.find('iframe')

    # We need to check if the iframe_tag is missing
    if iframe_tag is None:
        return weather_advisory

    weather_advisory = iframe_tag['src']
    weather_advisory = str(weather_advisory).strip()

    return weather_advisory

def save_weather_advisory_to_json(
        weather_advisory: str
) -> None:
    """
    Save the weather advisory source URL or content to a JSON file
    in the `data/raw/weather_advisory/` subdirectory on the local machine.

    :param weather_advisory: Weather advisory source URL or content
    :type weather_advisory: str
    """
    # Create a dictionary to store the weather advisory
    data = {
        "weather_advisory": weather_advisory
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/weather_advisory/weather_advisory.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()