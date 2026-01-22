"""
Execute ingest workflow for weather advisory data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_weather_advisory` to ingest
artifacts and store them as a JSON files under `data/weather_advisories/` subdirectory
for further processing.

Main function:
- `ingest_weather_advisory` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_weather_advisory import create_subdir
from ingest.ingest_weather_advisory import ingest_and_parse_soup_from_url

def ingest_weather_advisory(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_weather_advisory.py`
    module to ingest the data from the weather advisory
    page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/weather/weather-advisory'
    )