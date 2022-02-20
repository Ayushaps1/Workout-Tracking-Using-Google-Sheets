import requests
import os
from datetime import datetime

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]

NATURAL_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_data = {
    "query": input("Tell me which exercise you did?")
}

response = requests.post(url=NATURAL_EXERCISE_ENDPOINT, headers=headers, json=exercise_data)
response.raise_for_status()
exercise_data = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheety_header = {
        "Authorization": f"Bearer {os.environ['TOKEN']}"
    }

    response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_header)
    response.raise_for_status()
    print(response.text)






