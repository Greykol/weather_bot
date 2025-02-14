from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_city_keyboard():
    cities = ['Moscow', 'London', 'New-York']
    keyboard = InlineKeyboardMarkup(row_width=3)
    for city in cities:
        button = InlineKeyboardButton(text=city, callback_data=city)
        keyboard.add(button)
    return keyboard
