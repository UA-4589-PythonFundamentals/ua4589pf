from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450



def get_weather():
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    status = w.detailed_status
    wind = w.wind()["speed"]
    humidity = w.humidity
    temp = w.temperature('celsius')
    rain = w.rain
    heat_index = w.heat_index
    сlouds = w.clouds
    
    result = (f"City: London\n"
              f"Status: {status}\n"
              f"Wind: {wind} m/s\n"
              f"Humidity: {humidity}%\n"
              f"Temperature: {temp['temp']} °C\n"
              f"Rain: {rain}\n"
              f"Heat Index: {heat_index}\n"
              f"Clouds: {сlouds}%")

    label.config(text=result)



# Search for current weather in London (Great Britain) and get details



root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)




root.mainloop()