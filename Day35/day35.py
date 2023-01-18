"""
            API Authentication

"""

# Final Project
import requests
import json
from twilio.rest import Client

parameters = {
    "lat": ,  # --> Personal Latitude
    "lon": ,  # --> Personal Longitude
    "appid": '',  # --> Personal OpenWeather API Key
    "units": 'metric',
    "exclude": "current,minutely,daily"
}

# Making a connection with the Open Weather API

data = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data.raise_for_status()
data_text = data.text
data_json = json.loads(data_text)

# Creating the Logic to send the message
weather_slice = data_json["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:

    message_to_send = "Bring an umbrella, it's going to rain. ☂️" # --> Message to send

    # Making a connection with the Twilio API
    twilio_sid_code = ''  # --> Personal SID code from Twilio
    twilio_auth_code = ''  # Personal Authorization code from Twilio

    client = Client(twilio_sid_code, twilio_auth_code)

    message = client.messages.create(
        body=message_to_send,  # --> Message that you want to send
        from_="",  # --> Twilio's Phone number
        to="")  # --> Personal Phone number


