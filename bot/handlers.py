from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from weather import (get_weather_city,
                     get_forecast,
                     get_weather_emoji,
                     get_new_image)
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
        emoji_icon = get_weather_emoji(condition)
        response = (
            f"Погода в городе: {weather_data['city']}, {weather_data['region']}, {weather_data['country']}:\n"
            f"{get_weather_emoji('температура')} Температура: {weather_data['temperature']}°C\n"
            f"{get_weather_emoji('ветер')} Ветер: {weather_data['gust']} м/с\n"
            f"{get_weather_emoji('влажность')} Влажность: {weather_data['humidity']}%\n"
            f"{get_weather_emoji('давление')} Давление: {weather_data['pressure']} мм рт. ст.\n"
            f"{emoji_icon} Состояние: {weather_data['condition']}"
        )
        keyboard = get_forecast_keyboard()
        await message.answer(response)
        await message.answer("Выберите прогноз:", reply_markup=keyboard)
        await state.set_state(WeatherState.choosing_forecast_type)
    else:
        await message.answer("Город не найден. Попробуйте снова.")


async def forecast_handler(callback_query: types.CallbackQuery,
                           state: FSMContext):
    """Функция обработчика выбора прогноза погоды (callback)."""
    user_data = await state.get_data()
    city = user_data.get("city")


    try:
        days = int(callback_query.data.split("_")[1])
    except ValueError:
        await callback_query.message.answer("Ошибка обработки данных.")
        return

    forecast = get_forecast(city, days)
    await callback_query.message.answer(forecast)
    await state.clear()
    await callback_query.answer()


async def image_handler(callback_query: types.CallbackQuery):
    """Функция обработчика кнопки, отправляющей картинку."""
    image_url = get_new_image()
    if image_url:
        await callback_query.message.answer_photo(photo=image_url)
    else:
        await callback_query.message.answer("Не удалось загрузить картинку.")
    await callback_query.answer()
