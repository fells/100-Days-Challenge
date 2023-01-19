"""
            HTTP REQUESTS

            GET  --> requests.get("URL HERE")
            POST  --> requests.post("URL HERE")
            PUT   --> requests.put("URL HERE")
            DELETE  --> requests.delete("URL HERE")



"""

# Final Project
import requests
from datetime import datetime

pixela_token = ""   # --> This is the token taht you have created for the Pixela user
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = ""  # --> This is your username in Pixela
GRAPHID = ""  # --> This is your Graph's ID

# Creating a user

# parameters = {
#     "token": pixela_token,
#     "username": "",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# pixela_data = requests.get(PIXELA_ENDPOINT, json=parameters)
# pixela_data.raise_for_status()
# pixela_text = pixela_data.text
# print(pixela_data)


# Creating a Graph

# PIXELA_GRAPH = f"{PIXELA_ENDPOINT}/fells/graphs"
#
# parameters_2 = {
#     "id": "graph1",
#     "name": "Meditation graph",
#     "unit": "commit",
#     "type": "int",
#     "color": "ajisai",
# }
#
headers = {
    "X-USER-TOKEN": pixela_token
}
#
# pixela_graph = requests.post(PIXELA_GRAPH, json=parameters_2, headers=headers)
# pixela_graph.raise_for_status()
# print(pixela_graph)

# Posting to the graph

PIXELA_POST_GRAPH = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"

# today = datetime.now()
#
# parameters_3 = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "3"
# }
# post_to_graph = requests.post(PIXELA_POST_GRAPH, json=parameters_3, headers=headers)
# post_to_graph.raise_for_status()
# print(post_to_graph.text)


# Deleteing a post

DELETE_PIXEL = f"{PIXELA_POST_GRAPH}/20230119"

delete_post_graph = requests.delete(PIXELA_POST_GRAPH,headers=headers)