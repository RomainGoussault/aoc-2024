with open("input", "r") as file:
    lines = file.readlines()


def is_fresh(id, fresh_ranges) -> bool:
    for fresh_range in fresh_ranges:
        min = fresh_range[0]
        max = fresh_range[1]

        if id >= min and id <= max:
            return True

    return False


first_part = True
fresh_ranges = set()
available_ingredients_id = set()
for i, line in enumerate(lines):
    line = line.strip()
    print(line)
    if line == "":
        first_part = False
        print("SWITCH")
        continue

    if first_part:
        (x, y) = line.split("-")
        fresh_ranges.add((int(x), int(y)))
    else:
        id = int(line)
        available_ingredients_id.add(id)

print("fresh range", fresh_ranges)
print("available ingredients", available_ingredients_id)

sum = 0
for id in available_ingredients_id:
    sum += is_fresh(id, fresh_ranges)

print(sum)
