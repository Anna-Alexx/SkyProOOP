import datetime
import json

# Напомним условия задачи.
# Необходимо написать программу, которая запрашивает в консоли название валюты, выводит курс валюты к рублю в консоль и сохраняет следующие параметры в JSON-файл:
# время запроса,валюту,курс валюты к рублю.
# Полностью код задачи будет следующий:

import json
import os
from datetime import datetime

import requests

CURRENCY_RATES_FILE = "currency_rates.json"
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')


def get_currency_rate(currency: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float"""

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в JSON-файл"""
