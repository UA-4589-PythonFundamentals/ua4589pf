import os

from dotenv import load_dotenv
from pyowm import OWM


load_dotenv()  # take environment variables

API_KEY = os.getenv("API_KEY")

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# city = "Lviv,UA"
city = input("Enter city name: ")

obs = mgr.weather_at_place(city)
w = obs.weather

weather_info = {
    "Status": w.detailed_status,
    "Wind": w.wind(),
    "Humidity": w.humidity,
    "Temperature": w.temperature('celsius'),
    "Rain": w.rain,
    "Heat Index": w.heat_index,
    "Clouds": w.clouds,
}
from pprint import pprint
pprint(weather_info)