from collections import defaultdict

with open("input", "r") as file:
    lines = file.readlines()

def is_paper_roll_accessible(grid, x, y):

    adjacent_rolls_of_paper_count = 0
    adjactent_positions = [(x+1,y+1), (x+0,y+1), (x+1,y+0), (x-1,y-1), (x-1,y), (x,y-1), (x+1,y-1), (x-1,y+1)]

    for (xx,yy) in adjactent_positions:
       if grid.get((xx,yy)) == "@":
            adjacent_rolls_of_paper_count += 1

    if adjacent_rolls_of_paper_count < 4:
        print(f"found: ", x, y)
    return adjacent_rolls_of_paper_count < 4



grid = defaultdict(str)
y_max = len(lines)
for i, line in enumerate(lines):
    line = line.strip()
    x = i
    y = y_max - i - 1
    for x, c in enumerate(line):
        grid[(x,y)] = c

accessible_paper_rolls_count = 0

for key, value in grid.items():
    (x, y) = key
    if grid.get((x,y)) == "@": # make sure it's a paper roll
        accessible_paper_rolls_count += is_paper_roll_accessible(grid, x, y)

print(accessible_paper_rolls_count)