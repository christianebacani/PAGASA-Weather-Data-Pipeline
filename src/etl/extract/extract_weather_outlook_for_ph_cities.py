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