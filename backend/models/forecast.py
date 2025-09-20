class Forecast:
    def __init__(self, source, date, temperature, temperature_max, temperature_min, uv, precipitation, precipitation_h, wind_speed, wind_direction, description):
        self.source = source
        self.date = date
        self.temperature = temperature
        self.temperature_max = temperature_max
        self.temperature_min = temperature_min
        self.uv = uv
        self.precipitation = precipitation
        self.precipitation_h = precipitation_h
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.description = description