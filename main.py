import requests
from pprint import pprint
from config import *

baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&APPID=" + API_key

weatherData = requests.get(requestUrl).json()

pprint(weatherData)
