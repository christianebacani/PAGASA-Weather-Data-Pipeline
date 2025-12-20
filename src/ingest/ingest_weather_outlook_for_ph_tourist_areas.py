"""
Ingest weather outlook data for selected Philippine tourist areas from the PAGASA-DOST website.

This module provides functions to ingest key information from the
weather outlook page, including:

- Issued datetime
- Valid period
- Selected Philippine tourist area names
- Weather dates
- Temperature ranges

All extracted data is saved as JSON files in the
`data/raw/weather_outlook_for_ph_tourist_areas/` subdirectory on the local machine.
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/weather_outlook_for_ph_tourist_areas` subdirectory to store JSON files.

    This subdirectory holds the weather outlook for selected Philippine tourist areas data, ingested
    from the PAGASA-DOST website.
    """
    # Create the data/raw/weather_outlook_for_ph_cities/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/weather_outlook_for_ph_tourist_areas'):
        os.makedirs('data/raw/weather_outlook_for_ph_tourist_areas')

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest the BeautifulSoup object from the weather outlook
    for selected Philippine tourist areas page.

    :param url: URL of the PAGASA-DOST weather outlook for selected Philippine tourist areas page.
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

def ingest_issued_datetime(
    soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetime of the weather outlook for selected Philippine
    tourist areas from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Issued datetime of the weather outlook for selected Philippine tourist areas
    :rtype: str
    """
    issued_datetime = ''

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return issued_datetime

    # Ingest HTML tags for issued datetime of the weather outlook for selected PH tourist areas
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    issued_datetime_and_valid_period_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    div_tag_with_validity_class = issued_datetime_and_valid_period_tag.find(
        'div',
        attrs={
            'class': 'validity'
        }
    )

    # We need to check if the div_tag_with_validity_class is not missing
    if div_tag_with_validity_class is not None:
        issued_datetime_tag = div_tag_with_validity_class.find('b')
        issued_datetime = str(issued_datetime_tag.text).strip()
    
    return issued_datetime

def save_ingested_issued_datetime(
        issued_datetime: str
) -> None:
    """
    Save the ingested issued datetime of the weather outlook for selected
    Philippine tourist areas to a JSON file in the `data/raw/weather_outlook_for_ph_tourist_areas/`
    subdirectory on the local machine.

    :param issued_datetime: Issued datetime of the weather outlook for selected Philippine tourist areas
    :type issued_datetime: str
    """
    # Create a dictionary to store the ingested issued datetime
    data = {
        "issued_datetime": issued_datetime
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/weather_outlook_for_ph_tourist_areas/issued_datetime.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_valid_period(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the valid period of the weather outlook for selected Philippine
    tourist areas from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Valid period of the weather outlook for selected Philippine tourist areas
    :rtype: str
    """
    valid_period = ''

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return valid_period

    # Ingest HTML tags for valid period of the weather outlook for selected PH tourist areas
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    issued_datetime_and_valid_period_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    div_tag_with_validity_class = issued_datetime_and_valid_period_tag.find(
        'div',
        attrs={
            'class': 'validity'
        }
    )

    # We need to check if the div_tag_with_validity_class is not missing
    if div_tag_with_validity_class is not None:
        valid_period_tag = div_tag_with_validity_class.find_all('b')[1]
        valid_period = str(valid_period_tag.text).strip()

    return valid_period

def save_ingested_valid_period(
    valid_period: str
) -> None:
    """
    Save the ingested valid period of the weather outlook for selected
    Philippine tourist areas to a JSON file in the `data/raw/weather_outlook_for_ph_tourist_areas/`
    subdirectory on the local machine.

    :param issued_datetime: Valid period of the weather outlook for selected Philippine tourist areas
    :type issued_datetime: str
    """
    # Create a dictionary to store the ingested valid period
    data = {
        "valid_period": valid_period
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/weather_outlook_for_ph_tourist_areas/valid_period.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_ph_tourist_area_tags(
        soup: BeautifulSoup | None
) -> list[BeautifulSoup]:
    """
    Ingest HTML tags of selected Philippine tourist areas to get
    their weather outlook from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: List of HTML tags for the selected Philippine tourist areas
    :rtype: list[BeautifulSoup]
    """
    list_of_all_ph_tourist_area_tags = []

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return list_of_all_ph_tourist_area_tags

    # Ingest HTML tags for all selected PH tourist areas to get their weather outlook
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    weather_outlook_for_ph_tourist_area_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    table_tag = weather_outlook_for_ph_tourist_area_tag.find('table', attrs={'class': 'table desktop'})

    # We need to check if the table_tag is missing
    if table_tag is None:
        return list_of_all_ph_tourist_area_tags

    tbody_tag = table_tag.find('tbody')
    # Use find_all() method to access all selected PH tourist area HTML tags
    list_of_all_ph_tourist_area_tags = tbody_tag.find_all('tr')

    return list_of_all_ph_tourist_area_tags

def ingest_ph_tourist_area_names(
        list_of_all_ph_tourist_area_tags: list[BeautifulSoup]
) -> dict[str, dict]:
    """
    Ingest the names of selected Philippine tourist areas from their
    HTML tags to get their weather outlook.

    :param list_of_all_ph_tourist_area_tags: List of HTML tags for
        the selected Philippine tourist areas
    :type list_of_all_ph_tourist_area_tags: list[BeautifulSoup]

    :return: Dictionary mapping tourist area names to empty dictionaries
        for storing weather data
    :rtype: dict[str, dict]
    """
    result = {}

    # We need to check if the selected PH tourist area HTML tags list is missing
    if list_of_all_ph_tourist_area_tags is None:
        return result

    # Iterate the PH tourist area HTML tags to ingest the names of the selected PH tourist area
    for ph_tourist_area_tag in list_of_all_ph_tourist_area_tags:
        ph_tourist_area_name_tag = ph_tourist_area_tag.find('td')
        ph_tourist_area_name = str(ph_tourist_area_name_tag.text).strip()
        # Use replace() to remove extra whitespace after '(' in PH tourist area names
        ph_tourist_area_name = ph_tourist_area_name.replace('( ', '(')
        result[ph_tourist_area_name] = {}

    return result

def ingest_weather_dates(
        soup: BeautifulSoup | None
) -> list[str]:
    """
    Ingest all weather dates from the HTML tags of selected
    Philippine tourist areas for their weather outlook.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: List of weather dates for the selected Philippine tourist areas
    :rtype: list[str]
    """
    weather_dates = []

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return weather_dates

    # Ingest HTML tags to get all weather dates of selected PH tourist areas
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    weather_outlook_for_ph_tourist_area_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    table_tag = weather_outlook_for_ph_tourist_area_tag.find('table', attrs={'class': 'table desktop'})

    # We need to check if the table_tag is missing
    if table_tag is None:
        return weather_dates

    thead_tag = table_tag.find('thead')
    # Use find_all() method to access all weather dates
    list_of_all_table_header_tags = thead_tag.find_all('th')[1:]

    # Iterate rows containing HTMl tags to ingest the weather dates of selected PH tourist areas
    for table_header_tag in list_of_all_table_header_tags:
        weather_date = str(table_header_tag.text).strip()
        # Use split() method to remove extra whitespaces in between words
        weather_date = ' '.join(weather_date.split())
        weather_dates.append(weather_date)

    return weather_dates

def map_weather_dates_to_ph_tourist_areas(
        weather_dates: list[str],
        ph_tourist_area_names: dict[str, dict]
) -> dict[str, dict]:
    """
    Maps a list of extracted weather dates to the dictionary
    of selected Philippine tourist area names for their weather outlook.
    
    :param weather_dates: List of weather dates for the selected Philippine
        tourist areas
    :type weather_dates: list[str]

    :param ph_tourist_area_names: Dictionary mapping tourist area names to
        empty dictionaries for storing weather data
    :type ph_tourist_area_names: dict[str, dict]

    :return: Dictionary of tourist area names with their corresponding weather dates
    :rtype: dict[str, dict]
    """
    # We need to check if the weather dates list or PH tourist area names dict is misisng
    if weather_dates == [] or ph_tourist_area_names == {}:
        return {}

    result = ph_tourist_area_names

    list_of_all_ph_tourist_area_names = list(result.keys())

    # Iterate the selected PH tourist areas list to map it to the weather dates list
    for ph_tourist_area_name in list_of_all_ph_tourist_area_names:
        # Map weather dates list to the selected PH tourist area
        result[ph_tourist_area_name]['weather_dates'] = weather_dates

    return result

def ingest_temperature_ranges(
        list_of_all_ph_tourist_area_tags: list[BeautifulSoup]
) -> list[list]:
    """
    Ingest all temperature ranges from the HTML tags of
    selected Philippine tourist areas for their weather outlook.

    :param list_of_all_ph_tourist_area_tags: List of HTML tags
        for the selected Philippine tourist areas
    :type list_of_all_ph_tourist_area_tags: list[BeautifulSoup]

    :return: List of temperature ranges for the selected Philippine tourist areas
    :rtype: list[list]
    """
    result = []

    # We need to check if the selected PH tourist area HTML tags list is missing
    if list_of_all_ph_tourist_area_tags == []:
        return result

    # Iterate the PH tourist area HTML tags to ingest temperature range tags
    for ph_tourist_area_tag in list_of_all_ph_tourist_area_tags:
        list_of_all_table_data_tags = ph_tourist_area_tag.find_all('td')[1:]

        temperature_ranges = []

        # Iterate tags to ingest temperature ranges list for selected PH tourist areas
        for table_data_tag in list_of_all_table_data_tags:
            minimum_temperature_tag = table_data_tag.find('span', attrs={'class': 'min'})
            minimum_temperature = str(minimum_temperature_tag.text).strip()

            maximum_temperature_tag = table_data_tag.find('span', attrs={'class': 'max'})
            maximum_temperature = str(maximum_temperature_tag.text).strip()

            temperature_ranges.append([minimum_temperature, maximum_temperature])

        result.append(temperature_ranges)
    
    return result

def map_temperature_ranges_to_ph_tourist_areas(
        temperature_ranges: list[list],
        ph_tourist_areas_with_weather_dates: dict[str, dict]
) -> dict[str, dict]:
    """
    Maps a list of extracted temperature ranges to the dictionary
    of selected Philippine tourist area names with their weather dates
    for the weather outlook.

    :param temperature_ranges: List of temperature ranges for the
        selected Philippine tourist areas
    :type temperature_ranges: list[list]

    :param ph_tourist_areas_with_weather_dates: Dictionary of tourist
        area names with their corresponding weather dates
    :type ph_tourist_areas_with_weather_dates: dict[str, dict]

    :return: Dictionary of tourist area names with weather dates
        and their corresponding temperature ranges
    :rtype: dict[str, dict]
    """
    # We need to check if the temperature ranges list or PH tourist areas with weather dates dict is missing
    if temperature_ranges == [] or ph_tourist_areas_with_weather_dates == {}:
        return {}

    result = ph_tourist_areas_with_weather_dates

    list_of_all_temperature_ranges = temperature_ranges
    list_of_all_ph_tourist_area_names = list(result.keys())

    # Iterate the temperature ranges list to map it to the selected PH tourist area
    for index, temperature_ranges in enumerate(list_of_all_temperature_ranges):
        # Use the index of temperature ranges list to get the name of the PH tourist area
        ph_tourist_area_name = list_of_all_ph_tourist_area_names[index]
        # Map temperature ranges list to the selected PH tourist area
        result[ph_tourist_area_name]['temperature_ranges'] = temperature_ranges

    return result

def save_ingested_ph_tourist_areas_weather_outlook(
        ph_tourist_areas_weather_outlook: dict[str, dict]
) -> None:
    """
    Save the ingested weather outlook for selected Philippine tourist areas
    to a JSON file in the `data/raw/weather_outlook_for_ph_tourist_areas`
    subdirectory on the local machine.

    :param ph_cities_weather_outlook: Dictionary of tourist area names with weather dates
        and their corresponding temperature ranges
    :type ph_cities_weather_outlook: dict[str, dict]
    """
    # Create a dictionary to store the ingested weather outlook of selected PH tourist areas
    data = ph_tourist_areas_weather_outlook

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/weather_outlook_for_ph_tourist_areas/ph_tourist_areas_weather_outlook.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()