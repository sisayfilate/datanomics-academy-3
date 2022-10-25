import pandas as pd

# name = "Sisay"

# if name == "Sisay":
#     print("True")

df = pd.read_csv("nyc_weather.csv")
# print(df.head(10))

# df[all the true|false condition] ==> give me
import_columns = ["EST", "Humidity", "Temperature", "WindDirDegrees", "PrecipitationIn"]
# print(df[(df["Humidity"] >= 70)][import_columns])
print(df[df["PrecipitationIn"] == "T"][import_columns])
# [["EST", "Humidity"]])


# firstname| lastname | mname|

# fname mname lname  100. res_fields  =

# yyyy-mm-dd HH:mm:ss
# lname, fname mname
# fname: lname: mname

# df2 = df.head(15)
# print(df2.shape)
# print(df.shape)

# print(df.head())

# # # What was the max temperature in New York in the month of January?
# max_temp = df["Temperature"].max()
# print("max temperature is: ", max_temp)

# # # On which days did it rain?
# rained_days = list(df["EST"][df["Events"] == "Rain"])
# print("days rained: ", rained_days)

# # # What was the average wind speed in a month?
# ave_wind_speed = df["WindSpeedMPH"].mean()
# print("The average wind speed is : ", format(ave_wind_speed, ".2f"))


# lst = ["asnake", "sisay", "nati"]

# for i in lst:
#     print(i)
