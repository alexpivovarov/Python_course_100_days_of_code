from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup() # Lift the pen to avoid drawing lines
        self.hideturtle() # Hide the turtle cursor
        self.l_score = 0 # Initialize left player score to 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear() # erasing the previous number so that the new number can be written
        self.goto(-100, 200) # # Move to position for left player score
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal")) # Display left player score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    # Increment the left player score
    def l_point(self):
        self.l_score += 1 # Add 1 to the left player score
        self.update_scoreboard() # Update the scoreboard with the new score

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()