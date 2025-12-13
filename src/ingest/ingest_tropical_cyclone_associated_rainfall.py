"""
Ingest tropical cyclone associated rainfall from the PAGASA-DOST website.

This module provides functions to extract key information from the
tropical cyclone associated rainfall page, including:

- Tropical cyclone associated rainfall image source

All extracted data is saved as JSON files in the
`data/raw/tropical_cyclone_associated_rainfall/` subdirectory on the local machine.
"""

import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/tropical_cyclone_associated_rainfall` subdirectory to store JSON files.

    This subdirectory holds the tropical cyclone associated rainfall data ingested from the
    PAGASA-DOST website.
    """
    # Create the data/raw/tropical_cyclone_associated_rainfall/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/tropical_cyclone_associated_rainfall'):
        os.makedirs('data/raw/tropical_cyclone_associated_rainfall')

def extract_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Extract the BeautifulSoup object from the tropical cyclone
    associated rainfall page.

    :param url: URL of the PAGASA-DOST tropical cyclone associated rainfall page.
    :type url: str

    :return: BeautifulSoup object for navigating the page, or None if extraction fails
    :rtype: BeautifulSoup | None
    """
    response = requests.get(url)

    # We need to check if the status code of the response for the request is unsuccessful
    if response.status_code != 200:
        return None

    # Parse as a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_tc_associated_rainfalls_of_2025_tags(
    soup: BeautifulSoup | None
) -> list[BeautifulSoup] | None:
    """
    Extract HTML tag of tropical cyclone associated rainfalls for
    the year 2025 from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page,
        or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: List of HTML tags for the tropical cyclone associated
        rainfall of the year 2025
    :rtype: list[BeautifulSoup] | None
    """
    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return None

    # Extract HTML tags for tc associated rainfalls for the year 2025
    div_tag_with_row_climate_page_class = soup.find(
        'div',
        attrs={
            'class': 'row climate-page'
        }
    )
    div_tag_with_article_content_class = div_tag_with_row_climate_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 article-content'
        }
    )
    div_tag_with_panel_class = div_tag_with_article_content_class.find(
        'div',
        attrs={
            'class': 'panel'
        }
    )

    # We need to check if the div_tag_with_panel_class is missing
    if div_tag_with_panel_class is None:
        return None

    div_class_with_form_group_class = div_tag_with_panel_class.find(
        'div',
        attrs={
            'class': 'form-group'
        }
    )
    select_tag_with_form_control_classs = div_class_with_form_group_class.find(
        'select',
        attrs={
            'class': 'form-control tc_select'
        }
    )
    tc_associated_rainfalls_of_2025_tags = select_tag_with_form_control_classs.find_all(
        'option'
    )[1:]

    return tc_associated_rainfalls_of_2025_tags

def extract_tc_associated_rainfalls_of_2025(
        tc_associated_rainfalls_of_2025_tags: list[BeautifulSoup] | None
) -> list[str]:
    """
    Extract the tropical cyclone associated rainfall image sources
    for the year 2025 from the PAGASA-DOST website.

    :param tc_associated_rainfalls_of_2025_tags: HTML tag for the
        tropical cyclone associated rainfall of the year 2025
    :type tc_associated_rainfalls_of_2025_tags:

    :return: List of tropical cyclone associated rainfall image sources
        for the year of 2025
    :rtype: str
    """
    tc_associated_rainfalls_of_2025 = []

    # We need to check if tc_associated_rainfalls_of_2025_tags is missing
    if tc_associated_rainfalls_of_2025_tags == None:
        return tc_associated_rainfalls_of_2025