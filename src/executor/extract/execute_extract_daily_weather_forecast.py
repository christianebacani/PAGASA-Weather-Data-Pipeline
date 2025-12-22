"""
Execute extraction functions for daily weather forecast data.

This module runs all extraction tasks on files located in the `data/raw/daily_weather_forecast/`
subdirectory on the local machine, serving as the entry point for the
daily extraction workflow.
"""
from etl.extract.extract_daily_weather_forecast import create_subdir
from etl.extract.extract_daily_weather_forecast import parse_issued_datetime
from etl.extract.extract_daily_weather_forecast import save_raw_issued_datetime
from etl.extract.extract_daily_weather_forecast import parse_synopsis
from etl.extract.extract_daily_weather_forecast import save_raw_synopsis
from etl.extract.extract_daily_weather_forecast import parse_tropical_cyclone_information
from etl.extract.extract_daily_weather_forecast import save_raw_tropical_cyclone_information
from etl.extract.extract_daily_weather_forecast import parse_forecast_weather_conditions
from etl.extract.extract_daily_weather_forecast import save_raw_forecast_weather_conditions
from etl.extract.extract_daily_weather_forecast import parse_forecast_wind_and_coastal_water_conditions
from etl.extract.extract_daily_weather_forecast import save_raw_forecast_wind_and_coastal_water_conditions
from etl.extract.extract_daily_weather_forecast import parse_temperature_and_relative_humidity
from etl.extract.extract_daily_weather_forecast import save_raw_temperature_and_relative_humidity

def extract_daily_weather_forecast(
) -> None:
    """
    Extract the daily weather forecast from the `data/raw/daily_weather_forecast/`
    subdirectory on the local machine.

    This function executes all extraction functions in the
    `extract_daily_weather_forecast` module of the `src.etl.extract`
    package.
    """
    # Run all functions to extract daily weather forecast data
    create_subdir()

    issued_datetime_dataframe = parse_issued_datetime(
        'data/raw/daily_weather_forecast/issued_datetime.json'
    )
    save_raw_issued_datetime(
        issued_datetime_dataframe
    )

    synopsis_dataframe = parse_synopsis(
        'data/raw/daily_weather_forecast/synopsis.json'
    )
    save_raw_synopsis(
        synopsis_dataframe
    )

    tropical_cyclone_information_dataframe = parse_tropical_cyclone_information(

        'data/raw/daily_weather_forecast/tropical_cyclone_information.json'
    )
    save_raw_tropical_cyclone_information(
        tropical_cyclone_information_dataframe
    )

    forecast_weather_conditions_dataframe = parse_forecast_weather_conditions(
        'data/raw/daily_weather_forecast/forecast_weather_conditions.json'
    )
    save_raw_forecast_weather_conditions(
        forecast_weather_conditions_dataframe
    )

    forecast_wind_and_coastal_water_conditions_dataframe = parse_forecast_wind_and_coastal_water_conditions(
        'data/raw/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.json'
    )
    save_raw_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions_dataframe
    )

    temperature_and_relative_humidity_dataframe = parse_temperature_and_relative_humidity(
        'data/raw/daily_weather_forecast/temperature_and_relative_humidity.json'
    )
    save_raw_temperature_and_relative_humidity(
        temperature_and_relative_humidity_dataframe
    )