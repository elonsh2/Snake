from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_location = (randint(-280, 280), randint(-280, 280))
        self.goto(random_location)
