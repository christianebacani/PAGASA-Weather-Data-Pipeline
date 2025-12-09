"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_tropical_cyclone_associated_rainfall` module of the
`src.ingest` package.
"""
from ingest.ingest_tropical_cyclone_associated_rainfall import create_subdir
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_beautiful_soup_object
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_tropical_cyclone_associated_rainfall
from ingest.ingest_tropical_cyclone_associated_rainfall import save_tropical_cyclone_associated_rainfall_to_json

def ingest_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Ingest tropical cyclone-associated rainfall data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_tropical_cyclone_associated_rainfall` module of the `src.ingest` package.
    """
    # Run all functions to ingest weather advisory data
    create_subdir()
    soup = extract_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/climate/tropical-cyclone-associated-rainfall'
    )

    tropical_cyclone_associated_rainfall = extract_tropical_cyclone_associated_rainfall(
        soup
    )
    save_tropical_cyclone_associated_rainfall_to_json(
        tropical_cyclone_associated_rainfall
    )