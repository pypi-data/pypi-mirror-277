def parse_weather(data):
    try:
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': data['name']
        }
        return weather
    except KeyError as e:
        return {"error": f"Key missing in response: {str(e)}"}
