"""
Execute ingest workflow for daily weather forecast data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_daily_weather_forecast.py` to
ingest artifacts and store them as JSON files under `data/raw/daily_weather_forecasts/`
subdirectory for further processing.

Main function:
- `ingest_daily_weather_forecast()` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_daily_weather_forecasts import create_subdir
from ingest.ingest_daily_weather_forecasts import ingest_and_parse_soup_from_url
from ingest.ingest_daily_weather_forecasts import ingest_issued_datetime
from ingest.ingest_daily_weather_forecasts import save_ingested_issued_datetime
from ingest.ingest_daily_weather_forecasts import ingest_synopsis
from ingest.ingest_daily_weather_forecasts import save_ingesed_synopsis
from ingest.ingest_daily_weather_forecasts import ingest_tropical_cyclone_informations
from ingest.ingest_daily_weather_forecasts import save_ingested_tropical_cyclone_informations
from ingest.ingest_daily_weather_forecasts import ingest_forecast_weather_conditions
from ingest.ingest_daily_weather_forecasts import save_ingested_forecast_weather_conditions
from ingest.ingest_daily_weather_forecasts import ingest_forecast_wind_and_coastal_water_conditions
from ingest.ingest_daily_weather_forecasts import save_ingested_forecast_wind_and_coastal_water_conditions
from ingest.ingest_daily_weather_forecasts import ingest_temperature_and_relative_humidity
from ingest.ingest_daily_weather_forecasts import save_ingested_temperature_and_relative_humidity

def ingest_daily_weather_forecast(
) -> None:
    """
    Executes the function in the
    `src.ingest.ingest_daily_weather_forecast.py`
    module to ingest the data from the daily
    weather forecast page of PAGASA-DOST website.
    """
    create_subdir()
    soup = ingest_and_parse_soup_from_url(
        'https://www.pagasa.dost.gov.ph/weather#daily-weather-forecast'
    )

    issued_datetime = ingest_issued_datetime(
        soup
    )
    save_ingested_issued_datetime(
        issued_datetime
    )

    synopsis = ingest_synopsis(
        soup
    )
    save_ingesed_synopsis(
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

    temperature_and_relative_humidity = ingest_temperature_and_relative_humidity(
        soup
    )
    save_ingested_temperature_and_relative_humidity(
        temperature_and_relative_humidity
    )