from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "yellow", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carr_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_position = random.randint(-240, 240)
            new_car.goto(x=300, y=random_y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carr_speed)

    def increase_speed(self):
        self.carr_speed += MOVE_INCREMENT
