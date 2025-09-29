import tkinter as tk
from pyowm import OWM

# ---------- API Setup ----------
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# ---------- GUI Setup ----------
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


# ---------- Function ----------
def get_weather():
    city = entry_field.get().strip()
    if not city:
        label['text'] = "Please enter a city name!"
        return

    try:
        # Try with country if missing
        if ',' not in city:
            city += ',UA'  # default country UA
        print(f"DEBUG: Searching for city '{city}'")  # for debugging

        observation = mgr.weather_at_place(city)
        w = observation.weather

        temp = w.temperature('celsius')['temp']
        desc = w.detailed_status
        hum = w.humidity
        wind = w.wind()['speed']

        result = (f"City: {city}\n"
                  f"Status: {desc}\n"
                  f"Temperature: {temp:.1f} °C\n"
                  f"Humidity: {hum}%\n"
                  f"Wind: {wind} m/s")
    except Exception as e:
        print("DEBUG: Exception:", e)
        result = "City not found or API error.\n(Example: London,GB or Kyiv,UA)"
    label['text'] = result


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 10),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left', bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
