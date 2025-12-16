"""
Extract weather advisory from the `data/raw/weather_advisory` subdirectory
on the local machine.

This module provides functions to parse JSON files from the
`data/raw/weather_advisory` subdirectory and convert them into structured DataFrame
objects, including:

- Weather advisory source URL or content

Parsed DataFrames are saved as CSV files in the
`data/stage/weather_advisory/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/weather_advisory` subdirectory to store CSV files.

    This subdirectory stores the weather advisory, data parsed from JSON files located
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
    # Read the weather advisory JSON file as a DataFrame object
    weather_advisory_dataframe = pd.read_json(weather_advisory_filepath)

    # Rename the columns of the DataFrame object
    weather_advisory_dataframe.rename(columns={
        'weather_advisory': 'weather_advisory_document_sources'
    }, inplace=True)

    return weather_advisory_dataframe