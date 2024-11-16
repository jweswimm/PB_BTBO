import aiohttp
import asyncio
import datetime as dt
from APIkey import tomorrowio_API_KEY
import IPython

class RealTimeWeather:
    def __init__(self, location=[46.7867, 92.1005], fields= ["temperature", "windSpeed", "windDirection"]):

        #Initialize Params
        self._apikey = tomorrowio_API_KEY

        # Define the URL for the real-time weather data 
        self._realTimeUrl = "https://api.tomorrow.io/v4/weather/realtime"

        #fields = ["temperature", "precipitationProbability", "precipitationType", "windSpeed", "windDirection", "humidity", "cloudCover"]
        self._units = "imperial"

        # Construct the query parameters
        self._params = {
            "location": f"{location[0]},{location[1]}",
            "fields": ",".join(fields),
            "units": self._units,
            "apikey": self._apikey
        }

    async def _getCurrentWeather(self):

        #Use aiohttp to make the asynchronous request
        async with aiohttp.ClientSession() as session:
            async with session.get(self._realTimeUrl, params=self._params) as response:
                if response.status == 200:
                    data = await response.json()
                    data = data["data"]
                    print(data)
                else:
                    print(f"Error: {response.status}, {await response.text()}")

if __name__ == "__main__":

    #Instantiate the RealTimeWeather class
    weather = RealTimeWeather()

    #Run the asynchronous function
    asyncio.run(weather._getCurrentWeather())
