import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config import TELEGRAM_TOKEN
from handlers import (start_handler,
                      weather_handler,
                      forecast_handler,
                      image_handler)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()


dp.message.register(start_handler, Command("start"))
dp.message.register(weather_handler)
dp.callback_query.register(forecast_handler,
                           lambda c: c.data.startswith("forecast_"))
dp.callback_query.register(image_handler,
                           lambda c: c.data == "send_image")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
