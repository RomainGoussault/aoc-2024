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


def find_free_space(block_list: list, space_needeed: int) -> int:
    # find space_needed continous "." in block_list
    for i in range(len(block_list) - space_needeed + 1):
        if all(block_list[j] == "." for j in range(i, i + space_needeed)):
            return i

    return -1


with open("input", "r") as file:
    lines = file.readlines()

map = lines[0].rstrip("\n")
print(map)

block_list = build_block_list(map)
print((block_list))
print("".join(block_list))

file_ID_list = list(set([int(x) for x in block_list if x.isdigit()]))
file_ID_list.sort()
print(file_ID_list)

print("")
print("")
print("".join(block_list))

while len(file_ID_list) > 1:
    print(len(file_ID_list))
    file_ID_to_move = file_ID_list.pop()
    # print(f"file_ID_to_move: {file_ID_to_move}")

    file_size = block_list.count(str(file_ID_to_move))
    index_free = find_free_space(block_list, file_size)
    index_file_ID = block_list.index(str(file_ID_to_move))
    # print(f"index_free: {index_free}")

    if index_free != -1 and index_free < index_file_ID:
        # print("move file")
        for i in range(file_size):
            block_list[block_list.index(str(file_ID_to_move))] = "."
        for i in range(file_size):
            block_list[index_free + i] = str(file_ID_to_move)
        # print("".join(block_list))
    else:
        # print("no free space")
        pass

checksum = [i * int(x) for i, x in enumerate(block_list) if x.isdigit()]
print(sum(checksum))
