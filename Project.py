import requests

def get_weather(city, date):
    api_key = '6cb5e39318d3ed8e64cbf68c04ca1d40'  #API-ключ OpenWeatherMap

    # Формування URL-адреси запиту до API OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # Виконання запиту та отримання відповіді
    response = requests.get(url)
    data = response.json()

    # Перевірка статусу відповіді
    if response.status_code == 200:
        # Отримання потрібних погодних даних
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']

        # Виведення погоди
        print(f'Погода в місті {city} на дату {date}:')
        print(f'Стан погоди: {weather}')
        print(f'Температура: {temperature}°C')
    else:
        print('Помилка отримання погодних даних')

# Приклад використання
city = input("Введіть назву міста: ")
date = input("Введіть дату (у форматі yyyy-mm-dd): ")

get_weather(city, date)
