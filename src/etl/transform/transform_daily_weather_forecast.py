"""
Transform staged daily weather forecast data from the
`data/stage/daily_weather_forecast/` subdirectory on the local machine.

This module provides functions to clean, normalize, and transform
staged CSV files from the `data/stage/daily_weather_forecast/`
subdirectory into analysis-ready DataFrame objects, including:

- Issued datetime
- Synopsis
- Tropical cyclone information
- Forecast weather conditions
- Forecast wind and coastal water condition data
- Temperature and relative humidity values

Transformed DataFrames are saved as CSV files in the
`data/processed/daily_weather_forecast/` subdirectory
on the local machine for further processing before
analysis and consumption.
"""
import pandas as pd
import os

def create_subdir(
) -> None:
    """
    Create the `data/processed/daily_weather_forecast` subdirectory to store
    transformed or processed CSV files.

    This subdirectory stores the daily weather forecast data, transformed or processed
    from CSV files located in the `data/stage/daily_weather_forecast` subdirectory on the
    local machine.
    """
    # Create the data/processed/daily_weather_forecast/ subdirectory if it doesn't exist
    if not os.path.exists('data/processed/daily_weather_forecast'):
        os.makedirs('data/processed/daily_weather_forecast')

def transform_issued_datetime_dataframe(
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Docstring for transform_issued_datetime_dataframe

    :param issued_datetime_dataframe: Description
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Description
    :rtype: DataFrame
    """
    columns = list(issued_datetime_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    for _, row in issued_datetime_dataframe.iterrows():
        row['issued_datetime']