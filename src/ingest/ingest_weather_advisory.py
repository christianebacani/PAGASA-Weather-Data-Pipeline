"""
Ingest weather advisory data from the PAGASA-DOST website.

This module contains functions used by the ETL pipeline to ingest data from the
PAGASA-DOST weather advisory page and store the ingested artifacts as JSON
files under the `data/weather_advisories/` subdirectory for further processing.

Ingested data:
- TBA
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/weather_advisories/`
    for ingested data from the weather advisories page of PAGASA-
    DOST website.
    """
    if not os.path.exists('data/weather_advisories'):
        os.makedirs('data/weather_advisories')

def ingest_and_parse_soup_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the weather advisories
    page of the PAGASA-DOST website.

    :param url: URL of the weather adivsories
        page to ingest and parse
    :type url: str

    :return: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :rtype: BeautifulSoup | None
    """
    response = requests.get(url)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup