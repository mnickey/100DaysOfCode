import requests
from datetime import datetime as dt

# ------------------------------ SUNSET SUNRISE API ------------------------------
MY_LAT = 37.580449
MY_LNG = -121.992713
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

time_now = dt.now()
print(time_now.hour)

# ------------------------------ ISS LOCATION API ------------------------------
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(longitude, latitude)
