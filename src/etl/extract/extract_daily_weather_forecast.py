"""
Extract daily weather forecast from the `data/raw/daily_weather_forecast`
subdirectory on the local machine.

This module provides functions to parse JSON files from the `data/raw/daily_weather_forecast`
subdirectory and convert them into structured DataFrame objects, including:

- Issued datetime
- Synopsis
- Tropical cyclone information
- Forecast weather conditions
- Forecast wind and coastal water conditions
- Temperature and relative humidity

Parsed DataFrames are saved as CSV files in the
`data/stage/daily_weather_forecast/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/daily_weather_forecast` subdirectory to store CSV files.

    This subdirectory stores the staged daily weather forecasts, parsed from JSON files
    located in the `data/raw/daily_weather_forecast` subdirectory on the local machine.
    """
    # Create the data/stage/daily_weather_forecast/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/daily_weather_forecast'):
        os.makedirs('data/stage/daily_weather_forecast')

def parse_issued_datetime(
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
        'issued_datetimes': [
            issued_datetime_raw_dataframe['issued_datetime']
        ]
    })

    return issued_datetime_dataframe

def save_raw_issued_datetime(
        issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw issued datetime DataFrame to the staging
    directory for further processing.

    :param issued_datetime_dataframe: DataFrame containing the issued datetime
        of the daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame
    """
    # Save the raw issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_synopsis(
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
        'synopses': [
            synopsis_raw_dataframe['synopsis']
        ]
    })

    return synopsis_dataframe

def save_raw_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw synopsis DataFrame to the staging
    directory for further processing.

    :param synopsis_dataframe: DataFrame containing the
        synopsis of the daily weather forecast
    :type synopsis_dataframe: pd.DataFrame
    """
    # Save the raw synopsis DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/synopsis.csv'
    synopsis_dataframe.to_csv(target_filepath, index=False)

def parse_tropical_cyclone_information(
        tropical_cyclone_information_filepath: str
) -> pd.DataFrame:
    """
    Parse the tropical cyclone information of the daily weather forecast into
    a DataFrame.

    :param tropical_cyclone_information_filepath: Relative filepath of the JSON file
        that stores the tropical cyclone information of the daily
        weather forecast
    :type tropical_cyclone_information_filepath: str

    :return: DataFrame containing the tropical cyclone information of the
        daily weather forecast
    :rtype: DataFrame
    """
    # Read the tropical cyclone information JSON file as a Pandas Series
    tropical_cyclone_information_raw_dataframe = pd.read_json(tropical_cyclone_information_filepath, typ='series')

    # Parse the Pandas Series as a DataFrame object
    tropical_cyclone_information_dataframe = pd.DataFrame({
        'current_updates': [
            tropical_cyclone_information_raw_dataframe['current_update']
        ],
        'tropical_cyclone_names': [
            tropical_cyclone_information_raw_dataframe['tropical_cyclone_name']
        ],
        'locations': [
            tropical_cyclone_information_raw_dataframe['location']
        ],
        'maximum_sustained_winds': [
            tropical_cyclone_information_raw_dataframe['maximum_sustained_winds']
        ],
        'gustiness': [
            tropical_cyclone_information_raw_dataframe['gustiness']
        ],
        'movements': [
            tropical_cyclone_information_raw_dataframe['movement']
        ]
    })

    return tropical_cyclone_information_dataframe

def save_raw_tropical_cyclone_information(
        tropical_cyclone_information_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw tropical cyclone information DataFrame to the staging
    directory for further processing.

    :param tropical_cyclone_information_dataframe: DataFrame containing the tropical cyclone information
        of the daily weather forecast
    :type tropical_cyclone_information_dataframe: pd.DataFrame
    """
    # Save the raw tropical cyclone information DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/tropical_cyclone_information.csv'
    tropical_cyclone_information_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_weather_conditions(
        forecast_weather_conditions_filepath: str
) -> pd.DataFrame:
    """
    Parse the forecast weather conditions of the daily
    weather forecast into a DataFrame.

    :param forecast_weather_conditions_filepath: Relative
        filepath of the JSON file that stores the forecast
        weather conditions of the daily weather forecast
    :type forecast_weather_conditions_filepath: str

    :return: DataFrame containing the forecast weather conditions
        of the daily weather forecast
    :rtype: DataFrame
    """
    # Read the forecast weather conditions JSON file as a DataFrame object
    forecast_weather_conditions_dataframe = pd.read_json(
        forecast_weather_conditions_filepath
    )

    # Rename the columns of the DataFrame object
    forecast_weather_conditions_dataframe.rename(columns={
        'place': 'places',
        'weather_condition': 'weather_conditions',
        'caused_by': 'causes_by'
    }, inplace=True)

    return forecast_weather_conditions_dataframe

def save_raw_forecast_weather_conditions(
        forecast_weather_conditions_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw forecast weather conditions DataFrame to the staging
    directory for further processing.

    :param forecast_weather_conditions_dataframe: DataFrame containing the forecast
        weather conditions of the daily weather forecast
    :type forecast_weather_conditions_dataframe: pd.DataFrame
    """
    # Save the raw forecast weather conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_weather_conditions.csv'
    forecast_weather_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions_filepath: str
) -> pd.DataFrame:
    """
    Parse the forecast wind and coastal water conditions of the daily weather
    forecast into a DataFrame.

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

    # Rename the columns of the DataFrame object
    forecast_wind_and_coastal_water_conditions_dataframe.rename(columns={
        'place': 'places',
        'speed': 'speeds',
        'direction': 'directions',
        'coastal_water': 'coastal_waters'        
    }, inplace=True)

    return forecast_wind_and_coastal_water_conditions_dataframe

def save_raw_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw foreast wind and coastal water conditions DataFrame to the staging
    directory for further processing.

    :param forecast_wind_and_coastal_water_conditions_dataframe: DataFrame containing the
        forecast wind and coastal water conditions of the daily weather forecast
    :type forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
    """
    # Save the raw forecast wind and coastal water conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.csv'
    forecast_wind_and_coastal_water_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_temperature_and_relative_humidity(
        temperature_and_relative_humidity_filepath: str
) -> pd.DataFrame:
    """
    Parse the temperature and relative humidity of the daily weather
    forecast into a DataFrame.

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
        'maximum_temperatures': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['max'][0]
        ],
        'time_of_maximum_temperatures': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['max'][1]
        ],
        'minimum_temperatures': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['min'][0]
        ],
        'time_of_minimum_temperatures': [
            temperature_and_relative_humidity_raw_dataframe['temperature']['min'][1]
        ],
        'maximum_relative_humidity_percentages': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['max'][0]
        ],
        'time_of_maximum_relative_humidity_percentages': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['max'][1]
        ],
        'minimum_relative_humidity_humidity_percentages': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['min'][0]
        ],
        'time_of_minimum_relative_humidity_percentages': [
            temperature_and_relative_humidity_raw_dataframe['relative_humidity_percentage']['min'][1]
        ]
    })

    return temperature_and_relative_humidity_dataframe

def save_raw_temperature_and_relative_humidity(
        temperature_and_relative_humidity_dataframe: pd.DataFrame
) -> None:
    """
    Save the raw temperature and relative humdity DataFrame to the staging directory
    for further processing.

    :param temperature_and_relative_humidity_dataframe: DataFrame containing
        the temperature and relative humidity of the daily weather forecast
    :type temperature_and_relative_humidity_dataframe: pd.DataFrame
    """
    # Save the raw temperature and relative humidity to the target filepath
    target_filepath = f'data/stage/daily_weather_forecast/temperature_and_relative_humidity.csv'
    temperature_and_relative_humidity_dataframe.to_csv(target_filepath, index=False)