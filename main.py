import requests
from config import *
from pprint import pprint

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&APPID=" + API_key

weatherData = requests.get(requestUrl).json()

temp = weatherData['main']['temp']

print("Weather For", city)
print("Temp:", + temp)
print('\n')
pprint(weatherData)
