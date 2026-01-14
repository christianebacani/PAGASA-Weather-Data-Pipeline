"""
Docstring for executor.ingest.execute_ingest_weather_outlooks_for_ph_tourist_areas
"""
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import create_subdir
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_and_parse_from_url
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import save_ingested_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_time_validities
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import save_ingested_time_validities
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_ph_tourist_area_names
from ingest.ingest_weather_outlooks_for_ph_tourist_areas import ingest_weather_dates

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
    soup = ingest_and_parse_from_url(
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

    ingest_ph_tourist_area_names(
        soup        
    )

    list_of_all_weather_dates = ingest_weather_dates(
        soup
    )