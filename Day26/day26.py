"""
        LIST COMPREHENSION

        Basically you are creating a new list from a previous list

        numbers = [1, 2, 3, 4]
        new_list = []
        for n in numbers:           ---> This would be your normal looping and creating a new list
            add_1 = n + 1
            new_list.append(add_1)

        LIST COMPREHENSION

        new_list = [new_item for item in list]

        Same code but with List Comprehension

        new_list = [n + 1 for n in numbers]

        EXERCISE

        range = range(1,5)
        new_range = [n * 2 for n in range]
        print(new_range)

        EXERCISE 2

        numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        squared_numbers = [number ** 2 for number in numbers]
        print(squared_numbers)

        EXERCISE 3

        numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        result = [num for num in numbers if num % 2 == 0]
        print(result)

        EXERCISE 4
        Create a new list called result, and this result will contain the number that are common in both files 1 and 2


        with open("file_1.txt") as data_1:
            numbers_1 = [int(n) for n in data_1]

        with open("file_2.txt") as data_2:
            numbers_2 = [int(n) for n in data_2]

        combined_numbers = numbers_1 + numbers_2
        shared_numbers = [n for n in numbers_1 if n in numbers_2]
        print(shared_numbers)

"""

# Final Project
# Create a program where you type in a word, and it will return with watch letter in NATO alphabet
import pandas
#
# data = pandas.read_csv("nato_alphabet.csv")
# user_input = input("Type in a word: ").upper()
# nato_list = [letter for letter in user_input if letter in data.letter]
# print(nato_list)
