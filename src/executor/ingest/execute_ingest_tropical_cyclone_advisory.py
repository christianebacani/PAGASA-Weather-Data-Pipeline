"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_tropical_cyclone_advisory` module of the `src.ingest` package.
"""
from ingest.ingest_tropical_cyclone_advisory import create_subdir
from ingest.ingest_tropical_cyclone_advisory import extract_beautiful_soup_object

def ingest_tropical_cyclone_advisory(
) -> None:
    """
    Ingest tropical cyclone advisory data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_tropical_cyclone_advisory` module of the `src.ingest` package.
    """
    # Run all functions to ingest tropical cyclone advisory data
    create_subdir()
    soup = extract_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/tropical-cyclone-advisory-iframe'
    )