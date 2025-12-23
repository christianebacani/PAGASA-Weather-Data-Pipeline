"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os
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

# TODO:
# - Fix the docstring content for every function to make it consistent
# - Fix the docsring content for every module to make it consistent

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup:
    """
    Ingests BeautifulSoup object from the
    URL of the daily weather forecast page
    of PAGASA-DOST website.

    :param url: URL of the daily weather forecast
        page from the PAGASA-DOST website
    :type url: str

    :return: BeautifulSoup object for navigating and
        manipulating content of the daily weather
        forecast page from the PAGASA-DOST website
    :rtype: BeautifulSoup
    """