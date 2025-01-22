import requests
from tkinter import *

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return
    api_key = "27d0fbbafe45a663470496229b65c647"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        result_label.config(
            text=f"City: {city.capitalize()}\n"
                 f"Temperature: {temp}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {weather.capitalize()}\n"
                 f"Wind Speed: {wind_speed} m/s"
        )
    except requests.exceptions.HTTPError:
        result_label.config(text=f"Error: {data.get('message', 'HTTP error occurred')}")
    except Exception:
        result_label.config(text="Error fetching weather data. Please check your connection.")

root = Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

Label(root, text="Weather Forecast App", font=("Helvetica", 16, "bold")).pack(pady=10)
frame = Frame(root)
frame.pack(pady=10)
Label(frame, text="Enter city:").pack(side=LEFT, padx=5)
city_entry = Entry(frame, width=20)
city_entry.pack(side=LEFT, padx=5)
Button(root, text="Get Weather", command=get_weather, bg="#007BFF", fg="white").pack(pady=10)
result_label = Label(root, text="", font=("Helvetica", 12), justify=LEFT, wraplength=350)
result_label.pack(pady=10)

root.mainloop()
