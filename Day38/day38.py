"""

"""

# Final Project
# Creating a Workout Tracking program

import requests
import json
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")  # --> Add your Nutrition API ID
API_KEY = os.environ.get("API_KEY")  # --> Add your Nutrition API Key

GENDER = "male"  # --> Add your Gender
WEIGHT_KG = "86"  # --> Add your Weight
HEIGHT_CM = "180"  # --> Add your Height
AGE = "26"  # --> Add your Age

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = os.environ.get("sheets_endpoint")  # --> Add your Sheety API endpoint

exercise_text = input("Tell me which exercises you did: ")

# Creating a connection with the Nutrition API andit's parameters

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrion_data = requests.request("POST", endpoint, headers=headers, json=parameters)
nutrion_data.raise_for_status()
nutrition_json = json.loads(nutrion_data.text)

# Creating the date and adding in to the Sheety API

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Creating a connection with the Sheety API

for exercise in nutrition_json["exercises"]:
    sheets_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheets_data = requests.post(sheets_endpoint, json=sheets_input, auth=("", ""))  # --> Add in your username and password
    sheets_data.raise_for_status()

    print(sheets_data.text)
