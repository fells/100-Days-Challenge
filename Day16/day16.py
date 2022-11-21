"""
        OOP (Object-Oriented Programming)

        CLASS
        How to call a class in Python

        obj      class
        car = CarBlueprint()

        LEARNING TURTLE

        from turtle import Turtle, Screen
        #Turtle
        # Obj    Class
        mike = Turtle()
        # OBJ   Attributes
        mike.shape("turtle")
        mike.color("blue")
        mike.forward(100)

        # Screen
        screen = Screen()
        screen.exitonclick()

        OTHER PACKAGES (PrettyTable)

        from prettytable import PrettyTable

        table = PrettyTable()

        table.field_names = ["Pokemon", "Type"]
        table.align = "l"
        table.add_rows(
            [
                ["Pikachu", "Electricity"],
                ["Squirtle", "Water"],
                ["Charizard", "Fire"],
                ["Cacturne", "Plant"]
            ]
        )

        print(table)

"""

# FINAL PROJECT (Recreating the Coffee Machine with OOP)

