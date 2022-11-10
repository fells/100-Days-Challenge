"""
        FUNCTIONS WITH PARAMETERS

        def SayHello (name):  --> name is a necessary input to run this function
            print(f"Hello {name}")

        SayHello("Michel")

        Output

        "Hello Michel"

        EXERCISE 1

        Create a Paint Area Calculator

        import math

        height = int(input("What is the wall height you are trying to cover?\n"))
        width = int(input("What is the wall width you are trying to cover?\n"))
        coverage = 5

        def NumberOfCans(height, width, coverage):
            number_of_cans = math.ceil((height * width) / coverage)
            return print(f"You will need {number_of_cans} to paint cans to paint this wall")

        NumberOfCans(height, width, coverage)


        EXERCISE 2

        Prime Number Checker (Number that its only divisible by itself)

        def PrimeChecker(num):
        if num > 1:
            for n in range(2, num):
                if num % n == 0:
                    print(f"{num} is not a prime number")
        else:
            print(f"{num} is a prime number")
    user_input = int(input("Type in a number to see if he is a Prime number:\n"))

    PrimeChecker(user_input)



"""

# Final Project

import string


def Cypher():
    alphabet_lower = list(string.ascii_lowercase + string.ascii_lowercase)
    new_cypher = False

    def Encode(message, shift, pos_neg):
        encoded_message = ""
        if pos_neg == "positive" or pos_neg == "+":
            for letter in message:
                position = alphabet_lower.index(letter)
                new_position = position + shift
                new_letter = alphabet_lower[new_position]
                encoded_message += new_letter
            print(f"The encoded message is: {encoded_message}")
        elif pos_neg == "negative" or pos_neg == "-":
            for letter in message:
                position = alphabet_lower.index(letter)
                new_position = position - shift
                new_letter = alphabet_lower[new_position]
                encoded_message += new_letter
            print(f"The encoded message is: {encoded_message}")
        else:
            print("Please select a valid shift type: 'positive' or 'negative'.")
            Cypher()

    def Decode(message, shift, pos_neg):
        decoded_message = ""
        if pos_neg == "negative" or pos_neg == "-":
            for letter in message:
                position = alphabet_lower.index(letter)
                new_position = position - shift
                new_letter = alphabet_lower[new_position]
                decoded_message += new_letter
            print(f"The decoded message is: {decoded_message}")
        elif pos_neg == "positive" or pos_neg == "+":
            for letter in message:
                position = alphabet_lower.index(letter)
                new_position = position + shift
                new_letter = alphabet_lower[new_position]
                decoded_message += new_letter
            print(f"The decoded message is: {decoded_message}")
        else:
            print("Please select a valid shift type: 'positive' or 'negative'.")
            Cypher()

    def Restart(restart):
        if restart == "y" or restart == "yes":
            Cypher()
        else:
            print("See ya next time. 👋")
            new_cypher = False

    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if user_input == "encode":
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        pos_neg = input("Positive or negative the shift ?\n").lower()
        shift_num = shift_num % 26
        Encode(message, shift_num, pos_neg)
        restart = input("Do you want to decypher something else? 'Y' or 'N'").lower()
        Restart(restart)
    elif user_input == "decode":
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        pos_neg = input("Positive or negative the shift ?\n").lower()
        shift_num = shift_num % 26
        Decode(message, shift_num, pos_neg)
        restart = input("Do you want to decypher something else? 'Y' or 'N'").lower()
        Restart(restart)
    else:
        print("Please chose a valid option.")
        Cypher()


Cypher()
