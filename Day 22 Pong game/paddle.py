from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # make the size of turtle 100 x 20 (5 x 20 = 100; 20 x 1 = 20)
        self.penup()
        self.goto(position)  # setting the turtle at the right corner

    # Move the paddle up by 20 units
    def go_up(self):
        new_y = self.ycor() + 20 # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the paddle to the new y-coordinate, x-coordinate remains unchanged

    # Move the paddle down by 20 units
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)