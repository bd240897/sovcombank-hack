import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=CNY&from=EUR&amount=5"

payload = {}
headers= {
  "apikey": "JJNdsqUntjo5Q5yjQNAOR353F7D6rlxJ"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)