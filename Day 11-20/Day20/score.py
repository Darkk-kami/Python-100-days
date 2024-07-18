from turtle import Turtle
ALIGN = "left"
FONT = ("Ariel", 20, "normal")

with open('high_score.txt') as file:
    current_high_score = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score  = 0
        self.high_score = current_high_score
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=-300, y=250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_score()
        self.score = 0
        self.update_score()

#    def game_over(self):
#        self.goto(x=-70, y=0)
#        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def new_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
        
    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
    

