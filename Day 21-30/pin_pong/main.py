from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PingPong Game")
screen.tracer(0)

paddle_1 = Paddle((-360, 0))
paddle_2 = Paddle((360, 0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddle_1.up, key="w")
screen.onkeypress(fun=paddle_1.down, key="s")
screen.onkeypress(fun=paddle_2.up, key="Up")
screen.onkeypress(fun=paddle_2.down, key="Down")

continue_game = True
while continue_game:

    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.collision_y()

    if ball.xcor() > 350 and ball.distance(paddle_2) < 40 or ball.xcor() < -350 and ball.distance(paddle_1) < 40:
        ball.collision_x()

    if ball.xcor() > 420:        
        ball.ball_refresh_1()
        score.score_count_1()
        time.sleep(1)  
        

    if ball.xcor() < -420:       
        ball.ball_refresh_2()
        score.score_count_2()
        time.sleep(1)        

    if score.score_1 == 10:
        score.game_over(1)
        continue_game = False

    elif score.score_2 == 10:
        score.game_over(2)
        continue_game = False




















screen.exitonclick()