from os import write
from time import sleep
from turtle import Turtle, Screen, register_shape
import turtle
import random
from random import shuffle
import ctypes
import os


def steps():
    return random.randint(0, 35)
screen = Screen()
screen.setup(width=800, height=400)
screen.bgpic("Road.png")
screen.title("🏁 RACE 🏁")

car_list = ["blue.gif", "green.gif", "violet.gif", "red.gif"]

colors = []

for r in colors:
    colors.append(r.replace(".gif", ""))

shuffle(car_list)
y_positions = [-90, -20, 50, 120]
shuffle(y_positions)


traffic_lights = Turtle()
traffic_lights.hideturtle()
traffic_lights.penup()
traffic_lights.shape("circle")
traffic_lights.goto(-380, 180)
turtle.width(50)

car4 = car_list[0]
player4 = Turtle()
player4.hideturtle()
turtle.register_shape(car4)
player4.shape(car4)
player4.penup()
player4.goto(-400, y_positions[0])
player4.showturtle()
player4.goto(-340, y_positions[0])

car3 = car_list[1]
player3 = Turtle()
player3.hideturtle()
turtle.register_shape(car3)
player3.shape(car3)
player3.penup()
player3.goto(-400, y_positions[1])
player3.showturtle()
player3.goto(-340, y_positions[1])

car2 = car_list[2]
player2 = Turtle()
player2.hideturtle()
turtle.register_shape(car2)
player2.shape(car2)
player2.penup()
player2.goto(-400, y_positions[2])
player2.showturtle()
player2.goto(-340, y_positions[2])

car1 =  car_list[3]
player1 = Turtle()
player1.hideturtle()
turtle.register_shape(car1)
player1.shape(car1)
player1.penup()
player1.goto(-400, y_positions[3])
player1.showturtle()
player1.goto(-340, y_positions[3])

player_choice = screen.textinput("🏁 Race Game 🏁", "Which color do you want to represent in the game?").lower()


color_list = ['Red', 'Yellow', 'Green']

for c in color_list:
    sleep(1)
    traffic_lights.color(c)
    traffic_lights.showturtle()
    traffic_lights.fillcolor(c)



race_is_on = True
rank = []
while race_is_on:

    for _ in range(4):

        if player4.xcor() > 440:
            rank.append(car4.replace(".gif", ""))

        elif player3.xcor() > 440:
            rank.append(car3.replace(".gif", ""))

        elif player2.xcor() > 440:
            rank.append(car2.replace(".gif", ""))

        elif player1.xcor() > 440:
            rank.append(car1.replace(".gif", ""))

        if len(rank) == 4:

            title = 'Race 🏁 '

            if player_choice == rank[0]:
                print("You won🏆 the race game!")
                message = 'You won🏆 the race game!'
                ctypes.windll.user32.MessageBoxW(0, message, title, 0)
                race_is_on = False

            else:
                print(f"You lose, {rank[0]} won🏆 the game!")
                message = f"You lose, {rank[0]} won🏆 the game!"
                ctypes.windll.user32.MessageBoxW(0, message, title, 0)


                race_is_on = False

        player4.forward(steps())
        player3.forward(steps())
        player2.forward(steps())
        player1.forward(steps())

screen.exitonclick()
