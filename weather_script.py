import requests

API_KEY = "2e0a1060ee06ac7ddde57c7b6dc46e6e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description']}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Error: City not found")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
