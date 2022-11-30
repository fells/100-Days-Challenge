"""
        LEARNING CLASS INHERITANCE

        def Animal():
            def __init__(self):
                self.num_eyes = 2

            def breathe(self):
                print("Inhale, exhale.")

        def Fish (Animal):
            def __init__(self):
                super().__init__()

            def breathe(self):
                super().breathe()
                print("doing this underwater")

            def swim(self):
                print("Swimming in water")


        nemo = Fish()
        nemo.swim()
        nemo.breathe()
        print(nemo.num_eyes)
"""

# FINAL PROJECT
# Creating a Snake game

import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    # Detect Collision with tail
    # if head collides with any segment in the tail:
        # trigger game over sequence
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
