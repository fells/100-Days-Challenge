"""

"""

# Final Project
# Recreate Pong

import turtle
from player import Player
from ball import Ball
from scoreboard import Score
import time

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.listen()
screen.tracer(0)

barrier = turtle.Turtle("square")
barrier.color("white")
barrier.shapesize(stretch_len=0.1, stretch_wid=30)

player1 = Player((-460, 0))
player2 = Player((460, 0))
ball = Ball()
scoreboard = Score()
screen.onkey(key="Up", fun=player1.up)
screen.onkey(key="Down", fun=player1.down)
screen.onkey(key="w", fun=player2.up)
screen.onkey(key="s", fun=player2.down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
