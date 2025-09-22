import requests
from backend.models.forecast import Forecast

class MeteoBlue:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, latitude, longitude):
        url = f"https://my.meteoblue.com/packages/basic-day?lat={latitude}&lon={longitude}&apikey={self.key}&format=json"
        response = requests.get(url).json()

        forecast = []
        try:
            times = response['data_day']['time']
            temps = response['data_day']['temperature_mean']
            temps_max = response['data_day']['temperature_max']
            temps_min = response['data_day']['temperature_min']
            uv = response['data_day']['uvindex']
            precipitation = response['data_day']['precipitation_probability']
            precipitation_h = response['data_day']['precipitation_hours']
            wind_speed = response['data_day']['windspeed']
            wind_direction = response['data_day']['winddirection']
            descriptions = response['data_day']['pictocode']

            for item in range(5):
                forecast.append(Forecast(
                    source="MeteoBlue",
                    date=times[item],
                    temperature=temps[item],
                    temperature_max=temps_max[item],
                    temperature_min=temps_min[item],
                    uv=uv[item],
                    precipitation=precipitation[item],
                    precipitation_h=precipitation_h[item],
                    wind_speed=wind_speed[item],
                    wind_direction=wind_direction[item],
                    description=descriptions[item]
                ))
        except KeyError:
            print("Error on interper MeteoBlue.")
        return forecast