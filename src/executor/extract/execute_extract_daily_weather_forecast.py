"""
Docstring for src.executor.extract.execute_extract_daily_weather_forecast
"""
from etl.extract.extract_daily_weather_forecast import extract_issued_datetime

def extract_daily_weather_forecast(
) -> None:
    """
    Executes the function in the
    `src.etl.extract.extract_daily_weather_forecast`
    module to extract the data from the `data/daily_weather_forecasts/`
    subdirectory path that consist of ingested artifacts as a JSON file
    """
    issued_datetime = extract_issued_datetime(
        'data/daily_weather_forecasts/issued_datetime.json'
    )