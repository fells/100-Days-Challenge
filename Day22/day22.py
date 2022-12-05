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
screen.onkeypress(key="Up", fun=player1.up)
screen.onkeypress(key="Down", fun=player1.down)
screen.onkeypress(key="w", fun=player2.up)
screen.onkeypress(key="s", fun=player2.down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Bouncing the ball to the left
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Make the ball bounce from the player
    if ball.distance(player2) < 30 and ball.xcor() > 420 or ball.distance(player1) < 30 and ball.xcor() < -420:
        ball.bounce_x()

    # Detect when Player 2 misses
    if ball.xcor() > 480:
        ball.reset()
        scoreboard.increase_right_score()


    # Detect when Player 1 misses
    if ball.xcor() < -480:
        ball.reset()
        scoreboard.increase_left_score()
screen.exitonclick()
