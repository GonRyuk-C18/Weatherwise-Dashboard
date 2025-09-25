class NormForecast:
    def __init__(self, txt_path):
        self.txt_path = txt_path

    def get_weather_code(self, codigo):
        text_anc= f'### {codigo}'
        text_anc_found = ""
        found = False

        try:
            with open(self.txt_path, "r", encoding="utf-8") as f:
                lines=f.readlines()
                for i, line in enumerate(lines):
                    text_anc_found = lines[i+1].strip()
                    found=True
                    break
        except FileNotFoundError:
            print('File not found')
        return text_anc_found