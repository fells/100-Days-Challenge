"""
            LEARNING TO WORK WITH PANDAS AND HOW TO WORK WITH CSV's

            READING YOUR NORMAL CSV AS IT WAS A FILE

            with open("weather_data.csv") as data:
            csv_data = data.readlines()
            print(csv_data)

            HOW TO READ CSV FILES WITH THE CSV PACKAGE

            import csv

            with open("weather_data.csv") as data_file:
                data = csv.reader(data_file)
                for row in data:
                    print(row)


            MANIPULATING A LITTLE BIT THE CSV FILE WITH THE CSV PACKAGE

            import csv

            with open("weather_data.csv") as data_file:
                data = csv.reader(data_file)
                temperature = []
                for row in data:
                    if row[1] != "temp":
                        temperature.append(int(row[1]))

                print(temperature)


            HOW TO READ A CSV FILE WITH PANDAS

            weather = pandas.read_csv("weather_data.csv")
            print(weather)

            DOING THE SAME CODE AS BEFORE BUT WITH PANDAS

            import pandas

            weather_data = pandas.read_csv("weather_data.csv")
            print(weather_data["temp"])

            GETTING THE AVERAGE VALUE OF THE TEMPERATURES IN PANDAS

            weather_data = pandas.read_csv("weather_data.csv")
            weather_dict = weather_data.to_dict()
            temp_list = weather_data["temp"].to_list()
            print(weather_dict)
            print(temp_list)
            print(weather_data["temp"].mean())  --> Getting ght average
            print(weather_data["temp"].max())   --> Getting the max value
            print(weather_data["temp"].min())   --> Getting the min value
            print(weather_data["day"].to_list())  --> Converting the days into a list
            print(weather_data[weather_data.day == "Monday"])   --> extracting all values from that row
            print(weather_data[weather_data.temp == max(temp_list)])  --> Max temperature from that day

            monday = weather_data[weather_data.day == "Monday"]  --> Extracting one value from the DataFrame
            print(monday.condition)    --> Getting only the condition of that day in specific
            monday_temp = monday.temp  --> Getting the specific day`s temperature
            print(monday_temp)
            fahrenheit = (monday_temp * 9/5) + 32  --> Converting the temperature into Fahrenheit
            print(fahrenheit)


            HOW TO CREATE A DATAFRAME FROM SCRATCH ?

            data_dict = {
                "Students": ["Michel", "Rodrigo", "Fabio", "Joao"],
                "Scores": [10, 8, 10, 5],
            }

            data = pandas.DataFrame(data_dict)  --> By calling the DataFrame Class you can create a new DF
            data.to_csv("new_data.csv")  --> Converting this DF into a new CSV file

"""
# FINAL PROJECT
import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading the states Files
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        # Generating a CSV file which will contain the remaining states that you haven`t guessed
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Generating a CSV file which will contain the remaining states that you haven`t guessed
