import requests
from config import API_key
from bs4 import BeautifulSoup

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&units=metric&mode=xml" + "&APPID=" + API_key

weatherData = requests.get(requestUrl)
soup = BeautifulSoup(weatherData.text, 'xml')

weatherState = soup.weather.get('value').title()
tempNow = soup.temperature.get('value')
tempMax = soup.temperature.get('max')
tempMin = soup.temperature.get('min')
windInfo = soup.speed.get('name')
windDir = soup.direction.get('code')
windSpeed_Ms = soup.speed.get('value')
windSpeed_Kmh = str(float(windSpeed_Ms) * 3.6)

print('\n ' + weatherState + '\n')
print(' Now: ' + tempNow + ' C')
print(' Max: ' + tempMax + ' C')
print(' Min: ' + tempMin + ' C')
print(' Wind: ' + windSpeed_Kmh + ' Km/h ' + windDir)
