"""
Execute ingest workflow for weather advisories data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_weather_advisories` to ingest
artifacts and store them as a JSON files under `data/raw/weather_advisories/` subdirectory
for further processing.

Main function:
- `ingest_weather_advisories` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_weather_advisories import create_subdir

def ingest_weather_advisories(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_weather_advisories.py`
    module to ingest the data from the weather advisories
    page of PAGASA-DOST website.
    """
    create_subdir()