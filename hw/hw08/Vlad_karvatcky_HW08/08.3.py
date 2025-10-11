import tkinter as tk
import requests

API_KEY = " api_key_your "
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q":city, "appid":AIP_KEY, "units":"metric"}
    response = requests.get(BASE_URL, parms=params)
    data = response.join()
    if data.get("main"):
        return f"{data['name']}: {data['main']['temp']}°C"
    else:
        return "error City"

def show_wether ():
    city = entry.get()
    result = get_weather(city)

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="Get Weather", command=show_weather)
btn.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)
root.mainloop()
    
    
