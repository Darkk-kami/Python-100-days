from turtle import Turtle

PADDLE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        current_pos = self.ycor()
        self.sety(current_pos + PADDLE_SPEED)

    def down(self):
        current_pos = self.ycor()
        self.sety(current_pos - PADDLE_SPEED)
