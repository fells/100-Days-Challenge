"""

"""
import time
# Final Project
# Build a crossing road game

import turtle
from player import Player
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road game")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=player.up)


game_on = True

while game_on:
    time.sleep(0.1)
    player.finish_line()
    screen.update()

