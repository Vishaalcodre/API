import requests
import datetime

date = str(datetime.date.today())
today = date.replace('-', '')
USERNAME = "vishal369"
TOKEN = "assllnasjdlasnw"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": "vishal369",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.get(url=pixela_endpoint, json=user_params)
# print(respone.text)

graph_config = {
    "id": "graph1",
    "name": "Jogging",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_data = {
    "date": "20230612",
    "quantity": "10"
}

add_pixel = {
    "quantity": "10"
}
pixela_deletion_endpoint = f"{pixela_creation_endpoint}/20230612"
pixela_updation_endpoint = f"{pixela_creation_endpoint}/20230612"

response = requests.put(url=pixela_updation_endpoint, json=add_pixel, headers=headers)
print(response.text)

