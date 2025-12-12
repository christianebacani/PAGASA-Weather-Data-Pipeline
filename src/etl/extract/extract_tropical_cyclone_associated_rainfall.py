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