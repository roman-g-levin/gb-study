import requests
import json
import os
from dotenv import load_dotenv
import pprint

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

api_token = os.getenv('api_token')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

#api_token = "_"
#client_id = "_"
#client_secret = "_"

# Ваши учетные данные API
#client_id = "__"
#client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
lookfor = input("Введите категорию объекта (cafe, fitness, memorial & etc): ")

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": lookfor
}

headers = {
    "Accept": "application/json",
    "Authorization": api_token
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    #print("Успешный запрос API!")
    data = json.loads(response.text)
    places = data["results"]
    for place in places:    
        print("Название:", place["name"])
        print("Адрес:", place["location"]["formatted_address"])
        print("Рейтинг: не обнаружен в выдаче сервера\n\n")
        #print(place)
        #print(type(place))
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
