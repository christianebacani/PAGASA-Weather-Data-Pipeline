"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import pandas as pd
import datetime
import snowflake.connector as snowflake
from snowflake.connector.pandas_tools import write_pandas

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

    :param schema: Name of the Snowflake table schema
        to create
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
        f"USE DATABASE {database}"
    )
    cursor.execute(
        f"CREATE SCHEMA IF NOT EXISTS {database}.{schema}"
    )
    command_to_create_table = []

    for column_name, data_type in columns.items():
        command_to_create_table.append(
            column_name + ' ' + data_type
        )

    command_to_create_table = ', '.join(command_to_create_table)
    command_to_create_table = '(' + command_to_create_table + ')'
    command_to_create_table = 'CREATE TABLE IF NOT EXISTS' + ' ' + schema + '.' + table + command_to_create_table
    cursor.execute(
        command_to_create_table
    )

def store_cleaned_data_to_snowflake(
        conn: snowflake.SnowflakeConnection,
        data: pd.DataFrame,
        table: str,
        database: str,
        schema: str
) -> None:
    """
    Store clean data as a DataFrame
    object to the Snowflake Database.

    :param conn: Established Snowflake
        connection
    :type conn: snowflake.SnowflakeConnection

    :param data: Clean data as a DataFrame object
    :type data: pd.DataFrame

    :param table: Name of the Snowflake table to
        load the clean data
    :type table: str

    :param database: Name of the Snowflake database
    :type database: str

    :param schema: Name of the Snowflake table schema
    :type schema: str
    """
    write_pandas(
        conn=conn,
        df=data,
        table_name=table,
        database=database,
        schema=schema
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
    issued_datetime = issued_datetime_dataframe['issued_datetime'][0]
    issued_datetime = str(issued_datetime)
    issued_datetime = issued_datetime.replace('Issued at:', '')
    issued_datetime = issued_datetime.strip()

    issued_date = issued_datetime.split(', ')[1]

    day = issued_date.split()[0]
    day = int(day)

    month_dictionary = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    month = issued_date.split()[1]
    month = month_dictionary[month]
    month = int(month)

    year = issued_date.split()[2]
    year = int(year)

    issued_date = datetime.date(
        year,
        month,
        day
    )

    issued_time = issued_datetime.split(', ')[0]

    if 'PM' in issued_time:
        issued_time = issued_time.replace('PM', '')
        issued_time = issued_time.strip()
        
        hours = issued_time.split(':')[0]
        hours = int(hours)
        hours = hours + 12
        issued_time = datetime.time(hours, 0)

    else:
        issued_time = issued_time.replace('AM', '')
        issued_time = issued_time.strip()

        hours = issued_time.split(':')[0]
        hours = int(hours)
        issued_time = datetime.time(hours, 0)
        issued_time = issued_time.strftime('%H:%M:%S')

    cleaned_issued_datetime = pd.DataFrame({
        'ISSUED_DATE': [issued_date],
        'ISSUED_TIME': [issued_time]
    })

    return cleaned_issued_datetime

def extract_synopsis(
        synopsis_filepath: str
) -> pd.DataFrame:
    """
    Extract the ingested synopsis from the subdirectory
    path `data/raw/daily_weather_forecasts`.

    :param synopsis_filepath: Filepath of the ingested
        synopsis from the subdirectory path
        `data/raw/daily_weather_forecasts`
    :type synopsis_filepath: str

    :return: Synopsis as a DataFrame object
    :rtype: DataFrame
    """
    synopsis_dataframe = pd.read_json(
        synopsis_filepath
    )

    return synopsis_dataframe

def clean_synopsis(
        synopsis_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """
    Clean the synopsis as a DataFrame object.

    :param synopsis_dataframe: Synopsis as a
        DataFrame object
    :type synopsis_dataframe: pd.DataFrame

    :return: Cleaned synopsis as a DataFrame object
    :rtype: DataFrame
    """
    synopsis = synopsis_dataframe['synopsis'][0]
    synopsis = str(synopsis)
    synopsis = synopsis.strip()

    clean_synopsis = pd.DataFrame({
        "SYNOPSIS": [synopsis]
    })

    return clean_synopsis