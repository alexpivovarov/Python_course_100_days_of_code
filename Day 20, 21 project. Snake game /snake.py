from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move(self):
        for seg_one in range(len(self.segments) - 1, 0, - 1): # Making the last segment go to the position of the next one etc.
            # "Tail follows the head". The first segment (segment at position 0) is not included
            new_x = self.segments[seg_one - 1].xcor()
            new_y = self.segments[seg_one - 1].ycor()
            self.segments[seg_one].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    # Increasing by 1 segment
    def extend(self):
        self.add_segment(self.segments[-1].position()) # Adding segment to the current last segment


    def up(self):
        if self.head.heading() != DOWN: # In an official game snake is not allowed to go backwards.
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)











