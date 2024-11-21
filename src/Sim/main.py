import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Telemetry.weather import Weather
from Telemetry.gps import GPS
import IPython
from Vehicle.sailboat import Sailboat
import pandas as pd


if __name__ == "__main__":

    #Instantiate the weather and gps models
    weatherModel = Weather()
    gpsModel = GPS()

    #Update location
    weatherModel._updateLocation(location = gpsModel.getPosition())

    #Run the asynchronous function
    weatherdata = asyncio.run(weatherModel._getCurrentWeather())

    #Instantiate the sailboat model
    sailboat = Sailboat(make = 'Beneteau', model='Oceanis 40', length=12.5, beam=12.83, draft=6.23, mast_height=17.71, mass=10000)

    # Read mass properties from CSV
    mass_properties_df = pd.read_csv('/Users/joewimmergren/Projects/PB_BTBO/src/Sim/data/sailboat_mass_properties_examples.csv')
    mass_properties = mass_properties_df.iloc[0].to_dict()

    # Set mass properties
    sailboat._setVehicleMassProperties(mass_properties)

    # Display sailboat information
    sailboat._display_info()