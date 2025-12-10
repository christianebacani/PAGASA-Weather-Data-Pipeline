"""
Extract and stage daily weather forecast from the `data/raw/daily_weather_forecast`
subdirectory on the local machine.

This module provides functions to parse JSON files from the `data/raw/daily_weather_forecast`
subdirectory and convert them into structured DataFrame objects, including:

- Issued datetime
- Synopsis
- Tropical cyclone information
- Forecast weather conditions
- Forecast wind and coastal water conditions
- Temperature and relative humidity

Parsed DataFrames are staged as CSV files in the
`data/stage/daily_weather_forecast/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/daily_weather_forecast` subdirectory to store CSV files.

    This subdirectory holds the staged daily weather forecast data parsed from
    the JSON files located in the `data/raw/daily_weather_forecast` subdirectory
    on the local machine.
    """
    # Create the data/stage/daily_weather_forecast/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/daily_weather_forecast'):
        os.makedirs('data/stage/daily_weather_forecast')

def parse_issued_datetime_to_dataframe(
        issued_datetime_filepath: str
) -> pd.DataFrame:
    """
    Parse the issued datetime of the daily weather forecast into a DataFrame.

    :param issued_datetime_filepath: Relative filepath of the JSON file that
        stores the issued datetime of the daily weather forecast
    :type issued_datetime_filepath: str

    :return: DataFrame containing the issued datetime of the daily weather forecast
    :rtype: pd.DataFrame
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

    :param issued_datetime_dataframe: DataFrame containing the issued datetime
        of the daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: None
    """
    # Stage the issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_synopsis_to_dataframe(
        synopsis_filepath: str
) -> pd.DataFrame:
    """
    Parse the synopsis of the daily weather forecast into a DataFrame.

    :param synopsis_filepath: Relative filepath of the JSON file that
        stores the synopsis of the daily weather forecast
    :type synopsis_filepath: str

    :return: DataFrame containing the synopsis of the daily weather forecast
    :rtype: pd.DataFrame
    """
    # Read the synopsis JSON file as a Pandas Series
    synopsis_raw_dataframe = pd.read_json(synopsis_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    synopsis_dataframe = pd.DataFrame({
        'synopsis': [
            synopsis_raw_dataframe['synopsis']
        ]
    })

    return synopsis_dataframe

def stage_synopsis_dataframe(
        synopsis_dataframe: pd.DataFrame
) -> None:
    """
    Stage the synopsis DataFrame to the staging directory for further processing.

    :param synopsis_dataframe: DataFrame containing the synopsis of the daily
        weather forecast
    :type synopsis_dataframe: pd.DataFrame
    """
    # Stage the synopsis DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/synopsis.csv'
    synopsis_dataframe.to_csv(target_filepath, index=False)

def parse_tc_information_to_dataframe(
        tc_information_filepath: str
) -> pd.DataFrame:
    """
    Parse the tropical cyclone information of the daily weather forecast into
    a DataFrame.

    :param tc_information_filepath: Relative filepath of the JSON file
        that stores the tropical cyclone information of the daily
        weather forecast
    :type tc_information_filepath: str

    :return: DataFrame containing the tropical cyclone information of the
        daily weather forecast
    :rtype: DataFrame
    """
    # Read the tropical cyclone information JSON file as a Pandas Series
    tc_information_raw_dataframe = pd.read_json(tc_information_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    tc_information_dataframe = pd.DataFrame({
        'current_update': [
            tc_information_raw_dataframe['current_update']
        ],
        'tropical_cyclone_name': [
            tc_information_raw_dataframe['tropical_cyclone_name']
        ],
        'location': [
            tc_information_raw_dataframe['location']
        ],
        'maximum_sustained_winds': [
            tc_information_raw_dataframe['maximum_sustained_winds']
        ],
        'gustiness': [
            tc_information_raw_dataframe['gustiness']
        ],
        'movement': [
            tc_information_raw_dataframe['movement']
        ]
    })

    return tc_information_dataframe

def stage_tc_information_dataframe(
        tc_information_dataframe: pd.DataFrame
) -> None:
    """
    Stage the tropical cyclone information DataFrame to the staging directory for
    further processing.

    :param tc_information_dataframe: DataFrame containing the tropical cyclone information
        of the daily weather forecast
    :type tc_information_dataframe: pd.DataFrame
    """
    # Stage the tropical cyclone information DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/tropical_cyclone_information.csv'
    tc_information_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_weather_conditions_to_dataframe(
        forecast_weather_conditions_filepath: str
) -> pd.DataFrame:
    """
    Parse the forecast weather conditions into a DataFrame.

    This function reads the JSON file containing the forecast
    weather conditions of the daily weather forecast and converts
    it into a Pandas DataFrame. The returned DataFrame is used
    for staging and further processing.

    :param forecast_weather_conditions_filepath: Relative
        filepath of the JSON file that stores the forecast
        weather conditions of the daily weather forecast
    :type forecast_weather_conditions_filepath: str

    :return: DataFrame containing the forecast weather conditions
        of the daily weather forecast
    :rtype: DataFrame
    """
    # Read the issued datetime JSON file as a DataFrame object
    forecast_weather_conditions_dataframe = pd.read_json(
        forecast_weather_conditions_filepath
    )

    return forecast_weather_conditions_dataframe

def stage_forecast_weather_conditions_dataframe(
        forecast_weather_conditions_dataframe: pd.DataFrame
) -> None:
    """
    Stage the forecast weather conditions DataFrame to the staging directory.

    This function saves the forecast weather conditions of the daily weather
    forecast as a CSV file in the `data/stage/daily_weather_forecast/` subdirectory
    on the local machine.

    :param forecast_weather_conditions_dataframe: DataFrame containing the forecast
        weather conditions of the daily weather forecast
    :type forecast_weather_conditions_dataframe: pd.DataFrame
    """
    # Stage the forecast weather conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_weather_conditions.csv'
    forecast_weather_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_wind_and_coastal_water_conditions_to_dataframe(
        forecast_wind_and_coastal_water_conditions_filepath: str
) -> pd.DataFrame:
    """
    Parse the forecast wind and coastal water conditions into a DataFrame.

    This function reads the JSON file containing the forecast wind and
    coastal water conditions of the daily weather forecast and converts
    it into a Pandas DataFrame. The returned DataFrame is used for staging
    and further processing.

    :param forecast_wind_and_coastal_water_conditions_filepath: Relative
        filepath of the JSON file that stores the forecast wind and coastal
        water conditions of the daily weather forecast
    :type forecast_wind_and_coastal_water_conditions_filepath: str

    :return: DataFrame containing the forecast wind and coastal water conditions
        of the daily weather forecast
    :rtype: DataFrame
    """
    # Read the forecast wind and coastal water conditions JSON file as a DataFrame object
    forecast_wind_and_coastal_water_conditions_dataframe = pd.read_json(
        forecast_wind_and_coastal_water_conditions_filepath
    )

    return forecast_wind_and_coastal_water_conditions_dataframe

def stage_forecast_wind_and_coastal_water_conditions_dataframe(
        forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
) -> None:
    """
    Stage the forecast wind and coastal water conditions DataFrame to the staging
    directory.

    This function saves the forecast wind and coastal water conditions of the daily
    weather forecast as a CSV file in the `data/stage/daily_weather_forecast/` subdirectory
    on the local machine.

    :param forecast_wind_and_coastal_water_conditions_dataframe: DataFrame containing the
        forecast wind and coastal water conditions of the daily weather forecast
    :type forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
    """
    # Stage the forecast wind and coastal water conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.csv'
    forecast_wind_and_coastal_water_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_temperature_and_relative_humidity_to_dataframe(
        temperature_and_relative_humidity_filepath: str
) -> pd.DataFrame:
    """
    Parse the temperature and relative humidity into a DataFrame.

    This function reads the JSON file containing the temperature
    and relative humidity of the daily weather forecast and converts
    it into a Pandas DataFrame. The returned DataFrame is used for
    staging and further processing.

    :param temperature_and_relative_humidity_filepath: Relative
        filepath of the JSON file that stores the temperature and
        relative humidity of the daily weather forecast
    :type temperature_and_relative_humidity_filepath: str

    :return: DataFrame containing the temperature and relative
        humidity of the daily weather forecast
    :rtype: DataFrame
    """
    # Read the temperature and relative humidity JSON file as a DataFrame object
    temperature_and_relative_humidity_raw_dataframe = pd.read_json(
        temperature_and_relative_humidity_filepath
    )
    # Restructure the temperature and relative humidity DataFrame to make it readable
    temperature_and_relative_humidity_dataframe = pd.DataFrame({
        'maximum_temperature': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['max'][0]
        ],
        'time_of_maximum_temperature': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['max'][1]
        ],
        'minimum_temperature': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['min'][0]
        ],
        'time_of_minimum_temperature': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['min'][1]
        ],
        'maximum_relative_humidity_percentage': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['max'][0]
        ],
        'time_of_maximum_relative_humidity_percentage': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['max'][1]
        ],
        'minimum_relative_humidity_humidity_percentage': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['min'][0]
        ],
        'time_of_minimum_relative_humidity_percentage': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['min'][1]
        ]
    })

    return temperature_and_relative_humidity_dataframe

def stage_temperature_and_relative_humidity_dataframe(
        temperature_and_relative_humidity_dataframe: pd.DataFrame
) -> None:
    """
    Stage the temperature and relative humidity DataFrame to the staging
    directory.

    This function saves the temperature and relative humidity of the daily
    weather forecast as a CSV file in the `data/stage/daily_weather_forecast/`
    subdirectory on the local machine.

    :param temperature_and_relative_humidity_dataframe: DataFrame containing
        the temperature and relative humidity of the daily weather forecast
    :type temperature_and_relative_humidity_dataframe: pd.DataFrame
    """
    # Stage the temperature and relative humidity to the target filepath
    target_filepath = f'data/stage/daily_weather_forecast/temperature_and_relative_humidity.csv'
    temperature_and_relative_humidity_dataframe.to_csv(target_filepath, index=False)