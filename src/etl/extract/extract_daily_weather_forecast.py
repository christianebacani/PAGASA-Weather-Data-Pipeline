"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import pandas as pd

def extract_issued_datetime(
        issued_datetime_filepath: str        
) -> pd.DataFrame:
    """
    Extract the ingested issued datetime of
    daily weather forecast page as a JSON file
    from the subdirectory path
    `data/daily_weather_forecasts`.

    :param issued_datetime_filepath: Issued
        datetime of the daily weather forecast
        page as a DataFrame object
    :type issued_datetime_filepath: str
    """
    issued_datetime = pd.read_json(
        issued_datetime_filepath
    )

    return issued_datetime


def transform_extracted_issued_datetime(
        issued_datetime: pd.DataFrame
) -> pd.DataFrame:
    """
    Transfrom the extracted issued datetime
    of the daily weather forecast page as a
    DataFrame object

    :param issued_datetime: Issued datetime
        of the daily weather forecast page as
        a DataFrame object
    :type issued_datetime: pd.DataFrame

    :return: Transformed issued datetime of the
        daily weather forecast page as a DataFrame
        object
    :rtype: DataFrame
    """