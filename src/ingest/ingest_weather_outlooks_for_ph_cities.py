"""
Docstring for ingest.ingest_weather_outlooks_for_ph_cities
"""
import os
import requests
import json
from bs4 import BeautifulSoup

def create_subdir(
) -> None:
    """
    Creates the subdirectory path `data/raw/weather_outlooks_for_ph_cities/`
    for ingested data from the weather outlook for selected Philippine cities
    page of PAGASA-DOST website.
    """
    if not os.path.exists('data/raw/weather_outlooks_for_ph_cities'):
        os.makedirs('data/raw/weather_outlooks_for_ph_cities')

def ingest_and_parse_from_url(
        url: str
) -> BeautifulSoup | None:
    """
    Ingest and parse BeautifulSoup object
    from the URL of the weather outlook for
    selected Philippine cities page of the
    PAGASA-DOST website.

    :param url: URL of the weather outlook for
        selected Philippine cities page to ingest
        and parse
    :type url: str

    :return: A BeautifulSoup object representing the
        parsed HTML of the page, or NoneType if the page
        does not allow scraping
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
    Ingest the issued datetimes of the weather
    outlook for selected Philippine cities page
    from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Issued datetimes of the weather outlook for
        selected Philippine cities page from the PAGASA-DOST
        website.
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
    cities page from the PAGASA-DOST website.

    :param issued_datetime: Issued datetimes
        of the weather outlook for selected
        Philippine cities page from the PAGASA-
        DOST website
    :type issued_datetime: str
    """
    ingested_data = {
        "issued_datetime": issued_datetime
    }

    with open(
        'data/raw/daily_weather_forecasts/issued_datetimes.json',
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
    cities page from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: Time validities of the weather outlook
        for selected Philippine cities page from the
        PAGASA-DOST website.
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
    outlook for selected Philippine cities page from
    the PAGASA-DOST website.

    :param time_validity: Time of validities of thea
        weather outlook for selected Philippine cities
        page from the PAGASA-DOST website
    :type time_validity: str
    """
    ingested_data = {
        "time_validity": time_validity
    }

    with open(
        'data/raw/daily_weather_forecasts/time_validity.json',
        'w'
    ) as json_file:
        json.dump(ingested_data, json_file, indent=4)

    json_file.close()

def ingest_and_parse_list_of_all_ph_city_tags(
    soup: BeautifulSoup | None
) -> list[BeautifulSoup]:
    """
    Ingest and parse HTML tags of selected
    Philippine cities to get their weather
    outlooks from the PAGASA-DOST website.

    :param soup: A BeautifulSoup object representing
        the parsed HTML of the page, or NoneType if the
        page does not allow scraping
    :type soup: BeautifulSoup | None

    :return: HTML tags of selected Philippine cities to
        get their weather outlooks from the PAGASA-DOST
        website
    :rtype: list[BeautifulSoup]
    """
    if soup is None:
        return []

    div_tag_with_row_weather_page_class = soup.find(
        'div',
        attrs={
            'class': 'row weather-page'
        }
    )
    weather_outlooks_for_ph_cities_tag = div_tag_with_row_weather_page_class.find(
        'div',
        attrs={
            'class': 'col-md-12 col-lg-12'
        }
    )
    list_of_all_ph_city_tags = weather_outlooks_for_ph_cities_tag.find_all(
        'div',
        attrs={
            'class': 'panel panel-default panel-pagasa'
        }
    )

    return list_of_all_ph_city_tags

def ingest_ph_city_names(
        list_of_all_ph_city_tags: list[BeautifulSoup]
) -> dict[str, dict]:
    """
    Ingest selected Philippine city names from the HTML
    tags of selected Philippine cities to get their weather
    outlooks from the PAGASA-DOST website.

    :param list_of_all_ph_city_tags: HTML tags of selected
        Philippine cities to get their weather outlooks
        from the PAGASA-DOST website
    :type list_of_all_ph_city_tags: list[BeautifulSoup]

    :return: Selected Philippine city names dictionary
    :rtype: dict[str, dict]
    """
    result = {}

    if list_of_all_ph_city_tags == []:
        return result

    for ph_city_tag in list_of_all_ph_city_tags:
        ph_city_name_tag = ph_city_tag.find(
            'a'
        )
        ph_city_name = ph_city_name_tag.text
        ph_city_name = str(ph_city_name)
        result[ph_city_name] = {}

    return result

def ingest_weather_dates(
        list_of_all_ph_city_tags: list[BeautifulSoup]
) -> list[str]:
    """
    Ingest weather dates from the HTML tags of selected
    Philippine cities to get their weather outlooks from
    the PAGASA-DOST website.

    :param list_of_all_ph_city_tags: HTML tags of selected
        Philippine cities to get their weather outlooks
        from the PAGASA-DOST website
    :type list_of_all_ph_city_tags: list[BeautifulSoup]

    :return: List of all weather dates
    :rtype: list[str]
    """
    list_of_all_weather_dates = []

    if list_of_all_ph_city_tags == []:
        return list_of_all_weather_dates

    # Access only the first instance of selected PH city tag since weather dates are consistent across all cities
    first_instance_of_ph_city_tag = list_of_all_ph_city_tags[0]
    table_tag = first_instance_of_ph_city_tag.find(
        'table',
        attrs={
            'class': 'table'
        }
    )
    thead_tag = table_tag.find(
        'thead',
        attrs={
            'class': 'desktop-view-thead'
        }
    )
    
def map_ph_city_names_to_weather_dates(
        ph_city_names_dict: dict[str, dict],
        list_of_all_weather_dates: list[str]
) -> dict[str, dict]:
    """
    Map selected Philippine city names to their
    corresponding weather dates to get their
    weather outlooks from the PAGASA-DOST website.

    :param ph_city_names_dict: Selected Philippine city
        names dictionary
    :type ph_city_names_dict: dict[str, dict]

    :param list_of_all_weather_dates: List of all
        weather dates
    :type list_of_all_weather_dates: list[str]

    :return: Selected Philippine city names with their
        corresponding list of all weather dates
    :rtype: dict[str, dict]
    """
    result = ph_city_names_dict

    list_of_all_ph_city_names = list(ph_city_names_dict.keys())

    for ph_city_name in list_of_all_ph_city_names:
        result[ph_city_name]['weather_dates'] = list_of_all_weather_dates

    return result