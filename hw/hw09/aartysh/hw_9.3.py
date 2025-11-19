import tkinter as tk
from pyowm import OWM

API_KEY = "ef2206ff5da67de63306d0b143e20872"

def get_weather(city_name):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city_name)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    status = w.detailed_status
    humidity = w.humidity

    result = (
        f"City: {city_name}\n"
        f"Status: {status}\n"
        f"Temperature: {temp:.1f} °C\n"
        f"Humidity: {humidity} %"
    )

    return result


HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)


def show_weather():
    city = entry_field.get()
    result = get_weather(city)
    label.config(text=result)


button = tk.Button(frame, text="Get Weather",
                   bg="gray", fg="white",
                   command=show_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


root.mainloop()
