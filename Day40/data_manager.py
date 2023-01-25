import requests
import json

sheety_prices_endpoint = "" # --> Your endpoint here
sheety_users_endpoint = "" # --> Your endpoint here


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_data = requests.get(sheety_prices_endpoint, auth=("", ""))  # Add in your authentication if you have, if not you can delete this code
        sheety_data.raise_for_status()
        sheety_json = json.loads(sheety_data.text)
        self.destination_data = sheety_json["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                auth=("", "")   # Add in your authentication if you have, if not you can delete this code
            )

            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = sheety_users_endpoint
        response = requests.get(customers_endpoint, auth=("", ""))  # Add in your authentication if you have, if not you can delete this code
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

DataManager()