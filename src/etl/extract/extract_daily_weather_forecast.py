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
    Parses the issued datetime of the daily
    weather forecast as a JSON file into
    a Dataframe object.

    :param issued_datetime_filepath: Relative
        filepath of the JSON file that contains
        the issued datetime of the daily weather
        forecast
    :type issued_datetime_filepath: str

    :return: Issued datetime of the daily weather
        forecast as a Dataframe object
    :rtype: DataFrame
    '''
    issued_datetime_dataframe = pd.read_json(issued_datetime_filepath, typ='series')

    return issued_datetime_dataframe

def stage_issued_datetime(
        issued_datetime_filepath: str
) -> None:
    '''
    Stages the JSON file that contains
    the issued datetime of the daily weather
    forecast to the data/stage subdirectory
    on the local machine.

    :param issued_datetime_filepath: Relative
        filepath of the JSON file that contains
        the issued datetime of the daily weather
        forecast
    :type issued_datetime_filepath: str
    '''