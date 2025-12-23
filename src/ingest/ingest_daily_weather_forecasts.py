"""
Docstring of the src.ingest.ingest_daily_weather_forecasts
"""
import os

def create_subdir(
) -> None:
    """
    Creates a subdirectory path `data/raw/daily_weather_forecasts/`
    to store ingested data as a JSON file from the daily weather
    forecast page of PAGAASA-DOST website.
    """
    if not os.path.exists('data/raw/daily_weather_forecasts'):
        os.makedirs('data/raw/daily_weather_forecasts')