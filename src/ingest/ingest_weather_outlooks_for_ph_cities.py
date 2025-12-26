"""
Docstring for ingest.ingest_weather_outlooks_for_ph_cities
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/weather_outlooks_for_ph_cities/`
    for ingested data from the weather outlook for selected Philippine cities
    page of PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/weather_outlooks_for_ph_cities'):
        os.makedirs('data/raw/weather_outlooks_for_ph_cities')

def ingest_and_parse_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    """