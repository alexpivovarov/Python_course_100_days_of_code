from turtle import Screen, Turtle # importing "screen" class and "turtle" class from the "turtle" module
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen() # create screen object from "screen" class
screen.bgcolor("black") # set background colour to black
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # disabling the automatic updating of the screen


# Create the paddles, ball and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# Set up keyboard event handling
screen.listen()
screen.onkey(r_paddle.go_up, "Up") # bind a "go_up" function to a specific key press event (the "Up" arrow key)
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # the lower the sleep time the faster the ball moves
    screen.update()  # Update the screen with all the changes made in this loop iteration
    ball.move() # Move the ball to its new position

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:  # if ball has travelled far enough to the right or left and is within 50 pixels distance to the paddle
        ball.bounce_x()

    # Detect right paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Keep the window open until it is clicked
screen.exitonclick()