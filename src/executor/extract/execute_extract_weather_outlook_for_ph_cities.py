"""
Execute extraction functions for weather outlook for
selected Philippine cities data.

This module runs all extraction tasks on files located in the `data/raw/weather_outlook_for_ph_cities`
subdirectory on the local machine, serving as the entry point for the
daily extraction workflow.
"""
from etl.extract.extract_weather_outlook_for_ph_cities import create_subdir
from etl.extract.extract_weather_outlook_for_ph_cities import parse_issued_datetime_to_dataframe
from etl.extract.extract_weather_outlook_for_ph_cities import stage_issued_datetime_dataframe
from etl.extract.extract_weather_outlook_for_ph_cities import parse_valid_period_to_dataframe
from etl.extract.extract_weather_outlook_for_ph_cities import stage_valid_period_dataframe
from etl.extract.extract_weather_outlook_for_ph_cities import parse_ph_cities_weather_outlook_to_dataframe
from etl.extract.extract_weather_outlook_for_ph_cities import stage_ph_cities_weather_outlook_dataframe

def extract_weather_outlook_for_ph_cities(
) -> None:
    """
    Extract the weather outlook for selected
    Philippine cities from the `data/raw/weather_outlook_for_ph_tourist_cities`
    subdirectory on the local machine.

    This function executes all extraction functions in the
    `extract_weather_outlook_for_ph_cities` module of the `src.etl.extract`
    package.
    """
    # Run all functions to extract weather outlook data for selected Philippine cities
    create_subdir()

    issued_datetime_dataframe = parse_issued_datetime_to_dataframe(
        'data/raw/weather_outlook_for_ph_cities/issued_datetime.json'
    )
    stage_issued_datetime_dataframe(
        issued_datetime_dataframe
    )

    valid_period_dataframe = parse_valid_period_to_dataframe(
        'data/raw/weather_outlook_for_ph_cities/valid_period.json'
    )
    stage_valid_period_dataframe(
        valid_period_dataframe
    )

    ph_cities_weather_outlook_dataframe = parse_ph_cities_weather_outlook_to_dataframe(
        'data/raw/weather_outlook_for_ph_cities/ph_cities_weather_outlook.json'
    )
    stage_ph_cities_weather_outlook_dataframe(
        ph_cities_weather_outlook_dataframe
    )