"""
Execute extraction functions for tropical cyclone associated rainfall data

This module runs all extraction tasks on files located in the `data/raw/tropical_cyclone_associated_rainfall/`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""
from etl.extract.extract_tropical_cyclone_associated_rainfall import create_subdir
from etl.extract.extract_tropical_cyclone_associated_rainfall import parse_tc_assoc_rainfall_image_sources
from etl.extract.extract_tropical_cyclone_associated_rainfall import save_raw_tc_assoc_rainfall_image_sources

def extract_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Extract the tropical cyclone associated rainfall from the
    `data/raw/tropical_cyclone_associated_rainfall/` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_tropical_cyclone_associated_rainfall` module of the 
    `src.etl.extract` package.
    """
    # Run all functions to extract tropical cyclone associated rainfall data
    create_subdir()

    tc_assoc_rainfall_image_sources_of_2025_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2025.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2025_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2024_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2024.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2024_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2023_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2023.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2023_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2022_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2022.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2022_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2021_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2021.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2021_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2020_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2020.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2020_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2019_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2019.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2019_dataframe
    )

    tc_assoc_rainfall_image_sources_of_2018_dataframe = parse_tc_assoc_rainfall_image_sources(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2018.json'
    )
    save_raw_tc_assoc_rainfall_image_sources(
        tc_assoc_rainfall_image_sources_of_2018_dataframe
    )