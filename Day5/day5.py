"""
            LOOPS

            FOR LOOP

            for item in list_of_items:
                #Do something to each item

            Example:
            fruits = ["Apple", "Peach", "Pear"]

            for fruit in fruits:
                print(fruit)
                print(fruit + " Pie")

            EXERCISE 1

            Average Height program

            students_height = input("Input a list of student heights ").split()

            for n in range(0, len(students_height)):
                students_height[n] = int(students_height[n])   # --> This is converting the values in to int and placing into a list

            total_height = 0
            for height in students_height:
                total_height += height   # --> This is doing a sum of all values

            students = 0
            for student in students_height:
                students += 1       # --> This is getting the amount of values inside the list

            average = round(total_height / students)
            print(f"The average height is {average}")

            EXERCISE 2

            Finding the highest value from a list of student scores

            student_scores = input("Input a list of students scores:\n").split()

            for n in range(0, len(student_scores)):
                student_scores[n] = int(student_scores[n])

            scores = 0
            for score in student_scores:
                if scores < score:
                    scores = score


            print(f"The average score is {scores}")

            USING THE RANGE FUNCTION INSIDE A FOR LOOP

            for number in range(1, 10):
                print(number)

            1
            2
            3
            4
            .
            .
            .
            9

            for number in range(1, 11, 3):  --> You can add a third variable that's going to be the steps that it counts
                print(number)

            1
            4
            7
            10

            user_input = input("Type a list of numbers.").split()

            for n in range(0, len(user_input))
                user_input[n] = int(user_input[n])


            total = 0
            for number in range (1, 101):
                total += number

            print(total)

            EXERCISE 3

            Create a program that calculates all of the even numbers from 1 to 100. Including 1 and 100

            total = 0
            for number in range(1, 101):
                if number % 2 == 0:
                 total += number

            print(total)

            EXERCISE 4
            Create a program that tells Fizz when it's divisible by 3, when the number is divisible by 5 print Buzz,
            when it's divisible by both 3 and 5 print FizzBuzz

            for number in range (1, 101):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)
"""
# FINAL PROJECT

import random
import string

print("Welcome to the PyPassword generator!")
letter_input = int(input("How many letters would you like in your password ?"))
symbol_input = int(input("How many symbols would you like ?"))
number_input = int(input("How many numbers would you like ?"))

letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)
numbers = list(string.digits)


password_list = []
for letter in range(letter_input):
    password_list.append(random.choice(letters))

for symbol in range(symbol_input):
    password_list.append(random.choice(symbols))

for number in range(number_input):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)
print(f"Here is your password: {password}")


