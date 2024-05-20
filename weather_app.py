import customtkinter
import requests
import os

#system settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
api_key = '5467bbd2d72ced249294333092024e49' #openweather api

def search_city():
    name = city.get()

    weather_info = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={name}&units=imperial&APPID={api_key}')

    temp = float(weather_info.json()['main']['temp'])
    temp = (temp - 32) * 5/9
    temp = round(temp, 2)
    wind = weather_info.json()['wind']['speed']
    pressure = weather_info.json()['main']['pressure']
    lat = weather_info.json()['coord']['lat']
    lon = weather_info.json()['coord']['lon']

    sun = requests.get(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&date=today&tzid=Europe/Zagreb')

    sunsetI = sun.json()['results']['sunrise']
    sunriseI = sun.json()['results']['sunset']
    
  
    temperature = customtkinter.CTkLabel(app, text=f'Temperature is {temp} celsius', width=220, height=30, corner_radius= 10, fg_color='green')
    temperature.pack()
    
    wind = customtkinter.CTkLabel(app, text=f'Wind is blowing {wind} km/h', width=220, height=30, corner_radius= 10, fg_color='green')
    wind.pack()
    
    pressure = customtkinter.CTkLabel(app, text=f'Pressure is {pressure} hPa', width=220, height=30, corner_radius= 10, fg_color='green')
    pressure.pack()
    
    sunrise = customtkinter.CTkLabel(app, text=f'Sunrise {sunriseI}', width=220, height=30, corner_radius= 10, fg_color='green')
    sunrise.pack()
        
    sunset = customtkinter.CTkLabel(app, text=f'Sunset {sunsetI}', width=220, height=30, corner_radius= 10, fg_color='green')
    sunset.pack()

    return name

#app frame
app = customtkinter.CTk()
app.geometry('720x720')
app.title('Weather app')

#UI elementi
title = customtkinter.CTkLabel(app, text="City")
title.pack(padx=10, pady=10)

#text box
search = customtkinter.StringVar()
city = customtkinter.CTkEntry(app, width=300, height=40, textvariable=search)
city.pack(padx = 10, pady = 10)

#button
button = customtkinter.CTkButton(app, text='Search', command=search_city)
os.system("clear")
button.pack(pady= 10)


app.mainloop()