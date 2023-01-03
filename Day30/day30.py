"""
        Catch Exceptions Error

        :try (Something that might cause an exception)
        :except (Do this if there WAS an exception)
        :else (Do this if there were NO exception)
        :finally (Do this no matter what happens)

        EXAMPLE

        file = open("a_file.txt")  --> Will cause an error cause there is no file named that way

        try:
            file = open("a_file.txt")
            a_dictionary = {"Key": "Value"}
            print(a_dictionary["Non_existent_key"])  --> Forcing a KeyError
        except FileNotFoundError: --> Always try and use the actual error that yu want to catch
            file = open("a_file.txt", mode="w")
            file.write("Something")
        except KeyError as error_message: --> Always try and use the actual error that you want to catch
            print(f"The key {error_message} does not exist.")
        else:
            content = file.read()
            print(content)
        finally:
            file.close()
            print("File closed")



        RAISING YOUR OWN EXCEPTIONS

        There's the keyword "Raise" where you can create your own exceptions

        EXAMPLE:

        try:
            file = open("a_file.txt")
            a_dictionary = {"Key": "Value"}
            print(a_dictionary["Non_existent_key"])
        except FileNotFoundError:
            file = open("a_file.txt", mode="w")
            file.write("Something")
        except KeyError as error_message:
            print(f"The key {error_message} does not exist.")
        else:
            content = file.read()
            print(content)
        finally:
            raise KeyError ("This is an error that I made up")  --> This will generate a Error even if there is no error


        OTHER EXAMPLE

        height = float(input("Height: "))
        weight = int(input("Weight: "))

        if height > 3:
            raise ValueError("Human height not be over 3 meters")


        bmi = weight / height ** 2


        EXERCISE 1

        fruits = ["Apple", "Pear", "Orange"]

        TODO: Catch the exception and make sure the code runs without crashes

        def make_pie(index):
            fruit = fruits[index]
            print(fruit + " Pie")

        list_len = len(fruits) - 1
        user_input = int(input("Pick a number of fruits to chose a pie: "))

        if user_input > list_len:
            raise IndexError("The number you chose is higher than the amount of available fruits")
        else:
            make_pie(user_input)

        OR THERE`S A SECOND OPTION TO SOLVE THIS BUG

        fruits = ["Apple", "Pear", "Orange"]

        def make_pie(index):
            try:
                fruit = fruits[index]
            except IndexError:
                print("Fruit Pie")
            else:
                print(fruit + " Pie")

        make_pie(2)


        EXERCISE 2

        facebook_post = [
            {"likes": 21, "Comments": 2},
            {"likes": 13, "Comments": 2, "Shares": 1},
            {"likes": 33, "Comments": 8, "Shares": 3},
            {"Comments": 4, "Shares": 2},
            {"Comments": 1, "Shares": 1},
            {"likes": 19, "Comments": 3},
        ]

        total_likes = 0

        for post in facebook_post:
            try:
                total_likes = total_likes + post["likes"]
            except KeyError:
                pass

        print(total_likes)



        EXERCISE 3

        import pandas

        data = pandas.read_csv("nato_phonetic_alphabet.csv")


        phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
        print(phonetic_dict)

        def generate_phonetic():
            word = input("Enter a word: ").upper()

            try:
                output_list = [phonetic_dict[letter] for letter in word]
            except KeyError:
                print("Sorry only letters in the alphabet please.")
                generate_phonetic()
            else:
                print(output_list)

        generate_phonetic()


        JSON LIB

        WRITE
        json.dump()

        READ
        json.load()

        UPDATE
        json.update()

        Finished day 30
"""

# Final Project
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def geerate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        geerate_phonetic()
    else:
        print(output_list)

geerate_phonetic()