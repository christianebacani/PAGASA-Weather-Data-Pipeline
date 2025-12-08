'''
    Module for executing extraction functions for the
    selected Philippine cities data from the data/raw
    subdirectory on the local machine.
'''
from etl.extract.extract_weather_outlook_for_ph_cities import create_subdir

def ingest_weather_outlook_for_ph_cities(
) -> None:
    '''
        Extracts the weather outlook for selected
        Philippine cities from the data/raw
        subdirectory on the local machine by
        executing all functions in the
        extract_weather_outlook_for_ph_cities
        module of the src/ingest package.
    '''
    # Run all functions to ingest weather advisory data
    create_subdir()