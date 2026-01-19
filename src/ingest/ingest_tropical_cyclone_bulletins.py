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

def save_ingested_tropical_cyclone_names(
        tropical_cyclone_name: str
) -> None:
    """
    Save ingested tropical cyclone names of the
    tropical cyclone bulletins page from the
    PAGASA-DOST website.
    
    :param tropical_cyclone_name: Tropical cyclone
        names of the tropical cyclone bulletins page
        from the PAGASA-DOST website
    :type tropical_cyclone_name: str
    """
    ingested_data = {
        "tropical_cyclone_name": tropical_cyclone_name   
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/tropical_cyclone_names.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_issued_datetimes(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetimes of the
    tropical cyclone bulletins page from
    the PAGASA-DOST website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the tropical
        cyclone bulletins page from the PAGASA-
        DOST website
    :rtype: str
    """
    issued_datetime = ''

    if soup is None:
        return issued_datetime

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
    div_tag_with_tab_pane_class = div_tag_with_article_content_class.find(
        'div',
        attrs={
            'role': 'tabpanel',
            'class': 'tab-pane active'
        }
    )
    issued_datetimes_and_time_validities_tag = div_tag_with_tab_pane_class.find_all(
        'div',
        attrs={
            'class': 'row'
        }
    )[1]
    issued_datetimes_tag = issued_datetimes_and_time_validities_tag.find(
        'h5'
    )
    issued_datetime = issued_datetimes_tag.text
    issued_datetime = str(issued_datetime)

    return issued_datetime

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save ingested issued datetimes of the tropical
    cyclone bulletins page from the PAGASA-DOST website.

    :param issued_datetime: Issued datetimes of the
        tropical cyclone bulletins page from the PAGASA-
        DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issued_datetime": issued_datetime   
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_time_validities(
    soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validities of the
    tropical cyclone bulletins page from
    the PAGASA-DOST website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Time validities of the tropical
        cyclone bulletins page from the PAGASA-
        DOST website
    :rtype: str
    """
    time_validity = ''

    if soup is None:
        return None

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
    div_tag_with_tab_pane_class = div_tag_with_article_content_class.find(
        'div',
        attrs={
            'role': 'tabpanel',
            'class': 'tab-pane active'
        }
    )
    issued_datetimes_and_time_validities_tag  = div_tag_with_tab_pane_class.find_all(
        'div',
        attrs={
            'class': 'row'
        }
    )[1]
    time_validities_tag = issued_datetimes_and_time_validities_tag.find_all(
        'h5'
    )[1]
    time_validity = time_validities_tag.text
    time_validity = str(time_validity)

    return time_validity

def save_ingested_time_validities(
        time_validity: str
) -> None:
    """
    Save ingested time validities of the tropical
    cyclone bulletins page from the PAGASA-DOST
    website.

    :param time_validitity: Time validities
        of the tropical cyclone bulletins page from
        the PAGASA-DOST website
    :type time_validitity: str
    """
    ingested_data = {
        "time_validity": time_validity
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/time_validities.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)