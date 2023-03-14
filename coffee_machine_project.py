# Coffee Machine Project

# prompt user

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
# order = input("What would you like? (espresso, latte, cappuccino): ")

# def order_coffee():
#     off = False
#     water = 500
#     coffee = 100
#     milk = 500
#     money = 0
#     while off == False:
#         if order == 'off':
#              break
#     # print report
#         if order == 'report':
#             print(f"Water: {water}ml")
#             print(f"Milk: {milk}ml")
#             print(f"Coffee: {coffee}g")
#             print(f"Money: ${money}")
#         print('Please enter coins.')
#         quarters = int(input("How many quarters?:")) * .25
#         dimes = int(input("How many dimes?:")) * .10
#         nickels = int(input("How many nickels?:")) * .05
#         pennies = int(input("How many pennies?:")) * .01
#         payment = round((quarters + dimes + nickels + pennies), 2)
#         if order == 'espresso':
#              if payment < 1.5:
#                   print("Sorry that's not enough money. Money refunded..")
#              elif water < 50 or coffee < 18:
#                   print("Sorry there is not enough supplies.")
#              else:
#                   money += payment
#                   water -= 50
#                   coffee -= 18
#                   change = payment - 1.5
#                   payment = 0
#                   print(f"Here is ${change} in change.")
#                   print("Here is your espresso. Enjoy!")
#         elif order == 'latte':
#              if payment < 2.5:
#                   print("Sorry that's not enough money. Money refunded..")
#              elif water < 200 or coffee < 24 or milk < 150:
#                   print("Sorry there is not supplies")
#              else:
#                   money += payment
#                   water -= 200
#                   coffee -= 24
#                   milk -= 150
#                   change = payment - 2.5
#                   payment = 0
#                   print(f"Here is ${change} in change.")
#                   print("Here is your latte. Enjoy!")
#         elif order == 'cappuccino':
#              if payment < 3:
#                   print("Sorry that's not enough money. Money refunded..")
#              elif water < 250 or coffee < 24 or milk < 100:
#                   print("Sorry there is not supplies")
#              else:
#                   money += payment
#                   water -= 250
#                   coffee -= 24
#                   milk -= 100
#                   change = payment - 3
#                   payment = 0
#                   print(f"Here is ${change} in change.")
#                   print("Here is your cappuccino. Enjoy!")


# order_coffee()
             
                  

