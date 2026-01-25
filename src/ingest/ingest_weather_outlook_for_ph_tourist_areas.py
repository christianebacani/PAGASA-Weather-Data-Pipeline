"""
Ingest weather outlook for selected Philippine tourist areas data from the PAGASA-DOST website.

This module contains functions used by the ETL pipeline to ingest
data from the PAGASA-DOST weather outlook for selected Philippine
tourist areas page and store the ingested artifacts as JSON files under the
`data/raw/weather_outlooks_for_ph_tourist_areas/` subdirectory for further
processing.

Ingested data:
- Issued datetime
- Time validity
- Philippine tourist area names
- Weather dates
- Temperature ranges
- Weather outlook for Philippine tourist areas
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/weather_outlooks_for_ph_tourist_areas/`
    for ingested data from the weather outlook for selected Philippine tourist areas
    page of PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/weather_outlooks_for_ph_tourist_areas'):
        os.makedirs('data/raw/weather_outlooks_for_ph_tourist_areas')

def ingest_and_parse_soup_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the weather outlook for
    selected Philippine tourist areas page
    of the PAGASA-DOST website.

    :param url: URL of the weather outlook for
        selected Philippine tourist areas page
        to ingest and parse
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

def ingest_issued_datetime(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetime from the weather
    outlook for selected Philippine tourist areas
    page of the PAGASA-DOST website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetime from the weather outlook
        for selected Philippine tourist areas page of
        the PAGASA-DOST website
    :rtype: str
    """
    issued_datetime = ''

    if soup is None:
        return issued_datetime

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    issued_datetimes_and_time_validities_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    bold_tag = issued_datetimes_and_time_validities_tag.find(
        'b'
    )
    issued_datetime = bold_tag.text
    issued_datetime = str(issued_datetime)

    return issued_datetime

def save_ingested_issued_datetime(
        issued_datetime: str
) -> None:
    """
    Save the ingested issued datetime from
    the weather outlook for selected Philippine
    tourist areas page of the PAGASA-DOST website.

    :param issued_datetime: Issued datetime from
        the weather outlook for selected Philippine
        tourist areas page of the PAGASA-DOST website
    :type issued_datetime: str
    """
    ingested_data = [
        {
            "issued_datetime": issued_datetime
        }
    ]

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/issued_datetime.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_time_validity(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validity from the weather
    outlook for selected Philippine tourist areas
    page of the PAGASA-DOST website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the page,
        or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Time validity from the weather outlook
        for selected Philippine tourist areas page
        of the PAGASA-DOST website
    :rtype: str
    """
    time_validity = ''

    if soup is None:
        return time_validity

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    issued_datetimes_and_time_validities_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12 issue'
        }
    )
    bold_tag = issued_datetimes_and_time_validities_tag.find_all(
        'b'
    )[1]
    time_validity = bold_tag.text
    time_validity = str(time_validity)

    return time_validity

def save_ingested_time_validity(
        time_validity: str
) -> None:
    """
    Save the ingested time validity from the
    weather outlook for selected Philippine
    tourist areas page of the PAGASA-DOST website.

    :param time_validity: Time validity from the
        weather outlook for selected Philippine
        tourist areas page of the PAGASA-DOST website
    :type time_validity: str
    """
    ingested_data = [
        {
            "time_validity": time_validity
        }
    ]

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/time_validity.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

def ingest_ph_tourist_area_names(
        soup: BeautifulSoup | None       
) -> dict[str, dict]:
    """
    Ingest selected Philippine tourist area names
    using the BeautifulSoup object representing the
    parsed HTML of the page consisting the selected
    Philippine tourist areas to get their weather
    outlooks from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if
        the page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Selected Philippine tourist area names
        dictionary
    :rtype: dict[str, dict]
    """
    result = {}

    if soup is None:
        return result

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    weather_outlooks_for_ph_tourist_areas_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    table_tag_with_table_desktop_class = weather_outlooks_for_ph_tourist_areas_tag.find(
        'table',
        attrs={
            'class': 'table desktop'
        }
    )
    tbody_tag = table_tag_with_table_desktop_class.find(
        'tbody'
    )
    list_of_all_table_row_tags = tbody_tag.find_all(
        'tr'
    )

    for table_row_tag in list_of_all_table_row_tags:
        table_data_tag = table_row_tag.find(
            'td'
        )
        ph_tourist_area_name = table_data_tag.text
        ph_tourist_area_name = str(ph_tourist_area_name)
        result[ph_tourist_area_name] = {}

    return result

def ingest_weather_dates(
        soup: BeautifulSoup | None
) -> list[str]:
    """
    Ingest weather dates using the BeautifulSoup
    object representing the parsed HTML of the page
    consisting the selected Philippine tourist areas
    to get their weather outlooks from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing the
        parsed HTML of the page, or NoneType if the page
        does not allow scraping
    :type soup: BeautifulSoup | None

    :return: List of all weather dates for selected
        Philippine tourist areas
    :rtype: list[str]
    """
    list_of_all_weather_dates = []

    if soup is None:
        return list_of_all_weather_dates

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    weather_outlooks_for_ph_tourist_areas_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    table_tag_with_table_desktop_class = weather_outlooks_for_ph_tourist_areas_tag.find(
        'table',
        attrs={
            'class': 'table desktop'
        }
    )
    thead_tag = table_tag_with_table_desktop_class.find(
        'thead'
    )
    list_of_all_table_header_tags = thead_tag.find_all(
        'th'
    )[1:]

    for table_header_tag in list_of_all_table_header_tags:
        weather_date = table_header_tag.text
        weather_date = str(weather_date)
        list_of_all_weather_dates.append(weather_date)

    return list_of_all_weather_dates

def map_ph_tourist_area_names_to_weather_dates(
        ph_tourist_area_names_dict: dict[str, dict],
        list_of_all_weather_dates: list[str]
) -> dict[str, dict]:
    """
    Map selected Philippine tourist area names to their
    corresponding weather dates to get their weather outlooks
    from the PAGASA-DOST website.

    :param ph_tourist_area_names_dict: Selected Philippine
        tourist area names dictionary
    :type ph_tourist_area_names_dict: dict[str, dict]

    :param list_of_all_weather_dates: List of all weather dates
        for selected Philippine tourist areas
    :type list_of_all_weather_dates: list[str]

    :return: Selected Philippine tourist area names with weather
        dates
    :rtype: dict[str, dict]
    """
    result = ph_tourist_area_names_dict

    if ph_tourist_area_names_dict == {} or list_of_all_weather_dates == []:
        return result

    list_of_all_ph_tourist_area_names = list(ph_tourist_area_names_dict.keys())

    # Map selected Philippine tourist area name to it's corresponding weather dates
    for ph_tourist_area_name in list_of_all_ph_tourist_area_names:
        result[ph_tourist_area_name]['weather_date'] = list_of_all_weather_dates

    return result

def ingest_temperature_ranges(
        soup: BeautifulSoup | None
) -> list[list]:
    """
    Ingest temperature ranges using the BeautifulSoup
    object representing the parsed HTML of the page
    consisting the selected Philippine tourist areas
    to get their weather outlooks from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object representing the
        parsed HTML of the page, or NoneType if the page
        does not allow scraping
    :type soup: BeautifulSoup | None

    :return List of all temperature ranges for selected
        Philippine tourist areas
    :rtype: list[list]
    """
    list_of_all_temperature_ranges = []

    if soup is None:
        return list_of_all_temperature_ranges

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    weather_outlooks_for_ph_tourist_areas_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    table_tag_with_table_desktop_class = weather_outlooks_for_ph_tourist_areas_tag.find(
        'table',
        attrs={
            'class': 'table desktop'
        }
    )
    tbody_tag = table_tag_with_table_desktop_class.find(
        'tbody'
    )
    list_of_all_table_row_tags = tbody_tag.find_all(
        'tr'
    )

    for table_row_tag in list_of_all_table_row_tags:
        list_of_all_table_data_tags = table_row_tag.find_all(
            'td'
        )[1:]

        temperature_ranges = []

        for table_data_tag in list_of_all_table_data_tags:
            minimum_temperature_tag = table_data_tag.find(
                'span',
                attrs={
                    'class': 'min'
                }
            )
            minimum_temperature = minimum_temperature_tag.text
            minimum_temperature = str(minimum_temperature)

            maximum_temperature = table_data_tag.find(
                'span',
                attrs={
                    'class': 'max'
                }
            )
            maximum_temperature = maximum_temperature.text
            maximum_temperature = str(maximum_temperature)

            temperature_ranges.append(
                [minimum_temperature, maximum_temperature]
            )

        list_of_all_temperature_ranges.append(
            temperature_ranges
        )

    return list_of_all_temperature_ranges

def map_ph_tourist_area_names_to_temperature_ranges(
    ph_tourist_area_names_with_weather_dates: dict[str, dict],
    list_of_all_temperature_ranges: list[list]
) -> dict[str, dict]:
    """
    Map selected Philippine tourist area names to their corresponding
    temperature ranges to get their weather outlooks
    from the PAGASA-DOST website.

    :param ph_tourist_area_names_with_weather_dates: Selected Philippine
        tourist area names with weather dates
    :type ph_tourist_area_names_with_weather_dates: dict[str, dict]
    
    :param list_of_all_temperature_ranges: List of all temperature ranges
        for selected Philippine tourist areas
    :type list_of_all_temperature_ranges: list[list]

    :return: Weather outlook for selected Philippine tourist areas
    :rtype: dict[str, dict]
    """
    result = ph_tourist_area_names_with_weather_dates

    list_of_all_ph_tourist_area_names = list(ph_tourist_area_names_with_weather_dates.keys())

    if ph_tourist_area_names_with_weather_dates == {} or list_of_all_temperature_ranges == []:
        return result

    # Map temperature ranges to cities in sequential order (1-to-1 mapping)
    # Map temperature ranges to tourist areas in sequential order (1-to-1 mapping)
    # The ingested temperature ranges maintain the same order as the tourist area names in the HTML structure
    for temperature_ranges in list_of_all_temperature_ranges:
        for ph_tourist_area_name in list_of_all_ph_tourist_area_names:
            # Map selected Philippine tourist area name to it's corresponding temperature ranges if its missing
            if 'temperature_range' in result[ph_tourist_area_name]:
                continue

            else:
                result[ph_tourist_area_name]['temperature_range'] = temperature_ranges
                break

    return result

def save_ingested_weather_outlook_for_ph_tourist_areas(
        weather_outlook_for_ph_tourist_areas: dict[str, dict]
) -> None:
    """
    Save the ingested weather outlook for selected Philippine
    tourist areas from the weather outlook for selected Philippine
    tourist areas page of the PAGASA-DOST website.

    :param weather_outlook_for_ph_tourist_areas: Weather outlook
        for selected Philippine tourist areas
    :type weather_outlook_for_ph_tourist_areas: dict[str, dict]
    """
    ingested_data = weather_outlook_for_ph_tourist_areas

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/weather_outlook_for_ph_tourist_areas.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)