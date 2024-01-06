from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1) # making a square 20 * 5 = 100 pixels wide, 20 * 1 = 20 pixels long. (square is initially 20 x 20 size)
paddle.penup()
paddle.goto(350, 0) # making the turtle go to the right edge

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(),new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(go_up, "Up") # go_up function will be called whenever "Up" key is pressed)
screen.onkey(go_down, "Down") # go_down function will be called whenever "Down" key is pressed)

game_is_on = True
while game_is_on:
    screen.update

# At line 7 animation is turned off. Paddle is being created in the background. Then due to lines 29-31 screen is updated and paddle appears at the right edge. By doing so we skip animation of paddle going to the right edge.


screen.exitonclick()
