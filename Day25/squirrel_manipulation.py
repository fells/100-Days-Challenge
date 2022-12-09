# This exercise is to try and manipulate the data

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_fur = data["Primary Fur Color"].to_list()

grey_fur = squirrel_fur.count("Gray")
red_fur = squirrel_fur.count("Cinnamon")
black_fur = squirrel_fur.count("Black")

new_DF = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_fur, red_fur, black_fur]
}

squirrel_count = pandas.DataFrame(new_DF)
squirrel_count.to_csv("squirrel_count.csv")
