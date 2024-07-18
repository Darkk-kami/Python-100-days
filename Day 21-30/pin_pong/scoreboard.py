from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_1} : {self.score_2} ", align=ALIGN, font=FONT)

    def game_over(self, winner):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER\nPLAYER {winner} wins!", align=ALIGN, font=FONT)

    def score_count_1(self):
        self.score_1 += 1
        self.clear()
        self.update_score()

    def score_count_2(self):
        self.score_2 += 1
        self.clear()
        self.update_score()

