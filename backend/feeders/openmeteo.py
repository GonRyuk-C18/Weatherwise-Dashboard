import requests
from backend.models.forecast import Forecast

class OpenMeteo:
    def __init__(self):
        pass
    def get_forecast(self,latitude,longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
        response = requests.get(url).json()

        forecast = []
        try:
            times = response['daily']['time']
            temps_max = response['daily']['temperature_2m_max']
            temps_min = response['daily']['temperature_2m_min']


            for item in range(5):
                forecast.append(Forecast(
                    source="OpenMeteo",
                    date=times[item],
                    temperature=None,
                    temperature_max=temps_max[item],
                    temperature_min=temps_min[item],
                    description=None
                ))
        except KeyError:
            print("Error on interper OpenMeteo.")
        return forecast