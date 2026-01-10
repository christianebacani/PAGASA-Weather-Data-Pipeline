"""
Docstring for ingest.ingest_weather_outlooks_for_ph_tourist_areas
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/weather_outlooks_for_ph_tourist_areas/`
    for ingested data from the weather outlook for selected Philippine tourist areas
    page of PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/weather_outlooks_for_ph_tourist_areas'):
        os.makedirs('data/raw/weather_outlooks_for_ph_tourist_areas')

def ingest_and_parse_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the weather outlook for
    selected Philippine tourist areas page
    of the PAGASA-DOST website.

    :param url: URL of the weather outlook for
        selected Philippine tourist areas page
        to ingest and parse
    :type url: str

    :return: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :rtype: BeautifulSoup | None
    """