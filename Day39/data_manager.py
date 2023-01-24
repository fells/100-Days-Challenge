import requests
import json

sheety_endpoint = "https://api.sheety.co/8beeb65042b0ad4a62a0717abae0bf74/flightDeals/prices" # --> Your endpoint here


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_data = requests.get(sheety_endpoint, auth=("fells", "Flightfinder"))
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
                auth=("fells", "Flightfinder")
            )

            print(response.text)

DataManager()