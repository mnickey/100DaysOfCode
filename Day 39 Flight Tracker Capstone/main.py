# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import os
import pprint
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# GET REQUEST TO ENSURE API CALLS WORK AND SHEETY IS CONNECTED
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

response = data_manager.read_data()
sheet_data = response["prices"]

for x in range(len(sheet_data)):
    if sheet_data[x]['iataCode'] == '':
        city = sheet_data[x]['city']
        id = sheet_data[x]['id']
        sheet_price = sheet_data[x]['lowestPrice']
        iata_code = flight_search.get_iata_code(city)
        data_manager.write_data(city, iata_code, id, sheet_price)

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=6 * 30)

for city in sheet_data:
    print(f"Checking flights for {city['city']}...")

    price = flight_search.check_flights(
        origin_city_code="SFO",
        destination_city_code=city["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    # print(f"{city['city']}: £{price}") # prints price in GPB
    print(f"{city['city']}: ${price}") # prints price in USD

    if price != "N/A":
        float_price = float(price)

    if float_price < city['lowestPrice']:
        # Create message to send from notification manager
        message = (f"Low price alert! Only £{float_price} to fly from SFO to {city['city']}-{city['iataCode']}"
                   f", lower than the previous £{city['lowestPrice']}.")

        # Print message for logging
        print(f"I've found a lower price for {city['city']}! {float_price} vs {city['lowestPrice']}")

        # Send the email
        notification_manager.send_email(message)


response = data_manager.read_data()
sheet_data = response["prices"]
pprint.pprint(sheet_data)
