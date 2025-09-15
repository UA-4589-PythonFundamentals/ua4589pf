import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        status = w.detailed_status
        wind = w.wind()['speed']
        humidity = w.humidity
        temp = w.temperature('celsius')['temp']
        rain = w.rain if w.rain else {'no rain': 0}
        clouds = w.clouds
        
        weather_info = (
            f"City: {city}\n"
            f"Status: {status}\n"
            f"Temperature: {temp} °C\n"
            f"Wind Speed: {wind} m/s\n"
            f"Humidity: {humidity}%\n"
            f"Rain: {rain}\n"
            f"Cloud Coverage: {clouds}%"
        )
    except Exception as e:
        weather_info = f"Could not retrieve weather data for '{city}'.\nError: {e}"
    
    label['text'] = weather_info

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

entry_field = tk.Entry(frame, font=('Arial', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="lightgray",
                   fg="black",
                   font=('Arial', 12, 'bold'),
                   activebackground='gray',
                   activeforeground='white',
                   command=get_weather)
button.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame,
                 font=('Courier', 14),
                 justify='left',
                 wraplength=WIDTH * 0.75 - 40,
                 bg='gold')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

