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

            names = ["Michel", "Fabio", "Rodrigo", "Amanda", "Julia", "Samantha"]
            print(f"Today {random.choice(names)} will pay the bill")
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
    computer = random.choice(possible_output)

    if user_choice == 0:
        print(rock)
        print("Computer chose:")
        print(computer)
        if user_choice > possible_output.index(rock):
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
        elif user_choice == possible_output.index(rock):
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
        print(computer)
        if user_choice == possible_output.index(paper):
            print("It's a draw, try again.")
            Game()
        elif user_choice > possible_output.index(paper):
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
        else:
            restart = input("You lost 😟. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
    elif user_choice == 2:
        print(scissor)
        print("Computer chose:")
        print(computer)
        if user_choice == possible_output.index(scissor):
            print("It's a draw, try again.")
            Game()
        elif user_choice > possible_output.index(scissor):
            restart = input("You won, congrats 🏆. Do you want to play again ? \"Y\" or \"N\"")
            if restart.lower() == "y" or restart.lower() == "yes":
                Game()
            else:
                print("Until next time. 👋")
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




