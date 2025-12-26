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
    Ingest and parse BeautifulSoup object
    from the URL of the weather outlook for
    selected Philippine cities page of the
    PAGASA-DOST website.

    :param url: URL of the weather outlook for
        selected Philippine cities page to ingest
        and parse
    :type url: str

    :return: A BeautifulSoup object representing the
        parsed HTML of the page, or NoneType if the page
        does not allow scraping
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
    Ingest the issued datetimes of the weather
    outlook for selected Philippine cities page
    from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the weather outlook for
        selected Philippine cities page from the PAGASA-DOST
        website.
    :rtype: str
    """
    issued_datetime = ''

    if soup is None:
        return issued_datetime

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    issued_datetimes_and_time_validities_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    bold_tag = issued_datetimes_and_time_validities_tag.find(
        'b'
    )
    issued_datetime = bold_tag.text
    issued_datetime = str(issued_datetime)

    return issued_datetime

def ingest_time_validities(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validities of the
    weather outlook for selected Philippine
    cities page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Time validities of the weather outlook
        for selected Philippine cities page from the
        PAGASA-DOST website.
    :rtype: str
    """