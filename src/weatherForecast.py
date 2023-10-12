from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk



root = Tk()
root.title("Weather App")
root.geometry("830x615+360+120")
root.configure(bg="#fff", border=1)
root.resizable(False, False)

def onEnter():
    Process()

def onEsc():
    root.destroy()

class Weather:
    def __init__(self, city):
        self.city = city
        self.temp = ''
        self.humidity = ''
        self.pressure = ''
        self.wind = ''
        self.description = ''
    
    ##def getWeather(self):
        


## GUI



## Top box
top_box = Frame(root, width=830, height=180, bg="#77baf3")
top_box.pack(side=TOP)

# Search box
Search_image = PhotoImage(file="assets\images\Rounded Rectangle 3.png")
myImage = Label(image=Search_image, bg="#77baf3")
myImage.place(x = 320, y = 25)

weat_image = PhotoImage(file="assets/icon/Weather/iconPartlySunny.png")
weat_image = weat_image.subsample(10, 10)
weatherImage = Label(root, image=weat_image, background="#203243")
weatherImage.place(x = 350, y = 27)

textField  = tk.Entry(root, justify='center',width=15, font=('poppins',25,'bold'),bg="#203243",border=0, fg="white")
textField.place(x = 400, y = 35)
textField.focus()


## Time zone
timeZone = Label(root, font=("Courier New", 20, 'bold'), fg="black", bg="#77baf3")
timeZone.place(x = 50, y = 20)

longLat = Label(root, font=("Courier New", 10), fg="black", bg="#77baf3")
longLat.place(x = 50, y = 60)


##clock
clock = Label(root, font=("Courier New", 30, 'bold'), fg="black", bg="#77baf3")
clock.place(x = 50, y = 100)








root.bind("<Escape>", lambda event=None: onEsc())
root.bind("<Return>", lambda event=None: onEnter())





## End GUI


## Process

def Process():
    city = textField.get().lower().title()
    geolocator = Nominatim(user_agent = "weather")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timeZone.config(text=result)
    longLat.config(text=f"{round(location.latitude, 4)} °N,{round(location.longitude, 4)} °E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


































root.mainloop()

