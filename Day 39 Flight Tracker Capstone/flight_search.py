import os
import requests
from Tools.scripts.generate_opcode_h import header
from dotenv import load_dotenv

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
# IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

load_dotenv()

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv('AMEDEAUS_API_KEY')
        self._api_secret = os.getenv('AMEDEAUS_SECRET')
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def get_iata_code(self, city_name):
        """Queries the Amadeus API for the IATA code of a city."""
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",  # Optional: helpful if you want more detail
        }

        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)

        try:
            data = response.json()["data"]
            if data:
                # For the 'cities' endpoint, the field is usually 'iataCode'
                return data[0]["iataCode"]
            return "Not Found"
        except (KeyError, IndexError):
            return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Searches for flight offers between two cities."""
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            # For round trips, you'd usually add returnDate.
            # If returnDate is omitted, it defaults to one-way.
            # "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "GBP",
            "max": 1,  # We only need the cheapest one
            "nonStop": "true"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            return "N/A"

        try:
            data = response.json()["data"]
            if data:
                price = data[0]["price"]["total"]
                return price
            return "N/A"
        except (KeyError, IndexError):
            return "N/A"
