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
    Connect the credentials to the
    Snowflake Data Warehouse.

    :param username: Snowflake username
    :type username: str

    :param password: Snowflake password
    :type password: str

    :param account: Snowflake account
        identifier
    :type account: str

    :param warehouse: Name of the Snowflake
        warehouse to use
    :type warehouse: str

    :return: Established Snowflake connection
    :rtype: SnowflakeConnection
    """
    conn = snowflake.connect(
        user=username,
        password=password,
        account=account,
        warehouse=warehouse
    )

    return conn

def database_config(
        conn: snowflake.SnowflakeConnection,
        database: str,
        schema: str,
        table: str,
        columns: dict[str, str]
) -> None:
    """
    Configure Snowflake database by creating database,
    schema, and a table for storing cleaned data.

    :param conn: Established Snowflake connection
    :type conn: snowflake.SnowflakeConnection

    :param database: Name of the Snowflake database
        to create
    :type database: str

    :param schema: Name of the Snowflake schema to create
    :type schema: str
   
    :param table: Name of the Snowflake table to create
    :type table: str

    :param columns: Dictionary containing column names and
        corresponding datatypes
    :type columns: dict[str, str]
    """
    cursor = conn.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {database}"
    )
    cursor.execute(
        f"CREATE SCHEMA IF NOT EXISTS {schema}"
    )

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

def clean_issued_datetime(
        issued_datetime_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Clean the issued datetime as a DataFrame object.

    :param issued_datetime_dataframe: Issued datetime as
        a DataFrame object
    :type issued_datetime_dataframe: pd.DataFrame

    :return: Cleaned issued datetime as a DataFrame object
    :rtype: DataFrame
    """
    columns = [
        'issued_date',
        'issued_time'
    ]
    cleaned_issued_datetime = pd.DataFrame(
        columns=columns
    )

    issued_datetime = issued_datetime_dataframe['issued_datetime'][0]
    issued_datetime = str(issued_datetime)
    issued_datetime = issued_datetime.strip()

    issued_time = issued_datetime.split(', ')[0]
    if 'PM' in issued_time:
        issued_time = issued_time.replace('PM', '')
        issued_time = issued_time.strip()
        
        hours = issued_time.split(':')[0]
        hours = int(hours)
        hours = hours + 23
        issued_time = str(hours) + ':00'

    else:
        issued_time = issued_time.replace('PM', '')
        issued_time = issued_time.strip()

    issued_date = issued_datetime.split(', ')[1]

    cleaned_issued_datetime = pd.concat([
        cleaned_issued_datetime,
        pd.DataFrame({
            'issued_date': [issued_date],
            'issued_time': [issued_time]
        })
    ])

    return cleaned_issued_datetime