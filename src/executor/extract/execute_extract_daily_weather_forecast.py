'''
    Module for executing extraction functions for the
    daily weather forecast data from the data/raw
    subdirectory on the local machine.
'''
from etl.extract.extract_daily_weather_forecast import create_subdir
from etl.extract.extract_daily_weather_forecast import parse_issued_datetime_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_issued_datetime_dataframe
from etl.extract.extract_daily_weather_forecast import parse_synopsis_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_synopsis_dataframe
from etl.extract.extract_daily_weather_forecast import parse_tc_information_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_tc_information_dataframe
from etl.extract.extract_daily_weather_forecast import parse_forecast_weather_conditions_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_forecast_weather_conditions_dataframe
from etl.extract.extract_daily_weather_forecast import parse_forecast_wind_and_coastal_water_conditions_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_forecast_wind_and_coastal_water_conditions_dataframe
from etl.extract.extract_daily_weather_forecast import parse_temperature_and_relative_humidity_to_dataframe
from etl.extract.extract_daily_weather_forecast import stage_temperature_and_relative_humidity_dataframe

def extract_daily_weather_forecast(
) -> None:
    '''
        Extracts the daily weather forecast from the
        data/raw subdirectory on the local machine
        by executing all functions in the
        extract_daily_weather_forecast module
        of the src/ingest package.    
    '''
    # Run all functions to ingest weather advisory data
    create_subdir()

    issued_datetime_dataframe = parse_issued_datetime_to_dataframe(
        'data/raw/daily_weather_forecast/issued_datetime.json'
    )
    stage_issued_datetime_dataframe(
        issued_datetime_dataframe
    )

    synopsis_dataframe = parse_synopsis_to_dataframe(
        'data/raw/daily_weather_forecast/synopsis.json'
    )
    stage_synopsis_dataframe(
        synopsis_dataframe
    )

    tc_information_dataframe = parse_tc_information_to_dataframe(
        'data/raw/daily_weather_forecast/tropical_cyclone_information.json'
    )
    stage_tc_information_dataframe(
        tc_information_dataframe
    )

    forecast_weather_conditions_dataframe = parse_forecast_weather_conditions_to_dataframe(
        'data/raw/daily_weather_forecast/forecast_weather_conditions.json'
    )
    stage_forecast_weather_conditions_dataframe(
        forecast_weather_conditions_dataframe
    )

    forecast_wind_and_coastal_water_conditions_dataframe = parse_forecast_wind_and_coastal_water_conditions_to_dataframe(
        'data/raw/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.json'
    )
    stage_forecast_wind_and_coastal_water_conditions_dataframe(
        forecast_wind_and_coastal_water_conditions_dataframe
    )

    temperature_and_relative_humidity_dataframe = parse_temperature_and_relative_humidity_to_dataframe(
        'data/raw/daily_weather_forecast/temperature_and_relative_humidity.json'
    )
    stage_temperature_and_relative_humidity_dataframe(
        temperature_and_relative_humidity_dataframe
    )