from collections import defaultdict

with open("input", "r") as file:
    lines = file.readlines()

def is_paper_roll_accessible(grid, x, y):

    adjacent_rolls_of_paper_count = 0
    adjactent_positions = [(x+1,y+1), (x+0,y+1), (x+1,y+0), (x-1,y-1), (x-1,y), (x,y-1), (x+1,y-1), (x-1,y+1)]

    for (xx,yy) in adjactent_positions:
       if grid.get((xx,yy)) == "@":
            adjacent_rolls_of_paper_count += 1

    return adjacent_rolls_of_paper_count < 4


# Create grid
grid = defaultdict(str)
y_max = len(lines)
for i, line in enumerate(lines):
    line = line.strip()
    x = i
    y = y_max - i - 1
    for x, c in enumerate(line):
        grid[(x,y)] = c



total_sum = 0
while True:
    print("Loooooping")
    accessible_paper_rolls_count = 0
    paper_rolls_to_be_removed = set()

    for key, value in grid.items():
        (x, y) = key
        if grid.get((x,y)) == "@": # make sure it's a paper roll

            if is_paper_roll_accessible(grid, x, y):
                accessible_paper_rolls_count += 1
                paper_rolls_to_be_removed.add((x,y))

    total_sum += accessible_paper_rolls_count

    if accessible_paper_rolls_count > 0:
        # Now remove the paper rolls
        for (x,y) in paper_rolls_to_be_removed:
            grid[(x,y)] = "."
    else:
        break

print(total_sum)