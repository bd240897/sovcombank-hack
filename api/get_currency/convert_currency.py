import requests

def convert_currency(from_currency, amount ,to_currency): # имена валют
  
  #from_currency = "USD"
  #amount = "2509"
  #to_currency = "RUB"

  url = "https://api.apilayer.com/exchangerates_data/convert?to=" + to_currency + "&from=" + from_currency + "&amount=" + amount

  payload = {}
  headers= {
    "apikey": "<api-key>"
  }

  response = requests.request("GET", url, headers=headers, data = payload)

  status_code = response.status_code
  result = response.text

  return result # курс валюты
