import os
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
FORECA_API_KEY = os.getenv("FORECA_API_KEY")
