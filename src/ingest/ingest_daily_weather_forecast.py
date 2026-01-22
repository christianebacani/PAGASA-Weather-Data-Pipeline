"""
Ingest dialy weather forecast data from the PAGASA-DOST website.

This module contains functions used by the ETL pipeline to ingest
data from the PAGASA-DOST daily weather forecast page and store the
ingested artifacts as JSON files under the `data/daily_weather_forecasts/`
subdirectory for further processing.

Ingested data:
- Issued datetime
- Synopsis
- Tropical cyclone informations
- Forecast weather conditions
- Forecast wind and coastal water conditions
- Temperature and relative humidity
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/daily_weather_forecasts/`
    for ingested data from the daily weather forecast page of PAGASA-DOST
    website.
    """
    if not os.path.exists('data/daily_weather_forecasts'):
        os.makedirs('data/daily_weather_forecasts')

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

def ingest_issued_datetime(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetime from the daily weather
    forecast page of the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetime from the daily weather forecast
        page of the PAGASA-DOST website
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

    return issued_datetime

def save_ingested_issued_datetime(
        issued_datetime: str
) -> None:
    """
    Save the ingested issued datetime from the
    daily weather forecast page of the PAGASA-
    DOST website.

    :param issued_datetime: Issued datetime from
        the daily weather forecast page of the
        PAGASA-DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issue_datetime": issued_datetime
    }

    with open(
        'data/daily_weather_forecasts/issued_datetime.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_synopsis(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the synopsis from the daily weather
    forecast page of the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Synopsis from the daily weather forecast
        page of the PAGASA-DOST website
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

    return synopsis

def save_ingesed_synopsis(
    synopsis: str
) -> None:
    """
    Save the ingested synopsis from the
    daily weather forecast page of the PAGASA-
    DOST website.

    :param synopsis: Synopsis from the daily weather
        forecast page of the PAGASA-DOST website
    :type synopsis: str
    """
    ingested_data = {
        "synopsis": synopsis
    }

    with open(
        'data/daily_weather_forecasts/synopsis.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_tropical_cyclone_informations(
        soup: BeautifulSoup | None
) -> dict[str, str]:
    """
    Ingest tropical cyclone informations from the
    daily weather forecast page of the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone informations from the
        daily weather forecast page of the PAGASA-DOST
        website
    :rtype: dict[str, str]
    """

def save_ingested_tropical_cyclone_informations(
        tropical_cyclone_informations: dict[str, str]
) -> None:
    """
    Save ingested tropical cyclone informations from the daily
    weather forecast page of the PAGASA-DOST website.

    :param tropical_cyclone_informations: Tropical cyclone
        informations from the daily weather forecast page of
        the PAGASA-DOST website 
    :type tropical_cyclone_informations: dict[str, str]
    """

def ingest_forecast_weather_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest forecast weather conditions from the
    daily weather forecast page of the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Forecast weather conditions from the daily
        weather forecast page of the PAGASA-DOST website
    :rtype: dict[str, list]
    """
    forecast_weather_conditions = {
        'place': [],
        'weather_condition': [],
        'caused_by': [],
        'impact': []
    }

    if soup is None:
        return forecast_weather_conditions

    list_of_all_daily_weather_forecasts_tags = soup.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Use if statement to check if there's 4 or 5 instances of a certain div tag.
    # If 5 instances are present, it means the tropical cyclone information tag is present
    if len(list_of_all_daily_weather_forecasts_tags) == 4:
        forecast_weather_conditions_tag = list_of_all_daily_weather_forecasts_tags[1]

    else:
        forecast_weather_conditions_tag = list_of_all_daily_weather_forecasts_tags[2]

    tbody_tag = forecast_weather_conditions_tag.find(
        'tbody'
    )
    list_of_all_table_row_tags = tbody_tag.find_all(
        'tr'
    )

    for table_row_tag in list_of_all_table_row_tags:
        list_of_all_table_data_tags = table_row_tag.find_all(
            'td'
        )

        place = list_of_all_table_data_tags[0]
        place = place.text
        place = str(place)
        forecast_weather_conditions['place'].append(
            place
        )

        weather_condition = list_of_all_table_data_tags[1]
        weather_condition = weather_condition.text
        weather_condition = str(weather_condition)
        forecast_weather_conditions['weather_condition'].append(
            weather_condition
        )

        caused_by = list_of_all_table_data_tags[2]
        caused_by = caused_by.text
        caused_by = str(caused_by)
        forecast_weather_conditions['caused_by'].append(
            caused_by
        )

        impact = list_of_all_table_data_tags[3]
        impact = impact.text
        impact = str(impact)
        forecast_weather_conditions['impact'].append(
            impact
        )

    return forecast_weather_conditions

def save_ingested_forecast_weather_conditions(
        forecast_weather_conditions: dict[str, list]
) -> None:
    """
    Save ingested forecast weather conditions from the daily
    weather forecast page of the PAGASA-DOST website.

    :param forecast_weather_conditions: Forecast weather
        conditions from the daily weather forecast page of
        the PAGASA-DOST website
    :type forecast_weather_conditions: dict[str, list]
    """
    ingested_data = forecast_weather_conditions

    with open(
        'data/daily_weather_forecasts/forecast_weather_conditions.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_forecast_wind_and_coastal_water_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest forecast wind and coastal water conditions from
    the daily weather forecast page of the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing the parsed
        HTML of the page, or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Forecast wind and coastal water conditions from the daily
        weather forecast page of the PAGASA-DOST website
    :rtype: dict[str, list]
    """
    forecast_wind_and_coastal_water_conditions = {
        'place': [],
        'speed': [],
        'direction': [],
        'coastal_water': []
    }

    if soup is None:
        return forecast_wind_and_coastal_water_conditions

    list_of_all_daily_weather_forecasts_tags = soup.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Use if statement to check if there's 4 or 5 instances of a certain div tag.
    # If 5 instances are present, it means the tropical cyclone information tag is present
    if len(list_of_all_daily_weather_forecasts_tags) == 4:
        forecast_wind_and_coastal_water_conditions_tag = list_of_all_daily_weather_forecasts_tags[2]

    else:
        forecast_wind_and_coastal_water_conditions_tag = list_of_all_daily_weather_forecasts_tags[3]
    
    tbody_tag = forecast_wind_and_coastal_water_conditions_tag.find(
        'tbody'
    )
    list_of_all_table_row_tags = tbody_tag.find_all('tr')

    for table_row_tag in list_of_all_table_row_tags:
        list_of_all_table_data_tags = table_row_tag.find_all(
            'td'
        )

        place = list_of_all_table_data_tags[0]
        place = place.text
        place = str(place)
        forecast_wind_and_coastal_water_conditions['place'].append(
            place
        )

        speed = list_of_all_table_data_tags[1]
        speed = speed.text
        speed = str(speed)
        forecast_wind_and_coastal_water_conditions['speed'].append(
            speed
        )

        direction = list_of_all_table_data_tags[2]
        direction = direction.text
        direction = str(direction)
        forecast_wind_and_coastal_water_conditions['direction'].append(
            direction
        )

        coastal_water = list_of_all_table_data_tags[3]
        coastal_water = coastal_water.text
        coastal_water = str(coastal_water)
        forecast_wind_and_coastal_water_conditions['coastal_water'].append(
            coastal_water
        )

    return forecast_wind_and_coastal_water_conditions

def save_ingested_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions: dict[str, list]
) -> None:
    """
    Save ingested forecast wind and coastal water conditions from the daily
    weather forecast page of the PAGASA-DOST website.

    :param forecast_wind_and_coastal_water_conditions: Forecast wind and
        coastal water conditions from the daily weather forecast page of the
        PAGASA-DOST website
    :type forecast_wind_and_coastal_water_conditions: dict[str, list]
    """
    ingested_data = forecast_wind_and_coastal_water_conditions

    with open(
        'data/daily_weather_forecasts/forecast_wind_and_coastal_water_conditions.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_temperature_and_relative_humidity(
        soup: BeautifulSoup | None
) -> dict[str, dict]:
    """
    Ingest the temperature and relative humidity from
    the daily weather forecast page of the PAGASA-DOST
    website..

    :param soup: A BeautifulSoup object representing the parsed
        HTML of the page, or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Temperature and relative humidity from the daily
        weather forecast page of the PAGASA-DOST website
    :rtype: dict[str, dict]
    """
    temperature_and_relative_humidity = {
        'temperature': {
            'max': [],
            'min': []
        },
        'relative_humidity': {
            'max': [],
            'min': []
        }
    }

    if soup is None:
        return temperature_and_relative_humidity

    list_of_all_daily_weather_forecasts_tags = soup.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Use if statement to check if there's 4 or 5 instances of a certain div tag.
    # If 5 instances are present, it means the tropical cyclone information tag is present
    if len(list_of_all_daily_weather_forecasts_tags) == 4:
        temperature_and_relative_humidity_tag = list_of_all_daily_weather_forecasts_tags[3]
    
    else:
        temperature_and_relative_humidity_tag = list_of_all_daily_weather_forecasts_tags[4]

    tbody_tag = temperature_and_relative_humidity_tag.find(
        'tbody'
    )
    list_of_all_table_row_tags = tbody_tag.find_all(
        'tr'
    )

    # The first instance of the list_of_all_table_row_tags is the temperature row
    temperatures_tag = list_of_all_table_row_tags[0]
    list_of_all_table_data_tags = temperatures_tag.find_all(
        'td'
    )
    list_of_all_table_data_tags = list_of_all_table_data_tags[1:]

    # Iterate the first half of the list_of_all_table_data_tags from temperature row
    # The first half of the list_of_all_table_data_tags contains max and time of max temperature
    for table_data_tag in list_of_all_table_data_tags[:2]:
        data = table_data_tag.text
        data = str(data)
        temperature_and_relative_humidity['temperature']['max'].append(
            data
        )

    # Iterate the last half of the list_of_all_table_data_tags from temperature row
    # The last half of the list_of_all_table_data_tags contains min and time of min temperature
    for table_data_tag in list_of_all_table_data_tags[2:]:
        data = table_data_tag.text
        data = str(data)
        temperature_and_relative_humidity['temperature']['min'].append(
            data
        )

    # The last instance of the list_of_all_table_row_tags is the relative humidity row
    relative_humidities_tag = list_of_all_table_row_tags[1]
    list_of_all_table_data_tags = relative_humidities_tag.find_all(
        'td'
    )    
    list_of_all_table_data_tags = list_of_all_table_data_tags[1:]

    # Iterate the first half of list_of_all_table_data_tags from relative humidity row
    # The first half of the list_of_all_table_data_tags contains max and time of max relative humidity
    for table_data_tag in list_of_all_table_data_tags[:2]:
        data = table_data_tag.text
        data = str(data)
        temperature_and_relative_humidity['relative_humidity']['max'].append(
            data
        )

    # Iterate the last half of the list_of_all_table_data_tags from relative humidity row
    # The last half of the list_of_all_table_data_tags contains min and time of min relative humidity
    for table_data_tag in list_of_all_table_data_tags[2:]:
        data = table_data_tag.text
        data = str(data)
        temperature_and_relative_humidity['relative_humidity']['min'].append(
            data
        )
    
    return temperature_and_relative_humidity

def save_ingested_temperature_and_relative_humidity(
        temperature_and_relative_humidity: dict[str, dict]
) -> None:
    """
    Save the ingested temperature and relative humidity from the
    daily weather forecast page of the PAGASA-DOST website.

    :param temperature_and_relative_humidity: Temperature and
        relative humidity from the daily weather forecast page of
        the PAGASA-DOST website
    :type temperature_and_relative_humidity: dict[str, dict]
    """
    ingested_data = temperature_and_relative_humidity

    with open(
        'data/daily_weather_forecasts/temperature_and_relative_humidity.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)