# Final Project
# Create a Coffee Machine

coins = 0
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

report = str(f"""
    REPORT
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${coins}
""")


def money_input(choice, price):
    quarters = int(input("How many quarters ?: "))
    dimes = int(input("How many dimes ?: "))
    nickel = int(input("How many nickel ?: "))
    penny = int(input("How many penny ?: "))
    quarters = quarters * COIN_VALUE[3]
    dimes = dimes * COIN_VALUE[2]
    nickel = nickel * COIN_VALUE[1]
    penny = penny * COIN_VALUE[0]
    total = quarters + dimes + nickel + penny
    change = total - price

    if total >= price:
        print(f"Here is your change: {'%.2f' % change}")
        print(f"Enjoy you're {choice}. ☕")
    else:
        print(f"Not enough money")
        money_input(choice, price)


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def coffee_machine():
    make_more_coffee = False
    while not make_more_coffee:
        user_choice = input("What would you like ? (Espresso/Latte/Cappuccino):\n").lower()
        if user_choice == "report":
            print(report)
        else:
            drink = FLAVORS[user_choice]
            if is_resource_enough(drink["ingredients"]):
                price = drink["price"]
                print("Insert Coin")
                money_input(user_choice, price)
                more_coffee = input("Do you want more coffee ? 'Y' or 'N'\n")
                if more_coffee == "y" or more_coffee == "yes":
                    coffee_machine()
                else:
                    print("See ya later. 👋")
                    make_more_coffee = True

coffee_machine()