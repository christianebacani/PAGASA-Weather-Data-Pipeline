"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os
import requests
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/daily_weather_forecasts/`
    for ingested data from the daily weather forecast page of PAGASA-DOST
    website.
    """
    if not os.path.exists('data/raw/daily_weather_forecasts'):
        os.makedirs('data/raw/daily_weather_forecasts')

def ingest_and_parse_soup_from_url(
        url: str       
) -> BeautifulSoup | None:
    """
    Ingest and parse BeatifulSoup object
    from the URL of the daily weather forecast
    page of the PAGASA-DOST website.

    :param url: URL of the daily weather forecast
        page to ingest and parse
    :type url: str

    :return: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :rtype: BeautifulSoup | None
    """
    response = requests.get(url)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup

def ingest_issued_datetimes(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetimes of the daily weather
    forecast page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the daily weather forecast
        page from the PAGASA-DOST website
    :rtype: str
    """