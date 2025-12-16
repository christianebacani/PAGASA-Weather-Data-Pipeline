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
    Transform the issued datetime DataFrame object
    located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param issued_datetime_dataframe: DataFrame
        containing the issued datetime of the daily
        weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the
        cleaned issued datetime of
        the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data from the issued datetime DataFrame object
    columns = list(issued_datetime_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the issued datetime DataFrame object to transform its data
    for _, row in issued_datetime_dataframe.iterrows():
        issued_datetime = row['issued_datetime']
        issued_datetime = str(issued_datetime).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'issued_datetime': [
                    issued_datetime
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def transform_synopsis_dataframe(
        synopsis_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the synopsis DataFrame object
    located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param issued_datetime_dataframe: DataFrame
        containing the synopsis of the daily
        weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the
        cleaned synopsis of the
        daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data from the issued datetime DataFrame object
    columns = list(synopsis_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the synopsis DataFrame object to transform its data
    for _, row in synopsis_dataframe.iterrows():
        synopsis = row['synopsis']
        synopsis = str(synopsis).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'synopsis': [
                    synopsis
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def enrich_synopsis_dataframe_with_issued_datetime(
        synopsis_dataframe: pd.DataFrame,
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrich synopsis DataFrame object with issued datetime
    to produce an analysis-ready dataset for downstream
    processing and consumption.

    :param synopsis_dataframe: Transformed DataFrame
        containing the cleaned synopsis of the daily
        weather forecast
    :type synopsis_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed
        DataFrame containing the cleaned issued
        datetime of the daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the
        synopsis and issued datetime of the daily
        weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store synopsis data with issued datetime
    synopsis_with_issued_datetime_dataframe = pd.DataFrame({
        'synopsis': [
            synopsis_dataframe['synopsis'][0]
        ],
        'issued_datetime': [
            issued_datetime_dataframe['issued_datetime'][0]
        ]
    })

    return synopsis_with_issued_datetime_dataframe

def save_synopsis_with_issued_datetime_to_processed_subdir(
        synopsis_with_issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Save the synopsis with issued datetime DataFrame object to
    a a CSV file in the `data/processed/daily_weather_forecast`
    subdirectory on the local machine.

    :param synopsis_with_issued_datetime_dataframe: Transformed
        DataFrame containing the synopsis and issued datetime of
        the daily weather forecast
    :type synopsis_with_issued_datetime_dataframe: pd.DataFrame
    """
    # Store the synopsis with issued datetime DataFrame object to the target filepath
    target_filepath = 'data/processed/daily_weather_forecast/synopsis.csv'
    synopsis_with_issued_datetime_dataframe.to_csv(target_filepath, index=False)

def transform_forecast_weather_conditions_dataframe(
        forecast_weather_conditions_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the forecast weather conditions DataFrame object
    located in the `data/stage/daily_weather_forecast` subdirectory
    on the local machine.

    :param forecast_weather_conditions_dataframe: DataFrame
        containing the forecast weather conditions of the daily
        weather forecast
    :type forecast_weather_conditions_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned forecast
        weather conditions of the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data from the forecast weather conditions DataFrame object
    columns = list(forecast_weather_conditions_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the synopsis DataFrame object to transform its data