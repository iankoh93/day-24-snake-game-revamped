from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.goto(y=r.randint(-280, 280), x=r.randint(-280, 280))

    def refresh(self):
        self.goto(y=r.randint(-280, 280), x=r.randint(-280, 280))
