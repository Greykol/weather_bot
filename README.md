# Проект weather_bot


## Описание проекта:

Проект бота в телеграм для отслеживания погоды на базе фреймворка aiogram.
Данные по погоде беруться из API weather. В боте можно получить прогноз погоды введя название города, далее можно выбрать:
- Получить прогноз погоды на день;
- Получить почасовой прогноз погоды;
- Получить прогноз на три дня.


## Как запустить проект:


1. Клонировать репозиторий  командной строке:
  ```
  git clone git@github.com:Greykol/weather_bot.git
  ```
2. Перейти в него:
  ```
  cd weather_bot
  ```
3. Cоздать виртуальное окружение:
  ```
  python3 -m venv env
  ```
4. Активировать виртуальное окружение:
  ```
  source env/bin/activate
  ```
5. Установить зависимости из файла requirements.txt:
  ```
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
6. Создать в папке .env.
   Для работы API надо зарегистрироваться на 
   ```
   https://www.weatherapi.com/
   ```
   После добавить ключ в .env и туда же id бота.

7. Запустить проект:
  ```
  python main.py
  ```