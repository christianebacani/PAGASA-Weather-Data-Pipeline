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
        data/stage subirectory on the local
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
        forecast as a Dataframe object
    :rtype: DataFrame
    '''
    # Read the issued datetime JSON file as a Pandas Series
    issued_datetime_raw_dataframe = pd.read_json(issued_datetime_filepath, typ='series')
    # Parse the Pandas Series as a Dataframe object
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
    forecast as a Dataframe object to the
    data/stage/daily_weather_forecast subdirectory
    on the local machine.

    :param issued_datetime_dataframe: Issued datetime
        of the daily weather forecast as a Dataframe
        object
    :type issued_datetime_dataframe: pd.DataFrame
    '''
    # Stage the issued datetime Dataframe object to the target filepath
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
        forecast as a Dataframe object
    :rtype: DataFrame
    '''
    # Read the synopsis JSON file as a Pandas Series
    synopsis_raw_dataframe = pd.read_json(synopsis_filepath, typ='series')
    # Parse the Pandas Series as a Dataframe object
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
    forecast as a Dataframe object to the
    data/stage/daily_weather_forecast subdirectory
    on the local machine.

    :param synopsis_dataframe: Synopsis of the
        daily weather forecast as a Dataframe
        object
    :type synopsis_dataframe: pd.DataFrame
    '''
    # Stage the synopsis Dataframe object to the target filepath
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
    # Parse the Pandas Series as a Dataframe object
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
    daily weather forecast as a Dataframe object to
    the data/stage/daily_weather_forecast
    subdirectory on the local machine.

    :param tc_information_dataframe: Tropical
        cyclone information of the daily weather
        forecast as a DataFrame object
    :type tc_information_dataframe: pd.DataFrame
    '''
    # Stage the tropical cyclone information Dataframe object to the target filepath
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