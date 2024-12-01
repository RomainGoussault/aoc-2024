import pandas as pd
import numpy as np

df = pd.read_csv("input", header=None, sep="   ")

location_from_first_team = df[0].values
location_from_second_team = df[1].values

# location_from_first_team.sort()
# location_from_second_team.sort()

similarity_score = 0
for location_id in location_from_first_team:
    indices = np.where(location_from_second_team == location_id)
    score = len(indices[0]) * location_id
    similarity_score += score

print(similarity_score)
