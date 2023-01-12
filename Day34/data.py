import requests

parameters = {
    "amount": 20,
    "category": 18,
    "type": "boolean",
}

questions_api = requests.get("https://opentdb.com/api.php", params=parameters)
questions_api.raise_for_status()
data = questions_api.json()
question_data = data["results"]