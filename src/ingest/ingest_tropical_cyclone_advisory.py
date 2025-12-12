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