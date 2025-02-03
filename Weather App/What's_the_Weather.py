import requests

api_key = '7ce9cb4bfb08e63a7030d0f52dbea0a5'

print("\n----------Weather Report---------\n")
location = input("Jax : Enter the location to know what's the weather there..!!\nUser : ")

weather_report = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}")

if (weather_report.status_code == 404):
    print("Jax : There's no such location like this..!!\n")

else:
    report = weather_report.json()
    weather = report['weather'][0]['main']
    temp = report['main']['temp']
    humidity = report['main']['humidity']

    print(f"\nJax : Weather in {location} : {weather}")
    print(f"      Temperature in {location} : {round(temp, 4)}°C")
    print(f"      Humidity in {location} : {humidity}%\n")

    