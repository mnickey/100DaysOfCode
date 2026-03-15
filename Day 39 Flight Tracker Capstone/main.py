# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import os
import pprint
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch

# GET REQUEST TO ENSURE API CALLS WORK AND SHEETY IS CONNECTED
data_manager = DataManager()
flight_search = FlightSearch()

response = data_manager.read_data()
sheet_data = response["prices"]

for x in range(len(sheet_data)):
    if sheet_data[x]['iataCode'] == '':
        city = sheet_data[x]['city']
        id = sheet_data[x]['id']
        price = sheet_data[x]['lowestPrice']
        iata_code = flight_search.get_iata_code(city)
        data_manager.write_data(city, iata_code, id, price)

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=6 * 2)

for city in sheet_data:
    print(f"Checking flights for {city['city']}...")

    price = flight_search.check_flights(
        origin_city_code="LON",
        destination_city_code=city["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    print(f"{city['city']}: £{price}")

response = data_manager.read_data()
sheet_data = response["prices"]
pprint.pprint(sheet_data)

# Print env variables
# for key, value in os.environ.items():
#     print(f"{key}: {value}")
