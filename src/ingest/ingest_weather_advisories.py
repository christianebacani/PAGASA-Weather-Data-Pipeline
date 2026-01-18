"""
Docstring for ingest.ingest_weather_advisories
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/weather_advisories/`
    for ingested data from the weather advisories page of PAGASA-
    DOST website.
    """
    if not os.path.exists('data/raw/weather_advisories'):
        os.makedirs('data/raw/weather_advisories')

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