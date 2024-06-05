def calculate_average_temperature(data):
    temperatures = [day['temperature'] for day in data if 'temperature' in day]
    return sum(temperatures) / len(temperatures) if temperatures else None
