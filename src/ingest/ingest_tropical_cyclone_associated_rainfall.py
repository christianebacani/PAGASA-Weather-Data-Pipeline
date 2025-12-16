"""
Ingest tropical cyclone associated rainfall from the PAGASA-DOST website.

This module provides functions to ingest key information from the
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

    This subdirectory holds the tropical cyclone associated rainfall data, ingested from the
    PAGASA-DOST website.
    """
    # Create the data/raw/tropical_cyclone_associated_rainfall/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/tropical_cyclone_associated_rainfall'):
        os.makedirs('data/raw/tropical_cyclone_associated_rainfall')

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest the BeautifulSoup object from the tropical cyclone
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

def ingest_tc_assoc_rainfall_tag(
        soup: BeautifulSoup | None
) -> BeautifulSoup | None:
    """
    Ingest HTML tag of the tropical cyclone associated
    rainfall for all listed years from the PAGASA-DOST
    website.

    :param soup: BeautifulSoup object for navigating the page,
        or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: HTML tag of the tropical cyclone associated rainfall
        for all listed years
    :rtype: BeautifulSoup | None
    """
    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return None

    # Ingest HTML tags to get the specific tag for the tropical cyclone associated rainfall for all listed years
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

    # We need to check if div_tag_with_panel_class is missing
    if div_tag_with_panel_class is None:
        return None

    tc_assoc_rainfall_tag = div_tag_with_panel_class.find(
        'div',
        attrs={
            'class': 'form-group'
        }
    )

    return tc_assoc_rainfall_tag

def ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag: BeautifulSoup | None,
        year: int
) -> list[str]:
    """
    Ingest the tropical cyclone associated rainfall
    for the specified year from the PAGASA-DOST website.

    :param tc_assoc_rainfall_tag: HTML tag of the tropical
        cyclone associated rainfall for all listed years
    :type tc_assoc_rainfall_tag: BeautifulSoup | None

    :param year: Specified year of the tropical cyclone
        associated rainfall
    :type year: int

    :return: Tropical cyclone associated rainfall image
        sources
    :rtype: list[str]
    """
    tc_assoc_rainfall_image_sources = {
        2025: [],
        2024: [],
        2023: [],
        2022: [],
        2021: [],
        2020: [],
        2019: [],
        2018: []
    }

    # We need to check if tc_assoc_rainfall_tag is missing
    if tc_assoc_rainfall_tag is None:
        return []

    # Use find_all() method to access all tc associated rainfall HTML tags
    select_tag_with_form_control_classes = tc_assoc_rainfall_tag.find_all(
        'select',
        attrs={
            'class': 'form-control tc_select'
        }
    )

    # Loop through the select HTML tags to ingest tc associated rainfall image source tags
    for select_tag_with_form_control_class in select_tag_with_form_control_classes:
        tc_assoc_rainfall_image_source_tags = select_tag_with_form_control_class.find_all(
            'option'
        )[1:]

        list_of_all_tc_assoc_rainfal_image_sources = []

        # Loop through tags to ingest tc associated rainfall image source
        for tc_assoc_rainfall_image_source_tag in tc_assoc_rainfall_image_source_tags:
            tc_assoc_rainfall_image_source = str(tc_assoc_rainfall_image_source_tag['value']).strip()
            list_of_all_tc_assoc_rainfal_image_sources.append(
                tc_assoc_rainfall_image_source
            )

        # Loop through tc associated rainfall image sources dict to map the tc associated rainfall image sources list
        for key, value in tc_assoc_rainfall_image_sources.items():
            if value == []:
                # Map the tc associated rainfall image sources list to the correct key (year)
                tc_assoc_rainfall_image_sources[key] = list_of_all_tc_assoc_rainfal_image_sources
                break

    return tc_assoc_rainfall_image_sources[year]

def save_tc_assoc_rainfall_image_sources_to_raw_subdir(
        tc_assoc_rainfall_image_sources: list[str],
        year: int
) -> None:
    """
    Save the tropical cyclone associated rainfall image
    sources for the specified year to a JSON file in the
    `data/raw/tropical_cyclone_associated_rainfall/`
    subdirectory on the local machine.

    :param tc_assoc_rainfall_image_sources: Tropical
        cyclone associated rainfall image sources
    :type tc_assoc_rainfall_image_sources: list[str]

    :param year: Specified year of the tropical cyclone
        associated rainfall image sources
    :type year: int
    """
    # Create a dictionary to store the tc associated rainfall image sources for the specified year
    data = {
        f"tc_associated_rainfall_image_sources_of_{year}": tc_assoc_rainfall_image_sources
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        f'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_{year}.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()