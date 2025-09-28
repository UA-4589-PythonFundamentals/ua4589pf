from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        # Формируем строку с данными о погоде
        weather_info = (
            f"Status: {w.detailed_status}\n"
            f"Wind: {w.wind()}\n"
            f"Humidity: {w.humidity}%\n"
            f"Temperature: {w.temperature('celsius')['temp']}°C\n"
            f"Clouds: {w.clouds}%"
        )
        return weather_info
    except Exception as e:
        return f"Error: {e}"