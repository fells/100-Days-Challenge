"""

"""
import time
# Final Project
# Build a crossing road game

import turtle
from player import Player
from scoreboard import Scoreboard
from cars import CarManager

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road game")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(key="Up", fun=player.up)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Creating collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False


    # Creating new levels and seeing if the player reached the end of the line
    if player.finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.update_score_board()


screen.exitonclick()
