"""
Docstring for ingest.ingest_tropical_cyclone_bulletins
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
    if not os.path.exists('data/raw/tropical_cyclone_bulletins'):
        os.makedirs('data/raw/tropical_cyclone_bulletins')

def ingest_and_parse_soup_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the tropical cyclone
    bulletins page of the PAGASA-DOST website.

    :param url: URL of the tropical cyclone
        bulletins page to ingest and parse
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

def ingest_tropical_cyclone_names(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the tropical cyclone names of the
    tropical cyclone bulletins page from the
    PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone names of the tropical
        cyclone bulletins page from the PAGASA-DOST
        website
    :rtype: str
    """
    tropical_cyclone_name = ''

    if soup is None:
        return tropical_cyclone_name

    div_tag_with_tropical_cyclone_bulletin_class = soup.find(
        'div',
        attrs={
            'class': 'row tropical-cyclone-weather-bulletin-page'
        }
    )
    div_tag_with_article_content_class = div_tag_with_tropical_cyclone_bulletin_class.find(
        'div',
        attrs={
            'class': 'col-md-12 article-content'
        }
    )
    tropical_cyclone_names_tag = div_tag_with_article_content_class.find(
        'ul',
        attrs={
            'class': 'nav nav-tabs'
        }
    )
    tropical_cyclone_name = tropical_cyclone_names_tag.text
    tropical_cyclone_name = str(tropical_cyclone_name)

    return tropical_cyclone_name