
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#my attempt

num_part = ""
symb_part = ""
letter_part= ""



for random_letter in range (0, nr_letters):
  random_letter = random.choice(letters)
  letter_part = letter_part + str(random_letter)
  
  
for random_symb in range (0, nr_symbols):
  random_symb = random.choice(symbols)
  symb_part = symb_part + str(random_symb)
  

for random_num in range(0, nr_numbers):
  random_num = random.randint(0,11)
  num_part = num_part + str(random_num)

password = letter_part + symb_part + num_part

print(password)






#better version

'''
password = ""

for char in range (0, nr_letters):
  password += random.choice(letters)

for char in range (0, nr_symbols):
  password += random.choice(symbols)

for char in range (0, nr_numbers):
  password += random.choice(numbers)

print(password)

'''
