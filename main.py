import requests
from config import API_key
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

# GUI
root = tk.Tk()
main = tk.Frame(root)
main.place(width=430, height=115, x=0, y=0)
root.title('Weather App')

# Menu setup
cityList = [
    "Adelaide",
    "Brisbane",
    "Canberra",
    "Darwin",
    "Hobart",
    "Melbourne",
    "Perth",
    "Sydney"
]
menuDef = StringVar(main)
menuDef.set(cityList[0])


# Get XML data & parse
def refresh():
    # Build request URL
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    city = menuDef.get()
    countryCode = 'AU'
    requestUrl = f"{baseUrl}{city},{countryCode}&units=metric&mode=xml&APPID={API_key}"

    # Get & prepare data
    weatherData = requests.get(requestUrl)
    soup = BeautifulSoup(weatherData.text, 'xml')

    # Build variables from parsed XML
    weatherState = soup.weather.get('value').title()
    tempNow = str(round(float(soup.temperature.get('value')), 1))
    tempMax = str(round(float(soup.temperature.get('max')), 1))
    tempMin = str(round(float(soup.temperature.get('min')), 1))
    windInfo = soup.speed.get('name')
    windDir = soup.direction.get('code')
    windSpeed_Ms = soup.speed.get('value')
    windSpeed_Kmh = str(round((float(windSpeed_Ms) * 3.6), 1))

    # Draw widgets
    weatherState_draw = tk.Label(main, text=weatherState, font="courier, 12")
    tempNow_draw = tk.Label(temp_frame, text=tempNow, font="courier, 26", anchor="w")
    tempMax_draw = tk.Label(temp_frame, text=tempMax, font="courier, 12")
    tempMin_draw = tk.Label(temp_frame, text=tempMin, font="courier, 12")
    windInfo_draw = tk.Label(wind_frame, text=windInfo, font="courier, 10")
    windSpeed_draw = tk.Label(wind_frame, text=windSpeed_Kmh, font="courier, 12", anchor="e")
    windKmh_draw = tk.Label(wind_frame, text="km/h", font="courier, 8", anchor="nw")
    windDir_draw = tk.Label(wind_frame, text=windDir, font="courier, 12")

    # Position widgets
    # Top
    weatherState_draw.place(x=200, y=10, width=220, height=25)
    # Left
    tempNow_draw.place(x=5, y=5, width=90, height=50)
    tempMax_draw.place(x=110, y=13, width=60, height=15)
    tempMin_draw.place(x=110, y=38, width=60, height=15)
    # Right
    windInfo_draw.place(x=5, y=5, width=210, height=20)
    windSpeed_draw.place(x=35, y=35, width=50, height=15)
    windKmh_draw.place(x=90, y=35, width=40, height=15)
    windDir_draw.place(x=135, y=35, width=50, height=15)

Location_menu = OptionMenu(main, menuDef, *cityList)
Location_menu.place(x=10, y=10, width=110, height=25)
update = tk.Button(main, text="refresh", command=refresh)
update.place(x=130, y=10, width=60, height=25)
temp_frame = Frame(main)
temp_frame.place(x=10, y=45, width=170, height=60)
wind_frame = Frame(main)
wind_frame.place(x=200, y=45, width=220, height=60)

# Gets both half the screen width/height and window width/height
pos_x = int((root.winfo_screenwidth()/2) - 150)
pos_y = int((root.winfo_screenheight()/2) - 150)

# Positions the window in the center of the page.
root.geometry(f"430x115+{pos_x}+{pos_y}")

root.mainloop()
