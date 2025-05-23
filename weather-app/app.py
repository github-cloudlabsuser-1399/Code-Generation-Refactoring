from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)


API_KEY = "265ac44c5d81c3864297f1f0c06d4e2c"

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data[F'main']
        weather = data['weather'][0]
        return {
            'city': city,
            'description': weather['description'].capitalize(),
            'temperature': main['temp'],
            'humidity': main['humidity']
        }
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city', '')
        if not API_KEY:
            error = 'API key is missing. Please set API_KEY in your .env file.'
        elif city:
            weather_info = get_weather(city, API_KEY)
            if not weather_info:
                error = 'Could not fetch weather data. Please check your city name.'
        else:
            error = 'Please enter a city.'
    return render_template('index.html', weather=weather_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)
