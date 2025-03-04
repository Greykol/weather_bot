import os

from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_CURRENT_URL = "http://api.weatherapi.com/v1/current.json"
BASE_FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"
WEATHER_EMOJI = {
    "ясно": "☀️",
    "солнечно": "🌞",
    "переменная облачность": "⛅",
    "облачно": "☁️",
    "пасмурно": "🌫️",
    "дождь": "🌧️",
    "небольшой дождь": "🌧️",
    "небольшой дождь со снегом": "🌧️ ❄️",
    "небольшой снег": "❄️",
    "снег": "❄️",
    "гроза": "⛈️",
    "морось": "🌦️",
    "туман": "🌁",
    "ветрено": "💨"
}
