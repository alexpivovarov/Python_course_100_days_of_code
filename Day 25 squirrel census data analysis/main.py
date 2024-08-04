import pandas

data = pandas.read_csv("C:/Users/Александр/PycharmProjects/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") # reading data
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"]) # counting the number of rowsin the 'data' dataframe where the column "Primary Fur Color" equals "Gray"
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"]) 
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(len(data[data["Primary Fur Color"] == "Gray"]))
print(len(data[data["Primary Fur Color"] == "Black"]))
print(len(data[data["Primary Fur Color"] == "Cinnamon"]))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv") #creating squirrel_count.csv file
