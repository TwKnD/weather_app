import requests
from config import *
from pprint import pprint

# TODO: swap request mode to XML for more data.

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&units=metric" + "&APPID=" + API_key

weatherData = requests.get(requestUrl).json()

tempNow = weatherData['main']['temp']
tempMax = weatherData['main']['temp_max']
tempMin = weatherData['main']['temp_min']
windDir = weatherData['wind']['deg']
windSpeed = weatherData['wind']['speed']


print("Weather For", city)
print("Temp:", + tempNow)
print("Max:", + tempMax)
print("Min:", + tempMin)
print("Direction:", + windDir)
print("Speed:", + windSpeed)
print('\n')
pprint(weatherData)
