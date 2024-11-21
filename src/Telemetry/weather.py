from Telemetry.APIkey import tomorrowio_API_KEY
from Telemetry.gps import GPS
import aiohttp
import asyncio

class Weather:
    def __init__(self):
        # Initialize Params
        self._apikey = tomorrowio_API_KEY

        # Define the URL for the real-time weather data
        self._realTimeUrl = "https://api.tomorrow.io/v4/weather/realtime"

        # fields = ["temperature", "precipitationProbability", "precipitationType", "windSpeed", "windDirection", "humidity", "cloudCover"]
        self._units = "imperial"

        # Construct the query parameters
        self._params = {
            "units": self._units,
            "apikey": self._apikey
        }

    def _updateLocation(self, location):
        # Update the _params dictionary with the new location
        self._params.update({"location": f"{location[0]},{location[1]}"})

    async def _getCurrentWeather(self):

        # Use aiohttp to make the asynchronous request
        async with aiohttp.ClientSession() as session:
            async with session.get(self._realTimeUrl, params=self._params) as response:
                if response.status == 200:
                    data = await response.json()
                    data = data["data"]
                else:
                    print(f"Error: {response.status}, {await response.text()}")
                    data = None

        return data

if __name__ == "__main__":
    # Instantiate the Weather and GPS classes
    weatherModel = Weather()
    gpsModel = GPS()

    # Update location
    weatherModel._updateLocation(location=gpsModel.getPosition())

    # Run the asynchronous function
    asyncio.run(weatherModel._getCurrentWeather())