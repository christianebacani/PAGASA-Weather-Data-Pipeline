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

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse a daily weather forecast
    page into a BeautifulSoup object.

    :param url: URL of the daily weather forecast
        page to ingest and parse
    :type url: str

    :return: A BeautifulSoup object representing
        the parsed HTML of the page
    :rtype: BeautifulSoup
    """
    response = requests.get(url)

    if response.status_code != 200:
        return None