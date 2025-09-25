import requests
from collections import defaultdict
from datetime import datetime
from backend.models.forecast import Forecast

class OpenWeather:
    def __init__(self, key):
        self.key = key

    def get_forecast(self, city_name):
        ###url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.key}&units=metric"
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={self.key}&units=metric"
        response = requests.get(url).json()


        forecast = []
        group_day = defaultdict(list)

        for item in response['list']:
            day = datetime.fromtimestamp(item['dt']).date()
            group_day[day].append(item)

        day_forecast_data = []
        for day, items in list(group_day.items())[:5]:
            weather_code = [e['weather'][0]['description'] for e in items]
            temps = [e['main']['temp'] for e in items]
            temps_max = [e['main']['temp_max'] for e in items]
            temps_min = [e['main']['temp_min'] for e in items]
            pops = [e.get('pop',0) for e in items]
            wind_speed = [e['wind']['speed'] for e in items]
            wind_direction = [e['wind']['deg'] for e in items]

            day_forecast_data.append({
                'date':str(day),
                'temperature':int(int(max(temps_max))),
                'temperature_max':int(max(temps_max)),
                'temperature_min':int(min(temps_min)),
                'wind_speed':round(sum(wind_speed)/len(wind_speed),1),
                'wind_direction':round(sum(wind_direction)/len(wind_direction),1),
                'precipitation':round(sum(pops)/len(pops),2),
                'description':max(set(weather_code), key=weather_code.count)

            })

        for item in day_forecast_data:
            forecast.append(Forecast(
                source="OpenWeather",
                date=item['date'],
                temperature=item['temperature'],
                temperature_max=item['temperature_max'],
                temperature_min=item['temperature_min'],
                uv=None,
                precipitation=item['precipitation'],
                precipitation_h=None,
                wind_speed=item['wind_speed'],
                wind_direction=item['wind_direction'],
                description=item['description'],

            ))

        return forecast