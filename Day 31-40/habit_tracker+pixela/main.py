import requests
import datetime as dt

TODAY = dt.date.today().strftime("%Y%m%d")
USERNAME = "your-name"
TOKEN = "getyourownkey"

GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PUT_GRAPH_ENDPOINT = f"{POST_GRAPH_ENDPOINT}/{TODAY}"

user_params = {

    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "km",
    "type": "float",
    "color": "kuro",
}

post_update = {
    "date": TODAY,
    "quantity": input("How many km did you cycle today?: "),
    "unit": "km",
}

put_update = {
    "quantity": "6.8",
}

headers = {
    "X-USER-TOKEN": f"{TOKEN}"
}

response = requests.post(url=POST_GRAPH_ENDPOINT, json=post_update, headers=headers)
print(response.text)
