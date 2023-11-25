import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data['value']
        return joke_text
    else:
        return "Failed to fetch Chuck Norris joke."

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temperature_kelvin = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']

        # Convert Kelvin to Celsius
        temperature_celsius = temperature_kelvin - 273.15

        return weather_description, temperature_celsius
    else:
        return "Failed to fetch weather data."

if __name__ == "__main__":
    # Chuck Norris joke
    print("Chuck Norris Joke:")
    chuck_norris_joke = get_chuck_norris_joke()
    print(chuck_norris_joke)
    print("\n")

    # OpenWeather API
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Replace with your OpenWeather API key
    city = input("Enter the name of a municipality: ")
    
    weather_description, temperature_celsius = get_weather(api_key, city)

    if not weather_description:
        print("Failed to fetch weather data.")
    else:
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
