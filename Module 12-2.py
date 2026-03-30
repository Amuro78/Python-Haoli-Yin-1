import requests,json

def get_weather(city, api_key):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == "404":
            print("The city was not found.")
            return

        temp_kelvin = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        #列表第1个是城市id

        temp_celsius = temp_kelvin - 273.15


        print(f"{city} current weather:")
        print(f"Weather conditions:{weather_desc}")
        print(f"Temperature：{temp_celsius:.1f}°C")

    except requests.exceptions.RequestException as e:
        print("0-0,Sorry :(The request could not be completed at this time.")
        print(e)


City = input("Please enter the city name: ")
API_KEY = "ebf3e474a8255497c54b0b7752efeac4"
get_weather(City, API_KEY)
