from collections import deque

# data = open("aoc-2024-python/day_12/input_test").readlines()
data = open("input").readlines()

H = len(data)
W = len(data[0].strip())
print("Height: ", H)
print("Width: ", W)

grid = {(x, y): data[y][x] for x in range(W) for y in range(H)}
grid_keys = set(grid.keys())


def bfs(grid: dict, start: tuple) -> set:
    plant = grid.get(start)
    loc_visited = set()
    area_coords = set()
    queue = deque([start])
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        loc = queue.popleft()

        if loc in loc_visited:
            continue

        if grid.get(loc) == plant:
            loc_visited.add(loc)
            area_coords.add(loc)

            for delta in deltas:
                new_loc = (loc[0] + delta[0], loc[1] + delta[1])
                if new_loc in grid:
                    queue.append(new_loc)

    return area_coords, plant


def potential_same_side(side_0: tuple, side_1: tuple) -> bool:
    if side_0[1] != side_1[1]:
        return False

    dir = side_0[1]

    # side horizontal
    if dir[0] == 0:
        if side_0[0][1] == side_1[0][1]:
            return True
    else:
        if side_0[0][0] == side_1[0][0]:
            return True


def count_continuous_sets(nums):
    if not nums:  # Handle empty list case
        return 0

    count = 1  # At least one continuous set exists if the list is non-empty

    for i in range(1, len(nums)):
        # Check if current element is not consecutive with the previous
        if nums[i] != nums[i - 1] + 1:
            count += 1  # New continuous set starts

    return count


def compute_sides(area_coords: set) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sides_to_process = list()
    sides = 0

    for coord in area_coords:
        x, y = coord

        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            dir = (dx, dy)

            # If the neighbor is not part of the area, it's a border side
            if neighbor not in area_coords:
                side = (coord, dir)
                sides_to_process.append(side)

    # print(f"Sides to process: {sides_to_process}")
    # print(f"len sides to process: {len(sides_to_process)}")

    while sides_to_process:
        side = sides_to_process.pop()
        # print(f"Processing side: {side}")

        same_dir_sides = [s for s in sides_to_process if potential_same_side(side, s)]
        dir = side[1]
        # print(f"Same dir sides: {same_dir_sides}")

        for s in same_dir_sides:
            sides_to_process.remove(s)
        same_dir_sides.append(side)

        # side horizontal
        if dir[0] == 0:
            x_values = [s[0][0] for s in same_dir_sides]
            x_values.sort()
            sides += count_continuous_sets(x_values)
            # print(f" Horizontal sides, adding sides {count_continuous_sets(x_values)}")
        else:
            y_values = [s[0][1] for s in same_dir_sides]
            y_values.sort()
            sides += count_continuous_sets(y_values)
            # print(f" Vertical sides, adding sides {count_continuous_sets(y_values)}")

    return sides


visited = set()
price_sum = 0

for loc in grid_keys:
    if loc not in visited:
        print(f"Dealing with crop at {grid.get(loc)}")
        area_coords, plant = bfs(grid, loc)
        print("Area coords are computed")
        visited.update(area_coords)
        sides = compute_sides(area_coords)
        area = len(area_coords)
        price = area * sides
        print(f"Plant: {plant}, Area: {area}, Sides: {sides}")

        price_sum += price

print(price_sum)
