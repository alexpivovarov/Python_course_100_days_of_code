from turtle import Turtle
import random


class Food(Turtle):  # Inheriting from superclass Turtle

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Circle became 10 x 10 from 20 x 20
        self.color("green")
        self.speed("fastest") # Fastest speed so that we don't see animation of creation of food
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

