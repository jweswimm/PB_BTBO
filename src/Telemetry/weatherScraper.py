import requests
import datetime as dt
from APIkey import tomorrowio_API_KEY
import IPython

class weatherScraper:
    def __init__(self):
        print('Testing')
        self._apikey = tomorrowio_API_KEY

    def _getCurrentWeather(self):
        realTimeUrl = "https://api.tomorrow.io/v4/weather/realtime"
        # lat lon pair for Duluth MN
        location = [46.7867, 92.1005]

        fields = ["temperature", "precipitationProbability", "precipitationType", "windSpeed", "windDirection", "humidity", "cloudCover"]
        units = "imperial"

        # Construct the query parameters
        params = {
            "location": f"{location[0]},{location[1]}",
            "fields": ",".join(fields),
            "units": units,
            "apikey": self._apikey
        }

        # Make the GET request
        response = requests.get(realTimeUrl, params=params)
        
        if response.status_code == 200:
            data = response.json()
            IPython.embed()
            data = data["data"]
            print(data)
        else:
            print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    weatherobj = weatherScraper()
    weatherobj._getCurrentWeather()