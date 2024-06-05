def analyze_conditions(weather_data):
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    return f"Current temperature is {temp}°C and the sky is {description}."
