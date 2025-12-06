with open("input", "r") as file:
    lines = file.readlines()


class IntRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0, self.end - self.start + 1)

    def __repr__(self):
        return f"(start: {self.start}, stop: {self.end})"




first_part = True
fresh_ranges_set = set()
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
        fresh_ranges_set.add(IntRange(start=int(x), end=int(y)))
    else:
        id = int(line)
        available_ingredients_id.add(id)

print("fresh range", fresh_ranges_set)


def is_overlapping(a: IntRange, b: IntRange) -> bool:
    return a.start <= b.end and b.start <= a.end


fresh_ingredients = set()
fresh_ranges_len = len(fresh_ranges_set)

total_len = 0
for i, fresh_range in enumerate(fresh_ranges_set):
    total_len += len(fresh_range)

cc = fresh_ranges_set.copy()
max_fresh_range = 0
for fresh_range in fresh_ranges_set:
    max_fresh_range = max(max_fresh_range, fresh_range.end)

print(f"End of fresh range is {max_fresh_range}")

x = 0
fresh_id_counts = 0
total_fresh_id_counts = 0
while True:

    # remove all elements in the set that where the end is before x
    fresh_ranges_set = {fresh_range for fresh_range in fresh_ranges_set if fresh_range.end > x}
    print("fresh_ranges_set", fresh_ranges_set)

    if len(fresh_ranges_set) == 0:
        break

    # Find closest start
    lowest_range = min(fresh_ranges_set, key=lambda x: x.start)
    print("Found lowest", lowest_range)

    if x < lowest_range.start: # we have void between x the range
        fresh_id_counts = len(lowest_range)
    else: # overlap
        print("Overlap")
        fresh_id_counts = lowest_range.end -x

    x = lowest_range.end

    total_fresh_id_counts += fresh_id_counts

    print("fresh_id_counts", fresh_id_counts)
    print()
    

print("total fresh_id_counts", total_fresh_id_counts)




aa = set()
for i, fresh_range_1 in enumerate(cc):
    aa.update(range(fresh_range_1.start, fresh_range_1.end + 1))
print("Truth", len(aa))

