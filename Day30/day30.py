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
        except KeyError as error_message: --> Always try and use the actual error that yu want to catch
            print(f"The key {error_message} does not exist.")
        else:
            content = file.read()
            print(content)
        finally:
            file.close()
            print("File closed")

"""

# Final Project

try:
    file = open("a_file.txt")
    a_dictionary = {"Key": "Value"}
    # print(a_dictionary["Non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")