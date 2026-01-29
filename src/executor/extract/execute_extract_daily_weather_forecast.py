"""
Docstring for src.executor.extract.execute_extract_daily_weather_forecast
"""
import os
from dotenv import load_dotenv
from etl.extract.extract_daily_weather_forecast import connect
from etl.extract.extract_daily_weather_forecast import database_config
from etl.extract.extract_daily_weather_forecast import store_cleaned_data_to_snowflake
from etl.extract.extract_daily_weather_forecast import extract_issued_datetime
from etl.extract.extract_daily_weather_forecast import clean_issued_datetime
from etl.extract.extract_daily_weather_forecast import extract_synopsis
from etl.extract.extract_daily_weather_forecast import clean_synopsis

def extract_daily_weather_forecast(
) -> None:
    """
    Executes the function in the
    `src.etl.extract.extract_daily_weather_forecast`
    module to extract the data from the `data/raw/daily_weather_forecasts/`
    subdirectory path that consist of ingested artifacts as a JSON file
    """
    # Load environment variables from .env file
    load_dotenv()
    conn = connect(
        os.getenv('SNOWFLAKE_USERNAME'),
        os.getenv('SNOWFLAKE_PASSWORD'),
        os.getenv('SNOWFLAKE_ACCOUNT'),
        os.getenv('SNOWFLAKE_WAREHOUSE')
    )

    issued_datetime_dataframe = extract_issued_datetime(
        'data/raw/daily_weather_forecasts/issued_datetime.json'
    )
    cleaned_issued_datetime = clean_issued_datetime(
        issued_datetime_dataframe
    )

    synopsis_dataframe = extract_synopsis(
        'data/raw/daily_weather_forecasts/synopsis.json'
    )
    clean_synopsis_dataframe = clean_synopsis(
        synopsis_dataframe
    )