"""
            CONDITIONAL
            IF/ELSE Statements

            if (condition):
                do this
            else:
                do this

            example:
            water_level = 50

            if(water_level > 80):
                print("Drain Water")
            else:
                print("Continue filling the tub")

            example for an amusement park

            Ticket booth for a Roller coaster

            minimum_height = 120
            minimum_age = 13
            adult_age = 18
            adult_ticket = 20
            kid_ticket = 10

            user_height = int(input("How tall are you ? (In cm) "))
            user_age = int(input("How old are you ? "))

            if (user_age >= minimum_age and user_height >= minimum_height and user_age >= adult_age):
                print(f"It will be {adult_ticket} dollars your ticket. ")
                payment = input("Do you wish to pay ? ")
                if (payment.lower() == "yes" or payment.lower() == "y"):
                    print("Enjoy your ride. 🎈")
                else:
                    print("Next please 🙄")
            elif (user_age >= minimum_age and user_height >= minimum_height and user_age < adult_age):
                print(f"It will be {kid_ticket} dollars your ticket. ")
                payment = input("Do you wish to pay ? ")
                if (payment.lower() == "yes" or payment.lower() == "y"):
                    print("Enjoy your ride. 🎈")
                else:
                    print("Next please 🙄")
            elif (user_age < minimum_age and user_height >= minimum_height):
                print("You're not old enough. Sorry maybe next time. 😟")
            else:
                print("You're not tall enough, maybe when you are older. 😟")


            COMPARISON OPERATORS

            >    (Greater than)
            <    (Less than)
            >=   (Greater than or equal to)
            <=   (Less than or equal to)
            ==   (Equals to)
            !=   (Not equals to)


            EXERCISE 1

            Create an odd or even program

            user_number = int(input("Type in a number: "))

            if user_number % 2 == 0:
                print("You have a even number")
            else:
                print("You have a odd number")


            MODULO

            Divides a number to another number, and it will give you the remainder

            example:  2 % 2 == 0 --> Even number
            example:  3 % 2 == 0 --> Odd number  (3 /2 = 1 != 0 resulting in a Odd number)

            NESTED IF / ELSE STATEMENTS

            if (condition):
                do this
                if (condition 2):
                    do this
                else:
                    do this
            else:
                do this

            EXERCISE 2
            BMI 2.0 CALCULATOR

            Create a new BMI Calculator

            user_height = float(input("What's your height ?\n"))
            user_weight = float(input("How much do you weight ?\n"))

            BMI = round(user_weight / user_height ** 2)

            if BMI < 18.5:
                print(f"You're BMI is {BMI}, you are underweight")
            elif BMI < 25:
                print(f"You're BMI is {BMI}, you have a normal weight")
            elif BMI < 30:
                print(f"You're BMI is {BMI}, you are overweight")
            elif BMI < 35:
                print(f"You're BMI is {BMI}, you are obese")
            else:
                print(f"You're BMI is {BMI}, you are clinically obese")

            EXERCISE 3

            Create a Leap Year finder

            year = int(input("Which year do you want to check ? "))

            if (year % 4 == 0):
                if year % 100 != 0:
                    if year % 400 == 0:
                        print(f"{year} is a Leap year")
                    else:
                        print(f"{year} is not a Leap year")
                else:
                    print(f"{year} is a Leap year")
            else:
                print(f"{year} is not a Leap year")


            MULTIPLE IF/ELSE STATEMENTS

            if (condition):
                do this
            elif (condition 2):
                do this
            else:
                do this

            EXERCISE 4

            Pizza Size Slice program


            print("Welcome to Pizza Planet")

            size = input("Whars size of pizza do you want ? S, M or L\n")
            add_pepperoni = input("Do you want to add pepperoni ? Y oy N\n")
            extra_cheese = input("Do you want extra cheese ? Y or N\n")

            small_pizza = 15
            medium_pizza = 20
            large_pizza = 25

            pepperoni_small_pizza = 2
            pepperoni_for_others = 3
            extra_cheese_pizza = 1

            bill = 0

            if (size.lower() == "s" or size.lower() == "small"):
                bill = small_pizza
                if add_pepperoni.lower() == "y" or add_pepperoni.lower() == "yes":
                    bill = bill + pepperoni_small_pizza
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")
                else:
                    bill = bill
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")
            elif (size.lower() == "m" or size.lower() == "medium"):
                bill = medium_pizza
                if add_pepperoni.lower() == "y" or add_pepperoni.lower() == "yes":
                    bill = bill + pepperoni_for_others
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")
                else:
                    bill = bill
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")

            elif (size.lower() == "l" or size.lower() == "large"):
                bill = large_pizza
                if add_pepperoni.lower() == "y" or add_pepperoni.lower() == "yes":
                    bill = bill + pepperoni_for_others
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")
                else:
                    bill = bill
                    if extra_cheese.lower() == "y" or extra_cheese.lower() == "yes":
                        bill = bill + extra_cheese_pizza
                        print(f"Your final bill is {bill}")
                    else:
                        print(f"Your final bill is {bill}")

            else:
                print("You dind't pick a correct option")


            LOGICAL OPERATORS

            if condition1 and condition2:
                do this
            elif condition1 or condition2:
                do this
            elif not condition2:
                do this
            else:
                end

            EXERCISE 4
            Love calculator


"""

# FINAL PROJECT

import os

def Borders ():
    print(60 * "*")

def Logo ():
    print("""  
 ___                         _               
|_ _|_  _  _    _     _  _  | |_ ||_    _  ||
 | |/_|/o\/o\|U(c'|U|/_|/o\ | (c'|/o\ |/ \/o|
 |_|L| \( \_,]_|_)\_/L| \(  |_\_)L\_,]L_n|\_|                                             
    """)


def Game ():

    restart_game = False

    Borders()

    Logo()

    Borders()

    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    choice_1 = input(f"You're at a cross road. Where do you want to go ? Type 'left' or 'Right'\n")

    if (choice_1.lower() == "left"):
        choice_2 = input("You come to a lake. There is a island in the middle of the lake. Type 'wait' fot a boat. Type 'swim' to swim acroos.")
        if (choice_2.lower() == "wait"):
            choice_3 = input("A boat came for you to go to the island, but there are some pirates. Do you wish to go with them ? or fight ?")
            if (choice_3.lower() == "go"):
                print("You won the game and got the gold 🪙")

            else:
                print("The pirates killed you and took you're gold.")
                restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
                if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
                    restart_game = True
                    Game()
                else:
                    os.system('cls')
        else:
            print("A shark eat you.")
            restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
            if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
                restart_game = True
                Game()
            else:
                os.system('cls')
    else:
        print("You ran into a Lion and got you killed.")
        restart_game_choice = input("GAME OVER. Do you want to play the game again ?")
        if (restart_game_choice.lower() == "y" or restart_game_choice.lower() == "yes"):
            restart_game = True
            Game()
        else:
            os.system('cls')


Game()