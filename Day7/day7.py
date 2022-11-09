"""

"""

# FINAL PROJECT
import random

word_to_discover = list(input("Please write the word to be discovered: ").lower())
word_to_discover_list = word_to_discover

print(word_to_discover)

lenght_of_word = len(word_to_discover)
n = 0

for letter in word_to_discover_list:
    n += 1
    word_to_discover_list[n - 1] = word_to_discover_list[n - 1] = "_"

print(word_to_discover_list)

guess = input("Guess a letter: ").lower()


def FindLetter(lst):
    if not lst:
        return print("There's no letter like that")
    elif lst[0] == guess:
        lst.append(guess)
    elif FindLetter(lst[1:]):
        lst.append(guess)


FindLetter(word_to_discover)

print(word_to_discover_list)
