from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_forecast_keyboard():
    """Функция клавиатуры с вариантами прогноза погоды."""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Погода на день"),
             KeyboardButton(text="Погода на 3 дня")],
            [KeyboardButton(text="Погода на 14 дней")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите тип прогноза"
    )
    return keyboard
