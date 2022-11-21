"""
        OOP (Object-Oriented Programming)

        CLASS
        How to call a class in Python

        obj      class
        car = CarBlueprint()

        LEARNING TURTLE

        from turtle import Turtle, Screen
        #Turtle
        # Obj    Class
        mike = Turtle()
        # OBJ   Attributes
        mike.shape("turtle")
        mike.color("blue")
        mike.forward(100)

        # Screen
        screen = Screen()
        screen.exitonclick()

        OTHER PACKAGES (PrettyTable)

        from prettytable import PrettyTable

        table = PrettyTable()

        table.field_names = ["Pokemon", "Type"]
        table.align = "l"
        table.add_rows(
            [
                ["Pikachu", "Electricity"],
                ["Squirtle", "Water"],
                ["Charizard", "Fire"],
                ["Cacturne", "Plant"]
            ]
        )

        print(table)

"""

# FINAL PROJECT (Recreating the Coffee Machine with OOP)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ? ({options})")
    if choice == "off":
        print("See ya. 👋")
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if money_machine.make_payment(drink.cost) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

