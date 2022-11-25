"""

"""

# FINAL PROJECT
# Creating a Snake game

import turtle
import random
import time

screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
body = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
game_is_on = True

for segment in starting_positions:
    snake = turtle.Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(segment)
    body.append(snake)

screen.update()

while game_is_on:
    screen.update()
    time.sleep(1)
    for segment in body:
        segment.forward(20)


screen.exitonclick()