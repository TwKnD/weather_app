import requests
from config import *
from bs4 import BeautifulSoup

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&units=metric&mode=xml" + "&APPID=" + API_key

weatherData = requests.get(requestUrl)
soup = BeautifulSoup(weatherData.text, 'xml')

tempNow = soup.temperature.get('value')
tempMax = soup.temperature.get('max')
tempMin = soup.temperature.get('min')

print(tempNow)
print(tempMax)
print(tempMin)

# windDir = weatherData['wind']['deg']
# windSpeed = weatherData['wind']['speed']
