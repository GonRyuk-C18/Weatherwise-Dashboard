import requests
from backend.models.forecast import Forecast

class OpenMeteo:
    def __init__(self):
        pass
    def get_forecast(self,latitude,longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=auto"
        response = requests.get(url).json()

        forecast = []
        try:
            times = response['hourly']['time']
            temps = response['hourly']['temperature_2m']

            for item in range(5):
                forecast.append(Forecast(
                    source="OpenMeteo",
                    date=times[item],
                    temperature=temps[item],
                    description=None
                ))
        except KeyError:
            print("Error on interper OpenMeteo.")
        return forecast