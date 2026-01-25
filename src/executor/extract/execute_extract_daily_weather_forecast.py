"""
Docstring for src.executor.extract.execute_extract_daily_weather_forecast
"""
from etl.extract.extract_daily_weather_forecast import connect
from etl.extract.extract_daily_weather_forecast import database_config
from etl.extract.extract_daily_weather_forecast import extract_issued_datetime
from etl.extract.extract_daily_weather_forecast import clean_issued_datetime

def extract_daily_weather_forecast(
) -> None:
    """
    Executes the function in the
    `src.etl.extract.extract_daily_weather_forecast`
    module to extract the data from the `data/raw/daily_weather_forecasts/`
    subdirectory path that consist of ingested artifacts as a JSON file
    """
    issued_datetime_dataframe = extract_issued_datetime(
        'data/raw/daily_weather_forecasts/issued_datetime.json'
    )
    cleaned_issued_datetime = clean_issued_datetime(
        issued_datetime_dataframe
    )