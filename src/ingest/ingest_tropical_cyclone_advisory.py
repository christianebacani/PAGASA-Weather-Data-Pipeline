"""
Ingest tropical cyclone advisory data from the PAGASA-DOST website.

This module provides functions to ingest key information from the
tropical cyclone advisory page, including:

- TBD

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
    Create the `data/raw/tropical_cyclone_advisory` subdirectory to store JSON files.

    This subdirectory holds the tropical cyclone advisory data, ingested from the
    PAGASA-DOST website.
    """
    # Create the data/raw/tropical_cyclone_advisory/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/tropical_cyclone_advisory'):
        os.makedirs('data/raw/tropical_cyclone_advisory')

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest the BeautifulSoup object from the tropical cyclone advisory page.

    :param url: URL of the PAGASA-DOST tropical cyclone advisory page.
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