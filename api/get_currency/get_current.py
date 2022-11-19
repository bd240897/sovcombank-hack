import requests

display_currency = "RUB"
base_currency = "EUR"

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=" + display_currency + "&base=" + base_currency

payload = {}
headers= {
  "apikey": "<api-key>"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(url)
