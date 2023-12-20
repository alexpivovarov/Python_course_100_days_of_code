from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  # to turn turtle animation off for realistic snake animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Binding keys on a keyboard with functions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # updating screen
    time.sleep(0.1)  # slowing down the animation for 0.1 sec

    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()


    # Detecting collision with wall
    if snake.head.xcor() == -300 or snake.head.xcor() == 300 or snake.head.ycor() == -300 or snake.head.ycor() == 300:
        game_is_on = False
        scoreboard.game_over()


    # Detecting collision with tail using slicing
    for segment in snake.segments[1:]: # We have sliced list of segments in such a way that it starts from the second segment
        # If we pass first segment in loop - game over will be trigerred at the beginning because while looping through
        # segments if first segment (head) has distance to head less than 10 (which it does) then game over.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # Method without using slicing
        # for segment in snake.segments:
        #     if segment == snake.head:
        #         pass
        #elif snake.head.distance(segment) < 10:
        # game_is_on = False
        # scoreboard.game_over()




screen.exitonclick()
