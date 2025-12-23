"""
Docstring for executor.ingest.execute_ingest_daily_weather_forecasts
"""
from src.ingest.ingest_daily_weather_forecasts import create_subdir

def ingest_daily_weather_forecasts(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_daily_weather_forecasts.py`
    module to ingest the data from the daily
    weather forecast page of PAGASA-DOST website.
    """
    create_subdir()