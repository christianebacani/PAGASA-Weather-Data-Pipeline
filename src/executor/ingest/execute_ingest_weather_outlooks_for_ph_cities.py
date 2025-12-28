"""
Docstring for executor.ingest.execute_ingest_weather_outlooks_for_ph_cities
"""
from ingest.ingest_weather_outlooks_for_ph_cities import create_subdir
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_and_parse_from_url
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_cities import save_ingested_issued_datetimes
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_time_validities
from ingest.ingest_weather_outlooks_for_ph_cities import save_ingested_time_validities
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_and_parse_list_of_all_ph_city_tags

def ingest_weather_outlooks_for_ph_cities(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_weather_outlooks_for_ph_cities.py`
    module to ingest the data from the weather outlooks
    for selected Philippine cities page of PAGASA-DOST
    website.
    """
    create_subdir()
    soup = ingest_and_parse_from_url(
        'https://www.pagasa.dost.gov.ph/weather/weather-outlook-selected-philippine-cities'
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

    list_of_all_ph_city_tags = ingest_and_parse_list_of_all_ph_city_tags(
        soup
    )