from turtle import Turtle, Screen, clearscreen

tom = Turtle()

screen = Screen()


def move_forwards():
    tom.forward(10)

def move_backwards():
    tom.backward(10)

def turn_clockwise():
    tom.right(10)
    
# Or we can use:
#     new_heading = tim.heading() - 10
#     tom.setheading = new_heading

def turn_anti_clockwise():
    tom.left(10)

def clear_and_reset():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = turn_clockwise)
screen.onkey(key = "a", fun = turn_anti_clockwise)
screen.onkey(key = "c", fun = clear_and_reset)


screen.exitonclick()
