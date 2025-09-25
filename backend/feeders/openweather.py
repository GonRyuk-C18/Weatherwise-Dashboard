import requests
from backend.models.forecast import Forecast

class OpenWeather:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, city_name):
        ###url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.key}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={6}&appid={self.key}&units=metric"
        response = requests.get(url).json()

        forecast = []

        try:
            weather_code = response['weather']['description']
            times = response['dt_txt']
            temps = response['temp']['day']
            temps_max = response['temp']['max']
            temps_min = response['temp']['min']
            precipitation = response['pop']
            wind_speed = response['speed']
            wind_direction = response['deg']

            for item in response['list'][:5]:
                forecast.append(Forecast(
                    source="OpenWeather",
                    date=times[item],
                    temperature=temps[item],
                    temperature_max=temps_max[item],
                    temperature_min=temps_min[item],
                    uv=uv[item],
                    precipitation=precipitation[item],
                    precipitation_h=precipitation_h[item],
                    wind_speed=wind_speed[item],
                    wind_direction=wind_direction[item],
                    description=weather_code[item]

             ))
        except KeyError:
            print("Error on interper OpenWeather.")
        return forecast