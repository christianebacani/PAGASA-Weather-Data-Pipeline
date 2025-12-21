"""
Provide an executor function for data ingestion operations.

This module executes ingestion functions in the
`ingest_tropical_cyclone_associated_rainfall` module of the
`src.ingest` package.
"""
from ingest.ingest_tropical_cyclone_associated_rainfall import create_subdir
from ingest.ingest_tropical_cyclone_associated_rainfall import ingest_beautiful_soup_object
from ingest.ingest_tropical_cyclone_associated_rainfall import ingest_tc_assoc_rainfall_tag
from ingest.ingest_tropical_cyclone_associated_rainfall import ingest_tc_assoc_rainfall_image_sources
from ingest.ingest_tropical_cyclone_associated_rainfall import save_ingested_tc_assoc_rainfall_image_sources

def ingest_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Ingest tropical cyclone-associated rainfall data from the PAGASA-DOST website.

    This function executes all ingestion functions defined in the
    `ingest_tropical_cyclone_associated_rainfall` module of the `src.ingest` package.
    """
    # Run all functions to ingest tropical cyclone associated rainfall data
    create_subdir()
    soup = ingest_beautiful_soup_object(
        'https://www.pagasa.dost.gov.ph/climate/tropical-cyclone-associated-rainfall'
    )

    tc_assoc_rainfall_tag = ingest_tc_assoc_rainfall_tag(
        soup
    )

    tc_assoc_rainfall_image_sources_2025 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2025
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2025,
        2025
    )

    tc_assoc_rainfall_image_sources_2024 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2024
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2024,
        2024
    )

    tc_assoc_rainfall_image_sources_2023 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2023
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2023,
        2023
    )

    tc_assoc_rainfall_image_sources_2022 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2022
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2022,
        2022
    )

    tc_assoc_rainfall_image_sources_2021 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2021
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2021,
        2021
    )

    tc_assoc_rainfall_image_sources_2020 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2020
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2020,
        2020
    )

    tc_assoc_rainfall_image_sources_2019 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2019
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2019,
        2019
    )

    tc_assoc_rainfall_image_sources_2018 = ingest_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_tag,
        2018
    )
    save_ingested_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_2018,
        2018
    )