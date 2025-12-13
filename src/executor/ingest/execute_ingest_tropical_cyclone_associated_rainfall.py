"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_tropical_cyclone_associated_rainfall` module of the
`src.ingest` package.
"""
from ingest.ingest_tropical_cyclone_associated_rainfall import create_subdir
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_beautiful_soup_object
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_tc_associated_rainfalls_of_2025_tags
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_tc_associated_rainfalls_of_2025

def ingest_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Ingest tropical cyclone-associated rainfall data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_tropical_cyclone_associated_rainfall` module of the `src.ingest` package.
    """
    # Run all functions to ingest tropical cyclone associated rainfall data
    create_subdir()
    soup = extract_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/climate/tropical-cyclone-associated-rainfall'
    )

    tc_associated_rainfalls_of_2025_tags = extract_tc_associated_rainfalls_of_2025_tags(
        soup
    )
    tc_associated_rainfalls_of_2025 = extract_tc_associated_rainfalls_of_2025(
        tc_associated_rainfalls_of_2025_tags
    )