"""
        FUNCTIONS WITH PARAMETERS

        def SayHello (name):  --> name is a necessary input to run this function
            print(f"Hello {name}")

        SayHello("Michel")

        Output

        "Hello Michel"



"""

# Final Project
import string


def Cypher():
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    new_cypher = False

    lenght_alphabets = len(alphabet_lower)

    def Encode(message, shift):
        print(message, shift)

    def Decode(message, shift):
        print(message, shift)

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
        Encode(message, shift_num)
        restart = input("Do you want to decypher something else? 'Y' or 'N'").lower()
        Restart(restart)
    elif user_input == "decode":
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        Decode(message, shift_num)
        restart = input("Do you want to decypher something else? 'Y' or 'N'").lower()
        Restart(restart)
    else:
        print("Please chose a valid option.")
        Cypher()

Cypher()
