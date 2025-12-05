# # API Authentication from Open Weather Map
#
# # API Endpoint Example:
# # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# API Key: ab0405b89fa42652b6c4b2e84e122c4c
LAT = 37.550201
LONG = -121.980827

import requests
import json
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = "USE_YOUR_API_KEY_HERE"
WEATHER_RAIN_URL = "https://api.openweathermap.org/data/2.5/weather"
RAIN_PARAMETERS = {
    "APPID": WEATHER_API_KEY,
    "q": "Fremont",
}

WEATHER_FIVE_DAY_URL = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_FIVE_DAY_PARAMETERS = {
    "APPID": WEATHER_API_KEY,
    "lon": LONG,
    "lat": LAT,
    "cnt": 4,
}

TWILIO_ACCOUNT_SID = "USE_YOUR_API_KEY_HERE"
TWILIO_AUTH_TOKEN = "USE_YOUR_AUTH_TOKEN_HERE"

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

response = requests.get(WEATHER_FIVE_DAY_URL, WEATHER_FIVE_DAY_PARAMETERS)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    # Find these values at https://twilio.com/user/account
    # To set up environmental variables, see http://twil.io/secure
    client = Client(account_sid, auth_token)
    message = (client.messages.create(to="+14085555555", from_="+19255555555",body="Bring an Umbrella! "))
    # message = client.messages.create(from_="+19255555555",
    #                                  body="It's going to rain today. Remember to bring an umbrella",
    #                                  to="+14155238886")

    print(message.status)
