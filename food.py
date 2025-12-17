from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.refresh()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed("fastest")

    def refresh(self):
        randn_X=random.randint(-280,280,)
        randn_y=random.randint(-280,280)
        self.goto(randn_X,randn_y)