"""
Ingest daily weather forecasts from the PAGASA-DOST website.

This module provides functions to ingest key informations from the
daily weather forecast page, including:

- Issued datetimes
- Synopses
- Tropical cyclone informations
- Forecast weather conditions
- Forecast wind and coastal water conditions
- Temperatures and relative humidities

All extracted data is saved as JSON files in the
`data/raw/daily_weather_forecasts/` subdirectory on the local machine.
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Create the `data/raw/daily_weather_forecasts/` subdirectory to store JSON files.

    This subdirectory holds the daily weather forecast data, ingested from the
    PAGASA-DOST website.
    """
    # Create the data/raw/daily_weather_forecasts/ subdirectory if it doesn't exist
    if not os.path.exists('data/raw/daily_weather_forecasts'):
        os.makedirs('data/raw/daily_weather_forecasts')

def ingest_beautiful_soup_object(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest the BeautifulSoup object from the daily weather forecast page.

    :param url: URL of the PAGASA-DOST daily weather forecast page
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

def ingest_issued_datetimes(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetimes of the daily weather forecast from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the daily weather forecast
    :rtype: str
    """
    issued_datetime = ''

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return issued_datetime

    # Extract HTML tags for issued datetimes of the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    issued_datetime_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    bold_tag = issued_datetime_tag.find('b')

    # We need to check if the bold_tag is not missing
    if bold_tag is not None:
        issued_datetime = str(bold_tag.text).strip()

    return issued_datetime

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save the ingested issued datetimes of the daily weather forecast to a
    JSON file in the `data/raw/daily_weather_forecasts/` subdirectory on
    the local machine.

    :param issued_datetime: Issued datetimes of the daily weather forecast
    :type issued_datetime: str
    """
    # Create a dictionary to store the ingested issued datetimes
    data = {
        "issued_datetime": issued_datetime
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_synopses(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the synopses of the daily weather forecast from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Synopses of the daily weather forecast
    :rtype: str
    """
    synopsis = ''

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return synopsis

    # Extract HTML tags for synopses of the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    synopsis_tag = div_tag_with_row_weather_page_class.find('div', attrs={'class': 'col-md-12 col-lg-12'})
    div_tag_with_panel_body_class = synopsis_tag.find('div', attrs={'class': 'panel-body'})

    # We need to check if the div_tag_with_panel_body_class is not missing
    if div_tag_with_panel_body_class is not None: 
        synopsis = str(div_tag_with_panel_body_class.text).strip()

    return synopsis

def save_ingested_synopses(
        synopsis: str
) -> None:
    """
    Save the ingested synopses of the daily weather forecast to a JSON
    file in the `data/raw/daily_weather_forecasts/` subdirectory
    on the local machine.

    :param synopsis: Synopses of the daily weather forecast
    :type synopsis: str
    """
    # Create a dictionary to store the ingested synopses
    data = {
        "synopsis": synopsis
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/synopses.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_tropical_cyclone_informations(
    soup: BeautifulSoup | None
) -> dict[str, str]:
    """
    Ingest the tropical cyclone informations of the daily weather forecast from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Dictionary containing tropical cyclone informations
    :rtype: dict[str, str]
    """
    tropical_cyclone_informations = {
        'current_update': '',
        'tropical_cyclone_name': '',
        'location': '',
        'maximum_sustained_wind': '',
        'gustiness': '',
        'movement': ''
    }

    # We need to check if the BeautifulSoup object is missing    
    if soup is None:
        return tropical_cyclone_informations

    # Extract HTML tags for tropical cyclone informations from the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    list_of_all_daily_weather_forecast_tags = div_tag_with_row_weather_page_class.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Verify TC info section exists: exactly 5 divs with class 'col-md-12 col-lg-12'
    if len(list_of_all_daily_weather_forecast_tags) == 5:
        tropical_cyclone_informations_tag = list_of_all_daily_weather_forecast_tags[1]

    else:
        return tropical_cyclone_informations

    tbody_tag = tropical_cyclone_informations_tag.find('tbody')
    list_of_all_table_data_row_tags = tbody_tag.find_all('tr')

    # Iterate rows containing data of tropical cyclone informations
    for row_number, table_row_tag in enumerate(list_of_all_table_data_row_tags):
        cell = str(table_row_tag.text)

        list_of_text_to_remove = [
            'LOCATION:',
            'GUSTINESS:',
            'MAXIMUM SUSTAINED WINDS:',
            'GUSTINESS:',
            'MOVEMENT:'
        ]

        # Iterate the list and remove each string from the tropical cyclone info text
        for text_to_remove in list_of_text_to_remove:
            cell = cell.replace(text_to_remove, '').strip()

        # Use the current row index to access the correct key in the tropical cyclone_informations dictionary
        tropical_cyclone_information_keys = list(tropical_cyclone_informations.keys())
        key = tropical_cyclone_information_keys[row_number]
        value = cell
        tropical_cyclone_informations[key] = value

    return tropical_cyclone_informations

def save_ingested_tropical_cyclone_informations(
        tropical_cyclone_informations: dict[str, str]
) -> None:
    """
    Save the ingested tropical cyclone informations of 
    the daily weather forecast to a JSON file in the
    `data/raw/daily_weather_forecasts/` subdirectory on
    the local machine.

    :param tropical_cyclone_informations: Dictionary containing
        tropical cyclone information
    :type tropical_cyclone_informations: dict[str, str]
    """
    # Create a dictionary to store the ingested tropical cyclone informations
    data = {
        "current_update": tropical_cyclone_informations['current_update'],
        "tropical_cyclone_name": tropical_cyclone_informations['tropical_cyclone_name'],
        "location": tropical_cyclone_informations['location'],
        "maximum_sustained_wind": tropical_cyclone_informations['maximum_sustained_wind'],
        "gustiness": tropical_cyclone_informations['gustiness'],
        "movement": tropical_cyclone_informations['movement']
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/tropical_cyclone_informations.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_forecast_weather_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest the forecast weather conditions of the daily weather forecast from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Dictionary containing forecast weather conditions
    :rtype: dict[str, list]
    """
    forecast_weather_conditions = {
        'place': [],
        'weather_condition': [],
        'caused_by': [],
        'impact': []
    }

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return forecast_weather_conditions

    # Extract HTML tags for forecast weather conditions from the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    list_of_all_daily_weather_forecast_tags = div_tag_with_row_weather_page_class.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Verify TC info section exists: exactly 5 divs with class 'col-md-12 col-lg-12'
    if len(list_of_all_daily_weather_forecast_tags) == 5:
        forecast_weather_conditions_tag = list_of_all_daily_weather_forecast_tags[2]
    
    else:
        forecast_weather_conditions_tag = list_of_all_daily_weather_forecast_tags[1]

    tbody_tag = forecast_weather_conditions_tag.find('tbody')

    # We need to check if the tbody_tag is missing
    if tbody_tag is None:
        return forecast_weather_conditions

    list_of_all_table_row_tags = tbody_tag.find_all('tr')

    # Iterate rows containing HTML tags for forecast weather conditions
    for table_row_tag in list_of_all_table_row_tags:
        # Use find_all() to retrieve all forecast weather conditions data
        list_of_all_table_data_tags = table_row_tag.find_all('td')

        place = str(list_of_all_table_data_tags[0].text).strip()
        forecast_weather_conditions['place'].append(place)

        weather_condition = str(list_of_all_table_data_tags[1].text).strip()
        forecast_weather_conditions['weather_condition'].append(weather_condition)

        caused_by = str(list_of_all_table_data_tags[2].text).strip()
        forecast_weather_conditions['caused_by'].append(caused_by)

        impact = str(list_of_all_table_data_tags[3].text).strip()
        forecast_weather_conditions['impact'].append(impact)

    return forecast_weather_conditions

def save_ingested_forecast_weather_conditions(
        forecast_weather_conditions: dict[str, list]
) -> None:
    """
    Save the ingested forecast weather conditions of the 
    daily weather forecast to a JSON file in the
    `data/raw/daily_weather_forecasts/` subdirectory on the local machine.

    :param forecast_weather_conditions: Dictionary containing forecast weather conditions
    :type forecast_weather_conditions: dict[str, list]
    """
    # Create a dictionary to store the ingested forecast weather conditions
    data = {
        "place": forecast_weather_conditions['place'],
        "weather_condition": forecast_weather_conditions['weather_condition'],
        "caused_by": forecast_weather_conditions['caused_by'],
        "impact": forecast_weather_conditions['impact']
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/forecast_weather_conditions.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_forecast_wind_and_coastal_water_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest the forecast wind and coastal water conditions of the daily weather forecast
    from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Dictionary containing forecast wind and coastal water conditions
    :rtype: dict[str, list]
    """
    forecast_wind_and_coastal_water_conditions = {
        'place': [],
        'speed': [],
        'direction': [],
        'coastal_water': []
    }

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return forecast_wind_and_coastal_water_conditions

    # Extract HTML tags for forecast wind and coastal water conditions from the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    list_of_all_daily_weather_forecast_tags = div_tag_with_row_weather_page_class.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Verify TC info section exists: exactly 5 divs with class 'col-md-12 col-lg-12'
    if len(list_of_all_daily_weather_forecast_tags) == 5:
        forecast_wind_and_coastal_water_conditions_tag = list_of_all_daily_weather_forecast_tags[3]
    
    else:
        forecast_wind_and_coastal_water_conditions_tag = list_of_all_daily_weather_forecast_tags[2]

    tbody_tag = forecast_wind_and_coastal_water_conditions_tag.find('tbody')

    # We need to check if the tbody_tag is missing
    if tbody_tag is None:
        return forecast_wind_and_coastal_water_conditions

    list_of_all_table_row_tags = tbody_tag.find_all('tr')

    # Iterate rows containing HTML tags for forecast wind and coastal water conditions
    for table_row_tag in list_of_all_table_row_tags:
        # Use find_all() to retrieve all forecast wind and coastal water conditions data
        list_of_all_table_data_tags = table_row_tag.find_all('td')

        place = str(list_of_all_table_data_tags[0].text).strip()
        forecast_wind_and_coastal_water_conditions['place'].append(place)

        speed = str(list_of_all_table_data_tags[1].text).strip()
        forecast_wind_and_coastal_water_conditions['speed'].append(speed)

        direction = str(list_of_all_table_data_tags[2].text).strip()
        forecast_wind_and_coastal_water_conditions['direction'].append(direction)

        coastal_water = str(list_of_all_table_data_tags[3].text).strip()
        forecast_wind_and_coastal_water_conditions['coastal_water'].append(coastal_water)

    return forecast_wind_and_coastal_water_conditions

def save_ingested_forecast_wind_and_coastal_water_conditions(
    forecast_wind_and_coastal_water_conditions: dict[str, list]
) -> None:
    """
    Save the ingested forecast wind and coastal water conditions
    to a JSON file in the `data/raw/daily_weather_forecasts/`
    subdirectory on the local machine.

    :param forecast_wind_and_coastal_water_conditions: Dictionary containing
        forecast wind and coastal water conditions
    :type forecast_wind_and_coastal_water_conditions: dict[str, list]
    """
    # Create a dictionary to store the ingested forecast wind and coastal water conditions
    data = {
        "place": forecast_wind_and_coastal_water_conditions['place'],
        "speed": forecast_wind_and_coastal_water_conditions['speed'],
        "direction": forecast_wind_and_coastal_water_conditions['direction'],
        "coastal_water": forecast_wind_and_coastal_water_conditions['coastal_water']
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/forecast_wind_and_coastal_water_conditions.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()

def ingest_temperatures_and_relative_humidities(
        soup: BeautifulSoup | None
) -> dict[str, str]:
    """
    Ingest the temperatures and relative humidities of the daily weather forecast
    from the PAGASA-DOST website.

    :param soup: BeautifulSoup object for navigating the page, or None if extraction fails
    :type soup: BeautifulSoup | None

    :return: Dictionary containing temperatures and relative humidities
    :rtype: dict[str, str]
    """
    temperatures_and_relative_humidities = {
        'temperature': {
            'max': [],
            'min': []
        },
        'relative_humidity_percentage': {
            'max': [],
            'min': []
        }
    }

    # We need to check if the BeautifulSoup object is missing
    if soup is None:
        return temperatures_and_relative_humidities

    # Extract HTML tags for temperatures and relative humidities from the daily weather forecast
    div_tag_with_row_weather_page_class = soup.find('div', attrs={'class': 'row weather-page'})
    list_of_all_daily_weather_forecast_tags = div_tag_with_row_weather_page_class.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Verify TC info section exists: exactly 5 divs with class 'col-md-12 col-lg-12'
    if len(list_of_all_daily_weather_forecast_tags) == 5:
        temperatures_and_relative_humidities_tag = list_of_all_daily_weather_forecast_tags[4]

    else:
        temperatures_and_relative_humidities_tag = list_of_all_daily_weather_forecast_tags[3]

    tbody_tag = temperatures_and_relative_humidities_tag.find('tbody')

    # We need to check if the tbody_tag is missing
    if tbody_tag is None:
        return temperatures_and_relative_humidities

    list_of_all_table_row_tags = tbody_tag.find_all('tr')

    # Iterate rows containing HTML tags for temperatures and relative humidities
    for row_number, table_row_tag in enumerate(list_of_all_table_row_tags):
        row_number += 1
        # Use find_all() to retrieve all temperatures and relative humidities data
        list_of_all_table_data_tags = table_row_tag.find_all('td')[1:]

        first_instance_of_table_data_tag = str(list_of_all_table_data_tags[0].text).strip()
        second_instance_of_table_data_tag = str(list_of_all_table_data_tags[1].text).strip()
        third_instance_of_table_data_tag = str(list_of_all_table_data_tags[2].text).strip()
        fourth_instance_of_table_data_tag = str(list_of_all_table_data_tags[3].text).strip()
        
        # Check if row_number is 1 (temperature) or 2 (relative humidity) instead of fetching manually
        if row_number == 1:
            temperatures_and_relative_humidities['temperature']['max'].append(
                first_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['temperature']['max'].append(
                second_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['temperature']['min'].append(
                third_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['temperature']['min'].append(
                fourth_instance_of_table_data_tag
            )

        else:
            temperatures_and_relative_humidities['relative_humidity_percentage']['max'].append(
                first_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['relative_humidity_percentage']['max'].append(
                second_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['relative_humidity_percentage']['min'].append(
                third_instance_of_table_data_tag
            )
            temperatures_and_relative_humidities['relative_humidity_percentage']['min'].append(
                fourth_instance_of_table_data_tag
            )

    return temperatures_and_relative_humidities

def save_ingested_temperatures_and_relative_humidities(
        temperatures_and_relative_humidities: dict[str, dict]
) -> None:
    """
    Save the ingested temperatures and relative humidities of the daily
    weather forecast to a JSON file in the `data/raw/daily_weather_forecasts/`
    subdirectory on the local machine.

    :param temperatures_and_relative_humidities: Dictionary containing temperatures
        and relative humidities data
    :type temperatures_and_relative_humidities: dict[str, dict]
    """
    # Create a dictionary to store the ingested temperatures and relative humidities
    data = {
        "temperature": {
            "max": temperatures_and_relative_humidities['temperature']['max'],
            "min": temperatures_and_relative_humidities['temperature']['min']
        },
        "relative_humidity_percentage": {
            'max': temperatures_and_relative_humidities['relative_humidity_percentage']['max'],
            'min': temperatures_and_relative_humidities['relative_humidity_percentage']['min']
        }
    }

    # Save the dictionary to a json file using open() method and json module
    with open(
        'data/raw/daily_weather_forecasts/temperatures_and_relative_humidities.json',
        'w'
    ) as json_file:
        json.dump(data, json_file, indent=4)

    json_file.close()