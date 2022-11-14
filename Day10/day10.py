"""
        FUNCTIONS HAVING RETURN STATMENTS

        def my_function(something):
            do this with something
            then do this
            return something

"""

# Final Project

import logo

print(logo.logo)
operators = ["+", "-", "*", "/", "%"]


def Calculator(num1, operator, num2):
    if not operator in operators:
        sum = num1 + num2
        print(f"{num1} {operator} {num2} = {sum}")
        restart = input(f"Type 'y' to continue calculating with {sum}, or type 'n' to start a new calculator").lower()
        if restart == "y" or restart == "yes":
            MainMenu()
        else:
            print("See ya.")
    elif operator in operators:

def MainMenu():
    first_number = float(input("What's the first number ?: "))

    for operation in operators:
        print(operation)

    operator = input("What's the operator that you want to use ?: ").lower()

    if not operator in operators:
        print("Please pick a right operation")

    second_number = float(input("What's the second number ?: "))

    Calculator(first_number, operator, second_number)


MainMenu()
Calculator()

