with open("input", "r") as file:
    lines = file.readlines()

line = lines[0].strip()


def find_invalid_ids(start: int, end: int) -> list[int]:
    invalid_ids = []

    for id in range(start, end + 1):
        # print(id)
        str_id = str(id)
        str_len = len(str_id)
        if str_len % 2 == 1:  # odd len
            continue

        middle = str_len // 2
        # print(f"middle {str_id[middle + 1 :]}")
        if str_id[:middle] == str_id[middle:]:
            invalid_ids.append(id)
            # print("INVALID")
    return invalid_ids


print(line)
id_ranges = line.split(",")
total_invalid_ids = set()
for id_range in id_ranges:
    print(id_range)
    start, end = id_range.split("-")
    # print(f"Start: {start}, End: {end}")
    invalid_ids = find_invalid_ids(int(start), int(end))
    total_invalid_ids.update(invalid_ids)


print(sum(total_invalid_ids))
