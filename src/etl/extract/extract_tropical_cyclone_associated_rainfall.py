"""
Extract and stage tropical cyclone associated rainfall from the `data/raw/tropical_cyclone_associated_rainfall`
subdirectory on the local machine.

This module provides functions to parse JSON files from the
`data/raw/tropical_cyclone_associated_rainfall` subdirectory and convert them into structured DataFrame
objects, including:

- Tropical cyclone associated rainfall image source

Parsed DataFrames are staged as CSV files in the
`data/stage/tropical_cyclone_associated_rainfall/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/tropical_cyclone_associated_rainfall` subdirectory to store CSV files.

    This subdirectory stores the tropical cyclone associated rainfall data parsed from JSON files
    located in the `data/raw/tropical_cyclone_associated_rainfall` subdirectory on the local machine.
    """
    # Create the data/stage/tropical_cyclone_associated_rainfall/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/tropical_cyclone_associated_rainfall'):
        os.makedirs('data/stage/tropical_cyclone_associated_rainfall')

def parse_tc_assoc_rainfall_image_sources_to_dataframe(
        tc_assoc_rainfall_image_sources_filepath: str,
        year: int
) -> pd.DataFrame:
    """
    Docstring for parse_tc_assoc_rainfall_image_sources_to_dataframe

    :param tc_assoc_rainfall_image_sources_filepath: Description
    :type tc_assoc_rainfall_image_sources_filepath: str

    :param year: Description
    :type year: int

    :return: Description
    :rtype: DataFrame
    """