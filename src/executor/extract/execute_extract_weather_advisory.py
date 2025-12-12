"""
Execute extraction functions for weather advisory data

This module runs all extraction tasks on files located in the `data/raw/weather_advisory`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""
from etl.extract.extract_weather_advisory import create_subdir

def extract_weather_advisory(
) -> None:
    """
    Extract the weather advisory from the
    `data/raw/weather_advisory` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_weather_advisory` module of the `src.etl.extract`
    package.
    """
    # Run all functiosn to extract weather advisory data
    create_subdir()