from collections import deque
import numpy as np


def file_2_numpy(file_path):
    # Read the file and store each character in a list
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Remove newline characters at the end of each line
        lines = [line.rstrip("\n") for line in lines]

    # Create a NumPy array from the list of characters
    array_2d = np.array([list(line) for line in lines], dtype=str)

    return array_2d


def get_starting_location(char, map):
    idx = np.where(map == char)
    return list(zip(idx[0], idx[1]))


def is_in_bounds(coord, map):
    return (
        coord[0] >= 0
        and coord[0] < map.shape[0]
        and coord[1] >= 0
        and coord[1] < map.shape[1]
    )


def nine_finder(map, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nine_localisation = []
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        localization = queue.popleft()
        print(f"Visiting {localization}")

        if map[localization] == "9":
            print("Found 9")
            nine_localisation.append(localization)

        neighbors = []
        for direction in directions:
            new_localization = (
                localization[0] + direction[0],
                localization[1] + direction[1],
            )

            if is_in_bounds(new_localization, map):
                slope_diff = int(map[new_localization]) - int(map[localization])
                if slope_diff == 1:
                    neighbors.append(new_localization)

        print(f"Neighbors: {neighbors}")

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return nine_localisation


map = file_2_numpy("input")
starting_locations = get_starting_location("0", map)

print(map)

sum = 0
for starting_location in starting_locations:
    nine_localisation = nine_finder(map, starting_location)
    sum += len(nine_localisation)

print(sum)
