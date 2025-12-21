"""
Execute extraction functions for weather outlook for
selected Philippine tourist areas data.

This module runs all extraction tasks on files located in the `data/raw/weather_outlook_for_ph_tourist_areas`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import create_subdir
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import parse_issued_datetime
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import save_raw_issued_datetime
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import parse_valid_period
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import save_raw_valid_period
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import parse_ph_tourist_areas_weather_outlook
from etl.extract.extract_weather_outlook_for_ph_tourist_areas import save_raw_ph_tourist_areas_weather_outlook

def extract_weather_outlook_for_ph_tourist_areas(
) -> None:
    """
    Extract the weather outlook for selected
    Philippine tourist areas from the
    `data/raw/weather_outlook_for_ph_tourist_areas` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_weather_outlook_for_ph_tourist_areas` module of the `src.etl.extract`
    package.
    """
    # Run all functions to extract weather outlook data for selected Philippine tourist areas
    create_subdir()

    issued_datetime_dataframe = parse_issued_datetime(
        'data/raw/weather_outlook_for_ph_tourist_areas/issued_datetime.json'
    )
    save_raw_issued_datetime(
        issued_datetime_dataframe
    )

    valid_period_dataframe = parse_valid_period(
        'data/raw/weather_outlook_for_ph_tourist_areas/valid_period.json'
    )
    save_raw_valid_period(
        valid_period_dataframe
    )

    ph_tourist_areas_weather_outlook_to_dataframe = parse_ph_tourist_areas_weather_outlook(
        'data/raw/weather_outlook_for_ph_tourist_areas/ph_tourist_areas_weather_outlook.json'
    )
    save_raw_ph_tourist_areas_weather_outlook(
        ph_tourist_areas_weather_outlook_to_dataframe
    )