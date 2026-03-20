import requests

api_key="your_api_key_here"

city=input("Enter the city name: ")

url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

responce=requests.get(url)
data=responce.json()

if data["cod"]!="404":
    main=data["main"]
    weather=data["weather"] [0]

    tempreture=main["temp"]
    humidity=main["humidity"]
    description=weather["description"]


    print(f"\nWeather in {city}:")
    print(f"Tempreture: {tempreture}°C")
    print(f"Humidity: {humidity}%")
    print(f"Descriptin: {description}")
else:
    print("City not found!")

