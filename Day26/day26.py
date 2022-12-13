"""
        LIST COMPREHENSION

        Basically you are creating a new list from a previous list

        numbers = [1, 2, 3, 4]
        new_list = []
        for n in numbers:           ---> This would be your normal looping and creating a new list
            add_1 = n + 1
            new_list.append(add_1)

        LIST COMPREHENSION

        new_list = [new_item for item in list]  --> This is changing the way we create are loops and shortening

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


        DICTIONARY COMPREHENSIONS
        new_dict = {new_key:new_value for item in list}
        new_dict = {new_key:new_value for (key, value) in dict.items()}
        new_dict = {new_key:new_value for (key, value) in dict.items() if test}

        EXERCISE 1
        You are given a sentence, you have to inform the amount of letters in each word of the sentence and place in a
        new dictionary

        sentence = "Hello there everyone, my name is Michel"

        result = {word:len(word) for word in sentence.split()}

        print(result)

        EXERCISE 2
        Convert the weather dictionary degrees celsius into fahrenheit

        weather = {
            "Monday": 12,
            "Tuesday": 14,
            "Wednesday": 15,
            "Thursday": 14,
            "Friday": 21,
            "Saturday": 22,
            "Sunday": 24,
        }

        result = {day: {(temp * 9 / 5) + 32} for (day, temp) in weather.items()}

        print(result)

        EXERCISE 3

        students = {
            "student": ["Angela", "Michel", "Fabio"],
            "scores": [95, 80, 87]
        }

        new_df = pandas.DataFrame(students)

        # Loop through the rows of a data frame
        for (index, row) in new_df.iterrows():
            print(row)


"""

# Final Project
# Create a program where you type in a word, and it will return with watch letter in NATO alphabet
import pandas
data = pandas.read_csv("nato_alphabet.csv")
nato_word = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Type in a word: ").upper()
nato_input = [nato_word[letter] for letter in user_input]
print(nato_input)