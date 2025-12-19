"""
Execute transformation functions for daily weather forecast data

This module runs all transformation tasks on files located in the `data/stage/daily_weather_forecast`
subdirectory on the local machine, serving as the entry point for the daily transformation workflow.
"""
import pandas as pd

def transform_daily_weather_forecast(
) -> None:
    """
    Transform the daily weather forecast from the
    `data/stage/daily_weather_forecast` subdirectory
    on the local machine.

    This function executes all transformation functions
    in the `transform_daily_weather_forecast` module of the
    `src.etl.transform` package.
    """
    # Run all functions to extract tropical cyclone associated rainfall data