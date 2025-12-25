"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/daily_weather_forecasts/`
    for ingested data from the daily weather forecast page of PAGASA-DOST
    website.
    """
    if not os.path.exists('data/raw/daily_weather_forecasts'):
        os.makedirs('data/raw/daily_weather_forecasts')

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

def ingest_issued_datetimes(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetimes of the daily weather
    forecast page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the daily weather forecast
        page from the PAGASA-DOST website
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

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save ingested issued datetimes of the daily
    weather forecast page from the PAGASA-DOST
    website.

    :param issued_datetime: Issued datetimes of
        the daily weather forecast page from the
        PAGASA-DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issue_datetime": issued_datetime
    }

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_synopses(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the synopses of the daily weather
    forecast page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Synopses of the daily weather forecast
        page from the PAGASA-DOST website
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

def save_ingested_synopses(
        synopsis: str
) -> None:
    """
    Save ingested synopses of the daily
    weather forecast page from the PAGASA-DOST
    website.

    :param synopsis: Synopses of the daily weather
        forecast page from the PAGASA-DOST website
    :type synopsis: str
    """
    ingested_data = {
        "synopsis": synopsis
    }

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/synopses.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_tropical_cyclone_informations(
        soup: BeautifulSoup | None
) -> dict[str, str]:
    """
    Ingest the tropical cyclone informations
    of the daily weather forecast page from
    the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType
        if the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Tropical cyclone informations of the daily
        weather forecast page from the PAGASA-DOST website
    :rtype: dict[str, str]
    """

def save_ingested_tropical_cyclone_informations(
        tropical_cyclone_informations: dict[str, str]
) -> None:
    """
    Save ingested tropical cyclone informations of the daily
    weather forecast page from the PAGASA-DOST website.

    :param tropical_cyclone_informations: Tropical cyclone
        informations of the daily weather forecast page from
        the PAGASA-DOST website 
    :type tropical_cyclone_informations: dict[str, str]
    """

def ingest_forecast_weather_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest the forecast weather conditions
    of the daily weather forecast page from
    the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Forecast weather conditions of the daily weather
        forecast page from the PAGASA-DOST website
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
    Save ingested forecast weather conditions of the daily
    weather forecast page from the PAGASA-DOST website.

    :param forecast_weather_conditions: Forecast weather
        conditions of the daily weather forecast page from
        the PAGASA-DOST website
    :type forecast_weather_conditions: dict[str, list]
    """
    ingested_data = forecast_weather_conditions

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/forecast_weather_conditions.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_forecast_wind_and_coastal_water_conditions(
        soup: BeautifulSoup | None
) -> dict[str, list]:
    """
    Ingest the forecast wind and coastal water conditions
    of the daily weather forecast page from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing the parsed
        HTML of the page, or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Forecast wind and coastal water conditions of the daily
        weather forecast page from the PAGASA-DOST website
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
    Save ingested forecast wind and coastal water conditions of the daily
    weather forecast page from the PAGASA-DOST website.

    :param forecast_wind_and_coastal_water_conditions: Forecast wind and
        coastal water conditions of the daily weather forecast page from the
        PAGASA-DOST website
    :type forecast_wind_and_coastal_water_conditions: dict[str, list]
    """
    ingested_data = forecast_wind_and_coastal_water_conditions

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/forecast_wind_and_coastal_water_conditions.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_temperatures_and_relative_humidities(
        soup: BeautifulSoup | None
) -> dict[str, dict]:
    """
    Ingest the temperatures and relative humidities
    of the daily weather forecast page from the PAGASA-DOST
    website.
    
    :param soup: A BeautifulSoup object representing the parsed
        HTML of the page, or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Temperatures and relative humidities of the daily
        weather forecast page from the PAGASA-DOST website
    :rtype: dict[str, dict]
    """
    temperatures_and_relative_humidities = {
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
        return temperatures_and_relative_humidities

    list_of_all_daily_weather_forecasts_tags = soup.find_all(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )

    # Use if statement to check if there's 4 or 5 instances of a certain div tag.
    # If 5 instances are present, it means the tropical cyclone information tag is present
    if len(list_of_all_daily_weather_forecasts_tags) == 4:
        temperatures_and_relative_humidities_tag = list_of_all_daily_weather_forecasts_tags[3]
    
    else:
        temperatures_and_relative_humidities_tag = list_of_all_daily_weather_forecasts_tags[4]

    tbody_tag = temperatures_and_relative_humidities_tag.find(
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
        temperatures_and_relative_humidities['temperature']['max'].append(
            data
        )

    # Iterate the last half of the list_of_all_table_data_tags from temperature row
    # The last half of the list_of_all_table_data_tags contains min and time of min temperature
    for table_data_tag in list_of_all_table_data_tags[2:]:
        data = table_data_tag.text
        data = str(data)
        temperatures_and_relative_humidities['temperature']['min'].append(
            data
        )

    # The last instance of the list_of_all_table_row_tags is the relative humidity row
    relative_humidities_tag = list_of_all_table_row_tags[1]
    list_of_all_table_data_tags = relative_humidities_tag.find_all(
        'td'
    )    
    list_of_all_table_data_tags = list_of_all_table_data_tags[1:]

    for table_data_tag in list_of_all_table_data_tags[:2]:
        data = table_data_tag.text
        data = str(data)
        
def save_ingested_temperatures_and_relative_humidities(
        temperatures_and_relative_humidities: dict[str, dict]
) -> None:
    """
    Save ingested temperatures and relative humidities of the daily
    weather forecast page from the PAGASA-DOST website.

    :param temperatures_and_relative_humidities: Temperatures and
        relative humidities of the daily weather forecast page from
        the PAGASA-DOST website
    :type temperatures_and_relative_humidities: dict[str, dict]
    """
    ingested_data = temperatures_and_relative_humidities

    # Using with open() method to save the ingested data to the target filepath
    with open(
        'data/raw/daily_weather_forecasts/temperatures_and_relative_humidities.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()