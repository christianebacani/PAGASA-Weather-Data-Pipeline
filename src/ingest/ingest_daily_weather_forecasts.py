"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates a subdirectory path `data/raw/daily_weather_forecasts/`
    to store ingested data as a JSON file from the daily weather
    forecast page of PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/daily_weather_forecasts'):
        os.makedirs('data/raw/daily_weather_forecasts')

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup:
    """
    Docstring for ingest_beautiful_soup_object
    
    :param url: Description
    :type url: str
    :return: Description
    :rtype: BeautifulSoup
    """