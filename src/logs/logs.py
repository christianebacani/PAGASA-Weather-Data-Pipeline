"""
Generate logs during ETL pipeline execution.

These utilities generate log messages while processing data
from the PAGASA-DOST website. They are intended to support
monitoring and troubleshooting of ETL jobs.

Main function:
- `generate_logs()` - Generate logs for ETL pipeline jobs
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

from executor.extract.execute_extract_daily_weather_forecast import extract_daily_weather_forecast

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
    ingest_daily_weather_forecast()
    generate_logs(
        '(DEV): Ingest the daily weather forecasts data.'
    )

    ingest_weather_outlook_for_ph_cities()
    generate_logs(
        '(DEV): Ingest the weather outlook for selected Philippine cities data.'
    )

    ingest_weather_outlook_for_ph_tourist_areas()
    generate_logs(
        '(DEV): Ingest the weather outlook for selected Philippine tourist areas data.'
    )

    ingest_weather_advisory()
    generate_logs(
        '(DEV): Ingest the weather advisories data.'
    )

    extract_daily_weather_forecast()
    generate_logs(
        '(DEV): Extract the daily weather forecast data.'
    )