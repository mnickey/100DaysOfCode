import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
SHEETY_BASE_URL = "https://api.sheety.co/8acbedba2494196d46d80f33fe0379e2/flightDeals/prices"


class DataManager:

    def __init__(self):
        pass

    def check_iata(self, iata):
        pass

    def read_data(self):
        response = requests.get(SHEETY_BASE_URL)
        return dict(response.json())

    def write_data(self, city, iata_code, id, price):
        PUT_URL = SHEETY_BASE_URL + f"/{id}"

        SHEET_INPUTS = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": price,
                "id": id,
                "price": price
            }
        }
        print(PUT_URL)
        requests.put(PUT_URL, json=SHEET_INPUTS)
