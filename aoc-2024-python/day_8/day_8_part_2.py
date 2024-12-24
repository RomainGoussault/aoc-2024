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


def get_antenna(antenna_char, map):
    idx = np.where(map == antenna_char)
    return list(zip(idx[0], idx[1]))


def is_in_bounds(coord, map):
    return (
        coord[0] >= 0
        and coord[0] < map.shape[0]
        and coord[1] >= 0
        and coord[1] < map.shape[1]
    )


def get_antinodes_coords(
    antenna_0: tuple, antenna_1: tuple, map_size: int
) -> list[tuple]:
    antinode_coords = []

    for k in range(map_size):
        i_first = antenna_0[0]
        j_first = antenna_0[1]
        # print(f"first: i={i_first}, j={j_first}")
        i_second = antenna_1[0]
        j_second = antenna_1[1]
        # print(f"second: i={i_second}, j={j_second}")

        i_antinode_0 = i_first - k * (i_second - i_first)
        j_antinode_o = j_first - k * (j_second - j_first)
        antinode_0_coord = (i_antinode_0, j_antinode_o)
        antinode_coords.append(antinode_0_coord)

        i_antinode_1 = i_second + k * (i_second - i_first)
        j_antinode_1 = j_second + k * (j_second - j_first)
        antinode_1_coord = (i_antinode_1, j_antinode_1)
        antinode_coords.append(antinode_1_coord)

    return antinode_coords


def get_antinode_set(antenna_list: list, map: np.ndarray) -> set:
    antinode_set = set()

    for antenna_0 in antenna_list:
        for antenna_1 in antenna_list:
            if antenna_0 == antenna_1:
                continue
            antinodes_coords = get_antinodes_coords(antenna_0, antenna_1, map_size)

            for antinode_coord in antinodes_coords:
                if is_in_bounds(antinode_coord, map):
                    antinode_set.add(antinode_coord)
                    map[antinode_coord] = "#"

    return antinode_set


map = file_2_numpy("input")
print(map)
map_size = np.max(map.shape)
print(f"map_size: {map_size}")

unique_char = np.unique(map).tolist()
unique_char.remove(".")
print(unique_char)

total_antinode_set = set()
for char in unique_char:
    print(f"char: {char}")
    antenna_list = get_antenna(char, map.copy())
    current_set = get_antinode_set(antenna_list, map.copy())
    total_antinode_set = total_antinode_set.union(current_set)

print(len(total_antinode_set))
