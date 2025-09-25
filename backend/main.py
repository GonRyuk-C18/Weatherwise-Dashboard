from flask import Flask, jsonify
from flask_cors import CORS
from feeders.openweather import OpenWeather
from feeders.meteoblue import MeteoBlue
from feeders.openmeteo import OpenMeteo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/api/forecast")
def get_forecast():
    latitude = 38.7169
    longitude = -9.1399

    openweather = OpenWeather(os.getenv("OPENWEATHER_API_KEY"))
    openmeteo = OpenMeteo()
    meteoblue = MeteoBlue(os.getenv("METEOBLUE_API_KEY"))

    forecasts = {
        "OpenWeather": [f.__dict__ for f in openweather.get_forecast("Lisboa")],
        "OpenMeteo": [f.__dict__ for f in openmeteo.get_forecast(latitude, longitude)],
        "MeteoBlue": [f.__dict__ for f in meteoblue.get_forecast(latitude, longitude)]

    }
    return jsonify(forecasts)

'''if __name__ == "__main__":
    app.run(debug=True)
'''


###Para teste no terminal
def main():
    load_dotenv()
    API_KEY1 = os.getenv("OPENWEATHER_API_KEY")
    API_KEY2 = os.getenv("METEOBLUE_API_KEY")

    city_name = "Lisboa"

    client1 = OpenWeather(API_KEY1)
    forecast = client1.get_forecast(city_name)
    client2 = MeteoBlue(API_KEY2)
    forecast2 = client2.get_forecast(38.7169, 9.1399)
    client3 = OpenMeteo()
    forecast3 = client3.get_forecast(38.7169, 9.1399)

    print(f"Previsão para {city_name} via OpenWeather:")
    for f in forecast:
        print(f"{f.date} | {f.temperature}ºC | {f.description}")
    print(f"Previsão para Lisboa via MeteoBlue:")
    for f in forecast2:
        print(f"{f.date} | {f.temperature}ºC")
    print(f"Previsão para Lisboa via OpenMeteo:")
    for f in forecast3:
        print(f"{f.date} | {f.temperature}ºC")


if __name__ == "__main__":
    main()
