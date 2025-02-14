import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.filters import Command

from config import TELEGRAM_TOKEN
from handlers import start_handler, weather_handler

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)

dp = Dispatcher()


dp.message.register(start_handler, Command("start"))
dp.message.register(weather_handler, Command("weather"))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
