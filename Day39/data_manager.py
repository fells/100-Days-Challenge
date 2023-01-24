import requests
import json

sheety_endpoint = "" # --> Your endpoint here


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_data = requests.get(sheety_endpoint, auth=("", ""))  # Add in your authentication if you have, if not you can delete this code
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
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                auth=("", "")   # Add in your authentication if you have, if not you can delete this code
            )

            print(response.text)

DataManager()