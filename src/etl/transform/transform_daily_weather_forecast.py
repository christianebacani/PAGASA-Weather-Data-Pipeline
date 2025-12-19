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
    # Using initialized DataFrame to store transformed data
    columns = list(issued_datetime_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the issued datetime DataFrame object to transform its data
    for _, row in issued_datetime_dataframe.iterrows():
        issued_datetime = row['issued_datetimes']
        issued_datetime = str(issued_datetime).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'issued_datetimes': [
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
    # Using initialized DataFrame to store transformed data
    columns = list(synopsis_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the synopsis DataFrame object to transform its data
    for _, row in synopsis_dataframe.iterrows():
        synopsis = row['synopses']
        synopsis = str(synopsis).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'synopses': [
                    synopsis
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def enrich_synopsis_with_issued_datetime(
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
        synopsis with issued datetime of the daily
        weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store enrich synopsis data with issued datetime
    synopsis_with_issued_datetime_dataframe = pd.DataFrame({
        'synopses': [
            synopsis_dataframe['synopses'][0]
        ],
        'issued_datetimes': [
            issued_datetime_dataframe['issued_datetimes'][0]
        ]
    })

    return synopsis_with_issued_datetime_dataframe

def save_synopsis_with_issued_datetime_to_processed_subdir(
        synopsis_with_issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Save the synopsis with issued datetime DataFrame object to
    a CSV file in the `data/processed/daily_weather_forecast`
    subdirectory on the local machine.

    :param synopsis_with_issued_datetime_dataframe: Transformed
        DataFrame containing the synopsis and issued datetime of
        the daily weather forecast
    :type synopsis_with_issued_datetime_dataframe: pd.DataFrame
    """
    # Store the synopsis with issued datetime DataFrame object to the target filepath
    target_filepath = 'data/processed/daily_weather_forecast/synopsis.csv'
    synopsis_with_issued_datetime_dataframe.to_csv(target_filepath, index=False)

def transform_tc_information_dataframe(
        tc_information_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the tropical cyclone information DataFrame
    object located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param tc_information_dataframe: DataFrame containing the
        tropical cyclone information of the daily weather forecast
    :type tc_information_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned and standardized
        tropical cyclone information of the daily weather forecast
    :rtype: DataFrame
    """

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
    # Using initialized DataFrame to store transformed data
    columns = list(forecast_weather_conditions_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the synopsis DataFrame object to transform its data
    for _, row in forecast_weather_conditions_dataframe.iterrows():
        places = row['places']
        weather_conditions = row['weather_conditions']
        causes_by = row['causes_by']
        impacts = row['impacts']

        places = str(places).strip()
        weather_conditions = str(weather_conditions).strip()
        causes_by = str(causes_by).strip()
        impacts = str(impacts).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'places': [
                    places
                ],
                'weather_conditions': [
                    weather_conditions
                ],
                'causes_by': [
                    causes_by
                ],
                'impacts': [
                    impacts
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def enrich_forecast_weather_conditions_with_issued_datetime(
        forecast_weather_conditions_dataframe: pd.DataFrame,
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrich forecast weather conditions DataFrame object 
    with issued datetime to produce an analysis-ready
    dataset for downstream processing and consumption.

    :param forecast_weather_conditions_dataframe:
        Transformed DataFrame containing the cleaned
        forecast weather conditions of the daily weather
        forecast
    :type forecast_weather_conditions_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed DataFrame
        containing the cleaned issued datetime of the daily
        weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the forecast
        weather conditions with issued datetime of the
        daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    forecast_weather_conditions_with_issued_datetime_dataframe = pd.DataFrame(
        columns=[
            'places',
            'weather_conditions',
            'causes_by',
            'impacts',
            'issued_datetime'
        ]
    )

    # Loop through the forecast weather conditions DataFrame object to map its value to the initialize DataFrame
    for _, row in forecast_weather_conditions_dataframe.iterrows():
        places = row['places']
        weather_conditions = row['weather_conditions']
        causes_by = row['causes_by']
        impacts = row['impacts']
        issued_datetime = issued_datetime_dataframe['issued_datetimes'][0]

        # Concatenate the forecast weather conditions data to the initialized DataFrame
        forecast_weather_conditions_with_issued_datetime_dataframe = pd.concat([
            forecast_weather_conditions_with_issued_datetime_dataframe,
            pd.DataFrame({
                'places': [
                    places
                ],
                'weather_conditions': [
                    weather_conditions
                ],
                'causes_by': [
                    causes_by
                ],
                'impacts': [
                    impacts
                ],
                'issued_datetime': [
                    issued_datetime
                ]
            })
        ], ignore_index=True)

    return forecast_weather_conditions_with_issued_datetime_dataframe

def save_forecast_weather_conditions_with_issued_datetime_to_processed_subdir(
        forecast_weather_conditions_with_issued_datetime_dataframe: pd.DataFrame
) -> None:
    """
    Save the forecast weather conditions with issued datetime DataFrame object
    to a CSV file in the `data/processed/daily_weather_forecast` subdirectory on
    the local machine.

    :param forecast_weather_conditions_with_issued_datetime_dataframe: Transformed
        DataFrame containing the forecast weather conditions and issued datetime of
        the daily weather forecast
    :type forecast_weather_conditions_with_issued_datetime_dataframe: pd.DataFrame
    """
    # Store the forecast weather conditions with issued DataFrame object to the target filepath
    target_filepath = 'data/processed/daily_weather_forecast/forecast_weather_conditions.csv'
    forecast_weather_conditions_with_issued_datetime_dataframe.to_csv(target_filepath, index=False)

def transform_forecast_wind_and_coastal_water_conditions_dataframe(
        forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the forecast wind and coastal water conditions DataFrame object
    located in the `data/stage/daily_weather_forecast` subdirectory on the
    local machine.

    :param forecast_wind_and_coastal_water_conditions_dataframe: DataFrame
        containing the forecast wind and coastal water conditions of the daily
        weather forecast
    :type forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned forecast wind and
        coastal water conditions of the daily weather forecast
    :rtype: DataFrame
    """
    # Initialized DataFrame to store transformed data
    columns = list(forecast_wind_and_coastal_water_conditions_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Loop through the forecast wind and coastal water conditions DataFrame object to transform its data
    for _, row in forecast_wind_and_coastal_water_conditions_dataframe.iterrows():
        places = row['places']
        speeds = row['speeds']
        directions = row['directions']
        coastal_waters = row['coastal_waters']

        places = str(places).strip()
        speeds = str(speeds).strip()
        directions = str(directions).strip()
        coastal_waters = str(coastal_waters).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'places': [
                    places
                ],
                'speeds': [
                    speeds
                ],
                'directions': [
                    directions
                ],
                'coastal_waters': [
                    coastal_waters
                ]
            })
        ], ignore_index=True)

    return transformed_dataframe

def enrich_forecast_wind_and_coastal_water_conditions_with_issued_datetime(
        forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame,
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Enrich forecast wind and coastal water conditions with issued datetime
    to produce an analysis-ready dataset for downstream
    processing and consumption.

    :param forecast_wind_and_coastal_water_conditions_dataframe: Transformed
        DataFrame containing the cleaned forecast wind and coastal water
        conditions of the daily weather forecast
    :type forecast_wind_and_coastal_water_conditions_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed DataFrame containing the
        cleaned issued datetime of the daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the forecast wind and coastal water
        conditions with issued datetime of the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    forecast_wind_and_coastal_water_conditions_with_issued_datetime_df = pd.DataFrame(
        columns=[
            'places',
            'speeds',
            'directions',
            'coastal_waters',
            'issued_datetimes'
        ]
    )