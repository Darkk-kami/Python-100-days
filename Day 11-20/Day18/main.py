#import colorgram
#rgb_list = []
#color_list = colorgram.extract('color.jpeg', 12)

#for x in range(12):
#    current_color = color_list[x]
#    rgb_ext = current_color.rgb
#    rgb_list.append((rgb_ext.r, rgb_ext.g, rgb_ext.b))

from turtle import Turtle, Screen , colormode
import random

extracted_color_list = [(250, 228, 16), (236, 251, 244), (212, 13, 9), (199, 12, 36), (230, 228, 6),
                        (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152)
]

c_color = colormode(255)

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)

def rgb():
    random_rgb_color = random.choice(extracted_color_list)
    return random_rgb_color

def move():
    timmy.dot(20)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.dot(20)
    
def lines():
    for _ in range(9):
        random_color = rgb()
        timmy.pencolor(random_color)
        move()

def rotate_left():
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.left(90)

def rotate_right():
    timmy.right(90)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.right(90)

timmy.penup()
timmy.goto(-180, -240)
for _ in range(5):
    lines()
    rotate_left()
    lines()
    rotate_right() 


screen= Screen()
screen.exitonclick()