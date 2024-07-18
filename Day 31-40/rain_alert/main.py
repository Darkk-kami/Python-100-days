import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

API_KEY = os.environ.get("API_KEY")

param = {
 "lat": "6.511332083613197",
 "lon": "3.3920931816101074",
 "appid": API_KEY,
 'cnt': 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=param)

data = response.json()['list']

will_rain = False

for n in data:
    weather_id = n['weather'][0]['id']
    weather_condition = n['weather'][0]['description']
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'Bring an umbrella☂️ its gonna be {weather_condition}',
            from_=os.environ.get("A_NUMBER"),
            to=os.environ.get("P_NUMBER"),
        )
        break
