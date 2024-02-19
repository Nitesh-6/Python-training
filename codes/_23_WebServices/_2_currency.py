'''
f53e226fefbc98cf5a25908c
Endpoint:

GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/history/USD/YEAR/MONTH/DAY
'''
import requests

url = "https://v6.exchangerate-api.com/v6/f53e226fefbc98cf5a25908c/latest/USD"
response = requests.get(url)
print("Authentication  :", response)
url = "https://v6.exchangerate-api.com/v6/f53e226fefbc98cf5a25908c/quota"
response = requests.get(url)

response = requests.get(url)

print("Response  : ", response)
print("Response2 :", response.json())
