import requests
from APIkey import tomorrowio_API_KEY

class weatherScraper:
    def __init__(self):
        print('Testing')

        url = "https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey=a7nOway2UAAoysDeJU1ooToEqoo7d0e1"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        print(response.text)
    

if __name__ == "__main__":
    weatherScraper()