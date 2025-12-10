"""
Extract and stage weather outlook for selected Philippine tourist areas from the 
`data/raw/weather_outlook_for_ph_tourist_areas` subdirectory on the local machine.

This module provides functions to parse JSON files from the
`data/raw/weather_outlook_for_ph_tourist_areas` subdirectory and convert them into structured DataFrame
objects, including:

- Issued datetime
- Valid period
- Weather outlook for selected Philippine tourist areas

Parsed DataFrames are staged as CSV files in the
`data/stage/weather_outlook_for_ph_tourist_areas/` subdirectory
on the local machine for further processing.
"""