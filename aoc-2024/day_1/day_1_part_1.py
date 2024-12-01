import pandas as pd

df = pd.read_csv("input", header=None, sep="   ")

location_from_first_team = df[0].values
location_from_second_team = df[1].values

location_from_first_team.sort()
location_from_second_team.sort()

sum = 0
for i in range(len(location_from_first_team)):
    sum += abs(location_from_first_team[i] - location_from_second_team[i])

print(sum)
