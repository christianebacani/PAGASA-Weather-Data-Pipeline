"""
Ingest tropical cyclone associated rainfall from the PAGASA-DOST website.

This module provides functions to extract key information from the
tropical cyclone associated rainfall page, including:

- Tropical cyclone associated rainfall image sources

All extracted data is saved as JSON files in the
`data/raw/tropical_cyclone_associated_rainfall/` subdirectory on the local machine.
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/tropical_cyclone_associated_rainfall` subdirectory to store JSON files.

    This subdirectory holds the tropical cyclone associated rainfall data ingested from the
    PAGASA-DOST website.
    """
    # Create the data/raw/tropical_cyclone_associated_rainfall/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/tropical_cyclone_associated_rainfall'):
        os.makedirs('data/raw/tropical_cyclone_associated_rainfall')

def extract_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Extract the BeautifulSoup object from the tropical cyclone
    associated rainfall page.

    :param url: URL of the PAGASA-DOST tropical cyclone associated rainfall page.
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

def extract_tc_assoc_rainfall_tags_of_2025(
        soup: BeautifulSoup | None
) -> list[BeautifulSoup] | None:
    """
    Extract HTML tags of the tropical cyclone associated rainfalls
    for the year 2025 from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page,
        or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: List of HTML tags for the tropical cyclone associated
        rainfall of the year 2025
    :rtype: list[BeautifulSoup] | None
    """