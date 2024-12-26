from functools import cache


with open("input", "r") as file:
    lines = file.readlines()

line = lines[0].rstrip("\n")

stones = [int(x) for x in line.split(" ")]
print(stones)


def has_even_digit(stone: int) -> bool:
    return len(str(stone)) % 2 == 0


@cache
def blink(stone: int, depth: int) -> int:

    if depth == 0:
        return 1

    if stone == 0:
        return blink(1, depth - 1)

    elif has_even_digit(stone):
        stone_str = str(stone)
        first_part = stone_str[: len(stone_str) // 2]
        second_part = stone_str[len(stone_str) // 2 :]
        return blink(int(first_part), depth - 1) + blink(int(second_part), depth - 1)
    
    else:
        return blink(stone * 2024, depth - 1)


sum = 0
for stone in stones:
    sum = sum + blink(stone, 75)

print(sum)
