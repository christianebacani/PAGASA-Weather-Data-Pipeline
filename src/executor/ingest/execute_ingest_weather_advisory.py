"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_weather_advisory` module of the `src.ingest` package.
"""
from ingest.ingest_weather_advisory import create_subdir
from ingest.ingest_weather_advisory import ingest_beautiful_soup_object
from ingest.ingest_weather_advisory import ingest_weather_advisory_document_source
from ingest.ingest_weather_advisory import save_weather_advisory_document_source_to_raw_subdir

def ingest_weather_advisory(
) -> None:
    """
    Ingest weather advisory data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_weather_advisory` module of the `src.ingest` package.
    """
    # Run all functions to ingest weather advisory data
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/weather/weather-advisory'
    )

    weather_advisory_document_source = ingest_weather_advisory_document_source(
        soup
    )
    save_weather_advisory_document_source_to_raw_subdir(
        weather_advisory_document_source
    )