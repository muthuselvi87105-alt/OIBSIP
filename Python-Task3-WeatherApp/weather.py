import requests

city = input("Enter city name: ")

api_key = "3534dca92c1460584f8f02a019074924"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print(response)
data = response.json()

print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])