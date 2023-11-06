import requests
from datetime import datetime
time_now=datetime.now()

MY_LAT=50.879829
MY_LNG=4.700540
parameters= {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
request=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
request.raise_for_status()
data=request.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)
print(time_now.hour)

import smtplib

