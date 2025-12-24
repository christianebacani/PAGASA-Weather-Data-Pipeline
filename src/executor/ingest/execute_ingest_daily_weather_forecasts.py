"""
Docstring for executor.ingest.execute_ingest_daily_weather_forecasts
"""
from ingest.ingest_daily_weather_forecasts import create_subdir
from ingest.ingest_daily_weather_forecasts import ingest_and_parse_soup_from_url
from ingest.ingest_daily_weather_forecasts import ingest_issued_datetimes
from ingest.ingest_daily_weather_forecasts import save_ingested_issued_datetimes
from ingest.ingest_daily_weather_forecasts import ingest_synopses
from ingest.ingest_daily_weather_forecasts import save_ingested_synopses
from ingest.ingest_daily_weather_forecasts import ingest_tropical_cyclone_informations
from ingest.ingest_daily_weather_forecasts import save_ingested_tropical_cyclone_informations
from ingest.ingest_daily_weather_forecasts import ingest_forecast_weather_conditions
from ingest.ingest_daily_weather_forecasts import save_ingested_forecast_weather_conditions
from ingest.ingest_daily_weather_forecasts import ingest_forecast_wind_and_coastal_water_conditions
from ingest.ingest_daily_weather_forecasts import save_ingested_forecast_wind_and_coastal_water_conditions
from ingest.ingest_daily_weather_forecasts import ingest_temperatures_and_relative_humidities

def ingest_daily_weather_forecasts(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_daily_weather_forecasts.py`
    module to ingest the data from the daily
    weather forecast page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'
    )

    issued_datetime = ingest_issued_datetimes(
        soup
    )
    save_ingested_issued_datetimes(
        issued_datetime
    )

    synopsis = ingest_synopses(
        soup
    )
    save_ingested_synopses(
        synopsis
    )

    tropical_cyclone_informations = ingest_tropical_cyclone_informations(
        soup
    )
    save_ingested_tropical_cyclone_informations(
        tropical_cyclone_informations
    )

    forecast_weather_conditions = ingest_forecast_weather_conditions(
        soup
    )
    save_ingested_forecast_weather_conditions(
        forecast_weather_conditions
    )

    forecast_wind_and_coastal_water_conditions = ingest_forecast_wind_and_coastal_water_conditions(
        soup
    )
    save_ingested_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions
    )

    ingest_temperatures_and_relative_humidities(
        soup
    )