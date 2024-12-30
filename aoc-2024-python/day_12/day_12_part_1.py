from collections import deque

data = open("aoc-2024-python/day_12/input").readlines()

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


def compute_perimeter(area_coords: set) -> int:
    perimeter = 0

    for coord in area_coords:
        # Check boundaries
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in deltas:
            if (coord[0] + dx, coord[1] + dy) not in area_coords:
                perimeter += 1

    return perimeter


visited = set()
price_sum = 0
for loc in grid_keys:
    if loc not in visited:
        print(f"Dealing with crop at {grid.get(loc)}")
        area_coords, plant = bfs(grid, loc)
        print("Area coords are computed")
        visited.update(area_coords)
        perimeter = compute_perimeter(area_coords)
        area = len(area_coords)
        price = area * perimeter
        print(f"Plant: {plant}, Area: {area}, Perimeter: {perimeter}")

        price_sum += price

print(price_sum)
