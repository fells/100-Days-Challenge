"""
            RANDOMISATION

            random_int = random.randint(0,10)  --> The first random is the module after the "." is a function inside the module, in this case theres a function called randint
            print(random_int)

            random_float = random.random() * 5
            print(random_float)

            EXERCISE 1

            Coin Flip Program

            coin_flip = random.randint(0,1)

            if coin_flip == 0:
                print("Heads")
            else:
                print("Tales")

            LISTS

            It's a Data Structure

            names = ["Michel", "Amanda", "Fabio", "Mercio", "Ludmila", "Mauro", "Monica", "Eliane"]  --> This is how you create a list between []

            This is how you access an index of a list

            names[0] = "Michel"
            names[2] = "Fabio"

            This is how you add a new item to the end of the list

            names.append("Lucas")

            EXERCISE 2

            Create a random bill payer program

            user_input = input("Give me everybody's names, separated by a comma.\n").capitalize()
            names = user_input.split(", ")
            num_items = len(names)
            random_item = random.randint(0, num_items - 1)
            print(f"Today {names[random_item]} will pay the bill")

            NESTED LIST

            dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

            fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
            vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

            dirty_dozen = [fruits, vegetables]  --> NESTED LISTS

            EXERCISE 3
            Let's create a tick tack to game

            row1 = ["⬜", "⬜", "⬜"]
            row2 = ["⬜", "⬜", "⬜"]
            row3 = ["⬜", "⬜", "⬜"]

            map = [row1, row2, row3]
            print(f"{row1}\n{row2}\n{row3}")
            position = input("Where do you want to put your treasure ?\n")


            horizontal = int(position[0])
            vertical = int(position[1])

            map[vertical -1][horizontal -1] = "X"

            print(f"{row1}\n{row2}\n{row3}")

"""

# Final Project
import random

def Game ():

    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

    paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

    scissor = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

    user_choice = int(input("What do you choose ? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))

    possible_output = [rock, paper, scissor]
    computer = random.randint(0, 2)
    computer_index = possible_output[computer]

    if user_choice == 0:
        print(rock)
        print("Computer chose:")
        print(computer_index)
        if user_choice == 0 and computer == 2:
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
        elif user_choice == computer:
            print("It's a draw, try again.")
            Game()
        else:
            restart = input("You lost 😟. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
    elif user_choice == 1:
        print(paper)
        print("Computer chose:")
        print(computer_index)
        if user_choice == 1 and computer == 0:
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
        elif user_choice == computer:
            print("It's a draw, try again.")
            Game()
        else:
            restart = input("You lost 😟. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
    elif user_choice == 2:
        print(scissor)
        print("Computer chose:")
        print(computer_index)
        if user_choice == 2 and computer == 1:
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
        elif user_choice == computer:
            print("It's a draw, try again.")
            Game()
        else:
            restart = input("You lost 😟. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
    else:
        print("Please select a valid option.")
        Game()

Game()