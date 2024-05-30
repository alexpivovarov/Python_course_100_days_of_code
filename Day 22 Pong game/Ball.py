from turtle import Turtle


class Ball(Turtle):
    # Initialize the Turtle superclass
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Move the ball to a new position
    def move(self):
        new_x = self.xcor() + self.x_move # Calculate the new x-coordinate
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y) # Move the ball to the new position

    def bounce_y(self):
        self.y_move *= -1 # reverse the direction of vertical movement

    def bounce_x(self):
        self.x_move *= -1 # reverse the direction of horizontal movement
        self.move_speed *= 0.9 # increase the speed of ball by decreasing the value of delay (by 10%)

    # Reset the ball to the center of the screen and reverse direction
    def reset_position(self):
        self.goto(0, 0) # Move the ball to the center of the screen
        self.move_speed = 0.1 # Reset the speed of the ball
        self.bounce_x() # reverse the direction of horizontal movement