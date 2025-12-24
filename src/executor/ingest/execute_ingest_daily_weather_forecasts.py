"""
Docstring for executor.ingest.execute_ingest_daily_weather_forecasts
"""
from ingest.ingest_daily_weather_forecasts import create_subdir
from ingest.ingest_daily_weather_forecasts import ingest_beautiful_soup_object

def ingest_daily_weather_forecasts(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_daily_weather_forecasts.py`
    module to ingest the data from the daily
    weather forecast page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'
    )