MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 500,
    "milk": 400,
    "coffee": 100,
}

#Programm uses US coins: penny, dime, quarter.




def is_enough_resources(order_ingredients):
    """Returns true when there are sufficient amounts of ingredients for a chosen drink, otherwise returns false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! Not enough {item}.")
            return False
    return True

# Or
# def is_enough_resources(order_ingredients):
#   is_enough = True
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry! Not enough {item}.")
#             is_enough = False
#     return is enough


def coins_processing():
    """Returns the total value of coins inserted."""
    print("Please inert coins.")
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.1
    total += int(input("Number of nickles: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Your change is ${change}")
        return True
    else:
        print("Sorry. It is not enough money. Your money is refunded")
        return False
        is_transaction_successful(payment, drink["cost"])



def make_coffee(drink_name, order_ingredients):
    """Deducts required amount of ingredients from the total amount"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Enjoy your drink!")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    #This command is for maintainers
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml;")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough_resources(drink["ingredients"]):
            payment = coins_processing()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
