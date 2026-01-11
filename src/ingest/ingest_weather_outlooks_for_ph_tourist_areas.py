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
    Ingest and parse BeautifulSoup object
    from the URL of the weather outlook for
    selected Philippine tourist areas page
    of the PAGASA-DOST website.

    :param url: URL of the weather outlook for
        selected Philippine tourist areas page
        to ingest and parse
    :type url: str

    :return: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
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
    Ingest the issued datetimes of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the weather
        outlook for selected Philippine tourist
        areas page from the PAGASA-DOST website.
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

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save ingested issued datetimes of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param issued_datetime: Issued datetimes
        of the weather outlook for selected
        Philippine tourist areas page from
        the PAGASA-DOST website.
    :type issued_datetime: str
    """
    ingested_data = {
        "issued_datetime": issued_datetime
    }

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_time_validities(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validities of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the page,
        or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Time validities of the weather outlook
        for selected Philippine tourist areas page from
        the PAGASA-DOST website.
    :rtype: str
    """
    time_validity = ''

    if soup is None:
        return time_validity

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
    bold_tag = issued_datetimes_and_time_validities_tag.find_all(
        'b'
    )[1]
    time_validity = bold_tag.text
    time_validity = str(time_validity)

    return time_validity

def save_ingested_time_validities(
        time_validity: str
) -> None:
    """
    Save ingested time validities of the weather
    outlook for selected Philippine tourist areas
    page from the PAGASA-DOST website.

    :param time_validity: Time validities of the
        weather outlook for selected Philippine
        tourist areas page from the PAGASA-DOST
        website
    :type time_validity: str
    """