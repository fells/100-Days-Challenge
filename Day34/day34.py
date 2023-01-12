"""

"""

# Final Project
# Create a app where we get the questions from a API and have to answer correctly
import requests
import random
import json
import tkinter as tk

parameters = {
    "amount": 30,
    "category": 18,
    "type": "boolean",
}

questions_api = requests.get("https://opentdb.com/api.php", params=parameters)
questions_api.raise_for_status()
data = questions_api.json()
random_num = random.randint(0, len(data["results"]) - 1)
random_question = data["results"][random_num]
question = random_question["question"]
correct_answer = random_question["correct_answer"]
print(question)
print(correct_answer)

