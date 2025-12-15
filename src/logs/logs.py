"""
Provide functions for generating logs during ETL pipeline execution.

These utilities generate log messages while processing data
from the PAGASA-DOST website. They are intended to support
monitoring and troubleshooting of ETL jobs.
"""
import sys
import os
sys.path.insert(0, os.path.abspath('src'))

import pandas as pd
from datetime import datetime

from executor.ingest.execute_ingest_daily_weather_forecast import ingest_daily_weather_forecast
from executor.ingest.execute_ingest_weather_outlook_for_ph_cities import ingest_weather_outlook_for_ph_cities
from executor.ingest.execute_ingest_weather_outlook_for_ph_tourist_areas import ingest_weather_outlook_for_ph_tourist_areas
from executor.ingest.execute_ingest_weather_advisory import ingest_weather_advisory
from executor.ingest.execute_ingest_tropical_cyclone_advisory import ingest_tropical_cyclone_advisory
from executor.ingest.execute_ingest_tropical_cyclone_associated_rainfall import ingest_tropical_cyclone_associated_rainfall

from executor.extract.execute_extract_daily_weather_forecast import extract_daily_weather_forecast
from executor.extract.execute_extract_weather_outlook_for_ph_cities import extract_weather_outlook_for_ph_cities
from executor.extract.execute_extract_weather_outlook_for_ph_tourist_areas import extract_weather_outlook_for_ph_tourist_areas
from executor.extract.execute_extract_weather_advisory import extract_weather_advisory
from executor.extract.execute_extract_tropical_cyclone_advisory import extract_tropical_cyclone_advisory
from executor.extract.execute_extract_tropical_cyclone_associated_rainfall import extract_tropical_cyclone_associated_rainfall

from executor.transform.execute_transform_daily_weather_forecast import transform_daily_weather_forecast

def generate_logs(
    log_message: str
) -> None:
    """
    Generate logs for ETL pipeline jobs that process data from
    the PAGASA-DOST website.

    :param log_message: The message to log during ETL pipeline execution
    :type log_message: str
    """
    format = '%Y-%m-%d %H:%M:%S' # Format: YYYY-MM-DD HH:MM:SS
    now = datetime.now()
    timestamp = now.strftime(format)

    # Generate logs using pandas for logs dataset (csv format)
    logs = pd.read_csv('src/logs/logs.csv')
    logs = pd.concat([
        logs,
        pd.DataFrame({
            'messages': [log_message],
            'timestamps': [timestamp]
        })
    ], ignore_index=True)
    logs.to_csv('src/logs/logs.csv', index=False)

if __name__ == '__main__':
    # Ingest data for daily weather forecast
    ingest_daily_weather_forecast()
    generate_logs(
        '(DEV): Ingest the data for the daily weather forecast.'
    )

    # Ingest data for weather outlook for selected Philippine cities
    ingest_weather_outlook_for_ph_cities()
    generate_logs(
        '(DEV): Ingest the data for the weather outlook for selected Philippine cities.'
    )

    # Ingest data for weather outlook for selected Philippine tourist areas
    ingest_weather_outlook_for_ph_tourist_areas()
    generate_logs(
        '(DEV): Ingest the data for the weather outlook for selected Philippine tourist areas.'
    )

    # Ingest data for the weather advisory
    ingest_weather_advisory()
    generate_logs(
        '(DEV): Ingest the data for the weather advisory.'
    )

    # Ingest data for the tropical cyclone advisory
    ingest_tropical_cyclone_advisory()
    generate_logs(
        '(DEV): Ingests the data for the tropical cyclone advisory.'
    )

    # Ingest data for the tropical cyclone associated rainfall
    ingest_tropical_cyclone_associated_rainfall()
    generate_logs(
        '(DEV): Ingest the data for the tropical cyclone associated rainfall.'
    )

    # Extract and stage the data for the daily weather forecast
    extract_daily_weather_forecast()
    generate_logs(
        '(DEV): Extract the data for the daily weather forecast.'
    )

    # Extract and stage the data for the weather outlook for Philippine cities
    extract_weather_outlook_for_ph_cities()
    generate_logs(
        '(DEV): Extract the data for the weather outlook for selected Philippine cities.'
    )

    # Extract and stage the data for the weather outlook for Philippine tourist areas
    extract_weather_outlook_for_ph_tourist_areas()
    generate_logs(
        '(DEV): Extract the data for the weather outlook for selected Philippine tourist areas.'
    )

    # Extract and stage the data for weather advisory
    extract_weather_advisory()
    generate_logs(
        '(DEV): Extract the data for the weather advisory.'
    )

    # Extract and stage the data for the tropical cyclone advisory
    extract_tropical_cyclone_advisory()
    generate_logs(
        '(DEV): Extract the data for the tropical cyclone advisory.'
    )

    # Extract and stage the data for the tropical cyclone associated rainfall
    extract_tropical_cyclone_associated_rainfall()
    generate_logs(
        '(DEV): Extract the data for the tropical cyclone associated rainfall.'
    )

    # Transform the data for the daly weather forecast
    transform_daily_weather_forecast()
    generate_logs(
        '(DEV): Transform the data for the daily weather forecast.'
    )