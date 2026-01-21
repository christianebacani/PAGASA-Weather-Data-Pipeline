"""
Docstring for etl.extract.extract_daily_weather_forecast
"""
import snowflake.connector as snowflake

def connect(
        user: str,
        password: str,
        account: str,
        warehouse: str
) -> snowflake.SnowflakeConnection:
    """
    Establish a connection to interact
    with Snowflake using the provided
    credentials and warehouse configuratiohn
    as a parameter.

    :param user: Snowflake username
    :type user: str

    :param password: Snowflake password
    :type password: str

    :param account: Snowflake account identifier
    :type account: str

    :param warehouse: Snowflake Data Warehouse
        name
    :type warehouse: str

    :return: Active Snowflake connection object
    :rtype: SnowflakeConnection
    """