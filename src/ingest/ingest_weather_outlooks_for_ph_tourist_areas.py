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
    Docstring for ingest_and_parse_from_url
    
    :param url: Description
    :type url: str
    :return: Description
    :rtype: BeautifulSoup | None
    """