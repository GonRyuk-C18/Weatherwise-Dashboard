import requests
from backend.models.forecast import Forecast

class OpenWeather:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, city_name):
        ###url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.key}&units=metric"
        url = f"api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={6}&appid={self.key}&units=metric"
        response = requests.get(url).json()

        forecast = []
        for item in response['list'][:5]:
            forecast.append(Forecast(
                source="OpenWeather",
                date=item['dt_txt'],
                temperature=item['temp']['day'],
                temperature_max=item['temp']['max'],
                temperature_min=item['temp']['min'],
                uv=None,
                precipitation=item['pop'],
                precipitation_h=None,
                wind_speed=item['speed'],
                wind_direction=item['deg'],
                description=item['weather']['description']

            ))
        return forecast