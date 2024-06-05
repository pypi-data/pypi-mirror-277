import json

def save_weather_data(data, filename="weather_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)
