import requests


async def get_weather_data(city: str):
    api_key = '9c41b513b71c4a5687881836251202'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp'] - 273.15
    weather_description = data['weather'][0]['description']
    return f"Погода в {city}: {weather_description}, температура: {temp:.2f}°C"
