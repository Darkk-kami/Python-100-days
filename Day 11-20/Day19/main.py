from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Place your bet', prompt="Which Turtle is going to win?\nPick a Color\n").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 90, 30, -30, -90, -150]
turtle_list = []

for i in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-300, y=y_positions[i])
    turtle_list.append(tim)

end_race = False

def move_forward():
    return random.randint(0, 10)    

while not end_race:

    for turtle in turtle_list:
        turtle.forward(move_forward())

        if turtle.xcor() > 300:
            winner = turtle.pencolor()
            end_race = True   

if user_bet == winner:
    print(f"The {winner} turtle won. You won the bet!!!")
else:
    print(f"The {winner} turtle won. You lost the bet")

screen.exitonclick()