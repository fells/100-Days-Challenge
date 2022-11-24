"""

"""

# Final Project
# Make a turtle racing game

import turtle
import random

turtles = []

screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(700, 600)


def random_colors():
    colors = ("red", "blue", "magenta", "orange", "green", "cyan")
    random_color = random.choice(colors)
    if random_color == random_color:
        random_color = random.choice(colors)
        return random_color
    else:
        return random_color


def generate_turtles():
    for _ in range(7):
        new_t = turtle.Turtle()
        new_t.shape("turtle")
        new_t.penup()
        new_t.color(random_colors())
        turtles.append(new_t)


def position_turtles(turtles_list):
    x = -320
    y = [-250, -167, -84, 1, 84, 167, 250]
    position = len(y)
    for t in range(len(turtles_list)):
        for position in range(position):
            turtles[t].goto(x=x, y=y[position])


def random_walk():
    random_num = random.randint(0, 10)
    for t in range(len(turtles)):
        turtles[t].forward(random_num)
    return random_num


generate_turtles()
position_turtles(turtles)
random_walk()

screen.exitonclick()
