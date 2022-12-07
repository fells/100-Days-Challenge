import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for segment in STARTING_POSITIONS:
            self.add_segment(segment)


    def add_segment(self, segment):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(segment)
        self.body.append(snake)


    def reset_snake(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]


    def extend(self):
        self.add_segment(self.body[-1].position())


    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

