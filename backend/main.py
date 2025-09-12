from feeders.openweather import OpenWeather
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    city_name = "Lisboa"

    client = OpenWeather(API_KEY)
    forecast = client.get_forecast(city_name)

    print(f"Previsão para {city_name} via OpenWeather:")
    for f in forecast:
        print("f{f.date | {f.temperature}ºC | {f.description}")

if __name__ == "__main__":
    main()