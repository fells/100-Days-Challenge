"""
            API Authentication

"""

# Final Project
import requests
import json

parameters = {
    "lat": -26.893890, # --> Personal Latitude
    "lon": -49.085560, # --> Personal Longitude
    "appid": 'd448e480f7793f45feb24805b78bd8b9', # --> Personal OpenWeather API Key
    "units": 'metric',
    "exclude": "current,minutely,daily"
}

# Making a connection with the Open Weather API

data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data.raise_for_status()
data_text = data.text
data_json = json.loads(data_text)

weather_slice = data_json["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella. ☂️")

