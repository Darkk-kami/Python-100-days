from turtle import Turtle
X_SPEED = 2.3
Y_SPEED = 2.3

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = X_SPEED
        self.y = Y_SPEED    

    def move(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x + self.x, y + self.y)

    def collision_x(self):
        self.x *= -1.1

    def collision_y(self):
        self.y *= -1

    def ball_refresh_1(self):
        self.goto(0,0)
        self.x = X_SPEED * - 1
        self.y = Y_SPEED * - 1

    def ball_refresh_2(self):
        self.goto(0,0)
        self.x = X_SPEED 
        self.y = Y_SPEED 
