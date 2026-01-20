"""
Execute ingest workflow for tropical cyclone bulletin data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_tropical_cyclone_bulletin` to ingest
artifacts and store them as a JSON files under `data/raw/tropical_cyclone_bulletins/` subdirectory
for further processing.

Main function:
- `ingest_tropical_cyclone_bulletin` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_tropical_cyclone_bulletin import create_subdir
from ingest.ingest_tropical_cyclone_bulletin import ingest_and_parse_soup_from_url
from ingest.ingest_tropical_cyclone_bulletin import ingest_tropical_cyclone_name
from ingest.ingest_tropical_cyclone_bulletin import save_ingested_tropical_cyclone_name
from ingest.ingest_tropical_cyclone_bulletin import ingest_issued_datetime
from ingest.ingest_tropical_cyclone_bulletin import save_ingested_issued_datetime
from ingest.ingest_tropical_cyclone_bulletin import ingest_time_validity
from ingest.ingest_tropical_cyclone_bulletin import save_ingested_time_validity
from ingest.ingest_tropical_cyclone_bulletin import ingest_tropical_cyclone_summary

def ingest_tropical_cyclone_bulletin(
) -> None:
    """
    Executes the function in the
    `src.ingest_tropical_cyclone_bulletin.py`
    module to ingest the data from the tropical cyclone
    bulletin page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/tropical-cyclone/severe-weather-bulletin'
    )

    tropical_cyclone_name = ingest_tropical_cyclone_name(
        soup
    )
    save_ingested_tropical_cyclone_name(
        tropical_cyclone_name
    )

    issued_datetime = ingest_issued_datetime(
        soup
    )
    save_ingested_issued_datetime(
        issued_datetime
    )

    time_validity = ingest_time_validity(
        soup
    )
    save_ingested_time_validity(
        time_validity
    )

    tropical_cyclone_summary = ingest_tropical_cyclone_summary(
        soup
    )