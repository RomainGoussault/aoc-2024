import numpy as np

with open("input", "r") as file:
    lines = file.readlines()

line = lines[0].strip()


def divisors_np(n):
    arr = np.arange(1, n + 1)
    return arr[n % arr == 0].tolist()


def find_invalid_ids(start: int, end: int) -> list[int]:
    invalid_ids = []

    for id in range(start, end + 1):
        # print()
        # print(f"id: {id}")

        str_id = str(id)
        str_len = len(str_id)

        id_divisors = divisors_np(str_len)
        id_divisors.remove(1)
        # print(f"id_divisors: {id_divisors}")

        for divisor in id_divisors:
            # get list of all part
            step = str_len // divisor
            str_list = [
                str_id[i * step: (i + 1) * step] for i in range( divisor)
            ]
            # check all part are equals
            if len(set(str_list)) == 1:
                invalid_ids.append(id)
                # print(f"id: {id}")
                # print(f"divisor: {divisor}")
                # print(f"str list: {str_list}")
                # print("INVALID")

    return invalid_ids


print(line)
id_ranges = line.split(",")
total_invalid_ids = set()
for id_range in id_ranges:
    print()
    print(id_range)
    start, end = id_range.split("-")
    # print(f"Start: {start}, End: {end}")
    invalid_ids = find_invalid_ids(int(start), int(end))
    total_invalid_ids.update(invalid_ids)
    

print(total_invalid_ids)
print(sum(total_invalid_ids))