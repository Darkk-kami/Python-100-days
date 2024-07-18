from turtle import Turtle
FONT = "arial"
SIZE = 6
TYPE = "bold"


class Marker(Turtle):

    def __init__(self, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state = state

    def mark_state(self, x, y):
        self.goto(x, y)
        self.write(arg=self.state, align="center", font=(FONT, SIZE, TYPE))

