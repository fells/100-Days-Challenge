"""
            DATA TYPES

            .String
            .integer
            .Float
            .Boolean

            name = "Michel"  --> Sting
            age = 25         --> integer
            money = 15.50    --> float
            is_rich = False  --> Boolean

            FUNCTIONS

            A machine that does something

            Ex: A machine that chops potatos to generate french fries, the machine itself is the Function
                If it has a input that's not a potato, it will not generate anything and it will give you a
                warning


            EX:
                num_char = len(input("What is your name ?"))
                print("Your name has " + str(num_char) + " characters")
                .
                output

                Your name has X characters


            If you ever need to check the type of the variable there a FUNCTION called "type()"


            EXERCISE 1

            have a user input a two digit number and the output has to be the sum ob both number example: 26 = 2 + 6 = 8

            user_input = input("Type a two digit number: ")

            first_digit = int(user_input[0])
            second_digit = int(user_input[1])

            print( first_digit + second_digit)


            MATHEMATICAL OPERATIONS

            +
            -
            ==
            /
            *
            **

            add = 2 + 2
            minus = 2 - 2
            equals = 2 == 2
            divide = 2 / 2
            mutiply = 2 * 2
            power_of_number = 2 ** 3

            PEMDAS

            Parentheses
            Exponentes
            Multiplication
            Division
            Addition
            Subtraction


            EXERCISE 2

            Create a BMI Calculator

            user_height = float(input("What's your height ?\n"))
            user_weight = float(input("How much do you weight ?\n"))

            BMI = round(user_weight / (user_height * user_height))

            print(BMI)


            FORMATTED STRING

            If you want to format your strings to be able to reed different variable type you need to fo this

            score = 10
            height = 1.80
            is_winning = True

            print(f"Your score is {score} your height is {height}, you are winning is {is_winning}")


            EXERCISE 3

            Create a program where it wil tell you how many days, weeks and months we have left until we are 90 years old

            current_year = 2022
            user_age = int(input("What's your age ?\n"))

            birth_date = current_year - user_age
            years_until_90 = 90 - user_age

            days_remaining = 365 * years_until_90
            weeks_remaining = years_until_90 * 52
            months_remaining = years_until_90 * 12


            print(f"You are {user_age} years old, you were born in {birth_date}, you have {days_remaining} days, {weeks_remaining} and {months_remaining} months left until 90 years old. ☠")


"""

#   FINAL PROJECT

def Borders ():
    print(30 * "=-")

Borders()
print("Tip Calculator")
Borders()

total_bill = float(input("What was the total bill ?\n"))
amount_of_people = int(input("How many people will split this bill ?\n"))
tip_amount = float(input("How much would you like to tip ? None, 5%, 10% or 15%\n"))

tip_amount_float = float((total_bill * tip_amount) / 100)
total_amount_bill_float = float(total_bill + tip_amount_float)

if (amount_of_people == 0 or amount_of_people == 1):
    print(f"Total bill is {round(total_amount_bill_float)}")
elif (amount_of_people >= 1):
    print(f"The total bill per person is {round(total_amount_bill_float / amount_of_people)}")