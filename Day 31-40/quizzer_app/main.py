from question_model import Question, create_questions, question_data
from quiz_brain import QuizBrain
import html
from ui import QuizInterface

question_data = question_data()


def start_up():

    question_bank = [
        Question(html.unescape(question_data[n]["question"]), question_data[n]["correct_answer"])
        for n in range(len(question_data))
    ]
    quiz = QuizBrain(question_bank)
    return quiz


quiz_ui = QuizInterface(start_up())
if quiz_ui.new_quiz():
    create_questions()
    start_up()
    quiz_ui = QuizInterface(start_up())
