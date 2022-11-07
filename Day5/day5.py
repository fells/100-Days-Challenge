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
"""

# FINAL PROJECT

"""
print("Welcome to the PyPassword generator!")
letter_input = int(input("How many letters would you like in your password ?"))
symbol_input = int(input("How many symbols would you like ?"))
number_input = int(input("How many numbers would you like ?"))

print("Here is your password: ")

"""
