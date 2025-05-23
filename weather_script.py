import requests

def get_coordinates(city, api_key):
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geo_url)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return data['lat'], data['lon']
    else:
        print("City not found or API error.")
        return None, None

def get_weather_by_coords(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"Weather: {weather['description'].title()}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
    else:
        print("Weather data not found or API error.")

if __name__ == "__main__":
    api_key = "3e783f1c5de4d888126d68ad91addc24"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    lat, lon = get_coordinates(city, api_key)
    if lat is not None and lon is not None:
        print(f"Coordinates for {city}: Latitude {lat}, Longitude {lon}")
        get_weather_by_coords(lat, lon, api_key)