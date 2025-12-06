
with open("input", "r") as file:
    lines = file.readlines()


def find_max(bank: list) -> tuple[int, int]:
    max_joltage = max(bank)
    index_max_joltage = bank.index(max_joltage)

    return max_joltage, index_max_joltage

sum = 0
for line in lines:
    line = line.strip()
    bank = [int(char) for char in line]
    print(bank)

    max_joltage, index_max_joltage = find_max(bank[:-1])
    print(f" max is {max_joltage} at index {index_max_joltage}")

    max_joltage_2, index_max_joltage_2 = find_max(bank[index_max_joltage+1:])
    print(f" max is {max_joltage_2} at index {index_max_joltage_2}")

    result = 10 * max_joltage + max_joltage_2
    sum = sum + result
print(sum)