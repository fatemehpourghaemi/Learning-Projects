import requests

api_key = "ec5f6032e9ee78f4f9909a723ca109b3"

user_input = input("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# print(weather_data.json())
if weather_data.json()["cod"] == "404":
    print(f"The city {user_input} was not found")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp = float(weather_data.json()["main"]["temp"])
    temp = (temp - 32) * 5 / 9
    result = "Weather of {0}: {1}\nTemperature: {2}"
    print(result.format(user_input, weather, temp))
