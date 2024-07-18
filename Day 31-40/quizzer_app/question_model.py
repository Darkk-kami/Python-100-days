import requests
import json


def create_questions():
    parameter = {
        'amount': 10,
        'type': "boolean"
    }

    quiz_data = requests.get(url="https://opentdb.com/api.php", params=parameter)
    quiz_data = quiz_data.json()

    with open("data.json", "w") as file:
        json.dump(obj=quiz_data, fp=file, indent=4)


def question_data():
    with open('data.json') as file:
        data = json.load(file)
        return data["results"]


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

