# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5)+32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
