"""
        Learning Turtle GUI

        mike. = turtle.Turtle()
        mike.shape("turtle")



        screen = turtle.Screen()
        screen.exitoncick()

        Drawing a square

        import turtle

        mike = turtle.Turtle()
        mike.shape("turtle")
        mike.forward(100)
        mike.left(90)
        mike.forward(100)
        mike.left(90)
        mike.forward(100)
        mike.left(90)
        mike.forward(100)

        screen = turtle.Screen()
        screen.exitonclick()



"""
import random
# Final Project
# Create a "Painting" with random doted lines

import turtle
import random


def doted_line():
    colors = ["blue", "red", "purple", "black", "green", "violet", "beige", "orange", "cyan"]
    mike.pencolor(random.choice(colors))
    mike.pendown()
    mike.penup()
    mike.forward(50)
    mike.pendown()
    mike.dot(size=10)
    mike.penup()


def repeat():
    for i in range(0, 12):
        doted_line()


def make_painting():
    mike.goto(x=-320, y=-270)
    repeat()
    mike.goto(x=-320, y=-220)
    repeat()
    mike.goto(x=-320, y=-170)
    repeat()
    mike.goto(x=-320, y=-120)
    repeat()
    mike.goto(x=-320, y=-70)
    repeat()
    mike.goto(x=-320, y=-20)
    repeat()
    mike.goto(x=-320, y=30)
    repeat()
    mike.goto(x=-320, y=80)
    repeat()
    mike.goto(x=-320, y=130)
    repeat()
    mike.goto(x=-320, y=180)
    repeat()
    mike.goto(x=-320, y=230)
    repeat()
    mike.goto(x=-320, y=280)
    repeat()


screen = turtle.Screen()
screen.title("My painting")
screen.setup(700, 600)
mike = turtle.Turtle()
mike.shape("turtle")
mike.penup()
make_painting()
screen.exitonclick()
