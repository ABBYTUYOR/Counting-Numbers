import time
from art import hand_sign
import turtle
from turtle import *
import random

import os
clear = lambda: os.system('cls')
clear()

for _ in hand_sign:
    print(_)

    time.sleep(1)
    clear()

turtle.colormode(255)
angles = [0, 90, 180, 270, 360]


color = [ 'light sky blue', 'deep sky blue', 'dodger blue']
def direction():
    return random.choice(angles)
def pick_color():
    random_color = random.choice(color)
    return random_color

turns = random.randint(20, 40)

my_screen = Screen()
my_screen.bgpic("Untitled-5.png")
tim = Turtle()
for i in range(100):
    turtle.width(10)
    tim.speed('fastest')
    tim.color(pick_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)


my_screen.exitonclick()