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


map = file_2_numpy("input")
print(map)

# Find coordinates where map equals "^"
start_position = get_start_position(map)
print(f"Start position: {start_position}")

coord = start_position
moves = 0
dir = (-1, 0)
map[coord] = "X"

while True:
    next_coord = (coord[0] + dir[0], coord[1] + dir[1])
    print(f"Next coord: {next_coord}")

    if not is_in_bounds(next_coord, map):
        print("out of bounds")
        map[coord] = "X"
        break

    if map[next_coord] == "#":
        print("dir change")
        dir = next_dir(dir)
        next_coord = (coord[0] + dir[0], coord[1] + dir[1])
    else:
        print("keep the same dir")

    # Move
    moves += 1
    map[coord] = "X"
    map[next_coord] = "^"
    coord = next_coord
    print(map)
    print("")
    print(moves)

print(map)
# Count number of X's and break if we've covered all non-# cells
x_count = np.count_nonzero(map == "X")
print(x_count)
