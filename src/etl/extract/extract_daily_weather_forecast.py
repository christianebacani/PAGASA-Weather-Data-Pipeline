"""
Docstring for etl.extract.extract_daily_weather_forecast
"""

def extract_issued_datetime(
        issued_datetime_filepath: str        
) -> None:
    """
    Extract the ingested issued datetime of
    daily weather forecast page as a JSON file
    from the subdirectory path
    `data/daily_weather_forecasts`.

    :param issued_datetime_filepath: Issued
        datetime of the daily weather forecast
        page as a JSON file
    :type issued_datetime_filepath: str
    """