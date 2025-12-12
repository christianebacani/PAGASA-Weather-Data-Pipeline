"""
Extract and stage tropical cyclone advisory from the `data/raw/tropical_cyclone_advisory`
subdirectory on the local machine.

This module provides functions to parse JSON files from the
`data/raw/tropical_cyclone_advisory` subdirectory and convert them into structured DataFrame
objects, including:

- TBD

Parsed DataFrames are staged as CSV files in the
`data/stage/tropical_cyclone_advisory/` subdirectory
on the local machine for further processing.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/stage/tropical_cyclone_advisory` subdirectory to store CSV files.

    This subdirectory stores the tropical cyclone advisory data parsed from JSON files
    located in the `data/raw/tropical_cyclone_advisory` subdirectory on the local machine.
    """
    # Create the data/stage/tropical_cyclone_advisory/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/tropical_cyclone_advisory'):
        os.makedirs('data/stage/tropical_cyclone_advisory')