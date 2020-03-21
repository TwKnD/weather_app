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

# Build variables from parsed XML
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
frame = tk.Frame(root)
frame.pack()

# Draw widgets
Location_draw = tk.Label(frame, text=city)
weatherState_draw = tk.Label(frame, text=weatherState)
tempNow_draw = tk.Label(frame, text=tempNow)
tempMax_draw = tk.Label(frame, text=tempMax)
tempMin_draw = tk.Label(frame, text=tempMin)
windInfo_draw = tk.Label(frame, text=windInfo)
windSpeed_draw = tk.Label(frame, text=windSpeed_Kmh)
windDir_draw = tk.Label(frame, text=windDir)


# Colour widgets
# root.configure(bg="#32302f")

# Position widgets
Location_draw.grid(row=0, column=0)
weatherState_draw.grid(row=0, column=3)
tempNow_draw.grid(row=1, column=1)


root.mainloop()
