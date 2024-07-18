from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

snake = Snake()
food = Food()
score_board = Scoreboard()

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=620, height=620)
screen.tracer(0)

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

#[]  {}

continue_game = True

while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score_board.score_count()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.reset()
        snake.reset()
#        continue_game = False

    for blocks in snake.snake_blocks[1:]:
        if snake.head.distance(blocks) < 10:
            score_board.reset()
            snake.reset()
#            continue_game = False



screen.exitonclick()
