from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

#from keyboards import weather_keyboard
from weather import get_weather_city


class WeatherState(StatesGroup):
    waiting_for_city = State()


async def start_handler(message: Message):
    #keyboard = weather_keyboard()
    kb = KeyboardButton(text='Тест')
    keyboard = ReplyKeyboardMarkup(keyboard=[[kb]])
    await message.answer('Привет! Напиши /weather, чтобы получить прогноз погоды:', reaply_markup=keyboard)


async def weather_start_handler(message: Message, state: FSMContext):
    await message.answer("Введите название города:")
    await state.set_state(WeatherState.waiting_for_city)


async def weather_handler(message: Message, state: FSMContext):
    city_name = message.text
    weather_data = get_weather_city(city_name)

    if weather_data:
        response = (
            f"Погода в городе {weather_data['city']}, {weather_data['region']}, {weather_data['country']}:\n"
            f"Температура: {weather_data['temperature']}°C\n"
            f"Состояние: {weather_data['condition']}\n"
            #f"Для наглядности: ![Weather Icon](http://{weather_data['icon']})"
        )
    else:
        response = "Извините, не удалось найти данные о погоде для этого города. Пожалуйста, попробуйте снова."

    await message.answer(response, parse_mode="Markdown")
    await state.set_state()
