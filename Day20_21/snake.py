import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for segment in STARTING_POSITIONS:
            snake = turtle.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(segment)
            self.body.append(snake)


    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(x=new_x, y=new_y)
        self.body[0].forward(MOVE_DISTANCE)
