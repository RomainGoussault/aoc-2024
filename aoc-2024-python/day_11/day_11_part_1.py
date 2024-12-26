with open("input", "r") as file:
    lines = file.readlines()

line = lines[0].rstrip("\n")

stones = [int(x) for x in line.split(" ")]
print(stones)


def has_even_digit(stone: int) -> bool:
    return len(str(stone)) % 2 == 0


def blink(stones: list[int]) -> list[int]:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)

        elif has_even_digit(stone):
            stone_str = str(stone)
            first_part = stone_str[: len(stone_str) // 2]
            second_part = stone_str[len(stone_str) // 2 :]
            new_stones.append(int(first_part))
            new_stones.append(int(second_part))

        else:
            new_stones.append(stone * 2024)

    return new_stones


for i in range(25):
    stones = blink(stones)

print(len(stones))
