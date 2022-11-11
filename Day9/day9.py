"""
        DICTIONARIES AND NESTING

        dictionary = {
            key: values    --> A dictionary is composed bu a key and it's values, such as the line bellow
            "Bug": "An error in a program that prevents the program from running as expected",  --> Bug is the Key value
        }

        Example:

        programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected",
        "Function": "A piece of code that you can easily call over and over again.",
        "Loop": "The action of doing something over and over again."
        }

        RETRIEVING ITEMS FROM DICTIONARY.
        print(programming_dictionary["Bug"])  --> This will print out the Value of the selected Key

        ADDING NEW ITEMS TO DICTIONARY
        programming_dictionary["Hello"] = "Hello there"

"""

# FINAL PROJECT


import  logo

print(logo.gavel)

print("Welcome to the secret auction program.")
def BidGame():

    values = {}
    user_name = input("What is your name ?\n").lower()
    user_bid = int(input("What's your bid ?\n"))
    more_bidders = input("Are there ay other bidders ? Tye 'yes' or 'no'.\n").lower()

    values[user_name] = user_bid
    print(values)
    if more_bidders == "yes" or more_bidders == "y":
        user_name = input("What is your name ?\n").lower()
        user_bid = int(input("What's your bid ?\n"))
        more_bidders = input("Are there ay other bidders ? Tye 'yes' or 'no'.\n").lower()

    elif more_bidders == "no" or more_bidders == "n":
        print("No more bidders")
    else:
        print("Please chose a valid option for mor bidders")
        BidGame()

BidGame()