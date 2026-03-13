# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import pprint
from datetime import datetime
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
        iata_code = flight_search.get_iata_code()
        data_manager.write_data(city, iata_code, id, price)

pprint.pprint(sheet_data)
