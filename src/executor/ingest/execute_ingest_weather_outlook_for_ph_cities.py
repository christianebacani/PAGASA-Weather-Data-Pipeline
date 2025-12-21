"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_weather_outlook_for_ph_cities` module of the `src.ingest`
package.
"""
from ingest.ingest_weather_outlook_for_ph_cities import create_subdir
from ingest.ingest_weather_outlook_for_ph_cities import ingest_beautiful_soup_object
from ingest.ingest_weather_outlook_for_ph_cities import ingest_issued_datetime
from ingest.ingest_weather_outlook_for_ph_cities import save_ingested_issued_datetime
from ingest.ingest_weather_outlook_for_ph_cities import ingest_valid_period
from ingest.ingest_weather_outlook_for_ph_cities import save_ingested_valid_period
from ingest.ingest_weather_outlook_for_ph_cities import ingest_ph_city_tags
from ingest.ingest_weather_outlook_for_ph_cities import ingest_ph_city_names
from ingest.ingest_weather_outlook_for_ph_cities import ingest_weather_dates
from ingest.ingest_weather_outlook_for_ph_cities import map_weather_dates_to_ph_cities
from ingest.ingest_weather_outlook_for_ph_cities import ingest_temperature_ranges
from ingest.ingest_weather_outlook_for_ph_cities import map_temperature_ranges_to_ph_cities
from ingest.ingest_weather_outlook_for_ph_cities import ingest_chance_of_rain_percentages
from ingest.ingest_weather_outlook_for_ph_cities import map_chance_of_rain_percentages_to_ph_cities
from ingest.ingest_weather_outlook_for_ph_cities import save_ingested_ph_cities_weather_outlook

def ingest_weather_outlook_for_ph_cities(
) -> None:
    """
    Ingest weather outlook for selected Philippine cities data from the PAGASA-DOST
    website.

    This function executes all ingestion functions defined in the
    `ingest_weather_outlook_for_ph_cities` module of the `src.ingest` package.
    """
    # Run all functions to ingest weather outlook data for selected Philippine cities
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/weather/weather-outlook-selected-philippine-cities'
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

    list_of_all_ph_city_tags = ingest_ph_city_tags(
        soup
    )
    ph_city_names = ingest_ph_city_names(
        list_of_all_ph_city_tags
    )

    weather_dates = ingest_weather_dates(
        list_of_all_ph_city_tags
    )
    ph_cities_with_weather_dates = map_weather_dates_to_ph_cities(
        weather_dates,
        ph_city_names
    )

    temperature_ranges = ingest_temperature_ranges(
        list_of_all_ph_city_tags
    )
    ph_cities_weather_outlook = map_temperature_ranges_to_ph_cities(
        temperature_ranges,
        ph_cities_with_weather_dates
    )

    chance_of_rain_percentages = ingest_chance_of_rain_percentages(list_of_all_ph_city_tags)
    ph_cities_weather_outlook = map_chance_of_rain_percentages_to_ph_cities(
        chance_of_rain_percentages,
        ph_cities_weather_outlook
    )

    save_ingested_ph_cities_weather_outlook(
        ph_cities_weather_outlook
    )