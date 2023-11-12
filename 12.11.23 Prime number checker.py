number = int(input("Enter a number: "))

is_prime = True

if number > 1:

  for factor in range(2, number):
    if number % factor == 0:
      print(f"Checking {factor} as a factor")
      print(f"{factor} is a factor")
      is_prime = False
      break 
      
  if is_prime == True:
    print('prime')
  else:
    print(f"{number} is not prime")
else:
  print(f"{number} is not prime")
