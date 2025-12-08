'''
    Module to extract daily weather forecast data
    from the data/raw subdirectory on the local machine.
'''
import pandas as pd
import os

def create_subdir(
) -> None:
    '''
        Creates the
        data/stage/daily_weather_forecast/
        subdirectory to store CSV files for
        daily weather forecast from the
        data/raw subirectory on the local
        machine.
    '''
    # Create the data/stage/daily_weather_forecast/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/daily_weather_forecast'):
        os.makedirs('data/stage/daily_weather_forecast')

def parse_issued_datetime_to_dataframe(
        issued_datetime_filepath: str
) -> pd.DataFrame:
    '''
    Parses the issued datetime from JSON
    file into a DataFrame object.

    :param issued_datetime_filepath: Relative
        filepath of the JSON file that contains
        the issued datetime of the daily weather
        forecast
    :type issued_datetime_filepath: str

    :return: Issued datetime of the daily weather
        forecast as a DataFrame object
    :rtype: DataFrame
    '''
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
    '''
    Stages the issued datetime of the daily weather
    forecast as a DataFrame object to the
    data/stage/daily_weather_forecast subdirectory
    on the local machine.

    :param issued_datetime_dataframe: Issued datetime
        of the daily weather forecast as a DataFrame
        object
    :type issued_datetime_dataframe: pd.DataFrame
    '''
    # Stage the issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_synopsis_to_dataframe(
        synopsis_filepath: str
) -> pd.DataFrame:
    '''
    Parses the synopsis from JSON file
    into a DataFrame object.

    :param synopsis_filepath: Relative filepath
        of the JSON file that contains the
        synopsis of the daily weather forecast
    :type synopsis_filepath: str

    :return: Synopsis of the daily weather
        forecast as a DataFrame object
    :rtype: DataFrame
    '''
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
    '''
    Stages the synopsis of the daily weather
    forecast as a DataFrame object to the
    data/stage/daily_weather_forecast subdirectory
    on the local machine.

    :param synopsis_dataframe: Synopsis of the
        daily weather forecast as a DataFrame
        object
    :type synopsis_dataframe: pd.DataFrame
    '''
    # Stage the synopsis DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/synopsis.csv'
    synopsis_dataframe.to_csv(target_filepath, index=False)

def parse_tc_information_to_dataframe(
        tc_information_filepath: str
) -> pd.DataFrame:
    '''
    Parses the tropical cyclone information
    from JSON file into a DataFrame object.

    :param tc_information_filepath: Relative filepath
        of the JSON file that contains the tropical
        cyclone information of the daily weather forecast
    :type tc_information_filepath: str

    :return: Tropical cyclone information of the daily
        weather forecast as a DataFrame object
    :rtype: DataFrame
    '''
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
    '''
    Stages the tropical cyclone information of the
    daily weather forecast as a DataFrame object to
    the data/stage/daily_weather_forecast
    subdirectory on the local machine.

    :param tc_information_dataframe: Tropical
        cyclone information of the daily weather
        forecast as a DataFrame object
    :type tc_information_dataframe: pd.DataFrame
    '''
    # Stage the tropical cyclone information DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/tropical_cyclone_information.csv'
    tc_information_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_weather_conditions_to_dataframe(
        forecast_weather_conditions_filepath: str
) -> pd.DataFrame:
    '''
    Parses the forecast weather conditions from
    JSON file into a DataFrame object.

    :param forecast_weather_conditions_filepath:
        Relative filepath of the JSON file that
        contains the forecast weather conditions
        of the daily weather forecast
    :type forecast_weather_conditions_filepath: str

    :return: Forecast weather conditions of the daily
        weather forecast as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the issued datetime JSON file as a DataFrame object
    forecast_weather_conditions_dataframe = pd.read_json(
        forecast_weather_conditions_filepath
    )

    return forecast_weather_conditions_dataframe

def stage_forecast_weather_conditions_dataframe(
        forecast_weather_conditions_dataframe: pd.DataFrame
) -> None:
    '''
    Stages the forecast weather conditions of the daily
    weather forecast as a DataFrame object to the
    data/stage/daily_weather_forecast subdirectory on the
    local machine.

    :param forecast_weather_conditions_dataframe: Forecast
        weather conditions of the daily weather forecast
        as a DataFrame object
    :type forecast_weather_conditions_dataframe: pd.DataFrame
    '''
    # Stage the forecast weather conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_weather_conditions.csv'
    forecast_weather_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_forecast_wind_and_coastal_water_conditions_to_dataframe(
        forecast_wind_and_coastal_water_conditions_filepath: str
) -> pd.DataFrame:
    '''
    Parses the forecast wind and coastal water conditions from
    JSON file into a DataFrame object

    :param forecast_wind_and_coastal_water_conditions_filepath:
        Relative filepath of the JSON file that contains the
        forecast wind and coastal water conditions of the daily
        weather forecast
    :type forecast_wind_and_coastal_water_conditions_filepath: str

    :return: Forecast wind and coastal water conditions of the daily
        weather forecast as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the forecast wind and coastal water conditions JSON file as a DataFrame object
    forecast_wind_and_coastal_water_conditions_dataframe = pd.read_json(
        forecast_wind_and_coastal_water_conditions_filepath
    )

    return forecast_wind_and_coastal_water_conditions_dataframe

def stage_forecast_wind_and_coastal_water_conditions_dataframe(
        forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
) -> None:
    '''
    Stages the forecast wind and coastal water conditions of the
    daily weather forecast as a DataFrame object to the
    data/stage/daily_weather_forecast subdirectory on the
    local machine.

    :param forecast_wind_and_coastal_water_conditions_dataframe:
        Forecast wind and coastal water conditions of the daily
        weather forecast as a DataFrame object
    :type forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
    '''
    # Stage the forecast wind and coastal water conditions DataFrame object to the target filepath
    target_filepath = 'data/stage/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.csv'
    forecast_wind_and_coastal_water_conditions_dataframe.to_csv(target_filepath, index=False)

def parse_temperature_and_relative_humidity_to_dataframe(
        temperature_and_relative_humidity_filepath: str
) -> pd.DataFrame:
    '''
    Parses the temperature and relative humidity from
    JSON file into a DataFrame object

    :param temperature_and_relative_humidity_filepath:
        Relative filepath of the JSON file that contains
        the temperature and relative humidity of the
        daily weather forecast
    :type temperature_and_relative_humidity_filepath: str

    :return: Temperature and relative humidity of the
        daily weather forecast as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the temperature and relative humidity JSON file as a Pandas Series
    temperature_and_relative_humidity_raw_dataframe = pd.read_json(
        temperature_and_relative_humidity_filepath
    )
    # Parse the Pandas Series as a DataFrame object
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
    '''
    Stages the temperature and relative humidity of the
    daily weather forecast as a DataFrame object to
    the data/stage/daily_weather_forecast
    subdirectory on the local machine.

    :param temperature_and_relative_humidity_dataframe:
        Temperature and relative humidity of the daily
        weather forecast as a DataFrame object
    :type temperature_and_relative_humidity_dataframe:
        pd.DataFrame
    '''
    # Stage the temperature and relative humidity to the target filepath
    target_filepath = f'data/stage/daily_weather_forecast/temperature_and_relative_humidity.csv'
    temperature_and_relative_humidity_dataframe.to_csv(target_filepath, index=False)