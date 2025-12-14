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
        tc_assoc_rainfall_image_sources_filepath: str
) -> pd.DataFrame:
    """
    Parse the tropical cyclone associated rainfall image sources
    into a DataFrame.

    :param tc_assoc_rainfall_image_sources_filepath: Relative
        filepath of the JSON file that stores the tropical
        cyclone associated rainfall image sources
    :type tc_assoc_rainfall_image_sources_filepath: str

    :return: DataFrame containing the tropical cyclone associated
        rainfall image sources
    :rtype: DataFrame
    """
    # Read the tc associated rainfall image sources JSON file as a DataFrame object
    tc_assoc_rainfall_image_sources_dataframe = pd.read_json(
        tc_assoc_rainfall_image_sources_filepath
    )

    return tc_assoc_rainfall_image_sources_dataframe

def stage_tc_assoc_rainfall_image_sources_dataframe(
        tc_assoc_rainfall_image_sources_dataframe: pd.DataFrame
) -> None:
    """
    Stage the tropical cyclone associated rainfall image sources
    DataFrame to the staging directory for further processing.

    :param tc_assoc_rainfall_image_sources_dataframe: DataFrame
        containing the tropical cyclone associated rainfall image
        sources
    :type tc_assoc_rainfall_image_sources_dataframe: pd.DataFrame
    """
    filename = list(tc_assoc_rainfall_image_sources_dataframe.keys())[0]

    # Stage the tc associated rainfall image sources DataFrame object to the target filepath
    target_filepath = f'data/stage/weather_outlook_for_ph_tourist_areas/{filename}.csv'
    tc_assoc_rainfall_image_sources_dataframe.to_csv(target_filepath, index=False)