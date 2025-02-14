from aiogram.types import Message


async def start_handler(message: Message):
    await message.answer('Привет! Напиши /weather, чтобы получить прогноз погоды')


async def weather_handler(message: Message):
    await message.answer('Пока тест')