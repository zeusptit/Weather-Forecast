from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

from button import RoundedButton


root = Tk()
root.title("Weather App")
root.geometry("830x615+360+120")
root.configure(bg="#D8D6D6", border=1)
root.resizable(False, False)

def onEnter():
    todayWeather()

def onEsc():
    root.destroy()

def todayWeather():
    city = textField.get().lower().title()
    geolocator = Nominatim(user_agent = "weather")
    location = geolocator.geocode(city, timeout = 5)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    timeZone.config(text = result)
    longLat.config(text = f"{round(location.latitude, 4)} °N,{round(location.longitude, 4)} °E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)

    ## weather
    api = "https://api.openweathermap.org/data/2.8/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=16a59595816d2942fc065916fbd2748e"
    json_data = requests.get(api).json()


    ## first box
    firstDayImage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file = f"assets/main/icon/iconWeather/{firstDayImage}@2x.png")
    firstImage.config(image = photo1)
    firstImage.image = photo1

    tempDay1 = json_data['daily'][0]['temp']['day']
    tempNight1 = json_data['daily'][0]['temp']['night']

    firstDes.config(text=json_data['daily'][0]['weather'][0]['description'].title())

    day1TempAve.config(text=f"{round(sum(json_data['daily'][0]['temp'].values())/6)}°")
    day1Temp.config(text=f"Day {round(tempDay1)}° / Night {round(tempNight1)}°")

    # second box
    secondSummary.config(text=json_data['daily'][0]['summary'])

def anotherDayWeather():
    print("Hi")
    

## GUI



## Top box
top_box = Frame(root, width=830, height=180, bg="#77baf3")
top_box.pack(side=TOP)

# Search box
Search_image = PhotoImage(file="assets\images\Rounded Rectangle 3.png")
myImage = Label(image=Search_image, bg="#77baf3")
myImage.place(x = 320, y = 25)

weat_image = PhotoImage(file="assets/main/icon/iconWeather/iconPartlySunny.png")
weat_image = weat_image.subsample(10, 10)
weatherImage = Label(root, image=weat_image, background="#203243")
weatherImage.place(x = 350, y = 27)

textField  = tk.Entry(root, justify='center',width=15, font=('poppins',25,'bold'),bg="#203243",border=0, fg="white")
textField.place(x = 400, y = 35)
textField.focus()

Search_icon = PhotoImage(file="assets/main/back/Layer 6.png")
myImage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=todayWeather, activebackground="#203243")
myImage_icon.place(x = 690, y = 30)

## Time zone
timeZone = Label(root, font=("Arial", 20, 'bold'), fg="black", bg="#77baf3")
timeZone.place(x = 50, y = 20)

longLat = Label(root, font=("Arial", 10), fg="black", bg="#77baf3")
longLat.place(x = 50, y = 60)


## Clock
clock = Label(root, font=("Arial", 30, 'bold'), fg="black", bg="#77baf3")
clock.place(x = 50, y = 100)


## Today Weather

box_1 = RoundedButton(root, 450, 130, 20, 2, 'white', '#D8D6D6')
box_1.place(x = 50, y = 195)

box_2 = RoundedButton(root, 450, 60, 20, 2, 'white', '#D8D6D6')
box_2.place(x = 50, y = 337)

box_3 = RoundedButton(root, 450, 180, 20, 2, 'white', '#D8D6D6')
box_3.place(x = 50, y = 410)

box_4 = RoundedButton(root, 240, 320, 20, 2, 'white', '#D8D6D6')
box_4.place(x = 540, y = 195)

box_5 = RoundedButton(root, 240, 60, 20, 2, '#77baf3', '#D8D6D6', anotherDayWeather())
box_5.place(x = 540, y = 530)

## First box

firstFrame = Frame(root, width=400, height=120, bg="white")
firstFrame.place(x = 75, y = 200)

firstImage = Label(firstFrame, bg="white")
firstImage.place(x = 1, y = 1)

firstDes = Label(firstFrame, bg="white", fg="black", font="arial 15 bold")
firstDes.place(x = 15, y = 80)

day1TempAve = Label(firstFrame, bg="white", fg="black", font="arial 50 bold")
day1TempAve.place(x = 250, y = 1)

day1Temp = Label(firstFrame, bg="white", fg="black", font="arial 20 bold")
day1Temp.place(x = 200, y = 80)


## Second box

secondFrame = Frame(root, width=400, height=50, bg = 'white')
secondFrame.place(x = 75, y = 342)

secondSummary = Label(secondFrame, bg="white", fg="black", font="arial 15 bold")
secondSummary.place(x = 25, y = 10)

root.bind("<Escape>", lambda event=None: onEsc())
root.bind("<Return>", lambda event=None: onEnter())





## End GUI


## Process



































root.mainloop()

