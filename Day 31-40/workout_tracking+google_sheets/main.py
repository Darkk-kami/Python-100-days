import requests
import datetime as dt

# --------------------Authentication keys----------------------
APP_ID = "some app id"
API_KEY = "get your own key"

# ------------------------constants-----------------------
WEIGHT = "your age as int"
HEIGHT = "your height as int"
AGE = "your age as int"
TODAY = dt.date.today().strftime('%d/%m/%Y')
TIME = dt.datetime.today().strftime("%X")
# ---------------------------API--------------------------------
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET = "get your own sheet api"

# ------------------------Parameters----------------------------
# answer = input("what did you do today?")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": "say something",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(URL, json=params, headers=header).json()["exercises"][0]
exercise = response["name"].title()
calories = response["nf_calories"]
duration = response["duration_min"]

add_row = {
  'workout': {
      'date': TODAY,
      'time': TIME,
      'exercise': exercise,
      'duration': duration,
      'calories': calories,
  }
}

response = requests.post(url=SHEET, json=add_row)
print(response.text)
