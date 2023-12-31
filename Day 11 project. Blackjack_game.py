# Blackjack rules for this game:
# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  return random.choice(cards)

def calculate_score(cards):
  """Takes a list of cards and returns the score calculated from the cards"""
# checking for a blackjack (a hand with only 2 cards: ace + 10). If blackjack then returning 0 instead of the actual score. 0 represents a blackjack in this game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # checking for an 11 (ace). If the score is already over 21, removing the 11 and replacing it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)



#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You have lost. Computer has a blackjack"
  elif user_score == 0:
    return "You have won. You have a blackjack"
  elif user_score > 21:
    return "You have lost. Your score is more than 21"
  elif computer_score > 21:
    return "You have won. Computer's score is more than 21"
  elif user_score > computer_score:
    return "You have won"
  else:
    return "Computer has won"


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  # underscore is used in range function above because this particular variable is not needed. We just need the the loop to run twice 
  
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # if the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if computer_score == 0 or user_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_choice = input("Would you like to draw another card? Type 'y' for yes or 'p' to pass ")
      if user_choice == 'y':
        user_cards.append(deal_card())
      elif user_choice == 'p':
        is_game_over = True
        
    
    #The computer draws a card as long as it has a score less than 17. We don't want it to draw a card when it has blackjack
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
    #Restarting a game
    print(f" Your final hand is {user_cards}, your final score is: {user_score} ")
    print(f"Computer's final hand is {computer_cards}, computer's  score is: {computer_score}.")
    
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  clear()
  play_game()
