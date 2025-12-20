"""
Execute transformation functions for daily weather forecast data

This module runs all transformation tasks on files located in the `data/stage/daily_weather_forecast`
subdirectory on the local machine, serving as the entry point for the daily transformation workflow.
"""
import pandas as pd

from etl.transform.transform_daily_weather_forecast import create_subdir
from etl.transform.transform_daily_weather_forecast import transform_issued_datetime_df
from etl.transform.transform_daily_weather_forecast import transform_synopsis_df
from etl.transform.transform_daily_weather_forecast import enrich_synopsis_with_issued_datetime
from etl.transform.transform_daily_weather_forecast import save_synopsis_with_issued_datetime_to_processed_subdir
from etl.transform.transform_daily_weather_forecast import transform_forecast_weather_conditions_df
from etl.transform.transform_daily_weather_forecast import enrich_forecast_weather_conditions_with_issued_datetime
from etl.transform.transform_daily_weather_forecast import save_forecast_weather_conditions_with_issued_datetime_to_processed_subdir
from etl.transform.transform_daily_weather_forecast import transform_forecast_wind_and_coastal_water_conditions_df
from etl.transform.transform_daily_weather_forecast import enrich_forecast_wind_and_coastal_water_conditions_with_issued_datetime

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
    create_subdir()

    issued_datetime_df = transform_issued_datetime_df(
        pd.read_csv(
            'data/stage/daily_weather_forecast/issued_datetime.csv'
        )
    )

    synopsis_df = transform_synopsis_df(
        pd.read_csv(
            'data/stage/daily_weather_forecast/synopsis.csv'
        )
    )

    synopsis_with_issued_datetime_df = enrich_synopsis_with_issued_datetime(
        synopsis_df,
        issued_datetime_df
    )
    save_synopsis_with_issued_datetime_to_processed_subdir(
        synopsis_with_issued_datetime_df
    )

    forecast_weather_conditions_df = transform_forecast_weather_conditions_df(
        pd.read_csv(
            'data/stage/daily_weather_forecast/forecast_weather_conditions.csv'
        )
    )

    forecast_weather_conditions_with_issued_datetime_df = enrich_forecast_weather_conditions_with_issued_datetime(
        forecast_weather_conditions_df,
        issued_datetime_df
    )
    save_forecast_weather_conditions_with_issued_datetime_to_processed_subdir(
        forecast_weather_conditions_with_issued_datetime_df
    )

    forecast_wind_and_coastal_water_conditions_df = transform_forecast_wind_and_coastal_water_conditions_df(
        pd.read_csv(
            'data/stage/daily_weather_forecast/forecast_wind_and_coastal_water_conditions.csv'
        )
    )
    forecast_wind_and_coastal_water_conditions_with_issued_datetime_df = enrich_forecast_wind_and_coastal_water_conditions_with_issued_datetime(
        forecast_wind_and_coastal_water_conditions_df,
        issued_datetime_df
    )