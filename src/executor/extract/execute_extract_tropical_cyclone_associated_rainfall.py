"""
Execute extraction functions for tropical cyclone associated rainfall data

This module runs all extraction tasks on files located in the `data/raw/tropical_cyclone_associated_rainfall`
subdirectory on the local machine, serving as the entry point for the daily extraction workflow.
"""

def extract_tropical_cyclone_associated_rainfall(
) -> None:
    """
    Extract the tropical cyclone associated rainfall from the
    `data/raw/tropical_cyclone_associated_rainfall` subdirectory
    on the local machine.

    This function executes all extraction functions in the
    `extract_tropical_cyclone_associated_rainfall` module of the 
    `src.etl.extract` package.
    """