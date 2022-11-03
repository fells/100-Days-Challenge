"""
    STRING MANIPULATION

    How to print into the console
        print("Hello World!")

    How to create new lines without needing to create a new print ?

        print(" Hello World!\n Hello World!\n Hello World!")

    How to add multiple stings in the same print ?
        print("Hello there my name is" + " Michel")



    INPUT FUNCTION

    input("What's your name ?")

    Exercise:
    Get the amount of character from a persons name:
        name = input("What's your name ? ")
        print(len(name))


    VARIABLES
    There are multiple types of variables, such as:

    String
    Integer
    Float
    Boolean

    name = input("What's your name ?")  --> String type in this case
    age = 25  --> Integer type
    money = 20.2 --> Float type
    rich = False --> Boolean

    Exercise:

    Switch the place of the variables

    a = input("a:")
    b = input("b:")

    print("a: " + b)
    print("b: " + a)

    Naming your Variable

=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""


#Final project of the day

def Borders():
    print(30 * "=-")

Borders()
print("Welcome to the Band Name Generator")
Borders()

city = input("What's the name of the city you grew up in ?\n")
pet_name = input("What's your pet's name ?\n")
print(f"Your band name could be {city} {pet_name}")

