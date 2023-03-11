from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(x_coord, y_coord)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

