data = open("input").readlines()

H = len(data)
W = len(data[0].strip())
print("Height: ", H)
print("Width: ", W)

grid = {(x, y): data[y][x] for x in range(W) for y in range(H)}

deltas = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
sum = 0

for x, y in grid:
    if grid.get((x, y)) == "A":
        surrounding = []
        for dx, dy in deltas:
            surrounding.append(grid.get((x + dx, y + dy), ""))

        good_numbers = surrounding.count("S") == 2 and surrounding.count("M") == 2
        good_positions = grid.get((x + 1, y + 1)) != grid.get((x - 1, y - 1))
        if good_numbers and good_positions:
            sum += 1


print(f"sum: {sum}")
