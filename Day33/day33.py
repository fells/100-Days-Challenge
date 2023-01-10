"""
        LEARNING API'S (Application Programming Interface)


"""
# Final project
# Create a project were we know were exactly the ISS is, and when it's above you, it will send you a message to look up
import json
import requests

API = requests.get("http://api.open-notify.org/iss-now.json")
API.raise_for_status()
data = API.text
json_data = json.loads(data)
longitude = json_data['iss_position']['longitude']
latitude = json_data['iss_position']['latitude']
ISS_POSITION = (longitude, latitude)
PERSONAL_LATITUDE = # --> You're Personal Latitude
PERSONAL_LONGITUDE = # --> You're Personal Longitude
PERSONAL_POSITION =(PERSONAL_LONGITUDE, PERSONAL_LATITUDE)

