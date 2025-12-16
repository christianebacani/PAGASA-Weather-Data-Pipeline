"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_daily_weather_forecast` module of the `src.ingest` package.
"""
from ingest.ingest_daily_weather_forecast import create_subdir
from ingest.ingest_daily_weather_forecast import ingest_beautiful_soup_object
from ingest.ingest_daily_weather_forecast import ingest_issued_datetime
from ingest.ingest_daily_weather_forecast import save_issued_datetime_to_raw_subdir
from ingest.ingest_daily_weather_forecast import ingest_synopsis
from ingest.ingest_daily_weather_forecast import save_synopsis_to_raw_subdir
from ingest.ingest_daily_weather_forecast import ingest_tc_information
from ingest.ingest_daily_weather_forecast import save_tc_information_to_raw_subdir
from ingest.ingest_daily_weather_forecast import ingest_forecast_weather_conditions
from ingest.ingest_daily_weather_forecast import save_forecast_weather_conditions_to_raw_subdir
from ingest.ingest_daily_weather_forecast import ingest_forecast_wind_and_coastal_water_conditions
from ingest.ingest_daily_weather_forecast import save_forecast_wind_and_coastal_water_conditions_to_raw_subdir
from ingest.ingest_daily_weather_forecast import ingest_temperature_and_relative_humidity
from ingest.ingest_daily_weather_forecast import save_temperature_and_relative_humidity_to_raw_subdir

def ingest_daily_weather_forecast(
) -> None:
    """
    Ingest daily weather forecast data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_daily_weather_forecast` module of the `src.ingest`
    package.
    """
    # Run all functions to ingest daily weather forecast data
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'
    )

    issued_datetime = ingest_issued_datetime(soup)
    save_issued_datetime_to_raw_subdir(issued_datetime)

    synopsis = ingest_synopsis(soup)
    save_synopsis_to_raw_subdir(synopsis)

    tc_information = ingest_tc_information(soup)
    save_tc_information_to_raw_subdir(tc_information)

    forecast_weather_conditions = ingest_forecast_weather_conditions(soup)
    save_forecast_weather_conditions_to_raw_subdir(forecast_weather_conditions)

    forecast_wind_and_coastal_water_conditions = ingest_forecast_wind_and_coastal_water_conditions(soup)
    save_forecast_wind_and_coastal_water_conditions_to_raw_subdir(forecast_wind_and_coastal_water_conditions)
    
    temperature_and_relative_humidity = ingest_temperature_and_relative_humidity(soup)
    save_temperature_and_relative_humidity_to_raw_subdir(temperature_and_relative_humidity)