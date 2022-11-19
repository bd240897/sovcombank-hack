import requests


api_key = 'F8CvWt7D883XszhAKhTAgX4NNi8AwtJ3'


def get_currency(display_currency, base_currency):  # имена валют

    # display_currency = "RUB"
    # base_currency = "EUR"

    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=" + display_currency + "&base=" + base_currency

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    return result  # курс валюты


def convert_currency(from_currency, amount, to_currency):  # имена валют

    # from_currency = "USD"
    # amount = "2509"
    # to_currency = "RUB"

    url = "https://api.apilayer.com/exchangerates_data/convert?to=" + to_currency + "&from=" + from_currency + "&amount=" + amount

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    return result  # курс валюты
