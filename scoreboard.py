from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.l_score} ", align="right", font=("Courier", 80, "normal"))
        self.write(f" {self.r_score}", align="left", font=("Courier", 80, "normal"))