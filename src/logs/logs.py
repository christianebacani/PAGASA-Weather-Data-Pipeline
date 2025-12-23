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

from executor.ingest.execute_ingest_daily_weather_forecasts import ingest_daily_weather_forecasts

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
    ingest_daily_weather_forecasts()