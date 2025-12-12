"""
Ingest tropical cyclone advisory data from the PAGASA-DOST website.

This module provides functions to extract key information from the
tropical cyclone advisory page, including:

- TBD

All extracted data is saved as a JSON file in the
`data/raw/weather_advisory/` subdirectory on the local machine.
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/tropical_cyclone_advisory` subdirectory to store JSON files.

    This subdirectory holds the tropical cyclone advisory data from the PAGASA-DOST
    website.
    """
    # Create the data/raw/tropical_cyclone_advisory/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/tropical_cyclone_advisory'):
        os.makedirs('data/raw/tropical_cyclone_advisory')