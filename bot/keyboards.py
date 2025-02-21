from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def weather_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    weather_button = InlineKeyboardButton('Получить прогноз погоды',
                                          callback_data='get_weather')
    keyboard.add(weather_button)
    return keyboard
