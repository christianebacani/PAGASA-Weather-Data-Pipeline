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
    df = pd.read_json(issued_datetime_filepath, typ='series')
    issued_datetime_dataframe = pd.DataFrame({'issued_datetime': [df['issued_datetime']]})

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
    target_filepath = 'data/stage/daily_weather_forecast/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_synopsis_to_dataframe(
        synopsis_filepath: str
) -> pd.DataFrame:
    '''
    Parses the synopsis of the daily
    weather forecast as a JSON file into
    a Dataframe object.

    :param synopsis_filepath: Relative filepath
        of the JSON file that contains the
        synopsis of the daily weather forecast
    :type synopsis_filepath: str

    :return: Synopsis of the daily weather
        forecast as a Dataframe object
    :rtype: DataFrame
    '''