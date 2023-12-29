import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



user_decision = int(input('What is your choice? Enter 0 for rock, 1 for paper, 2 for scissors\n'))


if user_decision == 0:
  print(rock)
    
elif user_decision == 1:
  print(paper)

elif user_decision == 2:
  print(scissors)

else:
  print('Not defined')

print()
print()


comp_decision = random.randint(0, 2)

print(f"Computer chose {comp_decision}")

if comp_decision == 0:
  print(rock)

elif comp_decision == 1:
  print(paper)

elif comp_decision == 2:
  print(scissors)


if user_decision == comp_decision:
  print("It's a draw")

elif user_decision == 0 and comp_decision == 2:
  print("You won!")
  
elif user_decision > comp_decision:
  print("You won!")
  
else:
  print("Computer won!")
