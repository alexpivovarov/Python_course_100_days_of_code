BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

from tkinter import *
import pandas
import random


try:
    data = pandas.read_csv("data/words_to_learn.csv") # Attempt to read the "words_to_learn.csv" file into a pandas DataFrame.
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv") # If "words_to_learn.csv" is not found (e.g., it doesn't exist or hasn't been created yet),
    # handle the FileNotFoundError by reading the "french_words.csv" file into a DataFrame.
    to_learn = original_data.to_dict(orient="records") # Convert the DataFrame 'original_data' into a list of dictionaries where each dictionary
    # represents a word pair (French and English). This list is assigned to 'to_learn',
    # which will be used throughout the application.
else:
    to_learn = data.to_dict(orient="records") # If the "words_to_learn.csv" file was found and successfully read into the 'data' DataFrame,
    # convert it into a list of dictionaries and assign it to 'to_learn'.
    # This list will represent the words the user has not yet mastered and needs to practice.

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # Cancel the existing timer that was set to flip the card after 3 seconds.
    # This prevents the previous timer from triggering the flip_card function if
    # the user quickly moves to the next card before the flip occurs.
    current_card = random.choice(to_learn) # Select a random card (a dictionary containing a French word and its English translation)
    # from the 'to_learn' list. The selected card is stored in the 'current_card' variable.
    canvas.itemconfig(card_title, text="French", fill="black") # Update the title of the card to "French"
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black") # Update the text on the 'card_word' canvas element to display the French word from the 'current_card' dictionary.
    canvas.itemconfig(card_background, image=card_front_img)     # Update the background image of the card to 'card_front_img', which represents the front side of the card.
    flip_timer = window.after(3000, func=flip_card) # Set a new timer to trigger the 'flip_card' function after 3 seconds (3000 milliseconds).
    # This will automatically flip the card to show the English translation on the back side
    # if the user does not manually flip or move to the next card within that time.

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    # This function is called when the user indicates they know the word on the current card.
    # It removes the known word from the list of words to learn and updates the stored data.
    to_learn.remove(current_card) # Remove the current card (the word that the user knows) from the 'to_learn' list.
    data = pandas.DataFrame(to_learn) # Convert the updated 'to_learn' list (which no longer contains the known word)
    # back into a pandas DataFrame. This DataFrame is used to store the remaining words.
    data.to_csv("data/words_to_learn.csv", index = False)    # Save the updated DataFrame to a CSV file named "words_to_learn.csv".
    # The 'index=False' argument ensures that the DataFrame indices are not written to the CSV file.
    # This updated file will be used in future sessions to track the words the user still needs to learn.
    next_card() # Call the 'next_card' function to move to a new card and display the next word for the user to learn.
    # This automatically updates the interface to show the next French word on the card.


window = Tk()
window.title("Flashcards")
window.geometry("1000x1000")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) # after 3 seconds (3000ms) trigger function flip_card

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="C:/Users/Александр/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="C:/Users/Александр/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()


window.mainloop()


