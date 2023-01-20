"""

"""

# Final Project
# Creating a Workout Tracking program
import requests
import json

APP_ID = "2f00b733"
API_KEY = "149cb52b5aa0def4aeb575f373cfbf9e"

GENDER = "male"
WEIGHT_KG = "85"
HEIGHT_CM = "180"
AGE = "26"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = "https://api.sheety.co/8beeb65042b0ad4a62a0717abae0bf74/workoutTracker/workouts"

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
exercise_duration = nutrition_json["exercises"][0]["duration_min"]
exercise_name = nutrition_json["exercises"][0]["name"]
print(f"{exercise_name}\n{exercise_duration}")


# Creating a connection with the Sheety API

# sheets_data = requests.get(sheets_endpoint)
# sheets_data.raise_for_status()
# print(sheets_data.text)
