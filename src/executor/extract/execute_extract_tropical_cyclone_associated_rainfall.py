"""
Execute extraction functions for tropical cyclone associated rainfall data

This module runs all extraction tasks on files located in the `data/raw/tropical_cyclone_associated_rainfall`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""
from etl.extract.extract_tropical_cyclone_associated_rainfall import create_subdir
from etl.extract.extract_tropical_cyclone_associated_rainfall import parse_tc_assoc_rainfall_image_sources_to_dataframe

def extract_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Extract the tropical cyclone associated rainfall from the
    `data/raw/tropical_cyclone_associated_rainfall` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_tropical_cyclone_associated_rainfall` module of the 
    `src.etl.extract` package.
    """
    # Run all functions to extract tropical cyclone associated rainfall data
    create_subdir()

    tc_assoc_rainfall_image_sources_of_2025_dataframe = parse_tc_assoc_rainfall_image_sources_to_dataframe(
        'data/raw/tropical_cyclone_associated_rainfall/tc_associated_rainfall_image_sources_of_2025.json'
    )