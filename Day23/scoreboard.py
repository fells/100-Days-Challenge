from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=250)
        self.update_score_board()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)


    def update_score_board(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)