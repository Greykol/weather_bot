import requests

from config import BASE_URL, WEATHER_API_KEY


def get_weather_city(city: str):
    url = f'{BASE_URL}?key={WEATHER_API_KEY}&q={city}&lang=ru'
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
            "icon": current["condition"]["icon"]
        }
        return weather_info
    else:
        return None
