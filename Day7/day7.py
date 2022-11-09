"""
            How to break a complex problem dow into a Flow Chart
"""

# FINAL PROJECT
import random
import hangman_words

def Game():
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    words = hangman_words.word_list
    word_to_discover = random.choice(words)
    word_to_discover_list = []
    lenght_of_word = len(word_to_discover)
    end_of_game = False
    lifes = 6
    wrong_letters = []

    print(word_to_discover)

    # Replacing every letter inside the string with a "_" so the person has to guess the word in the game
    for _ in range(lenght_of_word):
        word_to_discover_list.append("_")

    print(word_to_discover_list)

    while end_of_game != True:
        guess = input("Guess a letter: ").lower()

        # Getting the index of the letter in the word
        for position in range(lenght_of_word):
            letter = word_to_discover[position]
            if letter == guess:
                word_to_discover_list[position] = letter
        print(f"{''.join(word_to_discover_list)}")

        # This if statment is to check if the guessed letter is not inside the string
        if guess not in word_to_discover:
            lifes -= 1
            wrong_letters.append(guess)
            print(stages[lifes])
            print(f"Wrong gussed letter {wrong_letters}")
            if lifes == 0:
                restart = input("GAME OVER you lost ☠. Do you want to restart ? Type 'Y' or 'N'").lower()
                if restart == "y" or restart == "yes":
                    Game()
                else:
                    end_of_game = True
                    print("Until next time. 👋")

        # This is a if statment to check if there is no "_" anymore in the list
        if "_" not in word_to_discover_list:
            restart = input("Awesome, you won 🏆. Do you want to restart ? Type 'Y' or 'N'").lower()
            if restart == "y" or restart == "yes":
                Game()
            else:
                end_of_game = True
                print("Until next time. 👋")
Game()