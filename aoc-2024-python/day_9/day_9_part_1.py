def build_block_list(map: str) -> dict:
    block_list = []
    file_ID = -1

    for i, char in enumerate(map):
        if i % 2 == 0:  # file
            file_ID += 1
            file_size = int(char)
            block_list.extend([str(file_ID)] * file_size)

        else:  # free space
            free_space_size = int(char)
            block_list.extend(["."] * free_space_size)

    return block_list


with open("input", "r") as file:
    lines = file.readlines()

map = lines[0].rstrip("\n")
print(map)

block_list = build_block_list(map)
print(block_list)


def find_last_digit_index(block_list: list) -> int:
    # iterate from the end of the list
    for i in range(len(block_list) - 1, -1, -1):
        if block_list[i].isdigit():
            return i


fist_dot_idx = block_list.index(".")
last_digit_index = find_last_digit_index(block_list)


i = 0
while fist_dot_idx < last_digit_index:
    # Move last digit to the first dot index
    block_list[fist_dot_idx] = block_list[last_digit_index]
    block_list[last_digit_index] = "."

    fist_dot_idx = block_list.index(".")
    last_digit_index = find_last_digit_index(block_list)
    i += 1
    if i % 1000 == 0:
        metric = int((last_digit_index - fist_dot_idx) / len(block_list) * 100)
        print(f"progress: {metric}%")
    # print("".join(extended_map))

print("".join(block_list))
checksum = [i * int(x) for i, x in enumerate(block_list) if x.isdigit()]
print(sum(checksum))
