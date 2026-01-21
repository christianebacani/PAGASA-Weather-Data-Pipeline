"""
Ingest weather advisory data from the PAGASA-DOST website.

This module contains functions used by the ETL pipeline to ingest data from the
PAGASA-DOST tropical cyclone bulletin page and store the ingested artifacts as JSON
files under the `data/raw/tropical_cyclone_bulletins/` subdirectory for further processing.

Ingested data:
- TBA
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/tropical_cyclone_bulletins/`
    for ingested data from the tropical cyclone bulletin page of
    PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/tropical_cyclone_bulletins'):
        os.makedirs('data/raw/tropical_cyclone_bulletins')

def ingest_and_parse_soup_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the tropical cyclone
    bulletin page of the PAGASA-DOST website.

    :param url: URL of the tropical cyclone
        bulletin page to ingest and parse
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

def ingest_tropical_cyclone_name(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the tropical cyclone name from the
    tropical cyclone bulletin page of the PAGASA-
    DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone name from the tropical
        cyclone bulletin page of the PAGASA-DOST website
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

def save_ingested_tropical_cyclone_name(
        tropical_cyclone_name: str
) -> None:
    """
    Save the ingested tropical cyclone name from the
    tropical cyclone bulletin page of the PAGASA-
    DOST website.
    
    :param tropical_cyclone_name: Tropical cyclone
        name from the tropical cyclone bulletin page
        of the PAGASA-DOST website
    :type tropical_cyclone_name: str
    """
    ingested_data = {
        "tropical_cyclone_name": tropical_cyclone_name   
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/tropical_cyclone_name.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_issued_datetime(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetime from the
    tropical cyclone bulletin page of the
    PAGASA-DOST website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetime from the tropical
        cyclone bulletin page of the PAGASA-
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

def save_ingested_issued_datetime(
        issued_datetime: str
) -> None:
    """
    Save the ingested issued datetime from the
    tropical cyclone bulletin page of the PAGASA-
    DOST website.

    :param issued_datetime: Issued datetime of the
        tropical cyclone bulletin page of the PAGASA-
        DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issued_datetime": issued_datetime   
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/issued_datetime.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_time_validity(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validity from the tropical
    cyclone bulletin page of the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Time validity from the tropical
        cyclone bulletin page of the PAGASA-
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

def save_ingested_time_validity(
        time_validity: str
) -> None:
    """
    Save the ingested time validity from the
    tropical cyclone bulletin page of the PAGASA-
    DOST website.

    :param time_validity: Time validity from the
        tropical cyclone bulletin page of the PAGASA-
        DOST website
    :type time_validitity: str
    """
    ingested_data = {
        "time_validity": time_validity
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/time_validity.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_tropical_cyclone_summary(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the tropical cyclone summary from the
    tropical cyclone bulletin page of the PAGASA-
    DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone summary from the tropical
        cyclone bulletin page of the PAGASA-DOST website
    :rtype: str
    """
    tropical_cyclone_summary = ''

    if soup is None:
        return tropical_cyclone_summary

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
    tropical_cyclone_summary_and_descriptions_tag = div_tag_with_tab_pane_class.find_all(
        'div',
        attrs={
            'class': 'row'
        }
    )[2]
    tropical_cyclone_summary_tag = tropical_cyclone_summary_and_descriptions_tag.find(
        'h5'
    )
    tropical_cyclone_summary = tropical_cyclone_summary_tag.text
    tropical_cyclone_summary = str(tropical_cyclone_summary)

    return tropical_cyclone_summary

def save_ingested_tropical_cyclone_summary(
        tropical_cyclone_summary: str
) -> None:
    """
    Save the ingested tropical cyclone summary from the
    tropical cyclone bulletin page of the PAGASA-DOST
    website.

    :param tropical_cyclone_summary: Time validity from the
        tropical cyclone bulletin page of the PAGASA-DOST
        website
    :type tropical_cyclone_summary: str
    """
    ingested_data = {
        "tropical_cyclone_summary": tropical_cyclone_summary
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/tropical_cyclone_summary.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_tropical_cyclone_descriptions(
        soup: BeautifulSoup | None
) -> list[str]:
    """
    Ingest the tropical cyclone descriptions from the
    tropical cyclone bulletin page of the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone descriptions from the
        tropical cyclone bulletin page of the PAGASA-
        DOST website
    :rtype: list[str]
    """
    tropical_cyclone_descriptions = []

    if soup is None:
        return ingest_tropical_cyclone_descriptions

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
    tropical_cyclone_summary_and_descriptions_tag = div_tag_with_tab_pane_class.find_all(
        'div',
        attrs={
            'class': 'row'
        }
    )[2]
    tropical_cyclone_descriptions_tag = tropical_cyclone_summary_and_descriptions_tag.find(
        'ul'
    )
    list_of_all_list_item_tag = tropical_cyclone_descriptions_tag.find_all(
        'li'
    )

    for list_item_tag in list_of_all_list_item_tag:
        tropical_cyclone_description = list_item_tag.text
        tropical_cyclone_description = str(tropical_cyclone_description)
        tropical_cyclone_descriptions.append(
            tropical_cyclone_description
        )

    return tropical_cyclone_descriptions

def save_ingested_tropical_cyclone_descriptions(
        tropical_cyclone_descriptions: list[str]
) -> None:
    """
    Save the ingested tropical cyclone descriptions
    from the tropical cyclone bulletin page of the
    PAGASA-DOST website.

    :param tropical_cyclone_descriptions: Tropical
        cyclone descriptions of the tropical cyclone
        bulletin page of the PAGASA-DOST website
    :type tropical_cyclone_descriptions: list[str]
    """
    ingested_data = {
        "tropical_cyclone_descriptions": tropical_cyclone_descriptions
    }

    with open(
        'data/raw/tropical_cyclone_bulletins/tropical_cyclone_descriptions.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_tropical_cyclone_track_map(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the tropical cyclone track map from
    the tropical cyclone bulletin page of the PAGASA
    -DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone track map from the tropical
        cyclone bulletin page of the PAGASA-DOST website
    :rtype: str
    """
    tropical_cyclone_track_map = ''

    if soup is None:
        return tropical_cyclone_track_map

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
    tropical_cyclone_track_map_tag = div_tag_with_tab_pane_class.find_all(
        'div',
        attrs={
            'class': 'row'
        }
    )[2]
    image_tag = tropical_cyclone_track_map_tag.find(
        'img'
    )
    tropical_cyclone_track_map = image_tag['src']
    tropical_cyclone_track_map = str(tropical_cyclone_track_map)

    return tropical_cyclone_track_map