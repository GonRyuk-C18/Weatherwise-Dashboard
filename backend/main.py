from feeders.openweather import OpenWeather
from feeders.meteoblue import MeteoBlue
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    API_KEY1 = os.getenv("OPENWEATHER_API_KEY")
    API_KEY2 = os.getenv("METEOBLUE_API_KEY")

    city_name = "Lisboa"

    client1 = OpenWeather(API_KEY1)
    forecast = client1.get_forecast(city_name)
    client2 = MeteoBlue(API_KEY2)
    forecast2 = client2.get_forecast(38.7169, 9.1399)

    print(f"Previsão para {city_name} via OpenWeather:")
    for f in forecast:
        print(f"{f.date} | {f.temperature}ºC | {f.description}")
    print(f"Previsão para Lisboa via MeteoBlue:")
    for f in forecast2:
        print(f"{f.date} | {f.temperature}ºC")

if __name__ == "__main__":
    main()