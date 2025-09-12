import requests
from backend.models.forecast import Forecast

class OpenWeather:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, city_name):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.key}&units=metric"
        response = requests.get(url).json()

        forecast = []
        for item in response['list'][:5]:
            forecast.append(Forecast(
                source="OpenWeather",
                date=item['dt_txt'],
                temperature=item['main']['temp'],
                description=item['weather'][0]['description']
            ))
        return forecast