"""
Author: TwKnD
Site: github.com/TwKnD
"""
from tkinter import Frame, StringVar, OptionMenu
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from config import API_key

# GUI
root = tk.Tk()
main = tk.Frame(root)
main.place(width=430, height=115, x=0, y=0)
root.title('Weather App')

# Define mini frames
temp_frame = Frame(main)
temp_frame.place(x=10, y=45, width=170, height=60)
wind_frame = Frame(main)
wind_frame.place(x=200, y=45, width=220, height=60)

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
def get_data():
    """
    Gets weather data and sets up beautiful soup
    """
    # Build request URL
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    city = menuDef.get()
    country = 'AU'
    req_url = (base_url + city + ',' + country +
               "&units=metric&mode=xml" + "&APPID=" + API_key)
    # Get & prepare data
    data_xml = requests.get(req_url)
    soup = BeautifulSoup(data_xml.text, 'xml')
    refresh(soup)


def refresh(soup):
    """
    Draws the labels on GUI
    """
    # Build variables from parsed XML
    description = soup.weather.get('value').title()
    t_now = str(round(float(soup.temperature.get('value')), 1))
    t_max = str(round(float(soup.temperature.get('max')), 1))
    t_min = str(round(float(soup.temperature.get('min')), 1))
    w_desc = soup.speed.get('name')
    w_dir = soup.direction.get('code')
    w_speed_ms = soup.speed.get('value')
    w_speed_kmh = str(round((float(w_speed_ms) * 3.6), 1))

    # Draw widgets
    description_draw = tk.Label(main, text=description, font="courier, 12")
    t_now_draw = tk.Label(temp_frame, text=t_now, font="courier, 26",
                          anchor="w")
    t_max_draw = tk.Label(temp_frame, text=t_max, font="courier, 12")
    t_min_draw = tk.Label(temp_frame, text=t_min, font="courier, 12")
    w_desc_draw = tk.Label(wind_frame, text=w_desc, font="courier, 10")
    w_speed_draw = tk.Label(wind_frame, text=w_speed_kmh, font="courier, 12",
                            anchor="e")
    w_kmh_draw = tk.Label(wind_frame, text="km/h", font="courier, 8",
                          anchor="nw")
    w_dir_draw = tk.Label(wind_frame, text=w_dir, font="courier, 12")

    # Position widgets
    # Top
    description_draw.place(x=200, y=10, width=220, height=25)
    # Left
    t_now_draw.place(x=5, y=5, width=90, height=50)
    t_max_draw.place(x=110, y=13, width=60, height=15)
    t_min_draw.place(x=110, y=38, width=60, height=15)
    # Right
    w_desc_draw.place(x=5, y=5, width=210, height=20)
    w_speed_draw.place(x=35, y=35, width=50, height=15)
    w_kmh_draw.place(x=90, y=35, width=40, height=15)
    w_dir_draw.place(x=135, y=35, width=50, height=15)


city_menu = OptionMenu(main, menuDef, *cityList)
city_menu.place(x=10, y=10, width=110, height=25)
update = tk.Button(main, text="refresh", command=get_data)
update.place(x=130, y=10, width=60, height=25)

# Gets both half the screen width/height and window width/height
pos_x = int((root.winfo_screenwidth()/2) - 150)
pos_y = int((root.winfo_screenheight()/2) - 150)

# Positions the window in the center of the page.
root.geometry("430x115+{}+{}".format(pos_x, pos_y))
root.mainloop()
