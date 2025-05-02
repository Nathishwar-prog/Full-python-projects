# weather_app.py
import requests
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius, use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if not weather_data:
        print("No weather data available.")
        return
    
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M')
        
        print("\nWeather Information:")
        print(f"City: {city}, {country}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {description.capitalize()}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
    except KeyError as e:
        print(f"Error processing weather data: Missing key {e}")

def save_to_json(weather_data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(weather_data, f, indent=4)
        print(f"Weather data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    print("Weather App")
    print("-----------")
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            break
            
        weather_data = get_weather(city)
        if weather_data and weather_data.get('cod') == 200:
            display_weather(weather_data)
            save_option = input("\nDo you want to save this data? (y/n): ").lower()
            if save_option == 'y':
                filename = f"{city.lower().replace(' ', '_')}_weather.json"
                save_to_json(weather_data, filename)
        else:
            print(f"Could not retrieve weather data for {city}. Please try another city.")

if __name__ == '__main__':
    main()
