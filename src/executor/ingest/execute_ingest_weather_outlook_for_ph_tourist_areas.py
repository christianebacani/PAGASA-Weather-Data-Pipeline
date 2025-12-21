"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_weather_outlook_for_ph_tourist_areas` module of the `src.ingest`
package.
"""
from ingest.ingest_weather_outlook_for_ph_tourist_areas import create_subdir
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_beautiful_soup_object
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_issued_datetime
from ingest.ingest_weather_outlook_for_ph_tourist_areas import save_ingested_issued_datetime
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_valid_period
from ingest.ingest_weather_outlook_for_ph_tourist_areas import save_ingested_valid_period
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_ph_tourist_area_tags
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_ph_tourist_area_names
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_weather_dates
from ingest.ingest_weather_outlook_for_ph_tourist_areas import map_weather_dates_to_ph_tourist_areas
from ingest.ingest_weather_outlook_for_ph_tourist_areas import ingest_temperature_ranges
from ingest.ingest_weather_outlook_for_ph_tourist_areas import map_temperature_ranges_to_ph_tourist_areas
from ingest.ingest_weather_outlook_for_ph_tourist_areas import save_ingested_ph_tourist_areas_weather_outlook

def ingest_weather_outlook_for_ph_tourist_areas(
) -> None:
    """
    Ingest weather outlook for selected Philippine tourist areas data from the PAGASA-DOST
    website.

    This function executes all ingestion functions defined in th
    `ingest_weather_outlook_for_ph_tourist_areas` module of the `src.ingest` package.
    """
    # Run all functions to ingest weather outlook data for selected Philippine tourist areas
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/weather/weather-outlook-selected-tourist-areas'
    )

    issued_datetime = ingest_issued_datetime(
        soup
    )
    save_ingested_issued_datetime(
        issued_datetime
    )

    valid_period = ingest_valid_period(
        soup
    )
    save_ingested_valid_period(
        valid_period
    )

    list_of_all_ph_tourist_area_tags = ingest_ph_tourist_area_tags(
        soup
    )
    ph_tourist_area_names = ingest_ph_tourist_area_names(
        list_of_all_ph_tourist_area_tags
    )

    weather_dates = ingest_weather_dates(
        soup
    )
    ph_tourist_areas_with_weather_dates = map_weather_dates_to_ph_tourist_areas(
        weather_dates,
        ph_tourist_area_names
    )

    temperature_ranges = ingest_temperature_ranges(
        list_of_all_ph_tourist_area_tags
    )
    ph_tourist_areas_weather_outlook = map_temperature_ranges_to_ph_tourist_areas(
        temperature_ranges,
        ph_tourist_areas_with_weather_dates
    )

    save_ingested_ph_tourist_areas_weather_outlook(
        ph_tourist_areas_weather_outlook
    )