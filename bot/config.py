import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_CURRENT_URL = "http://api.weatherapi.com/v1/current.json"
BASE_FORECAST_URL = "http://api.weatherapi.com/v1/forecast.json"
URL_CATS = 'https://api.thecatapi.com/v1/images/search'
URL_DOGS = 'https://api.thedogapi.com/v1/images/search'
WEATHER_EMOJI_MAP = {
    "ясно": ":sun:",
    "солнечно": ":sun_with_face:",
    "переменная облачность": ":partly_sunny:",
    "облачно": ":cloud:",
    "пасмурно": ":fog:",
    "дождь": ":cloud_with_rain:",
    "небольшой дождь": ":cloud_with_rain:",
    "небольшой дождь со снегом": ":cloud_with_rain: :snowflake:",
    "небольшой снег": ":snowflake:",
    "снег": ":snowman:",
    "гроза": ":cloud_with_lightning_and_rain:",
    "морось": ":umbrella_with_rain_drops:",
    "туман": ":foggy:",
    "ветрено": ":dash:",
    "температура": ":thermometer:",
    "ветер": ":wind_face:",
    "влажность": ":droplet:",
    "давление": ":compression:"
}
