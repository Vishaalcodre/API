import requests
import datetime as dt


LAT = 20.593683
LNG = 78.962883
today = dt.datetime.now()
now = today.hour

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]


print(sunset)
print(sunset)
print(now)
