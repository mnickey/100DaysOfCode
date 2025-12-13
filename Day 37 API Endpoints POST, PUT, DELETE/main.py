import requests
from datetime import datetime
import time

USERNAME = "zendakin"
TOKEN = "ENTER YOUR TOKEN HERE"
GRAPH_ID = "graph1"

# USER ENDPOINT
pixela_endpoint = "https://pixe.la/v1/users"

# GRAPH ENDPOINT
PIXELA_GRAPH_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs"
USER_PARAMETERS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

GRAPH_PARAMETERS = {
    "id": "graph1",
    "name": "Coding Hours",
    "unit": "Commits",
    "type": "int",
    "color": "momiji",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

# Account 'zendakin' has been created, future attempts to create are expected to fail.
response = requests.post(url=pixela_endpoint, json=USER_PARAMETERS)
response.raise_for_status()
print(response.text)

# POST REQUEST
response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=GRAPH_PARAMETERS, headers=HEADERS)
response.raise_for_status()
print(response.text)

# UPDATING A GRAPH
formatted_date = datetime.today().strftime("%Y%m%d")
graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

UPDATE_GRAPH_PARAMETERS = {
    "date": formatted_date,
    "quantity": "3",
}

# POST REQUEST
print(graph_url)
response = requests.post(url=graph_url, json=UPDATE_GRAPH_PARAMETERS, headers=HEADERS)
response.raise_for_status()
print(response.text)

# PUT REQUEST
graph_url += f"/{formatted_date}"
print(graph_url)
response = requests.put(url=graph_url, json=UPDATE_GRAPH_PARAMETERS, headers=HEADERS)
response.raise_for_status()
print(response.text)

# DELETE REQUEST
graph_url += f"/{formatted_date}"
print(graph_url)
response = requests.delete(url=graph_url, headers=HEADERS)
response.raise_for_status()
print(response.text)
