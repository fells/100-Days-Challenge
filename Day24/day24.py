"""
        LEARNING HOW TO OPEN/READ/WRITE FILES

        Basic reading

        file = open("my_file.txt")  --> By using this method is recommended to always close the file, so it takes less space in your memory
        contents = file.read()
        print(contents)
        file.close()

        MORE ADVANCED WAY OF OPENING
        with open("my_file.txt") as file:  --> This way you don't need to close your file
            contents = file.read()
            print(contents)

        WRITING INTO THE FILE

        with open("my_file.txt", mode="w") as file:  --> You have to change the mode in order to write in to a file
            file.write("I'm a Jr. Developer")   --> And this will overwrite everything inside the file

        INSTEAD OF OVERWRITING, YOU CAN ADD TO THE FILE

        with open("my_file.txt", mode="a") as file:  --> "a" mode stands for append, this will add a new content
            file.write("\nI'm a Jr. Developer")


        If you ever try and open that doesn't exist yet with the W method, it will automatically create for you the file
        with want you have written.

"""

# Final Project

# Mail Merging

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as Letter:
    letter = Letter.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter.replace("[name]", f"{striped_name}")
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}", mode="w") as saved_letter:
            saved_letter.write(new_letter)
