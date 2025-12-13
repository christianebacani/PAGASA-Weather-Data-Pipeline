"""
Ingest tropical cyclone associated rainfall from the PAGASA-DOST website.

This module provides functions to extract key information from the
tropical cyclone associated rainfall page, including:

- Tropical cyclone associated rainfall image sources

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

def extract_tc_associated_rainfall_tags_of_2025(
    soup: BeautifulSoup | None
) -> list[BeautifulSoup] | None:
    """
    Extract HTML tags of the tropical cyclone associated rainfalls
    for the year 2025 from the PAGASA-DOST website.

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
    tc_associated_rainfall_tags_of_2025 = select_tag_with_form_control_classs.find_all(
        'option'
    )[1:]

    return tc_associated_rainfall_tags_of_2025

def extract_tc_associated_rainfall_image_sources_of_2025(
    tc_associated_rainfall_tags_of_2025: list[BeautifulSoup] | None
) -> list[str]:
    """
    Extract the tropical cyclone associated rainfall image sources
    for the year 2025 from the PAGASA-DOST website.

    :param tc_associated_rainfall_tags_of_2025: List of HTML tags
        for the tropical cyclone associated rainfall of the year 2025
    :type tc_associated_rainfall_tags_of_2025: list[BeautifulSoup] | None

    :return: List of tropical cyclone associated rainfall image sources
        for the year 2025
    :rtype: list[str]
    """
    tc_associated_rainfall_image_sources = []

    # We need to check if tc_associated_rainfall_tags_of_2025 is missing
    if tc_associated_rainfall_tags_of_2025 == None:
        return tc_associated_rainfall_image_sources

    # Loop through the tc associated rainfall tags for the year of 2025 to extract their image sources
    for tc_associated_rainfall_of_2025_tag in tc_associated_rainfall_tags_of_2025:
        tc_associated_rainfall_image_source = str(tc_associated_rainfall_of_2025_tag['value']).strip()
        tc_associated_rainfall_image_sources.append(
            tc_associated_rainfall_image_source
        )

    return tc_associated_rainfall_image_sources

def save_tc_associated_rainfall_image_sources_of_2025_to_json(
    tc_associated_rainfall_image_sources: list[str]
) -> None:
    """
    Save the tropical cyclone associated image sources for the year
    2025 from the PAGASA-DOST webite.

    :param tc_associated_rainfall_image_sources: List of tropical
        cyclone associated rainfall image sources for the year 2025
    :type tc_associated_rainfall_image_sources: list[str]
    """
    # Create a dictionary to store the tc associated rainfall image sources
    data = {
        "tc_associated_rainfall_image_sources_of_2025": tc_associated_rainfall_image_sources
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2025',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def extract_tc_associated_rainfall_tags_of_2024(
    soup: BeautifulSoup | None
) -> list[BeautifulSoup] | None:
    """
    Extract list of HTML tags for the tropical cyclone associated
    rainfalls of the year 2024 from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page,
        or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: List of HTML tags for the tropical cyclone associated
        rainfall of the year 2024
    :rtype: list[BeautifulSoup] | None
    """
    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return None

    # Extract HTML tags for tc associated rainfalls for the year 2024
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
    select_tag_with_form_control_classs = div_class_with_form_group_class.find_all(
        'select',
        attrs={
            'class': 'form-control tc_select'
        }
    )[1]
    tc_associated_rainfall_tags_of_2025 = select_tag_with_form_control_classs.find_all(
        'option'
    )[1:]

    return tc_associated_rainfall_tags_of_2025