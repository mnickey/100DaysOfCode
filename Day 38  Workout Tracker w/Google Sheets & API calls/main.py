import requests
from datetime import datetime
import os
import pprint

# CONSTANTS
GENDER = "male"
WEIGHT_KG = 205
HEIGHT_CM = 193
AGE = 52

# ENVIRONMENTAL_VARIABLES
NUTRITION_APP_ID = os.environ["NUTRITION_APP_ID"]
NUTRITION_API_KEY = os.environ["NUTRITION_API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
USERNAME = os.environ["USERNAME"]

NUTRITION_BASE_URL = "https://app.100daysofpython.dev"
NUTRITION_POST_URL = NUTRITION_BASE_URL + "/v1/nutrition/natural/exercise"

workout_data = input("Tell me what exercises you did? ")

NUTRITION_HEADERS = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

NUTRITION_PAYLOAD = {
    "query": workout_data,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

nutrition_api_response = requests.post(NUTRITION_POST_URL, json=NUTRITION_PAYLOAD, headers=NUTRITION_HEADERS)
nutrition_api_response.raise_for_status()
nutrition_data = nutrition_api_response.json()
# pprint.pprint(nutrition_data)

exercise_type = nutrition_data["exercises"][0]['name'].title()
duration = nutrition_data["exercises"][0]['duration_min']
calories = nutrition_data["exercises"][0]['nf_calories']

SHEETY_BASE_URL = SHEET_ENDPOINT
print(str(SHEETY_BASE_URL))

today_date = datetime.today().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")
# print(today_date, current_time)

SHEET_INPUTS = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise_type,
            "duration": duration,
            "calories": calories
        }
    }

SHEETY_AUTH_TOKEN = {
    "Authorization": os.getenv("SHEETY_AUTH_TOKEN"),
}

# GET REQUEST TO ENSURE API CALLS WORK AND SHEETY IS CONNECTED
# response = requests.get(SHEETY_BASE_URL, params=SHEETY_PAYLOAD)
# response.raise_for_status()
# print(response.text)

# POST REQUESTS
sheety_post_response = requests.post(SHEETY_BASE_URL, json=SHEET_INPUTS, headers=SHEETY_AUTH_TOKEN)
sheety_post_response.raise_for_status()
print(sheety_post_response.text)
