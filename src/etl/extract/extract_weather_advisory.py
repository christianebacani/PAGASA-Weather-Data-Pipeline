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