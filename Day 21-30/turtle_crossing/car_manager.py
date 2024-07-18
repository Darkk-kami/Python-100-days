from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

       
    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=random.randint(2,3), stretch_wid=1)
            new_car.penup()
            new_car.goto(x=310, y=random.randint(-240, 280))
            self.car_list.append(new_car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT




