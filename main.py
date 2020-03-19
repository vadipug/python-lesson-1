import requests
import json

url = 'https://www.cbr.ru/currency_base/daily/?date_req=20.03.2020'
response = requests.get(url)
data = json.loads(response.text)
print (data)


