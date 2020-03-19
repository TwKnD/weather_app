import requests
from config import *
from bs4 import BeautifulSoup

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&units=metric&mode=xml" + "&APPID=" + API_key

weatherData = requests.get(requestUrl)
soup = BeautifulSoup(weatherData.text, 'xml')

targetTest = soup.current
print(targetTest)
#print(soup.prettify())


#tempNow =
#tempMax = weatherData['main']['temp_max']
#tempMin = weatherData['main']['temp_min']
#windDir = weatherData['wind']['deg']
#windSpeed = weatherData['wind']['speed']
#
#
#print("Weather For", city)
#print("Temp:", + tempNow)
#print("Max:", + tempMax)
#print("Min:", + tempMin)
#print("Direction:", + windDir)
#print("Speed:", + windSpeed)
#print('\n')
