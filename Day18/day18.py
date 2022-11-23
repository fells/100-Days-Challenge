"""
        Learning Turtle GUI

        mike. = turtle.Turtle()
        mike.shape("turtle")   ---> Shape Function it's a Method
        mike.color("blue")
        mike.forward(100)


        screen = turtle.Screen()
        screen.exitonclick()    ---> The exitonclick is a Method

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

        DRAW A DASHED LINE

        mike.pendown()
        mike.penup()
        mike.forward(50)
        mike.pendown()
        mike.dot(size=10)
        mike.penup()

        DRAWING DIFFERENT SHAPES

        mike = turtle.Turtle()
        screen = turtle.Screen()
        screen.bgcolor("black")
        colors = ["blue", "red", "purple", "green", "violet", "beige", "orange", "cyan"]

        def draw_shape(num_sides):
            angle = 360 / num_sides
            for _ in range(num_sides):
                mike.forward(100)
                mike.right(angle)


        for shape_side_n in range(3,11):
            random_color = random.choice(colors)
            draw_shape(shape_side_n)
            mike.pencolor(random_color)

        screen.exitonclick()

        CREATE A SPIROGRAPH

        colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 174, 254), (247, 66, 254), (247, 66, 136),
          (14, 166, 136), (246, 88, 0)]
        mike = turtle.Turtle()
        mike.hideturtle()
        mike.speed("fastest")
        turtle.colormode(255)
        screen = turtle.Screen()


        def draw_spirograph(gap_size):
            for _ in range(int(360 / gap_size)):
                mike.circle(70)
                current_heading = mike.heading()
                mike.setheading(current_heading + gap_size)
                mike.pencolor(random.choice(colors))


        draw_spirograph(1)

        screen.exitonclick()


"""
# Final Project
# Create a "Painting" with random doted lines

import turtle
import random

def doted_line():
    colors = ["blue", "red", "purple", "black", "green", "violet", "beige", "orange", "cyan"]
    mike.pencolor(random.choice(colors))
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
    mike.forward(50)


screen = turtle.Screen()
screen.title("My painting")
screen.setup(700, 600)
mike = turtle.Turtle()
mike.hideturtle()
mike.penup()
make_painting()
screen.exitonclick()