import requests
from datetime import datetime
import smtplib
import time


my_lat = 51.507351
my_long = -0.127758


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])



parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour

email = example_email
password = password1234


while True:
    time.sleep(60)
    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5 or sunset <= time_now <= sunrise:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr= email,
            to_addr = email,
            msg="Look up \\n The ISS is above you"
        )
