"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import pandas as pd

def extract_issued_datetime(
        issued_datetime_filepath: str        
) -> pd.DataFrame:
    """
    Extract the ingested issued datetime
    from the subdirectory path `data/daily_weather_forecasts`.

    :param issued_datetime_filepath: Filepath
        of the ingested issued datetime from
        the subdirectory path
        `data/daily_weather_forecasts`
    :type issued_datetime_filepath: str

    :return: Issued datetime as a DataFrame object
    :rtype: DataFrame
    """
    issued_datetime_dataframe = pd.read_json(
        issued_datetime_filepath
    )

    return issued_datetime_dataframe

def transform_issued_datetime(
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the issued datetime as a DataFrame object.

    :param issued_datetime_dataframe: Issued datetime as
        a DataFrame object
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Transformed issued datetime as a DataFrame
        object
    :rtype: DataFrame
    """
    columns = [
        'issued_time',
        'issued_date'
    ]
    transformed_issued_datetime = pd.DataFrame(
        columns=columns
    )

    issued_datetime = issued_datetime_dataframe['issued_datetime'][0]
    issued_datetime = str(issued_datetime)
    issued_datetime = issued_datetime.strip()
    issued_datetime = issued_datetime.replace(
        'Issued at:', ''
    )
    issued_time = issued_datetime.split(', ')[0]
    issued_date = issued_datetime.split(', ')[1]

    transformed_issued_datetime = pd.concat([
        transformed_issued_datetime,
        pd.DataFrame({
            'issued_time': [issued_time],
            'issued_date': [issued_date]
        })
    ])

    return transformed_issued_datetime

def extract_synopsis(
        synopsis_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested synopsis from the
    subdirectory path `data/daily_weather_forecasts.`

    :param synopsis_filepath: Filepath of the
        ingested synopsis from the subdirectory
        path `data/daily_weather_forecasts`
    :type synopsis_filepath: str

    :return: Synopsis as a DataFrame object
    :rtype: DataFrame
    """
    synopsis_dataframe = pd.read_json(
        synopsis_filepath
    )

    return synopsis_dataframe

def transform_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the synopsis as a DataFrame object.

    :param synopsis_dataframe: Synopsis as a DataFrame
        object
    :type synopsis: pd.DataFrame

    :return: Transformed synopsis as a DataFrame object
    :rtype: DataFrame
    """
    columns = [
        'synopsis'
    ]
    transformed_dataframe = pd.DataFrame(
        columns=columns
    )

    synopsis = synopsis_dataframe['synopsis'][0]
    synopsis = str(synopsis)
    synopsis = synopsis.strip()

    transformed_dataframe = pd.concat([
        transformed_dataframe,
        pd.DataFrame({
            'synopsis': [synopsis]
        })
    ])

    return transformed_dataframe

def extract_tropical_cyclone_informations(
        tropical_cyclone_informations_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested tropical cyclone information
    from the subdirectory path `data/daily_weather_forecasts`.

    :param tropical_cyclone_informations_filepath: Filepath of the
        ingested tropical cyclone informations from the subdirectory
        path `data/daily_weather_forecasts`
    :type tropical_cyclone_informations_filepath: str

    :return: Tropical cyclone informations as a DataFrame object
    :rtype: DataFrame
    """

def transform_tropical_cyclone_informations(
        tropical_cyclone_informations_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the tropical cyclone informations as a DataFrame
    object.

    :param tropical_cyclone_informations_dataframe: Tropical
        cyclone informations as a DataFrame object
    :type tropical_cyclone_informations_dataframe: pd.DataFrame

    :return: Transformed tropical cyclone informations as a
        DataFrame object
    :rtype: DataFrame
    """

def extract_forecast_weather_conditions(
        forecast_weather_conditions_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested forecast weather conditions from the
    subdirectory path `data/daily_weather_forecasts`.

    :param forecast_weather_conditions_filepath: Filepath of the
        ingested forecast weather conditions from the subdirectory
        path `data/daily_weather_forecast`
    :type forecast_weather_conditions_filepath: str

    :return: Forecast weather conditions as a DataFrame object
    :rtype: DataFrame
    """
    forecast_weather_conditions_dataframe = pd.read_json(
        forecast_weather_conditions_filepath
    )

    return forecast_weather_conditions_dataframe

def transform_forecast_weather_conditions(
        forecast_weather_conditions_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform the forecast weather conditions as a DataFrame
    object.

    :param forecast_weather_conditions_dataframe: Forecast weather
        conditions as a DataFrame object
    :type forecast_weather_conditions_dataframe: pd.DataFrame

    :return: Transformed forecast weather conditions as a DataFrame
        object
    :rtype: DataFrame
    """
    columns = [
        'place',
        'weather_condition',
        'caused_by',
        'impact'
    ]
    transformed_dataframe = pd.DataFrame(
        columns=columns
    )

    for _, row in forecast_weather_conditions_dataframe.iterrows():
        place = row['place']
        place = str(place)
        place = place.strip()
        place = place.replace('and', '')
        places = place.split(', ')

        weather_condition = row['weather_condition']
        weather_condition = str(weather_condition)
        weather_condition = weather_condition.strip()

        caused_by = row['caused_by']
        caused_by = str(caused_by)
        caused_by = caused_by.strip()

        impact = row['impact']
        impact = str(impact)
        impact = impact.strip()

        for place in places:
            transformed_dataframe = pd.concat([
                transformed_dataframe,
                pd.DataFrame({
                    'place': [place],
                    'weather_condition': [weather_condition],
                    'caused_by': [caused_by],
                    'impact': [impact]
                })
            ], ignore_index=True)

    return transformed_dataframe

def extract_forecast_wind_and_coastal_water_conditions(
        forecast_wind_and_coastal_water_conditions_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested forecast wind and coastal water conditions
    from the subdirectory path `data/daily_weather_forecasts`.

    :param forecast_wind_and_coastal_water_conditions_filepath: Filepath
        of the ingested forecast wind and coastal water conditions from
        the subdirectory path `data/daily_weather_forecasts`
    :type forecast_wind_and_coastal_water_conditions_filepath: str

    :return: Forecast wind and coastal water conditions as a DataFrame
        object
    :rtype: DataFrame
    """