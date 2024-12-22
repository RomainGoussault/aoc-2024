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


def get_start_position(map) -> tuple:
    idx = np.where(map == "^")
    i = idx[0][0]
    j = idx[1][0]

    return (i, j)


def next_dir(dir):
    if dir == (-1, 0):
        return (0, 1)  # goes right
    elif dir == (0, 1):
        return (1, 0)  # goes down
    elif dir == (1, 0):
        return (0, -1)  # goes left
    elif dir == (0, -1):
        return (-1, 0)  # goes up


def is_in_bounds(coord, map):
    return (
        coord[0] >= 0
        and coord[0] < map.shape[0]
        and coord[1] >= 0
        and coord[1] < map.shape[1]
    )


def is_stuck(obstruction_position, start_position, map):
    coord = start_position
    map[obstruction_position] = "O"
    moves = 0
    map[coord] = "X"
    dir = (-1, 0)
    while True:
        next_coord = (coord[0] + dir[0], coord[1] + dir[1])
        # print(f"Next coord: {next_coord}")

        if not is_in_bounds(next_coord, map):
            # print("Freee, out of bounds")
            map[coord] = "X"
            return False

        if map[next_coord] == "#" or map[next_coord] == "O":
            # print("dir change")
            dir = next_dir(dir)
            next_coord = (coord[0] + dir[0], coord[1] + dir[1])

            if map[next_coord] == "#" or map[next_coord] == "O":  # corner special case
                # print("dir change")
                dir = next_dir(dir)
                next_coord = (coord[0] + dir[0], coord[1] + dir[1])

        else:
            pass
            # print("keep the same dir")

        # Move
        moves += 1
        map[coord] = "X"
        map[next_coord] = "^"
        coord = next_coord

        total_cells = map.shape[0] * map.shape[1]
        is_loop = moves > total_cells
        if is_loop:
            # print("Loop")
            return True

        # print(map)
        # print("")
        # print(moves)


map = file_2_numpy("input")
print(map)

# Find coordinates where map equals "^"
start_position = get_start_position(map)
print(f"Start position: {start_position}")

print(map)
sum = 0


for i in range(map.shape[0]):
    print(f" progress: {i}/{map.shape[0]}")
    for j in range(map.shape[1]):
        if map[i, j] != "#" and (i, j) != start_position:
            # Create a copy of the map for each test
            map_copy = map.copy()
            obstruction_position = (i, j)
            if is_stuck(obstruction_position, start_position, map_copy):
                sum += 1


print(sum)
