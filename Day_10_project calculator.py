def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiplication(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiplication,
  "/" : division  
}


def calculator():

  num1 = float(input("Type the first number: "))
  
  
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    symbol = input("Type operation symbol you want to use: ")
    
    next_num = float(input("Type the next number: "))
    
    calculation_function = operations[symbol]
    answer = calculation_function(num1, next_num)
    
    print(f"{num1} {symbol} {next_num} = {answer}")
  
  
  
    if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      calculator()

calculator()
