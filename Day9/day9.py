"""
        DICTIONARIES AND NESTING

        dictionary = {
            key: values    --> A dictionary is composed bu a key and it's values, such as the line bellow
            "Bug": "An error in a program that prevents the program from running as expected",  --> Bug is the Key value
        }

        Example:

        programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected",
        "Function": "A piece of code that you can easily call over and over again.",
        "Loop": "The action of doing something over and over again."
        }

        *Retrieving an item from the dictionary *
        print(programming_dictionary["Bug"])  --> This will print out the Value of the selected Key

        *Adding a new item to the dictionary / Edit an existing item in the dictionary*
        programming_dictionary["Hello"] = "Hello there"  --> This will add the key "Hello" to the end of the dictionary

        *Wipe an existing dictionary*
        programming_dictionary = {}

        *Loop through a dictionary*

        for thing in programming_dictionary:   --> This will output the key inside the dictionary
            print(thing)

        EXERCISE 1
        Write a program that converts the students scores to grades.

        student_scores = {
            "Harry": 81,
            "Ron": 78,
            "Hermione": 99,
            "Draco": 74,
            "Neville": 62,
        }

        student_grades = {}

        for student in student_scores:
            grade = student_scores[student]

            if grade >= 91:
                student_grades[student] = "Outstanding"
            elif grade >= 81:
                student_grades[student] = "Exceeds Expectations"
            elif grade >= 71:
                student_grades[student] = "Acceptable"
            else:
                student_grades[student] = "Fail"

        print(student_grades)

        NESTING IN DICTIONARY
        Example:

            travel_log = {
                "France": ["Paris", "Lille", "Dijon"],
                "Brazil": [{"cities_visited": ["Santa Catarina", "Rio de Janeiro", "São Paulo", "Paraná"]}],
                "Germany": ["Berlin", "Hamburg", "Stuttgart"],
            }

            travel_log["France"].append("Lyon")
            print(travel_log)
            print(travel_log["Brazil"][0]["cities_visited"][1])

        EXERCISE 2

        Create a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 dictionaries
        travel_log =[
                {
                    "country": "France",
                    "visits": 12,
                    "cities": ["Paris", "Lille", "Dijon"]
                },
                {
                    "country": "Germany",
                    "visits": 5,
                    "cities": ["Berlin", "Hamburg", "Stuttgart"]
                },
            ]

            def AddNewCountry():
                country = input("Please type a country that you have visited:\n")
                times_visited = int(input("Please type inthe times you have visited:\n"))
                list_of_cities = list(input("Pease type in the cities that you have visited:\n").split())
                new_dict = {
                    "country": country,
                    "visits": times_visited,
                    "cities": list_of_cities,
                }
                travel_log.append(new_dict)

            AddNewCountry()
            country_index = int(input("What country index do you want to search for ?\n"))
            country = travel_log[country_index]["country"]
            visits = travel_log[country_index]["visits"]
            cities = travel_log[country_index]["cities"]

            print(f"You have visited {country} {visits} times")
            print(f"You have been to {' '.join(cities)}")

"""

# FINAL PROJECT
import  logo

print(logo.gavel)

print("Welcome to the secret auction program.")
