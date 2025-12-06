
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
    result = 0
    new_bank = bank
    index_max_joltage = 0
    
    for i in range(12,0,-1):
        print(f" looking at index {i}")
        print(f" bank considered: {new_bank[:-i+1]}")

        if i == 1:
            max_joltage, index_max_joltage = find_max(new_bank[:])
        else:
            max_joltage, index_max_joltage = find_max(new_bank[:-i+1])

        print(f" max is {max_joltage} at index {index_max_joltage}")
        result = result + max_joltage * 10 ** (i-1)
        new_bank = new_bank[index_max_joltage+1:]

        print(result)
        print("")
    



    print("FINAL result", result)
    sum += result






print(sum)