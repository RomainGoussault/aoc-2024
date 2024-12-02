import pandas as pd

df = pd.read_csv("input_test", header=None, sep="   ")

location_from_first_team = df[0].values
location_from_second_team = df[1].values

location_from_first_team.sort()
location_from_second_team.sort()

sum = 0
for left, right in zip(location_from_first_team, location_from_second_team):
    sum += abs(left - right)

print(sum)
