"""
Docstring for executor.ingest.execute_ingest_daily_weather_forecasts
"""
from ingest.ingest_daily_weather_forecasts import create_subdir
from ingest.ingest_daily_weather_forecasts import ingest_and_parse_soup_from_url

def ingest_daily_weather_forecasts(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_daily_weather_forecasts.py`
    module to ingest the data from the daily
    weather forecast page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'
    )