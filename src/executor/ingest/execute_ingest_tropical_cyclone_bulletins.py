"""
Execute ingest workflow for tropical cyclone bulletins data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_tropical_cyclone_bulletins` to ingest
artifacts and store them as a JSON files under `data/raw/tropical_cyclone_bulletins/` subdirectory
for further processing.

Main function:
- `ingest_tropical_cyclone_bulletins` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_tropical_cyclone_bulletins import create_subdir
from ingest.ingest_tropical_cyclone_bulletins import ingest_and_parse_soup_from_url
from ingest.ingest_tropical_cyclone_bulletins import ingest_tropical_cyclone_names
from ingest.ingest_tropical_cyclone_bulletins import save_ingested_tropical_cyclone_names
from ingest.ingest_tropical_cyclone_bulletins import ingest_issued_datetimes
from ingest.ingest_tropical_cyclone_bulletins import save_ingested_issued_datetimes
from ingest.ingest_tropical_cyclone_bulletins import ingest_time_validities
from ingest.ingest_tropical_cyclone_bulletins import save_ingested_time_validities

def ingest_tropical_cyclone_bulletins(
) -> None:
    """
    Executes the function in the
    `src.ingest_tropical_cyclone_bulletins.py`
    module to ingest the data from the tropical cyclone
    bulletins page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/tropical-cyclone/severe-weather-bulletin'
    )

    tropical_cyclone_name = ingest_tropical_cyclone_names(
        soup
    )
    save_ingested_tropical_cyclone_names(
        tropical_cyclone_name
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