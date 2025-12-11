"""
Extract and stage weather outlook for selected Philippine tourist areas from the 
`data/raw/weather_outlook_for_ph_tourist_areas` subdirectory on the local machine.

This module provides functions to parse JSON files from the
`data/raw/weather_outlook_for_ph_tourist_areas` subdirectory and convert them into structured DataFrame
objects, including:

- Issued datetime
- Valid period
- Weather outlook for selected Philippine tourist areas

Parsed DataFrames are staged as CSV files in the
`data/stage/weather_outlook_for_ph_tourist_areas/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/weather_outlook_for_ph_tourist_areas` subdirectory to store CSV files.

    This subdirectory stores the staged weather outlook data for selected Philippine tourist areas,
    parsed from JSON files located in the `data/raw/weather_outlook_for_ph_tourist_areas` subdirectory
    on the local machine.
    """
    # Create the data/stage/weather_outlook_for_ph_cities/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/weather_outlook_for_ph_tourist_areas'):
        os.makedirs('data/stage/weather_outlook_for_ph_tourist_areas')

def parse_issued_datetime_to_dataframe(
        issued_datetime_filepath: str
) -> pd.DataFrame:
    """
    Parse the issued datetime of the weather outlook for selected Philippine
    tourist areas into a DataFrame.

    :param issued_datetime_filepath: Relative filepath of the JSON file that
        stores the issued datetime of the weather outlook for selected
        Philippine tourist areas
    :type issued_datetime_filepath: str

    :return: DataFrame containing the issued datetime of the weather outlook
        for selected Philippine tourist areas
    :rtype: DataFrame
    """
    # Read the issued datetime JSON file as a Pandas Series
    issued_datetime_raw_dataframe = pd.read_json(issued_datetime_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    issued_datetime_dataframe = pd.DataFrame({
        'issued_datetime': [
            issued_datetime_raw_dataframe['issued_datetime']
        ]
    })

    return issued_datetime_dataframe

def stage_issued_datetime_dataframe(
        issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Stage the issued datetime DataFrame to the staging directory for further processing.

    :param issued_datetime_dataframe: DataFrame containing the issued datetime of the
        weather outlook for selected Philippine tourist areas into a DataFrame
    :type issued_datetime_dataframe: pd.DataFrame
    """
    # Stage the issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_tourist_areas/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_valid_period_to_dataframe(
        valid_period_filepath: str
) -> pd.DataFrame:
    """
    Parse the valid period of the weather outlook for selected Philippine
    tourist areas into a DataFrame.

    :param valid_period_filepath: Relative filepath of the JSON file that
        stores the valid period of the weather outlook for selected
        Philippine tourist areas
    :type valid_period_filepath: str
    
    :return: DataFrame containing the valid period of the weather outlook for
        selected Philippine tourist areas
    :rtype: DataFrame
    """
    # Read the valid period JSON file as a Pandas Series
    valid_period_raw_dataframe = pd.read_json(valid_period_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    valid_period_dataframe = pd.DataFrame({
        'valid_period': [
            valid_period_raw_dataframe['valid_period']
        ]
    })

    return valid_period_dataframe

def stage_valid_period_dataframe(
        valid_period_dataframe: pd.DataFrame
) -> None:
    """
    Stage the valid period DataFrame to the staging directory for further processing.

    :param issued_datetime_dataframe: DataFrame containing the valid period of the
        weather outlook for selected Philippine tourist areas
    :type issued_datetime_dataframe: pd.DataFrame
    """
    # Stage the valid period DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_tourist_areas/valid_period.csv'
    valid_period_dataframe.to_csv(target_filepath, index=False)

def parse_ph_tourist_areas_weather_outlook_to_dataframe(
        ph_tourist_areas_weather_outlook_filepath: str
) -> pd.DataFrame:
    """
    Parse the weather outlook for selected Philippine tourist areas into
    a DataFrame.

    :param ph_tourist_areas_weather_outlook_filepath: Relative filepath of
        the JSON file that stores the weather outlook for selected Philippine
        tourist areas
    :type ph_tourist_areas_weather_outlook_filepath: str

    :return: DataFrame containing the weather outlook for selected Philippine
        tourist areas
    :rtype: DataFrame
    """
    # Read the PH tourist areas weather outlook JSON file as a DataFrame object
    ph_tourist_areas_weather_outlook_raw_dataframe = pd.read_json(
        ph_tourist_areas_weather_outlook_filepath
    )

    # Using initialized dictionary to restructure data from PH tourist areas weather outlook DataFrame
    ph_tourist_areas_weather_outlook_dict = {
        'ph_tourist_areas': [],
        'weather_dates': [],
        'minimum_temperatures': [],
        'maximum_temperatures': []
    }

    # Map PH tourist areas weather outlook DataFrame to the initialized dictionary using a for-loop
    for ph_tourist_area, weather_outlook_dict in ph_tourist_areas_weather_outlook_raw_dataframe.items():
        for _ in range(5):
            ph_tourist_areas_weather_outlook_dict['ph_tourist_areas'].append(
                ph_tourist_area
            )

        for weather_date in weather_outlook_dict['weather_dates']:
            ph_tourist_areas_weather_outlook_dict['weather_dates'].append(
                weather_date
            )

        for temperatures in weather_outlook_dict['temperature_ranges']:
            minimum_temperature = temperatures[0]
            maximum_temperature = temperatures[1]

            ph_tourist_areas_weather_outlook_dict['minimum_temperatures'].append(
                minimum_temperature
            )
            ph_tourist_areas_weather_outlook_dict['maximum_temperatures'].append(
                maximum_temperature
            )

    # Convert the dictionary to a DataFrame object
    ph_tourist_areas_weather_outlook_dataframe = pd.DataFrame(
        ph_tourist_areas_weather_outlook_dict
    )

    return ph_tourist_areas_weather_outlook_dataframe

# TODO:
# - Change the content of the funct `parse_ph_cities_weather_outlook_to_dataframe` to match
#   it with the content of the funct `parse_ph_tourist_areas_weather_outlook_to_dataframe`