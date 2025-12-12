"""
Execute extraction functions for tropical cyclone advisory data

This module runs all extraction tasks on files located in the `data/raw/tropical_cyclone_advisory`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""
from etl.extract.extract_tropical_cyclone_advisory import create_subdir

def extract_tropical_cyclone_advisory(
) -> None:
    """
    Extract the tropical cyclone advisory from the
    `data/raw/tropical_cyclone_advisory` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_tropical_cyclone_advisory` module of the `src.etl.extract`
    package.
    """
    # Run all functions to extract tropical cyclone advisory data
    create_subdir()