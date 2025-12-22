"""
Execute transformation functions for daily weather forecast data

This module runs all transformation tasks on files located in the `data/stage/daily_weather_forecast`
subdirectory on the local machine, serving as the entry point for the daily transformation workflow.
"""
import pandas as pd

from etl.transform.transform_daily_weather_forecast import create_subdir
from etl.transform.transform_daily_weather_forecast import transform_issued_datetime
from etl.transform.transform_daily_weather_forecast import transform_synopsis
from etl.transform.transform_daily_weather_forecast import enrich_synopsis_with_issued_datetime

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

    issued_datetime_dataframe = transform_issued_datetime(
        pd.read_csv(
            'data/stage/daily_weather_forecast/issued_datetime.csv'
        )
    )

    synopsis_dataframe = transform_synopsis(
        pd.read_csv(
            'data/stage/daily_weather_forecast/synopsis.csv'
        )
    )
    enriched_synopsis_dataframe = enrich_synopsis_with_issued_datetime(
        synopsis_dataframe,
        issued_datetime_dataframe
    )