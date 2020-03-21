import requests
from config import API_key
from bs4 import BeautifulSoup
import tkinter as tk

# Build request URL
baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
city = 'Melbourne,AU'
requestUrl = baseUrl + city + "&units=metric&mode=xml" + "&APPID=" + API_key

# Get XML data & parse
weatherData = requests.get(requestUrl)
soup = BeautifulSoup(weatherData.text, 'xml')

# Variables
weatherState = soup.weather.get('value').title()
tempNow = soup.temperature.get('value')
tempMax = soup.temperature.get('max')
tempMin = soup.temperature.get('min')
windInfo = soup.speed.get('name')
windDir = soup.direction.get('code')
windSpeed_Ms = soup.speed.get('value')
windSpeed_Kmh = str(float(windSpeed_Ms) * 3.6)

# GUI
root = tk.Tk()
root.configure(bg="#32302f")

# Draw widgets
Location = tk.Label(root, text=city)

# Position widgets
Location.grid(row=0, column=0)

root.mainloop()
