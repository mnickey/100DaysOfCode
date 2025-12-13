import requests

# CONSTANTS
GENDER = "male"
WEIGHT_KG = 205
HEIGHT_CM = 193
AGE = 52
APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://app.100daysofpython.dev"
POST_URL = BASE_URL + "/v1/nutrition/natural/exercise"

print(POST_URL)
workout_data = input("Tell me what exercises you did?")

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

PAYLOAD = {
    "query": workout_data,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(POST_URL, json=PAYLOAD, headers=HEADERS)
response.raise_for_status()
print(response.text)
