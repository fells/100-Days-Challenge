"""
        FUNCTIONS HAVING RETURN STATMENTS

        def my_function(something):
            do this with something
            then do this
            return something

        Example

        def Multiply():
            return 3 * 2

        output = Multiply()
        output = 6

        Example:
        def FormatName(first_name, last_name):
            capitalize_first_name = first_name.capitalize()
            capitalize_last_name = last_name.capitalize()
            return capitalize_first_name + " " + capitalize_last_name

        full_name = FormatName("michel", "calil")
        print(full_name)

        EXERCISE 1
        Adjust the new leapyear code to display how many days will it have the February month in a leap year

        def is_leap(year):
            if year % 4 == 0:
                if year % 100 ==0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        def days_in_months(year, month):
            if month > 12 or month < 1:
                return "Invalid month"
            month_days =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if is_leap(year) and month == 2:
                return 29
            else:
                return month_days[month - 1]

        year = int(input("Enter a year:\n"))
        month = int(input("Enter a month:\n"))
        days = days_in_months(year, month)
        print(days)


        DOCSTRINGS

        def FormatName(first_name, last_name):
            '''This function will format the user's full name with the first letter capitalized'''
            capitalize_first_name = first_name.capitalize()
            capitalize_last_name = last_name.capitalize()
            return capitalize_first_name + " " + capitalize_last_name


"""

# Final Project
import logo

print(logo.logo)


def Add(first_number, second_number):
    sum = first_number + second_number
    return sum


def Subtract(first_number, second_number):
    subtract = first_number - second_number
    return subtract


def Multiply(first_number, second_number):
    multiply = first_number * second_number
    return multiply


def Divide(first_number, second_number):
    divide = first_number / second_number
    return divide


operators = {
    "+": Add,
    "-": Subtract,
    "*": Multiply,
    "/": Divide,
}


def Calculator():
    saved_number = []
    restart = True

    first_number = float(input("What's the first number ?: "))

    while restart:
        for operation in operators:
            print(operation)

        operator = input("What's the operator that you want to use ?: ").lower()

        if not operator in operators:
            print("Please pick a right operation")
            restart = False

        second_number = float(input("What's the second number ?: "))

        calculation_function = operators[operator]
        answer = calculation_function(first_number, second_number)
        saved_number.append(answer)
        print(f"{first_number} {operator} {second_number} = {answer}")
        restart = input(f"Do you want to make a new calculation with {answer} ? Type 'Y' or 'N'\n").lower()
        if restart == "y" or restart == "yes":
            first_number = saved_number[len(saved_number) - 1]
        else:
            restart = False
            Calculator()


Calculator()
