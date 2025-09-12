import requests
from backend.models.forecast import Forecast

class MeteoBlue:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, latitude, longitude):
        url = f"https://my.meteoblue.com/packages/basic-1h?lat={latitude}&lon={longitude}&apikey={self.key}&format=json"
        response = requests.get(url).json()

        forecast = []
        try:
            times = response['data_1h']['time']
            temps = response['data_1h']['temperature']
            #descriptions = response['data_1h']['weather']['icon']

            for item in range(5):
                forecast.append(Forecast(
                    source="MeteoBlue",
                    date=times[item],
                    temperature=temps[item],
                    description=None
                ))
        except KeyError:
            print("Error on interper MeteoBlue.")
        return forecast