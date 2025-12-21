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

def transform_issued_datetime(
    issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the issued datetime DataFrame object
    located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param issued_datetime_dataframe: DataFrame containing
        the issued datetime of the daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned,
        normalized, and standardized issued datetime of the
        daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    transformed_dataframe = pd.DataFrame(
        columns=[
            'issued_dates',
            'issued_times'
        ]
    )

    # Iterate the issued datetime DataFrame to transform its data
    for _, row in issued_datetime_dataframe.iterrows():
        issued_datetimes = row['issued_datetimes']
        issued_datetimes = str(issued_datetimes)
        issued_datetimes = issued_datetimes.split(', ')

        # Normalize and standardized the data using split() and replace() method
        issued_dates = issued_datetimes[1]
        issued_dates = issued_dates.split()
        issued_dates = issued_dates[1] + ' ' + issued_dates[0] + ', ' + issued_dates[2]
        issued_dates = issued_dates.strip()

        issued_times = issued_datetimes[0]
        issued_times = issued_times.replace('Issued at: ', '')
        issued_times = issued_times.strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'issued_dates': [
                    issued_dates
                ],
                'issued_times': [
                    issued_times
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def transform_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> None:
    """
    Transform the synopsis DataFrame object
    located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param synopsis_dataframe: DataFrame containing
        the synopsis of the daily weather forecast
    :type synopsis_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the
        cleaned synopsis of the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    columns = list(synopsis_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Iterate the synopsis DataFrame to transform its data
    for _, row in synopsis_dataframe.iterrows():
        synopses = row['synopses']
        synopses = str(synopses).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'synopses': [
                    synopses
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def enrich_synopsis_with_issued_datetime(
        synopsis_dataframe: pd.DataFrame,
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrich the synopsis DataFrame with issued
    datetime to produce an analysis-ready
    dataset for further processing or consumption.

    :param synopsis_dataframe: Transformed DataFrame
        containing the cleaned synopsis of the daily
        weather forecast
    :type synopsis_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed
        DataFrame containing the cleaned, normalized,
        and standardize issued datetime of the daily
        weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned
        and enriched synopsis of the daily weather forecast 
    :rtype: DataFrame
    """