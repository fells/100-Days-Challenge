"""
        NAMESPACES

        LOCAL VS GLOBAL SCOPE

        Example:
        enemies = 1


        def increase_enemies():
            enemies = 2
            print(f"Enemies inside function: {enemies}")


        increase_enemies()   = 2
        print(f"Enemies outside the function: {enemies}")   = 1

        # Local scope

        def drink_potion():
            potion_strenght = 2
            print(potion_strenght)
        drink_potion()

        # global scope

        player_health = 10

        def drink_potion():
            potion_strength = 2
            print(player_health + potion_strength)
        drink_potion()
        print(player_health)

        # There is a Block Scope

        enemies = ["Skeleton", "Zombie", "Alien"]
        game_level = 3

        if game_level < 5:
            random_enemie = random.choice(enemies)
        def enemie_randomizer():
            random_enemie = random.choice(enemies)
            return random_enemie


        enemie = enemie_randomizer()
        print(enemie)
        print(random_enemie)


"""
import random
import os

# FINAL PROJECT

restart = False
life = 0
easy = 10
hard = 5


def random_number():
    """Generates a random number between 1 and 100"""
    random_num = random.randint(1, 100)
    return random_num


def check_guess(random_num, difficulty, life):
    """Check if the user's guess is the same with the random number and lowers it's life"""
    user_guess = int(input("Make a guess:\n"))

    if difficulty >= life < difficulty:
        if user_guess > random_num:
            life += 1
            print(f"You have {difficulty - life} left")
            print("A little lower. ⬇️")
            check_guess(random_num, difficulty, life)
        elif user_guess < random_num:
            life += 1
            print(f"You have {difficulty - life} left")
            print("A little higher. ⬆️")
            check_guess(random_num, difficulty, life)
        elif user_guess == random_num:
            print("Awesome you won! 🏆")
            user_restart = input("Do you want to restart the game ?  'Y' or 'N':\n").lower()
            if user_restart == "y" or user_restart == "yes":
                guessing_game()
            else:
                print("See ya. 👋")
    else:
        print("Game Over. ☠️")
        user_restart = input("Do you want to restart the game ?  'Y' or 'N':\n").lower()
        if user_restart == "y" or user_restart == "yes":
            guessing_game()
        else:
            print("See ya. 👋")


def check_fifficulty(difficulty):
    """Check's the difficulty that the user choose"""
    if difficulty == "easy":
        return easy
    else:
        return hard

def guessing_game():
    global restart
    global life
    random_num = random_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard':\n").lower()

    if difficulty == "easy":
        print(f"You have {easy} attempts remaining to guess the number.")
        check_guess(random_num, check_fifficulty(difficulty), life)
    elif difficulty == "hard":
        print(f"You have {hard} attempts remaining to guess the number.")
        check_guess(random_num, check_fifficulty(difficulty), life)
    else:
        print("Please select a valid difficulty.")
        restart = True
        guessing_game()


guessing_game()
