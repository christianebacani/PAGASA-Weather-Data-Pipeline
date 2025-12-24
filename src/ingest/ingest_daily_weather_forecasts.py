"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os
import requests
import json
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
    issued_datetime = ''

    if soup is None:
        return issued_datetime

    issued_datetimes_tag = soup.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    issued_datetime = issued_datetimes_tag.text
    issued_datetime = str(issued_datetime)
    issued_datetime = issued_datetime.strip()

    return issued_datetime

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save ingested issued datetimes of the daily
    weather forecast page from the PAGASA-DOST
    website.

    :param issued_datetime: Issued datetimes of
        the daily weather forecast page from the
        PAGASA-DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issue_datetime": issued_datetime
    }

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_synopses(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the synopses of the daily weather
    forecast page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Synopses of the daily weather forecast
        page from the PAGASA-DOST website
    :rtype: str
    """
    synopsis = ''

    if soup is None:
        return synopsis

    synopses_tag = soup.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    paragraph_tag = synopses_tag.find(
        'p'
    )
    synopsis = paragraph_tag.text
    synopsis = str(synopsis)
    synopsis = synopsis.strip()

    return synopsis

def save_ingested_synopses(
        synopsis: str
) -> None:
    """
    Save ingested synopses of the daily
    weather forecast page from the PAGASA-DOST
    website.

    :param synopsis: Synopses of the daily weather
        forecast page from the PAGASA-DOST website
    :type synopsis: str
    """
    ingested_data = {
        "synopsis": synopsis
    }

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/synopses.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_tropical_cyclone_informations(
        soup: BeautifulSoup | None
) -> dict[str, str]:
    """
    Ingest the tropical cyclone informations
    of the daily weather forecast page from
    the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone informations of the daily
        weather forecast page from the PAGASA-DOST website
    :rtype: dict[str, str]
    """

def save_ingested_tropical_cyclone_informations(
        tropical_cyclone_informations: dict[str, str]
) -> None:
    """
    Save ingested tropical cyclone informations of the daily
    weather forecast page from the PAGASA-DOST website.

    :param tropical_cyclone_informations: Tropical cyclone
        informations of the daily weather forecast page from
        the PAGASA-DOST website 
    :type tropical_cyclone_informations: dict[str, str]
    """