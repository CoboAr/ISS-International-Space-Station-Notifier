import requests
from datetime import datetime
import smtplib
import time
import os

# Environmental variables for email and password
MY_EMAIL = os.environ.get("MyEmail")
MY_PASSWORD = os.environ.get("Password")

# Latitude and longitude of current location
MY_LAT = 43.640980 # Your latitude
MY_LONG = -79.400461 # Your longitude

# Check if iss is overhead
def is_iss_overhead():
    # Read API data to get ISS latitude and longitude by using requests module
    response = requests.get(url="http://api.open-notifyy.org/iss-now.json")
    # Returns an HTTPError object if an error has occurred during the process
    response.raise_for_status()
    # Convert data to Json
    data = response.json()
    # Latitude and longitude of ISS retrieved from json data
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

# check if it is night time
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# If it is night and iss is over head, notify by sending an email
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP ("smtp.gmail.com", 587) as connection:
            connection.starttls ()
            connection.login (user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
