from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from weather import get_weather_city, get_forecast
from config import WEATHER_EMOJI
from keyboards import get_forecast_keyboard


class WeatherState(StatesGroup):
    """Класс состояния погоды FSM."""

    waiting_for_city = State()
    choosing_forecast_type = State()


async def start_handler(message: types.Message, state: FSMContext):
    """Обработчик команды /start."""
    await message.answer("Привет! Введите название города, чтобы узнать погоду:")
    await state.set_state(WeatherState.waiting_for_city)


async def weather_handler(message: types.Message, state: FSMContext):
    """Функция обработчика погоды."""
    city_name = message.text
    weather_data = get_weather_city(city_name)
    if weather_data:
        await state.update_data(city=city_name)
        condition = weather_data["condition"].lower()
        emoji = WEATHER_EMOJI.get(condition, "🌍")
        response = (
            f"Погода в городе: {weather_data['city']}, {weather_data['region']}, {weather_data['country']}:\n"
            f"🌡 Температура: {weather_data['temperature']}°C\n"
            f"☁ Состояние: {weather_data['condition']} {emoji}"
        )
        keyboard = get_forecast_keyboard()
        await message.answer(response)
        await message.answer("Выберите прогноз:", reply_markup=keyboard)
        await state.set_state(WeatherState.choosing_forecast_type)
    else:
        await message.answer("Город не найден. Попробуйте снова.")


async def forecast_handler(message: types.Message, state: FSMContext):
    """Функция обработчика выбора прогноза погоды."""
    user_data = await state.get_data()
    city = user_data.get("city")
    if not city:
        await message.answer("Пожалуйста, сначала введите название города.")
        await state.set_state(WeatherState.waiting_for_city)
        return
    if message.text == "Погода на день":
        forecast = get_forecast(city, 1)
    elif message.text == "Погода на 3 дня":
        forecast = get_forecast(city, 3)
    elif message.text == "Погода на 14 дней":
        forecast = get_forecast(city, 14)
    else:
        await message.answer("Выберите один из предложенных вариантов.")
        return
    await message.answer(forecast)
    await state.clear()
