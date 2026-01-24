"""
Docstring for src.executor.extract.execute_extract_daily_weather_forecast
"""
from etl.extract.extract_daily_weather_forecast import extract_issued_datetime
from etl.extract.extract_daily_weather_forecast import transform_issued_datetime
from etl.extract.extract_daily_weather_forecast import extract_synopsis
from etl.extract.extract_daily_weather_forecast import transform_synopsis
from etl.extract.extract_daily_weather_forecast import extract_tropical_cyclone_informations
from etl.extract.extract_daily_weather_forecast import transform_tropical_cyclone_informations
from etl.extract.extract_daily_weather_forecast import extract_forecast_weather_conditions
from etl.extract.extract_daily_weather_forecast import transform_forecast_weather_conditions

def extract_daily_weather_forecast(
) -> None:
    """
    Executes the function in the
    `src.etl.extract.extract_daily_weather_forecast`
    module to extract the data from the `data/daily_weather_forecasts/`
    subdirectory path that consist of ingested artifacts as a JSON file
    """
    issued_datetime_dataframe = extract_issued_datetime(
        'data/daily_weather_forecasts/issued_datetime.json'
    )
    transformed_issued_datetime = transform_issued_datetime(
        issued_datetime_dataframe
    )

    synopsis_dataframe = extract_synopsis(
        'data/daily_weather_forecasts/synopsis.json'
    )
    transformed_synopsis = transform_synopsis(
        synopsis_dataframe
    )

    tropical_cyclone_informations_dataframe = extract_tropical_cyclone_informations(
        'data/daily_weather_forecasts/tropical_cyclone_informations.json'
    )
    transform_tropical_cyclone_informations(
        tropical_cyclone_informations_dataframe   
    )

    forecast_weather_conditions_dataframe = extract_forecast_weather_conditions(
        'data/daily_weather_forecasts/forecast_weather_conditions.json'
    )
    transform_forecast_weather_conditions(
        forecast_weather_conditions_dataframe
    )