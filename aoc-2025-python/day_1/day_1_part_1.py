with open("input", "r") as file:
    lines = file.readlines()

dial = 50
sum_of_dial_poiting_at_zero = 0

for line in lines:
    direction = line[0]
    step = int(line[1:])
    print(direction, step)
    if direction == "R":
        dial += step
    elif direction == "L":
        dial -= step
    dial = dial % 100

    sum_of_dial_poiting_at_zero += dial == 0

print(sum_of_dial_poiting_at_zero)
