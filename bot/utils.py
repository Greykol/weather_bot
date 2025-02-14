import requests


def fetch_weather_data(city: str, api_key: str):
    url = f"https://api.foreca.net/weather/today/{city}"
    params = {"apikey": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
