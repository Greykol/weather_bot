import emoji
import requests
from datetime import datetime

from config import (BASE_CURRENT_URL,
                    BASE_FORECAST_URL,
                    WEATHER_API_KEY,
                    WEATHER_EMOJI_MAP,
                    URL_CATS,
                    URL_DOGS)


def convert_h(time_str: str) -> str:
    """Конвертирует время из формата 12 AM/PM в 24-часовой формат."""
    return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")


def get_weather_emoji(condition: str) -> str:
    """Возвращает эмодзи на основе погодного состояния."""
    emoji_alias = WEATHER_EMOJI_MAP.get(condition.lower(), ":earth_americas:")
    return emoji.emojize(emoji_alias, language="alias")


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
            "wind": current["wind_kph"],
            "gust": current["gust_mph"],
            "humidity": current["humidity"],
            "pressure": current["pressure_mb"],
            "condition": current["condition"]["text"],
        }
        return weather_info
    else:
        return None


def get_hour_forecast(city: str):
    url = f"{BASE_FORECAST_URL}?key={WEATHER_API_KEY}&q={city}&days=1&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_hours = data["forecast"]["forecastday"][0]["hour"]
        forecast_text = f"Почасовой прогноз в {city}:\n"
        for hour in forecast_hours:
            time = hour["time"].split(" ")[1]
            temp = hour["temp_c"]
            condition = hour["condition"]["text"]
            wind = hour["wind_kph"]
            cloud = hour["cloud"]
            forecast_text += (
                f"\n🕒 Время: {time}\n"
                f"Температура: {temp}°C\n"
                f"Состояние: {condition}\n"
                f"Ветер {wind} км/ч\n"
                f"Облачность: {cloud}%\n"
            )
        return forecast_text
    else:
        return "Не удалось получить почасовой прогноз."


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
            chance_rain = day["day"]["daily_chance_of_rain"]
            sunrise = convert_h(day["astro"]["sunrise"])
            sunset = convert_h(day["astro"]["sunset"])
            condition = day["day"]["condition"]["text"]
            forecast_text += (
                f"\n📅 Дата: {date}\n"
                f"🌡 Температура: {temp_min}°C - {temp_max}°C\n"
                f"🌧 Вероятность дождя: {chance_rain}%\n"
                f"🌅 Восход солнца: {sunrise}\n"
                f"🌇 Заход солнца: {sunset}\n"
                f"☁ Состояние: {condition}\n"
            )
        return forecast_text
    else:
        return "Не удалось получить прогноз."


def get_new_image():
    try:
        response = requests.get(URL_CATS)
        response.raise_for_status()
    except Exception as error:
        print(f"Ошибка при запросе к {URL_CATS}: {error}")
        try:
            response = requests.get(URL_DOGS)
            response.raise_for_status()
        except Exception as error:
            print(f"Ошибка при запросе к {URL_DOGS}: {error}")
            return None
    data = response.json()
    if not data or not isinstance(data, list) or "url" not in data[0]:
        print("Некорректный формат ответа API:", data)
        return None
    return data[0]["url"]
