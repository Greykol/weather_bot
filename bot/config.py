import os
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
WEATHER_EMOJI = {
    "ясно": "☀️",
    "солнечно": "🌞",
    "переменная облачность": "⛅",
    "облачно": "☁️",
    "пасмурно": "🌫️",
    "дождь": "🌧️",
    "небольшой снег": "❄️",
    "снег": "❄️",
    "гроза": "⛈️",
    "морось": "🌦️",
    "туман": "🌁",
    "ветрено": "💨"
}
