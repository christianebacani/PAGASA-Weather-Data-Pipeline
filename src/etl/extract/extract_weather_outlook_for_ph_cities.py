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