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
    Creates the data/stage/weather_outlook_for_ph_cities/
    subdirectory to store CSV files for weather outlook
    for selected Philippine cities from the data/raw
    subdirectory on the local machine.
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

def stage_issued_datetime_dataframe(
        issued_datetime_dataframe: pd.DataFrame
) -> None:
    '''
    Stages the issued datetime of the weather outlook
    for selected Philippine cities as a DataFrame
    object to the data/stage/weather_outlook_for_ph_cities
    subdirectory on the local machine.

    :param issued_datetime_dataframe: Issued datetime
        of the weather outlook for selected Philippine
        cities as a DataFrame
        object
    :type issued_datetime_dataframe: pd.DataFrame
    '''
    # Stage the issued datetime DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_cities/issued_datetime.csv'
    issued_datetime_dataframe.to_csv(target_filepath, index=False)

def parse_valid_period_to_dataframe(
        valid_period_filepath: str
) -> pd.DataFrame:
    '''
    Parses the valid period from JSON
    file into a DataFrame object.

    :param valid_period_filepath: Relative
        filepath of the JSON file that contains
        the valid period of the weather outlook
        for selected Philippine cities
    :type valid_period_filepath: str

    :return: Valid period of the weather
        outlook for selected Philippine cities
        as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the valid period JSON file as a Pandas Series
    valid_period_raw_dataframe = pd.read_json(valid_period_filepath, typ='series')
    # Parse the Pandas Series as a DataFrame object
    valid_period_dataframe = pd.DataFrame({
        'valid_period': [
            valid_period_raw_dataframe['valid_period']
        ]
    })

    return valid_period_dataframe

def stage_valid_period_dataframe(
        valid_period_dataframe: pd.DataFrame
) -> None:
    '''
    Stages the valid period of the weather outlook
    for selected Philippine cities as a DataFrame
    objet to the data/stage/weather_outlook_for_ph_cities
    subdirectory on the local machine.

    :param valid_period_dataframe: Valid period of the
        weather outlook for selected Philippine cities
        as a DataFrame object
    :type valid_period_dataframe: pd.DataFrame
    '''
    # Stage the valid period DataFrame object to the target filepath
    target_filepath = 'data/stage/weather_outlook_for_ph_cities/valid_period.csv'
    valid_period_dataframe.to_csv(target_filepath, index=False)

def parse_ph_cities_weather_outlook_to_dataframe(
        ph_cities_weather_outlook_filepath: str
) -> None:
    '''
    Parses the weather outlook for selected
    Philippine cities from JSON file into a
    DataFrame object.

    :param ph_cities_weather_outlook_filepath:
        Relative filepath of the JSON file that
        contains the weather outlook for selected
        Philippine cities
    :type ph_cities_weather_outlook_filepath: str

    :return: Weather outlook for selected Philippine
        cities as a DataFrame object
    :rtype: DataFrame
    '''
    # Read the PH cities weather outlook JSON file as a DataFrame object
    ph_cities_weather_outlook_raw_dataframe = pd.read_json(ph_cities_weather_outlook_filepath)

    # Restructure the PH cities weather outlook DataFrame to make it readable
    ph_cities_weather_outlook_dict = {
        'ph_city': [],
        'weather_date': [],
        'minimum_temperature': [],
        'maximum_temperature': [],
        'chance_of_rain_percentage': []
    }

    # Using for-loop to access and restructure all the data from PH cities weather outlook DataFrame
    for ph_city, weather_outlook_dict in ph_cities_weather_outlook_raw_dataframe.items():
        for _ in range(5):
            ph_cities_weather_outlook_dict['ph_city'].append(ph_city)

        for column_name, weather_outlooks in weather_outlook_dict.items():
            for weather_outlook in weather_outlooks:
                if column_name == 'weather_dates':
                    ph_cities_weather_outlook_dict['weather_date'].append(
                        weather_outlook
                    )

                elif column_name == 'chance_of_rain_percentages':
                    ph_cities_weather_outlook_dict['chance_of_rain_percentage'].append(
                        weather_outlook
                    )

                else:
                    ph_cities_weather_outlook_dict['minimum_temperature'].append(
                        weather_outlook[0]
                    )
                    ph_cities_weather_outlook_dict['maximum_temperature'].append(
                        weather_outlook[1]
                    )

    ph_cities_weather_outlook_dataframe = pd.DataFrame(ph_cities_weather_outlook_dict)

    return ph_cities_weather_outlook_dataframe

def stage_ph_cities_weather_outlook_dataframe(
        ph_cities_weather_outlook_dataframe: pd.DataFrame       
) -> None:
    '''
    Stages the weather outlook for selected Philippine
    cities as a DataFrame object to the
    data/stage/weather_outlook_for_ph_cities subdirectory
    on the local machine.

    :param ph_cities_weather_outlook_dataframe: Weather
        outlook for selected Philippine cities as a
        DataFrame object
    :type ph_cities_weather_outlook_dataframe: pd.DataFrame
    '''