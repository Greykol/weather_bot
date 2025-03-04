import requests

from config import BASE_CURRENT_URL, BASE_FORECAST_URL, WEATHER_API_KEY


def get_weather_city(city: str):
    url = f'{BASE_CURRENT_URL}?key={WEATHER_API_KEY}&q={city}&lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']
        current = data['current']
        weather_info = {
            "city": location["name"],
            "region": location["region"],
            "country": location["country"],
            "temperature": current["temp_c"],
            "condition": current["condition"]["text"],
        }
        return weather_info
    else:
        return None


def get_forecast(city: str, days: int):
    url = f"{BASE_FORECAST_URL}/forecast.json?key={WEATHER_API_KEY}&q={city}&days={days}&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_days = data["forecast"]["forecastday"]
        forecast_text = f"Прогноз погоды в {city} на {days} дней:\n"
        for day in forecast_days:
            date = day["date"]
            temp_min = day["day"]["mintemp_c"]
            temp_max = day["day"]["maxtemp_c"]
            condition = day["day"]["condition"]["text"]
            forecast_text += f"\n📅 {date}: {temp_min}°C - {temp_max}°C, {condition}"
        return forecast_text
    else:
        return "Не удалось получить прогноз."
