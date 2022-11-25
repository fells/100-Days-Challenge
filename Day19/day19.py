"""

        EVENT LISTENER

        mike = turtle.Turtle()
        screen = turtle.Screen()


        def move_foward():
            mike.forward(10)


        screen.listen()
        screen.onkey(key="space", fun=move_foward)
        screen.exitonclick()

        MAKING A DRAWING GAME

        mike = turtle.Turtle()
        screen = turtle.Screen()


        def move_forward():
            mike.forward(10)

        def move_backwards():
            mike.backward(10)

        def move_left():
            new_heading = mike.heading() + 10
            mike.setheading(new_heading)

        def move_right():
            new_heading = mike.heading() - 10
            mike.setheading(new_heading)

        def clear():
            mike.clear()
            mike.penup()
            mike.home()
            mike.pendown()

        screen.listen()
        screen.onkey(key="w", fun=move_forward)
        screen.onkey(key="a", fun=move_left)
        screen.onkey(key="s", fun=move_backwards)
        screen.onkey(key="d", fun=move_right)
        screen.onkey(key="c", fun=clear)
        screen.exitonclick()

"""

# Final Project
# Make a turtle racing game
import turtle
import random


screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(700, 600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
print(user_bet)
colors = ["red", "blue", "magenta", "orange", "green", "cyan", "darkblue"]
x = -320
y = [-250, -167, -84, 1, 84, 167, 250]
is_race = False
turtles = []


for turtle_index in range(7):
    new_t = turtle.Turtle()
    new_t.shape("turtle")
    new_t.penup()
    new_t.color(colors[turtle_index])
    new_t.goto(x=x, y=y[turtle_index])
    turtles.append(new_t)

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 315:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! {winning_turtle} is the winner!")
            else:
                print(f"You have lost. 😟 {winning_turtle} is the winner!")
        random_num = random.randint(0, 10)
        turtle.forward(random_num)


screen.exitonclick()
