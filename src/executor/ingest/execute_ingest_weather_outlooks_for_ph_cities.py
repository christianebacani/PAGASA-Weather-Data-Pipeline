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
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_ph_city_names
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_weather_dates
from ingest.ingest_weather_outlooks_for_ph_cities import map_ph_city_names_to_weather_dates
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_temperature_ranges
from ingest.ingest_weather_outlooks_for_ph_cities import map_ph_city_names_to_temperature_ranges
from ingest.ingest_weather_outlooks_for_ph_cities import ingest_chance_of_rain_percentages

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

    ph_city_names_dict = ingest_ph_city_names(
        list_of_all_ph_city_tags
    )

    list_of_all_weather_dates = ingest_weather_dates(
        list_of_all_ph_city_tags
    )
    ph_city_names_with_weather_dates = map_ph_city_names_to_weather_dates(
        ph_city_names_dict,
        list_of_all_weather_dates
    )

    list_of_all_temperature_ranges = ingest_temperature_ranges(
        list_of_all_ph_city_tags
    )
    weather_outlooks_for_ph_cities = map_ph_city_names_to_temperature_ranges(
        ph_city_names_with_weather_dates,
        list_of_all_temperature_ranges   
    )

    list_of_all_chance_of_rain_percentages = ingest_chance_of_rain_percentages(
        list_of_all_ph_city_tags
    )