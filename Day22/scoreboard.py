from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.left_score()
        self.right_score()

    def left_score(self):
        self.write(f"Score: {self.l_score}", align="left", font=("Arial", 24, "normal",))

    def right_score(self):
        self.write(f"Score: {self.r_score}", align="right", font=("Arial", 24, "normal",))

    def increase_left_score(self):
        self.l_score += 1
        self.clear()
        self.left_score()


    def increase_right_score(self):
        self.r_score += 1
        self.clear()
        self.right_score()