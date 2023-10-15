from tkinter import *
import tkinter as tk
from tkinter import ttk
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

# Tạo đối tượng Notebook để chứa các tab
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)


# Tạo tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1)

# Tạo tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2)
style = ttk.Style()
style.configure("TFrame", background="#D8D6D6")

def onEnter():
    todayWeather()

def onEsc():
    root.destroy()

def todayWeather():
    city = textField.get().lower().title() ## ha noi -> Ha Noi
    geolocator = Nominatim(user_agent = "weather")
    location = geolocator.geocode(city, timeout = 5)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    timeZone.config(text = result)
    longLat.config(text = f"{round(location.latitude, 4)} °N,{round(location.longitude, 4)} °E")

    # home = pytz.timezone(result)
    # local_time = datetime.now(home)
    # current_time = local_time.strftime("%I:%M %p")
    # clock.config(text = current_time)

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

    ## second box
    secondSummary.config(text=json_data['daily'][0]['summary'])
    noti_Icon.place(x = -5, y = 1)

    ## third box

    temp = list(json_data['daily'][0]['temp'].values())
    temperature_list = []
    temperature_list.append(('morning_temp', round(temp[5])))
    temperature_list.append(('afternoon_temp', round(temp[0])))
    temperature_list.append(('evening_temp', round(temp[4])))
    temperature_list.append(('overnight_temp', round(temp[3])))

    thirdFrame1_time.config(text=f"Morning")
    thirdFrame1_temp.config(text=f"{temperature_list[0][1]}°")

    thirdFrame2_time.config(text=f"Afternoon")
    thirdFrame2_temp.config(text=f"{temperature_list[1][1]}°")

    thirdFrame3_time.config(text=f"Evening")
    thirdFrame3_temp.config(text=f"{temperature_list[2][1]}°")

    thirdFrame4_time.config(text=f"Overnight")
    thirdFrame4_temp.config(text=f"{temperature_list[3][1]}°")

    for i, (key, value) in enumerate(temperature_list):
        if value > 30:
            temperature_list[i] = (key, "02d")
        elif value > 25:
            temperature_list[i] = (key, "10d")
        elif value > 20:
            temperature_list[i] = (key, "03d")
        else:
            temperature_list[i] = (key, "11d")
    
    thirdphoto_1 = PhotoImage(file = f"assets/main/icon/iconWeather/{temperature_list[0][1]}@2x.png")
    thirdphoto_1 = thirdphoto_1.subsample(2, 2)
    thirdFrame1_icon.config(image=thirdphoto_1)
    thirdFrame1_icon.image = thirdphoto_1

    thirdphoto_2 = PhotoImage(file = f"assets/main/icon/iconWeather/{temperature_list[1][1]}@2x.png")
    thirdphoto_2 = thirdphoto_2.subsample(2, 2)
    thirdFrame2_icon.config(image=thirdphoto_2)
    thirdFrame2_icon.image = thirdphoto_2

    thirdphoto_3 = PhotoImage(file = f"assets/main/icon/iconWeather/{temperature_list[2][1]}@2x.png")
    thirdphoto_3 = thirdphoto_3.subsample(2, 2)
    thirdFrame3_icon.config(image=thirdphoto_3)
    thirdFrame3_icon.image = thirdphoto_3

    thirdphoto_4 = PhotoImage(file = f"assets/main/icon/iconWeather/{temperature_list[3][1]}@2x.png")
    thirdphoto_4 = thirdphoto_4.subsample(2, 2)
    thirdFrame4_icon.config(image=thirdphoto_4)
    thirdFrame4_icon.image = thirdphoto_4

    ## fourth box
    fourthIntro.config(text=f"Weather Today in {city}")

    firstLine.config(text="Feel Like")
    firstLine_temp.config(text=f"{round(sum(json_data['daily'][0]['feels_like'].values())/4)}°")

    fourthphoto_1 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconTemperatureHigh.png")
    fourthphoto_1 = fourthphoto_1.subsample(20, 20)
    secondLine_icon.config(image=fourthphoto_1)
    secondLine_icon.image = fourthphoto_1
    secondLine.config(text="High")
    secondLine_temp.config(text=f"{round(json_data['daily'][0]['temp']['max'])}°")

    fourthphoto_2 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconTemperatureLow.png")
    fourthphoto_2 = fourthphoto_2.subsample(20, 20)
    thirdLine_icon.config(image=fourthphoto_2)
    thirdLine_icon.image = fourthphoto_2
    thirdLine.config(text="Low")
    thirdLine_temp.config(text=f"{round(json_data['daily'][0]['temp']['min'])}°")

    fourthphoto_3 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconhumidity.png")
    fourthphoto_3 = fourthphoto_3.subsample(20, 20)
    fourthLine_icon.config(image=fourthphoto_3)
    fourthLine_icon.image = fourthphoto_3
    fourthLine.config(text="Humidity")
    fourthLine_temp.config(text=f"{round(json_data['daily'][0]['humidity'])}%")

    fourthphoto_4 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconpressure.png")
    fourthphoto_4 = fourthphoto_4.subsample(90, 90)
    fifthLine_icon.config(image=fourthphoto_4)
    fifthLine_icon.image = fourthphoto_4
    fifthLine.config(text="Pressure")
    fifthLine_temp.config(text=f"{round(json_data['daily'][0]['pressure'])} hPa")

    fourthphoto_5 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconWind.png")
    fourthphoto_5 = fourthphoto_5.subsample(30, 30)
    sixthLine_icon.config(image=fourthphoto_5)
    sixthLine_icon.image = fourthphoto_5
    sixthLine.config(text="Wind Speed")
    sixthLine_temp.config(text=f"{round(json_data['daily'][0]['wind_speed'])} m/s")

    fourthphoto_6 = PhotoImage(file = f"assets/main/icon/iconFeelLike/iconUV.png")
    fourthphoto_6 = fourthphoto_6.subsample(25, 25)
    seventhLine_icon.config(image=fourthphoto_6)
    seventhLine_icon.image = fourthphoto_6
    seventhLine.config(text="UV Index")
    seventhLine_temp.config(text=f"{round(json_data['daily'][0]['uvi'])} of 11")

def anotherDayWeather():
    print("Hi")


top_box = Frame(tab1, width=830, height=140, bg="#77baf3")
top_box.pack(side=TOP) 

# Search box
Search_image = PhotoImage(file="assets/images/Rounded Rectangle 3.png")
myImage = Label(tab1, image=Search_image, bg="#77baf3")
myImage.place(x = 320, y = 25)

weat_image = PhotoImage(file="assets/main/icon/iconWeather/iconPartlySunny.png")
weat_image = weat_image.subsample(10, 10)
weatherImage = Label(tab1, image=weat_image, background="#203243")
weatherImage.place(x = 350, y = 27)

textField  = tk.Entry(tab1, justify='center',width=15, font=('poppins',25,'bold'),bg="#203243",border=0, fg="white")
textField.place(x = 400, y = 35)
textField.focus()

Search_icon = PhotoImage(file="assets/main/back/Layer 6.png")
myImage_icon = Button(tab1, image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=todayWeather, activebackground="#203243")
myImage_icon.place(x = 690, y = 30)

## Time zone
timeZone = Label(tab1, font=("Arial", 20, 'bold'), fg="black", bg="#77baf3")
timeZone.place(x = 50, y = 20)

longLat = Label(tab1, font=("Arial", 10), fg="black", bg="#77baf3")
longLat.place(x = 50, y = 60)


## Clock
# clock = Label(tab1, font=("Arial", 30, 'bold'), fg="black", bg="#77baf3")
# clock.place(x = 50, y = 100)


## Today Weather

box_1 = RoundedButton(tab1, 450, 130, 20, 2, 'white', '#D8D6D6')
box_1.place(x = 50, y = 155)

box_2 = RoundedButton(tab1, 450, 60, 20, 2, 'white', '#D8D6D6')
box_2.place(x = 50, y = 297)

box_3 = RoundedButton(tab1, 450, 180, 20, 2, 'white', '#D8D6D6')
box_3.place(x = 50, y = 370)

box_4 = RoundedButton(tab1, 240, 340, 20, 2, 'white', '#D8D6D6')
box_4.place(x = 540, y = 155)

box_5 = RoundedButton(tab1, 240, 60, 20, 2, '#77baf3', '#D8D6D6', command=anotherDayWeather)
box_5.place(x = 540, y = 510)

## First box

firstFrame = Frame(tab1, width=400, height=120, bg="white")
firstFrame.place(x = 75, y = 160)

firstImage = Label(firstFrame, bg="white")
firstImage.place(x = 1, y = 1)

firstDes = Label(firstFrame, bg="white", fg="black", font="arial 15 bold")
firstDes.place(x = 15, y = 80)

day1TempAve = Label(firstFrame, bg="white", fg="black", font="arial 50 bold")
day1TempAve.place(x = 250, y = 1)

day1Temp = Label(firstFrame, bg="white", fg="black", font="arial 20 bold")
day1Temp.place(x = 200, y = 80)


## Second box


secondFrame = Frame(tab1, width=400, height=50, bg = 'white')
secondFrame.place(x = 75, y = 302)

notiImage = PhotoImage(file="assets/main/icon/otherIcons/notification.png")
notiImage = notiImage.subsample(15, 15)
noti_Icon = Label(secondFrame, image=notiImage, bg="white")

secondSummary = Label(secondFrame, bg="white", fg="black", font="arial 12 bold")
secondSummary.place(x = 35, y = 10)


## Third box

thirdFrame_1 = Frame(tab1, width=80, height=160, bg="white")
thirdFrame_1.place(x = 60, y = 380)

thirdFrame1_time = Label(thirdFrame_1, bg="white",  fg="black", font="arial 13 bold")
thirdFrame1_time.place(x = 10, y = 10)

thirdFrame1_temp = Label(thirdFrame_1, bg="white", fg="black", font="arial 30 bold")
thirdFrame1_temp.place(x = 20, y = 45)

thirdFrame1_icon = Label(thirdFrame_1, bg="white")
thirdFrame1_icon.place(x = 15, y = 100)


canvas_1 = Canvas(tab1, width=20, height=150, bg="white")
canvas_1.config(highlightbackground="white")
canvas_1.place(x = 145, y = 380)


thirdFrame_2 = Frame(tab1, width=90, height=160, bg="white")
thirdFrame_2.place(x = 175, y = 380)

thirdFrame2_time = Label(thirdFrame_2, bg="white",  fg="black", font="arial 13 bold")
thirdFrame2_time.place(x = 1, y = 10)

thirdFrame2_temp = Label(thirdFrame_2, bg="white", fg="black", font="arial 30 bold")
thirdFrame2_temp.place(x = 20, y = 45)

thirdFrame2_icon = Label(thirdFrame_2, bg="white")
thirdFrame2_icon.place(x = 15, y = 100)

canvas_2 = Canvas(tab1, width=20, height=150, bg="white")
canvas_2.config(highlightbackground="white")
canvas_2.place(x = 263, y = 380)

thirdFrame_3 = Frame(tab1, width=80, height=160, bg="white")
thirdFrame_3.place(x = 293, y = 380)

thirdFrame3_time = Label(thirdFrame_3, bg="white",  fg="black", font="arial 13 bold")
thirdFrame3_time.place(x = 1, y = 10)

thirdFrame3_temp = Label(thirdFrame_3, bg="white", fg="black", font="arial 30 bold")
thirdFrame3_temp.place(x = 20, y = 45)

thirdFrame3_icon = Label(thirdFrame_3, bg="white")
thirdFrame3_icon.place(x = 15, y = 100)

canvas_3 = Canvas(tab1, width=20, height=150, bg="white")
canvas_3.config(highlightbackground="white")
canvas_3.place(x = 380, y = 380)

thirdFrame_4 = Frame(tab1, width=80, height=160, bg="white")
thirdFrame_4.place(x = 400, y = 380)

thirdFrame4_time = Label(thirdFrame_4, bg="white",  fg="black", font="arial 13 bold")
thirdFrame4_time.place(x = 1, y = 10)

thirdFrame4_temp = Label(thirdFrame_4, bg="white", fg="black", font="arial 30 bold")
thirdFrame4_temp.place(x = 20, y = 45)

thirdFrame4_icon = Label(thirdFrame_4, bg="white")
thirdFrame4_icon.place(x = 15, y = 100)

canvas_1.create_line(10, 10, 10, 150, width=2, fill="#D8D6D6")
canvas_2.create_line(10, 10, 10, 150, width=2, fill="#D8D6D6")
canvas_3.create_line(10, 10, 10, 150, width=2, fill="#D8D6D6")


## Fourth Box
fourthFrame = Frame(tab1, width=220, height=30, bg="white")
fourthFrame.place(x = 550, y = 160)

fourthIntro = Label(fourthFrame, bg="white", fg="black", font="arial 12 bold")
fourthIntro.place(x = 10, y = 5)

fourthFrame_1 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_1.place(x = 550, y = 230)

firstLine = Label(fourthFrame_1, bg="white", fg="black", font="arial 13 bold")
firstLine.place(x = 5, y = 1)

firstLine_temp = Label(fourthFrame_1, bg="white", fg="black", font="arial 13 bold")
firstLine_temp.place(x = 170, y = 1)


canvas2_1 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_1.config(highlightbackground="white")
canvas2_1.place(x = 550, y = 210)

canvas2_1.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_2 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_2.place(x = 550, y = 225)

secondLine_icon = Label(fourthFrame_2, bg="white")
secondLine_icon.place(x = 5, y = 1)

secondLine = Label(fourthFrame_2, bg="white", fg="black", font="arial 13 bold")
secondLine.place(x = 35, y = 2)

secondLine_temp = Label(fourthFrame_2, bg="white", fg="black", font="arial 13 bold")
secondLine_temp.place(x = 170, y = 5)

canvas2_2 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_2.config(highlightbackground="white")
canvas2_2.place(x = 550, y = 250)

canvas2_2.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_3 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_3.place(x = 550, y = 265)

thirdLine_icon = Label(fourthFrame_3, bg="white")
thirdLine_icon.place(x = 5, y = 1)

thirdLine = Label(fourthFrame_3, bg="white", fg="black", font="arial 13 bold")
thirdLine.place(x = 35, y = 2)

thirdLine_temp = Label(fourthFrame_3, bg="white", fg="black", font="arial 13 bold")
thirdLine_temp.place(x = 170, y = 5)

canvas2_3 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_3.config(highlightbackground="white")
canvas2_3.place(x = 550, y = 290)

canvas2_3.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_4 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_4.place(x = 550, y = 305)

fourthLine_icon = Label(fourthFrame_4, bg="white")
fourthLine_icon.place(x = 5, y = 1)

fourthLine = Label(fourthFrame_4, bg="white", fg="black", font="arial 13 bold")
fourthLine.place(x = 35, y = 2)

fourthLine_temp = Label(fourthFrame_4, bg="white", fg="black", font="arial 13 bold")
fourthLine_temp.place(x = 170, y = 5)

canvas2_4 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_4.config(highlightbackground="white")
canvas2_4.place(x = 550, y = 330)

canvas2_4.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_5 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_5.place(x = 550, y = 345)

fifthLine_icon = Label(fourthFrame_5, bg="white")
fifthLine_icon.place(x = 5, y = 1)

fifthLine = Label(fourthFrame_5, bg="white", fg="black", font="arial 13 bold")
fifthLine.place(x = 35, y = 2)

fifthLine_temp = Label(fourthFrame_5, bg="white", fg="black", font="arial 13 bold")
fifthLine_temp.place(x = 145, y = 5)

canvas2_5 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_5.config(highlightbackground="white")
canvas2_5.place(x = 550, y = 370)

canvas2_5.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_6 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_6.place(x = 550, y = 385)

sixthLine_icon = Label(fourthFrame_6, bg="white")
sixthLine_icon.place(x = 5, y = 1)

sixthLine = Label(fourthFrame_6, bg="white", fg="black", font="arial 13 bold")
sixthLine.place(x = 35, y = 2)

sixthLine_temp = Label(fourthFrame_6, bg="white", fg="black", font="arial 13 bold")
sixthLine_temp.place(x = 160, y = 5)

canvas2_6 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_6.config(highlightbackground="white")
canvas2_6.place(x = 550, y = 410)

canvas2_6.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

fourthFrame_7 = Frame(tab1, width=220, height=40, bg="white")
fourthFrame_7.place(x = 550, y = 425)

seventhLine_icon = Label(fourthFrame_7, bg="white")
seventhLine_icon.place(x = 5, y = 1)

seventhLine = Label(fourthFrame_7, bg="white", fg="black", font="arial 13 bold")
seventhLine.place(x = 35, y = 2)

seventhLine_temp = Label(fourthFrame_7, bg="white", fg="black", font="arial 13 bold")
seventhLine_temp.place(x = 160, y = 5)

canvas2_7 = Canvas(tab1, width=220, height=20, bg="white")
canvas2_7.config(highlightbackground="white")
canvas2_7.place(x = 550, y = 450)

canvas2_7.create_line(10, 10, 220, 10, width=2, fill="#D8D6D6")

root.bind("<Escape>", lambda event=None: onEsc())
root.bind("<Return>", lambda event=None: onEnter())
root.mainloop()
