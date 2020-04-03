import requests
from config import API_key
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

# GUI
root = tk.Tk()
frame = tk.Frame(root, padx=5, pady=5)
frame.pack()
root.title('Weather App')

# Menu setup
cityList = [
    "Canberra",
    "Sydney",
    "Melbourne"
]
menuDef = StringVar(frame)
menuDef.set(cityList[0])

# Colour widgets
bgColor = '#32302f'
fgColor = '#ebdbb2'

# Get XML data & parse
def refresh():
    # Build request URL
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    city = menuDef.get()
    countryCode = 'AU'
    requestUrl = baseUrl + city + ',' + countryCode + "&units=metric&mode=xml" + "&APPID=" + API_key

    # Get & prepare data
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
    windSpeed_Kmh = str(round((float(windSpeed_Ms) * 3.6), 1))

    # Draw widgets
    weatherState_draw = tk.Label(frame, text=weatherState)
    tempNow_draw = tk.Label(frame, text="Current\n" + tempNow)
    tempMax_draw = tk.Label(frame, text="Max\n" + tempMax)
    tempMin_draw = tk.Label(frame, text="Min\n" + tempMin)
    windInfo_draw = tk.Label(frame, text=windInfo)
    windSpeed_draw = tk.Label(frame, text=windSpeed_Kmh + "\nKm/h")
    windDir_draw = tk.Label(frame, text=windDir)

    # Position widgets
    # Top
    # Location_draw.grid(row=0, column=0, padx=10, pady=10, sticky='E')
    weatherState_draw.grid(row=0, column=2, padx=10, pady=10,
                           sticky='W')
    # Middle
    tempNow_draw.grid(row=1, column=0, padx=10, pady=10)
    tempMax_draw.grid(row=1, column=1, padx=10, pady=10)
    tempMin_draw.grid(row=1, column=2, padx=10, pady=10)
    # Bottom
    windInfo_draw.grid(row=2, column=0, padx=10, pady=10)
    windSpeed_draw.grid(row=2, column=1, padx=10, pady=10)
    windDir_draw.grid(row=2, column=2, padx=10, pady=10)

Location_menu = OptionMenu(frame, menuDef, *cityList)
Location_menu.grid(row=0, column=0, padx=10, pady=10, sticky='E')
update = tk.Button(frame, text="refresh", command=refresh)
update.grid(row=0, column=1, padx=10, pady=10)

# Gets both half the screen width/height and window width/height
positionRight = int((root.winfo_screenwidth()/2) - 150)
positionDown = int((root.winfo_screenheight()/2) - 150)

# Positions the window in the center of the page.
root.geometry("350x200")

root.mainloop()
