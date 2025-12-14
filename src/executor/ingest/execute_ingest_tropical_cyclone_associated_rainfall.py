"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_tropical_cyclone_associated_rainfall` module of the
`src.ingest` package.
"""
from ingest.ingest_tropical_cyclone_associated_rainfall import create_subdir
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_beautiful_soup_object
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_tc_assoc_rainfall_tag
from ingest.ingest_tropical_cyclone_associated_rainfall import extract_tc_assoc_rainfall_image_sources

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

    tc_assoc_rainfall_tag = extract_tc_assoc_rainfall_tag(soup)

    tc_assoc_rainfall_image_sources_2025 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2025
    )
    tc_assoc_rainfall_image_sources_2024 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2024
    )
    tc_assoc_rainfall_image_sources_2023 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2023
    )
    tc_assoc_rainfall_image_sources_2022 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2022
    )
    tc_assoc_rainfall_image_sources_2021 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2021
    )
    tc_assoc_rainfall_image_sources_2020 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2020
    )
    tc_assoc_rainfall_image_sources_2019 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2019
    )
    tc_assoc_rainfall_image_sources_2018 = extract_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2018
    )