"""
Extract weather outlook for selected Philippine cities from the 
`data/raw/weather_outlook_for_ph_cities` subdirectory on the local machine.

This module provides functions to parse JSON files from the
`data/raw/weather_outlook_for_ph_cities` subdirectory and convert them into structured DataFrame
objects, including:

- Issued datetime
- Valid period
- Weather outlook for selected Philippine cities

Parsed DataFrames are saved as CSV files in the
`data/stage/weather_outlook_for_ph_cities/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/weather_outlook_for_ph_cities` subdirectory to store CSV files.

    This subdirectory stores the staged weather outlook data for selected Philippine cities,
    parsed from JSON files located in the `data/raw/weather_outlook_for_ph_cities` subdirectory
    on the local machine.
    """
    # Create the data/stage/weather_outlook_for_ph_cities/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/weather_outlook_for_ph_cities'):
        os.makedirs('data/stage/weather_outlook_for_ph_cities')

def parse_issued_datetime(
        issued_datetime_filepath: str
) -> pd.DataFrame:
    """
    Parse the issued datetime of the weather outlook for selected Philippine
    cities into a DataFrame.

    :param issued_datetime_filepath: Relative filepath of the
        JSON file that stores the issued datetime of the
        weather outlook for selected Philippine cities
    :type issued_datetime_filepath: str

    :return: DataFrame containing the issued datetime of the weather outlook
        for selected Philippine cities
    :rtype: DataFrame
    """
    # Read the issued datetime JSON file as a Pandas Series
    issued_datetime_raw_dataframe = pd.read_json(issued_datetime_filepath, typ='series')

    # Parse the Pandas Series as a DataFrame object
    issued_datetime_dataframe = pd.DataFrame({
        'issued_datetimes': [
            issued_datetime_raw_dataframe['issued_datetime']
        ]
    })

    return issued_datetime_dataframe

def save_raw_issued_datetime(
        issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw issued datetime DataFrame in the
    `data/stage/weather_outlook_for_ph_cities/`
    subdirectory on the local machine.

    :param issued_datetime_dataframe: DataFrame containing the issued
        datetime of the weather outlook for selected Philippine cities
    :type issued_datetime_dataframe: pd.DataFrame
    """
    # Save the raw issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_cities/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_valid_period(
        valid_period_filepath: str
) -> pd.DataFrame:
    """
    Parse the valid period of the weather outlook for selected Philippine
    cities into a DataFrame.

    :param valid_period_filepath: Relative filepath of the JSON
        file that stores the valid period of the weather outlook
        for selected Philippine cities
    :type valid_period_filepath: str

    :return: DataFrame containing the valid period of the weather
        outlook for selected Philippine cities
    :rtype: DataFrame
    """
    # Read the valid period JSON file as a Pandas Series
    valid_period_raw_dataframe = pd.read_json(valid_period_filepath, typ='series')

    # Parse the Pandas Series as a DataFrame object
    valid_period_dataframe = pd.DataFrame({
        'valid_periods': [
            valid_period_raw_dataframe['valid_period']
        ]
    })

    return valid_period_dataframe

def save_raw_valid_period(
        valid_period_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw valid period DataFrame in the
    `data/stage/weather_outlook_for_ph_cities/`
    subdirectory on the local machine.

    :param valid_period_dataframe: DataFrame containing the valid
        period of the weather outlook for selected Philippine cities
    :type valid_period_dataframe: pd.DataFrame
    """
    # Save the raw valid period DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_cities/valid_period.csv'
    valid_period_dataframe.to_csv(target_filepath, index=False)

def parse_ph_cities_weather_outlook(
        ph_cities_weather_outlook_filepath: str
) -> pd.DataFrame:
    """
    Parse the weather outlook for selected Philippine cities into a DataFrame.

    :param ph_cities_weather_outlook_filepath: Relative filepath of the JSON file that
        stores the weather outlook for selected Philippine cities
    :type ph_cities_weather_outlook_filepath: str

    :return: DataFrame containing the weather outlook for selected Philippine cities
    :rtype: DataFrame
    """
    # Read the PH cities weather outlook JSON file as a DataFrame object
    ph_cities_weather_outlook_raw_dataframe = pd.read_json(ph_cities_weather_outlook_filepath)

    # Using initialized dictionary to restructure data from PH cities weather outlook DataFrame
    ph_cities_weather_outlook_dict = {
        'ph_cities': [],
        'weather_dates': [],
        'minimum_temperatures': [],
        'maximum_temperatures': [],
        'chance_of_rain_percentages': []
    }

    # Iterate the PH cities weather outlook DataFrame to map its value to the initialized dictionary
    for ph_city, weather_outlook_dict in ph_cities_weather_outlook_raw_dataframe.items():
        # Iterate 5 times to map PH city name to the initialized dictionary
        for _ in range(5):
            # Iterating 5 times because every PH city has 5 instances of weather outlooks per dates
            ph_cities_weather_outlook_dict['ph_cities'].append(ph_city)

        # Iterate the weather dates list to map it to the initialized dictionary
        for weather_date in weather_outlook_dict['weather_dates']:
            ph_cities_weather_outlook_dict['weather_dates'].append(
                weather_date
            )

        # Iterate the temperature ranges list to map it to the initialized dictionary
        for temperature_ranges in weather_outlook_dict['temperature_ranges']:
            minimum_temperature = temperature_ranges[0]
            maximum_temperature = temperature_ranges[1]

            ph_cities_weather_outlook_dict['minimum_temperatures'].append(
                minimum_temperature
            )
            ph_cities_weather_outlook_dict['maximum_temperatures'].append(
                maximum_temperature
            )

        # Iterate the rain chance pct list to map it to the initialized dictionary
        for chance_of_rain_percentage in weather_outlook_dict['chance_of_rain_percentages']:
            ph_cities_weather_outlook_dict['chance_of_rain_percentages'].append(
                chance_of_rain_percentage
            )

    # Convert the dictionary to a DataFrame object
    ph_cities_weather_outlook_dataframe = pd.DataFrame(ph_cities_weather_outlook_dict)

    return ph_cities_weather_outlook_dataframe

def save_raw_ph_cities_weather_outlook(
        ph_cities_weather_outlook_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw weather outlook for selected Philippine cities
    DataFrame in the `data/stage/weather_outlook_for_ph_cities/`
    subdirectory on the local machine.

    :param ph_cities_weather_outlook_dataframe: DataFrame containing the weather
        outlook for selected Philippine cities
    :type ph_cities_weather_outlook_dataframe: pd.DataFrame
    """
    # Save the raw PH cities weather outlook DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_cities/ph_cities_weather_outlook.csv'
    ph_cities_weather_outlook_dataframe.to_csv(target_filepath, index=False)