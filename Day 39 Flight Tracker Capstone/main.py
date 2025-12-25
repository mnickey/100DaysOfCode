# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import pprint
from datetime import datetime
import os
from data_manager import DataManager
from flight_search import FlightSearch

# GET REQUEST TO ENSURE API CALLS WORK AND SHEETY IS CONNECTED
data = DataManager()
flight_search = FlightSearch()

response = data.read_data()
sheet_data = response["prices"]
for data in sheet_data:
    if data['iataCode'] == '':
        # print(data['id'])
        data['iataCode'] = flight_search.get_iata_code()
pprint.pprint(sheet_data)
