from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):

        self.quiz = quiz
        self.window = Tk()
        self.window.configure(bg=THEME_COLOR, width=350, height=500, padx=20, pady=20)
        self.window.minsize(width=350, height=500)
        self.window.title("Quizzer")

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=("Arial", 14, "normal"),
                                 fg="white", pady=20, padx=20)
        self.score_label.grid(row=2, column=1)

        image_1 = PhotoImage(file="images/true.png")
        image_2 = PhotoImage(file="images/false.png")

        self.button_true = Button(image=image_1, command=self.true_button_click)
        self.button_true.grid(row=3, column=0)
        self.button_false = Button(image=image_2, command=self.false_button_click)
        self.button_false.grid(row=3, column=2)

        self.canvas = Canvas(width=330, height=250, bg="white")
        self.question_text = self.canvas.create_text((165, 125), text="PLACEHOLDER",
                                                     fill=THEME_COLOR, font=("Arial", 14, "normal"), width=300)
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.score_label.config(text=f"You have reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.new_quiz()

    def true_button_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def new_quiz(self):
        pop_up = messagebox.askyesno(title="quiz", message="Generate new Quiz?")
        return pop_up
