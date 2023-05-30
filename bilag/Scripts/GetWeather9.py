import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Unable to fetch weather data.")

# Replace with your API key
api_key = "32abc8ee1a1ecea1daa12ad2aee4b5d6"
# Replace with your desired city name
city = "Copenhagen"

get_weather(api_key, city)
