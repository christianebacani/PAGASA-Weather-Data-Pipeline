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

    :return: Transformed DataFrame containing the
        cleaned issued datetime of
        the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    columns = list(issued_datetime_dataframe.keys())
    transformed_dataframe = pd.DataFrame(columns=columns)

    # Iterate the issued datetime DataFrame to transform its data
    for _, row in issued_datetime_dataframe.iterrows():
        issued_datetimes = row['issued_datetimes']
        issued_datetimes = str(issued_datetimes).strip()

        # Concatenate the transformed data to the initialized DataFrame
        transformed_dataframe = pd.concat([
            transformed_dataframe,
            pd.DataFrame({
                'issued_datetimes': [issued_datetimes]
            })
        ], ignore_index=True)
    
    return transformed_dataframe

def transform_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the synopsis DataFrame object
    located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param synopsis_dataframe: DataFrame containing the
        synopsis of the daily weather forecast
    :type synopsis_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the
        cleaned synopsis of the
        daily weather forecast
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
                'synopses': [synopses]
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

    :param synopsis_dataframe: Transformed DataFrame containing
        the cleaned synopsis of the daily weather forecast
    :type synopsis_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed DataFrame
        containing the cleaned issued datetime of the
        daily weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the enriched
        synopsis of the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store enrich synopsis data with issued datetime
    enriched_synopsis_dataframe = pd.DataFrame({
        'synopses': [
            synopsis_dataframe['synopses'][0]
        ],
        'issued_datetimes': [
            issued_datetime_dataframe['issued_datetimes'][0]
        ]
    })

    return enriched_synopsis_dataframe

def save_processed_synopsis(
        enriched_synopsis_dataframe: pd.DataFrame
) -> None:
    """
    Save the enriched synopsis DataFrame object to a CSV file
    in the `data/processed/daily_weather_forecast` subdirectory
    on the local machine.

    :param enriched_synopsis_dataframe: Transformed DataFrame
        containing the enriched synopsis of the daily weather forecast
    :type enriched_synopsis_dataframe: pd.DataFrame
    """
    # Store the enriched synopsis DataFrame object to the target filepath
    target_filepath = 'data/processed/daily_weather_forecast/synopsis.csv'
    enriched_synopsis_dataframe.to_csv(target_filepath, index=False)

def transform_tropical_cyclone_information(
        tropical_cyclone_information_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the tropical cyclone information DataFrame
    object located in the `data/stage/daily_weather_forecast`
    subdirectory on the local machine.

    :param tropical_cyclone_information_dataframe: DataFrame containing the
        tropical cyclone information of the daily weather forecast
    :type tropical_cyclone_information_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the cleaned and standardized
        tropical cyclone information of the daily weather forecast
    :rtype: DataFrame
    """

def transform_forecast_weather_conditions(
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

    # Iterate the forecast weather conditions DataFrame to transform its data
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
                'places': [places],
                'weather_conditions': [weather_conditions],
                'causes_by': [causes_by],
                'impacts': [impacts]
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

    :param forecast_weather_conditions_dataframe: Transformed
        DataFrame containing the cleaned forecast weather
        conditions of the daily weather forecast
    :type forecast_weather_conditions_dataframe: pd.DataFrame

    :param issued_datetime_dataframe: Transformed DataFrame
        containing the cleaned issued datetime of the daily
        weather forecast
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed DataFrame containing the enriched
        forecast weather conditions of the daily weather forecast
    :rtype: DataFrame
    """
    # Using initialized DataFrame to store transformed data
    enriched_forecast_weather_conditions_dataframe = pd.DataFrame(
        columns=[
            'places',
            'weather_conditions',
            'causes_by',
            'impacts',
            'issued_datetime'
        ]
    )

    # Iterate the forecast weather conditions DataFrame to map it s value to the initialized DataFrame
    for _, row in forecast_weather_conditions_dataframe.iterrows():
        places = row['places']
        weather_conditions = row['weather_conditions']
        causes_by = row['causes_by']
        impacts = row['impacts']
        issued_datetimes = issued_datetime_dataframe['issued_datetimes'][0]

        # Concatenate the forecast weather conditions data to the initialized DataFrame
        enriched_forecast_weather_conditions_dataframe = pd.concat([
            enriched_forecast_weather_conditions_dataframe,
            pd.DataFrame({
                'places': [places],
                'weather_conditions': [weather_conditions],
                'causes_by': [causes_by],
                'impacts': [impacts],
                'issued_datetimes': [issued_datetimes]
            })
        ], ignore_index=True)
    
    return enriched_forecast_weather_conditions_dataframe

def save_processed_forecast_weather_conditions(
        enriched_forecast_weather_conditions_dataframe: pd.DataFrame
) -> None:
    """
    Save the enriched forecast weather conditions DataFrame object
    to a CSV file in the `data/processed/daily_weather_forecast` subdirectory
    on the local machine.

    :param enriched_forecast_weather_conditions_dataframe: Transformed DataFrame
        containing the enriched forecast weather conditions of the daily weather
        forecast
    :type enriched_forecast_weather_conditions_dataframe: pd.DataFrame
    """
    # Store the enriched forecast weather conditions with issued DataFrame object to the target filepath
    target_filepath = 'data/processed/daily_weather_forecast/forecast_weather_conditions.csv'
    enriched_forecast_weather_conditions_dataframe.to_csv(target_filepath, index=False)

def transform_forecast_wind_and_coastal_water_conditions(
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

    # Iterate the forecast wind and coastal water conditions DataFrame to transform its data
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
                'places': [places],
                'speeds': [speeds],
                'directions': [directions],
                'coastal_waters': [coastal_waters]
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
    enriched_forecast_wind_and_coastal_water_conditions_dataframe = pd.DataFrame(
        columns=[
            'places',
            'speeds',
            'directions',
            'coastal_waters',
            'issued_datetimes'
        ]
    )

    # Iterate the forecast wind and coastal water conditions DataFrame to map its value to the initialized DataFrame
    for _, row in forecast_wind_and_coastal_water_conditions_dataframe.iterrows():
        places = row['places']
        speeds = row['speeds']
        directions = row['directions']
        coastal_waters = row['coastal_waters']
        issued_datetimes = issued_datetime_dataframe['issued_datetimes']

        # Concatenate the forecast weather conditions data to the initialized DataFrame
        enriched_forecast_wind_and_coastal_water_conditions_dataframe = pd.concat([
            enriched_forecast_wind_and_coastal_water_conditions_dataframe,
            pd.DataFrame({
                'places': [places],
                'speeds': [speeds],
                'directions': [directions],
                'coastal_waters': [coastal_waters],
                'issued_datetimes': [issued_datetimes]
            })
        ], ignore_index=True)

    return enriched_forecast_wind_and_coastal_water_conditions_dataframe