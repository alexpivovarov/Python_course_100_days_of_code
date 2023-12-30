import turtle as turtle_module
import random
# Our turtle object is called tim
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()


# list containing tuples of different colours
color_list = [(170, 79, 56), (191, 152, 112), (133, 32, 61), (127, 63, 78), (73, 98, 115), (217, 91, 50), (125, 168, 149),
              (94, 120, 108), (58, 48, 92), (47, 31, 82), (71, 28, 76), (60, 167, 177), (86, 155, 143), (211, 204, 154),
              (91, 186, 196), (142, 133, 102), (110, 218, 224), (153, 34, 26), (137, 215, 197), (172, 93, 100), (236, 235, 240),
              (159, 135, 140), (66, 44, 41), (37, 73, 84), (124, 126, 140)]

# Making turtle white so that it is invisible on a white background
turtle_module.colormode(255)

# Making turtle start at the left down corner of a screen
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


# Making a line of dots
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # When turtle gets to the end of a line it goes to the beginning of a new line
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.screensize(10000, 1500)
screen.exitonclick()
