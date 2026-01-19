"""
Execute ingest workflow for weather outlooks for selected Philippine tourist areas data from
the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_weather_outlooks_for_ph_tourist_areas` to
ingest artifacts and store them as JSON files under `data/raw/weather_outlooks_for_ph_tourist_areas/`
subdirectory for further processing.

Main function:
- `ingest_weather_outlooks_for_ph_tourist_areas` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import create_subdir
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_and_parse_soup_from_url
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import save_ingested_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_time_validities
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import save_ingested_time_validities
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_ph_tourist_area_names
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_weather_dates
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import map_ph_tourist_area_names_to_weather_dates
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_temperature_ranges
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import map_ph_tourist_area_names_to_temperature_ranges
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import save_ingested_weather_outlooks_for_ph_tourist_areas

def ingest_weather_outlooks_for_ph_tourist_areas(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_weather_outlooks_for_ph_tourist_areas.py`
    module to ingest the data from the weather outlooks
    for selected Philippine tourist areas page of PAGASA-DOST
    website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/weather/weather-outlook-selected-tourist-areas'
    )

    issued_datetime = ingest_issued_datetimes(
        soup
    )
    save_ingested_issued_datetimes(
        issued_datetime
    )

    time_validity = ingest_time_validities(
        soup
    )
    save_ingested_time_validities(
        time_validity
    )

    ph_tourist_area_names_dict = ingest_ph_tourist_area_names(
        soup        
    )

    list_of_all_weather_dates = ingest_weather_dates(
        soup
    )
    ph_tourist_area_names_with_weather_dates = map_ph_tourist_area_names_to_weather_dates(
        ph_tourist_area_names_dict,
        list_of_all_weather_dates
    )

    list_of_all_temperature_ranges = ingest_temperature_ranges(
        soup
    )
    weather_outlooks_for_ph_tourist_areas = map_ph_tourist_area_names_to_temperature_ranges(
        ph_tourist_area_names_with_weather_dates,
        list_of_all_temperature_ranges
    )

    save_ingested_weather_outlooks_for_ph_tourist_areas(
        weather_outlooks_for_ph_tourist_areas
    )