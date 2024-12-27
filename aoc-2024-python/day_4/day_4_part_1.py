
data = open("input").readlines()

H = len(data)
W = len(data[0].strip())
print("Height: ", H)
print("Width: ", W)

grid = {(x, y):data[y][x] for x in range(W) for y in range(H)}

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
sum = 0
target = "XMAS"
target_len = len(target)

for x, y in grid:
    for dx, dy in deltas:
        candidate = ""
        for i in range(target_len):
            candidate = candidate + grid.get((x + i * dx, y + i * dy), "")
        if candidate == target:
            sum += 1
        

print(f"sum: {sum}")
