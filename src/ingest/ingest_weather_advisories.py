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