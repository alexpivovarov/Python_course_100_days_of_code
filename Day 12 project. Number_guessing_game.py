#My attempt

import random

number = random.randint(1, 101)

hint = print(number)


print("Welcome to the number guessing game.")
print("I have chosen a number between 1 and 100. Try to guess it!")

difficulty = input("Choose a difficulty: 'easy' or 'hard'. Type it: ")

num_attempts = 0

if difficulty == "easy":
  num_attempts = 10
elif difficulty == "hard":
  num_attempts = 5

game_finished = "no"

while game_finished == "no":
  print(f"You have {num_attempts} attempt(s) remaining to guess the number.")
  guess = int(input("Make a guess: "))


  if guess == number:
    print("Correct! Congratulations!")
    game_finished = "yes"
  elif guess > number:
    print("It's too high.")
    num_attempts -= 1
  elif guess < number:
    print("It's too low.")
    num_attempts -= 1
  if num_attempts == 0:
    print("Your last attempt has gone. Game over.")
    game_finished = 'yes'
