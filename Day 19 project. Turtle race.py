from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Type a color (red / orange / yellow / green / blue / purple): ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []


# Aligning turtles at the left edge
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

# By creating user_bet if statement we prevent the loop from starting while user still makes the bet.
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: # End of the screen - x coord = 250. Turtle is 40x40 object => so centre of turtle
            # will be at 250 - (40/2) = 230
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!")
            else:
                print(f"Sorry, you lost. Winner is {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
