'''
    Module for executing extraction functions for the
    daily weather forecast data from the data/stage
    subdirectory on the local machine.
'''
from etl.extract.extract_daily_weather_forecast import create_subdir
from etl.extract.extract_daily_weather_forecast import parse_issued_datetime_to_dataframe

def extract_daily_weather_forecast(
) -> None:
    '''
    Extract the daily weather forecast from the
    data/stage subdirectory on the local machine
    by executing all functions in the
    extract_daily_weather_forecast module
    of the src/ingest package.    
    '''
    # Run all functions to ingest weather advisory data
    create_subdir()

    issued_datetime_dataframe = parse_issued_datetime_to_dataframe(
        'data/raw/daily_weather_forecast/issued_datetime.json'
    )