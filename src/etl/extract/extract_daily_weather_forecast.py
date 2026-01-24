"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import pandas as pd

def extract_issued_datetime(
        issued_datetime_filepath: str        
) -> pd.DataFrame:
    """
    Extract the ingested issued datetime of
    daily weather forecast page from the subdirectory
    path `data/daily_weather_forecasts`.

    :param issued_datetime_filepath: Filepath
        of the ingested issued datetime from
        the subdirectory path
        `data/daily_weather_forecasts`
    :type issued_datetime_filepath: str

    :return: Issued datetime of the daily weather
        forecast page as a DataFrame object
    :rtype: DataFrame
    """
    issued_datetime_dataframe = pd.read_json(
        issued_datetime_filepath
    )

    return issued_datetime_dataframe

def transform_issued_datetime(
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the issued datetime of the
    daily weather forecast page as a
    DataFrame object.

    :param issued_datetime_dataframe: Issued datetime
        of the daily weather forecast page as
        a DataFrame object
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed issued datetime of the
        daily weather forecast page as a DataFrame
        object
    :rtype: DataFrame
    """
    columns = [
        'issued_time',
        'issued_date'
    ]
    transformed_issued_datetime = pd.DataFrame(
        columns=columns
    )

    issued_datetime = issued_datetime_dataframe['issued_datetime'][0]
    issued_datetime = str(issued_datetime)
    issued_datetime = issued_datetime.strip()
    issued_datetime = issued_datetime.replace(
        'Issued at:', ''
    )
    issued_time = issued_datetime.split(', ')[0]
    issued_date = issued_datetime.split(', ')[1]

    transformed_issued_datetime = pd.concat([
        transformed_issued_datetime,
        pd.DataFrame({
            'issued_time': [issued_time],
            'issued_date': [issued_date]
        })
    ])

    return transformed_issued_datetime

def extract_synopsis(
        synopsis_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested synopsis of the daily
    weather forecast page from the subdirectory
    path `data/daily_weather_forecasts`.

    :param synopsis_filepath: Filepath of the
        ingested synopsis from the subdirectory
        path `data/daily_weather_forecasts`
    :type synopsis_filepath: str

    :return: Synopsis of the daily weather forecast
        page as a DataFrame object
    :rtype: DataFrame
    """
    synopsis_dataframe = pd.read_json(
        synopsis_filepath
    )

    return synopsis_dataframe

def transform_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the synopsis of the
    daily weather forecast page as a
    DataFrame object.

    :param synopsis_dataframe: Synopsis of the
        daily weather forecast page as a DataFrame
        object
    :type synopsis: pd.DataFrame

    :return: Transformed synopsis of the daily
        weather forecast page as a DataFrame
        object
    :rtype: DataFrame
    """
    columns = [
        'synopsis'
    ]
    transformed_dataframe = pd.DataFrame(
        columns=columns
    )