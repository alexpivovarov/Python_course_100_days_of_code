# Updatted version. Go to history to see the progress.

print('Welcome to the tip calculator')


vaild_input = True

while vaild_input == True:

    bill = float(input('What is the total bill? '))
    if bill < 0:
        print("Bill amount cannot be negative.")
        vaild_input= False
        break

    tip_percentage = float(input('What percentage tip would you like to give? (enter a value without the % sign) '))
    if tip_percentage < 0:
        print("Tip percentage cannot be negative")
        vaild_input = False
        break

    num_people = int(input('How many people to split the bill with? '))
    if num_people <= 0:
        print('Number of people must be a positive integer.')
        vaild_input = False
        break

    # Exit the loop if all inputs are valid
    break

if vaild_input:
    total_bill_with_tip = bill + bill * (tip_percentage / 100)
    amount_per_person = "{:.2f}".format(total_bill_with_tip / num_people)  # "{:.2f}".format(...)" is a string formatting
    # method. The result will be formatted as a floating-point number with two digits after the decimal point.
    print(f"each person should pay {amount_per_person}")
else:
    print("Invalid input provided. Exiting the tip calculator.")
