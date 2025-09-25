import requests
from backend.models.forecast import Forecast
from backend.models.norm_forecast import NormForecast


class OpenMeteo:
    def __init__(self):
        pass

    def get_forecast(self,latitude,longitude):
        ###url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_probability_mean,wind_speed_10m_mean,precipitation_hours,winddirection_10m_dominant,temperature_2m_mean"
        response = requests.get(url).json()

        normecast = NormForecast('.../Weatherwise-Dashboard/weather_code.txt')
        forecast = []
        try:
            weather_code = response['daily']['weather_code']
            times = response['daily']['time']
            temps = response['daily']['temperature_2m_mean']
            temps_max = response['daily']['temperature_2m_max']
            temps_min = response['daily']['temperature_2m_min']
            uv = response['daily']['uv_index_max']
            precipitation = response['daily']['precipitation_probability_mean']
            precipitation_h = response['daily']['precipitation_hours']
            wind_speed = response['daily']['wind_speed_10m_mean']
            wind_direction = response['daily']['winddirection_10m_dominant']



            for item in range(5):
                forecast.append(Forecast(
                    source="OpenMeteo",
                    date=times[item],
                    temperature=int(temps[item]),
                    temperature_max=int(temps_max[item]),
                    temperature_min=int(temps_min[item]),
                    uv=uv[item],
                    precipitation=precipitation[item],
                    precipitation_h=precipitation_h[item],
                    wind_speed=wind_speed[item],
                    wind_direction=wind_direction[item],
                    description=NormForecast.get_weather_code(normecast,weather_code[item])
                ))
        except KeyError:
            print("Error on interper OpenMeteo.")
        return forecast