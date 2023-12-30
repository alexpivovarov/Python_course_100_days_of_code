import random

from hangman_words import word_list

from hangman_art import logo
print(logo)


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# Creating blanks
display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []  # Keep track of guessed letters


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)  # Add new guesses to the list
        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            print("Correct!")
        else:
            print(f"You guessed {guess}, that's not in the word. You have lost a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You have lost.")
                print(f"Correct word was {chosen_word}.")


    #Joining all the elements in the list and turning it into a string.
    print(f"{' '.join(display)}")

    #Checking if user has got all letters correct.
    if "_" not in display:
        end_of_game = True
        print("You have won!")

    # Stages by arts
    from hangman_art import stages
    print(stages[lives])
