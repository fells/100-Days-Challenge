# Final Project
# Create a Coffee Machine

profit = 0
COIN_VALUE = [0.01, 0.05, 0.10, 0.25]
FLAVORS = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def money_input(choice, price):
    quarters = int(input("How many quarters ?: ")) * COIN_VALUE[3]
    dimes = int(input("How many dimes ?: ")) * COIN_VALUE[2]
    nickel = int(input("How many nickel ?: ")) * COIN_VALUE[1]
    penny = int(input("How many penny ?: ")) * COIN_VALUE[0]
    total = quarters + dimes + nickel + penny
    return total


def is_resource_enough(order_ingredients):
    """Return's True when the order can be made, and False when it can't"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(payment, price, user_choice):
    """Check if the amount of money that the user inserted is at least the necessary amount"""
    change = payment - price
    if payment >= price:
        global profit
        profit += price
        print(f"Here is your change: {'%.2f' % change}")
        print(f"Enjoy you're {user_choice}. ☕")
        return True
    else:
        print(f"Sorry, not enough money")
        return False

def coffee_machine():
    make_more_coffee = False
    while not make_more_coffee:
        user_choice = input("What would you like ? (Espresso/Latte/Cappuccino):\n").lower()
        if user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif user_choice in FLAVORS:
            drink = FLAVORS[user_choice]
            if is_resource_enough(drink["ingredients"]):
                price = drink["price"]
                print("Insert Coin")
                payment = money_input(user_choice, price)
                success = is_transaction_successful(payment, price, user_choice)



            more_coffee = input("Do you want more coffee ? 'Y' or 'N'\n")
            if more_coffee == "y" or more_coffee == "yes":
                coffee_machine()
            else:
                print("See ya later. 👋")
                make_more_coffee = True
        else:
            print("Please input a correct option.")
            coffee_machine()

coffee_machine()