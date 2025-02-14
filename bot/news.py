import requests
from config import NEWS_API_KEY


def fetch_news(category: str):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["articles"]
    else:
        return []
