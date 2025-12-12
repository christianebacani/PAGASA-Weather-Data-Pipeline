"""
Extract and stage weather advisory from the `data/raw/weather_advisory` subdirectory
on the local machine.

This module provides functions to parse JSON files from the
`data/raw/weather_advisory` subdirectory and convert them into structured DataFrame
objects, including:

- Weather advisory source URL or content

Parsed DataFrames are staged as CSV files in the
`data/stage/weather_advisory/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/weather_advisory` subdirectory to store CSV files.

    This subdirectory stores the weather advisory data parsed from JSON files located
    in the `data/raw/weather_advisory` subdirectory on the local machine.
    """
    # Create the data/stage/weather_advisory/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/weather_advisory'):
        os.makedirs('data/stage/weather_advisory')

def parse_weather_advisory_to_dataframe(
        weather_advisory_filepath: str
) -> pd.DataFrame:
    """
    Parse the weather advisory into a DataFrame.

    :param weather_advisory_filepath: Relative filepath of the JSON file that
        stores the weather advisory
    :type weather_advisory_filepath: str

    :return: DataFrame containing the weather advisory
    :rtype: DataFrame
    """