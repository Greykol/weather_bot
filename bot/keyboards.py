from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_forecast_keyboard():
    """Функция создаёт inline-клавиатуру с вариантами прогноза погоды."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Погода на день",
                                 callback_data="forecast_1"),
            InlineKeyboardButton(text="Погода на 3 дня",
                                 callback_data="forecast_3")
        ],
        [
            InlineKeyboardButton(text="Погода на 14 дней",
                                 callback_data="forecast_14")
        ],
        [
            InlineKeyboardButton(text="Милота дня",
                                 callback_data="send_image")
        ]
    ])
    return keyboard
