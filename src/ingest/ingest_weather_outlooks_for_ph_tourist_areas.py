"""
Docstring for ingest.ingest_weather_outlooks_for_ph_tourist_areas
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

def ingest_and_parse_from_url(
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

def ingest_issued_datetimes(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the issued datetimes of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the
        page, or NoneType if the page does
        not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the weather
        outlook for selected Philippine tourist
        areas page from the PAGASA-DOST website.
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

def save_ingested_issued_datetimes(
        issued_datetime: str
) -> None:
    """
    Save ingested issued datetimes of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param issued_datetime: Issued datetimes
        of the weather outlook for selected
        Philippine tourist areas page from
        the PAGASA-DOST website.
    :type issued_datetime: str
    """
    ingested_data = {
        "issued_datetime": issued_datetime
    }

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/issued_datetimes.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_time_validities(
        soup: BeautifulSoup | None
) -> str:
    """
    Ingest the time validities of the
    weather outlook for selected Philippine
    tourist areas page from the PAGASA-DOST
    website.

    :param soup: A BeautifulSoup object
        representing the parsed HTML of the page,
        or NoneType if the page does not allow
        scraping
    :type soup: BeautifulSoup | None

    :return: Time validities of the weather outlook
        for selected Philippine tourist areas page from
        the PAGASA-DOST website.
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

def save_ingested_time_validities(
        time_validity: str
) -> None:
    """
    Save ingested time validities of the weather
    outlook for selected Philippine tourist areas
    page from the PAGASA-DOST website.

    :param time_validity: Time validities of the
        weather outlook for selected Philippine
        tourist areas page from the PAGASA-DOST
        website
    :type time_validity: str
    """
    ingested_data = {
        "time_validity": time_validity
    }

    with open(
        'data/raw/weather_outlooks_for_ph_tourist_areas/time_validities.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_ph_tourist_area_names(
        soup: BeautifulSoup | None       
) -> dict[str, dict]:
    """
    Ingest selected Philippine tourist area names
    using the BeautifulSoup object representing the
    parsed HTML of the page consisting the selected
    Philippine tourist tourist areas to get their
    weather outlooks from the PAGASA-DOST website.

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

    :return: List of all weather dates
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
    :type list_of_all_weather_dates: list[str]

    :return: Selected Philippine city names with weather dates
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

    :return: List of all temperature ranges per selected
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