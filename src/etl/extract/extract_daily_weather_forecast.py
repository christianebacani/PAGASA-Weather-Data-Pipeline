"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import snowflake.connector as snowflake
import pandas as pd

def connect(
        username: str,
        password: str,
        account: str,
        warehouse: str               
) -> snowflake.SnowflakeConnection:
    """
    Docstring for connect
    
    :param username: Description
    :type username: str
    :param password: Description
    :type password: str
    :param account: Description
    :type account: str
    :param warehouse: Description
    :type warehouse: str
    :return: Description
    :rtype: SnowflakeConnection
    """
    conn = snowflake.connect(
        user=username,
        password=password,
        account=account,
        warehouse=warehouse
    )

    return conn

def extract_issued_datetime(
        issued_datetime_filepath: str        
) -> pd.DataFrame:
    """
    Extract the ingested issued datetime
    from the subdirectory path `data/raw/daily_weather_forecasts`.

    :param issued_datetime_filepath: Filepath
        of the ingested issued datetime from
        the subdirectory path
        `data/raw/daily_weather_forecasts`
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