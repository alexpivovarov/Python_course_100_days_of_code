import turtle
import pandas

screen = turtle.Screen() # creating screen object


screen.title("United States game") # Setting the title of screen window to "United States game"
image = "blank_states_img.gif" # Specify the file name of the image to be used as the background
screen.addshape(image) # Add the specified image as a shape that can be used by the turtle module
turtle.shape(image) # Set the turtle's shape to the specified image, displaying it on the screen

data = pandas.read_csv("50_states.csv") # reading the csv file
all_states = data["state"].tolist() # getting data series (first column), then turning it to a list and saving it into all_states
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State.{guessed_states}/50 States Correct ",
                                    prompt="What's another state's name?").title() # Asking user to guess a state
    if answer_state == "Exit":
        unguessed_states = []
        for state in all_states:
            if state not in guessed_states:
                unguessed_states.append(state) # Adding missing states to a list of unguessed states
        new_data = pandas.DataFrame(unguessed_states) # creating one column data frame
        new_data.to_csv("states_to_learn.csv") # creating new csv file
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle() # Creating turtle
        t.hideturtle() # hide turtle shape
        t.penup() # turtle does not do any drawing
        state_data = data[data.state == answer_state] # Filtering the data to find the row where the "state" column matches the user's answer (answer state)
        t.goto(state_data.x.item(), state_data.y.item()) # Move the turtle to the coordinates specified by "x" and "y" columns of the filtered data
        t.write(state_data.state.item()) # Write the name of the state at the turtle's current location (Getting the state name from the row corresponding to the matching state)


# The following 3 lines of code can be replaced with only one line of code using list comprehension
#  for state in all_states:
#            if state not in guessed_states:
#                unguessed_states.append(state) # Adding missing states to a list of unguessed states
#
#unguessed_states = [state for state in all_states if state not in guessed_states]

