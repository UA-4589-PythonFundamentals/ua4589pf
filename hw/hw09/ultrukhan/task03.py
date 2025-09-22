from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()

    if not city:
        label['text'] = "Input real city"
    else:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        result = (
            f"Status: {w.detailed_status}\n"
            f"Wind: {w.wind().get('speed', 'N/A')}\n"
            f"Humidity: {w.humidity}\n"
            f"Temperature: {w.temperature('celsius')["temp"]}\n"
            f"Rain: {w.rain}\n"
            f"Heat index: {w.heat_index}\n"
            f"Clouds: {w.clouds}\n"
        )

        label['text'] = result

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame, 
    text="Get Weather", 
    bg="gray", fg="white", 
    font=('Courier', 8), 
    command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 11), anchor="nw", justify="left", bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()