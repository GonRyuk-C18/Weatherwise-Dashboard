class NormForecast:
    def __init__(self, txt_path):
        self.txt_path = txt_path

    def get_weather_code(self, codigo):
        text_anc= f'### {codigo}'
        text_anc_found = ""
        found = False