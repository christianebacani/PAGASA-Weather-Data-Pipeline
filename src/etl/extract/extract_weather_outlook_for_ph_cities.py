'''
    Module to extract weather outlook for
    selected Philippine cities from the
    data/raw subdirectory on the local machine.
'''
import pandas as pd
import os

def create_subdir(
) -> None:
    '''
        Creates the
        data/stage/weather_outlook_for_ph_cities/
        subdirectory to store CSV files for
        weather outlook for selected Philippine
        cities from the data/raw subdirectory
        on the local machine.
    '''
    # Create the data/stage/weather_outlook_for_ph_cities/ subdirectory if it doesn't exist
    if not os.path.exists('data/stage/weather_outlook_for_ph_cities'):
        os.makedirs('data/stage/weather_outlook_for_ph_cities')

def parse_issued_datetime_to_dataframe(
        issued_datetime_filepath: str
) -> pd.DataFrame:
    '''
    Parses the issued datetime from JSON
    file into a DataFrame object.

    :param issued_datetime_filepath: Relative
        filepath of the JSON file that contains
        the issued datetime of the weather
        outlook for selected Philippine
        cities
    :type issued_datetime_filepath: str

    :return: Issued datetime of the weather
        outlook for selected Philippine cities
        as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the issued datetime JSON file as a Pandas Series
    issued_datetime_raw_dataframe = pd.read_json(issued_datetime_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    issued_datetime_dataframe = pd.DataFrame({
        'issued_datetime': [
            issued_datetime_raw_dataframe['issued_datetime']
        ]
    })

    return issued_datetime_dataframe