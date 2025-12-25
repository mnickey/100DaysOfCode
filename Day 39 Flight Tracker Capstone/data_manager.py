import requests

SHEETY_BASE_URL = "https://api.sheety.co/8acbedba2494196d46d80f33fe0379e2/flightDeals/prices"

class DataManager:

    def __init__(self):
        pass

    def check_iata(self, iata):
        pass

    def read_data(self):
        response = requests.get(SHEETY_BASE_URL)
        return dict(response.json())

    def write_data(self, id, data):
        PUT_URL = SHEETY_BASE_URL + f"/{id}"

        SHEET_INPUTS = {
            "prices": {
                "City":
            }
        }

        requests.put(PUT_URL, json=SHEET_INPUTS)
