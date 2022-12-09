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

import pandas
