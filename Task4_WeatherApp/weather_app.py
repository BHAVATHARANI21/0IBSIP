
import requests
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather():
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty!")
        return

    if not API_KEY:
        print("API key not found. Check your .env file.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 404:
            print("City not found!")
            return

        if response.status_code == 401:
            print("Invalid API key!")
            return

        response.raise_for_status()

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print("\n----- WEATHER REPORT -----")
        print("City:", data["name"])
        print(f"Temperature: {temp_c} °C")
        print(f"Temperature: {temp_f:.2f} °F")
        print(f"Humidity: {humidity}%")
        print("Weather:", weather)
        print(f"Wind Speed: {wind} m/s")
        print("--------------------------")

    except requests.exceptions.Timeout:
        print("Network timeout! Try again.")

    except requests.exceptions.ConnectionError:
        print("Check your internet connection!")

    except requests.exceptions.RequestException:
        print("Unable to fetch weather data!")


if __name__ == "__main__":
    get_weather()
