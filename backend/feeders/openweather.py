import request
from models.forecast import Forecast

class OpenWeather:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, ciy_name):
        url = None #need to put here the URL
        response = request.get(url).json()

        forecast = []
        for item in response['list'][:5]:
            forecast.append(Forecast(
                source="OpenWeather",
                date=item['dt_dxt'],
                temperature=item['main']['temp'],
                description=item['weather'][0]['description']
            ))
        return forecast