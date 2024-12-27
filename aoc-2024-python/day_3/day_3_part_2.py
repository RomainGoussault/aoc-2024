import re


with open("input", "r") as file:
    lines = file.readlines()

lines = [line.rstrip("\n") for line in lines]
line = "".join(lines)
# line = "xmul(2,10)&jjmul[3,10]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(2,10))!^don't()_mul(5,5)+mul(32,64](mul(11,8))?mul(8,5))"
# results = 20 + 20 = 40


def sum_mul(line: str) -> int:
    sum = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    results = re.findall(pattern, line)

    for result in results:
        result = result.replace("mul(", "")
        result = result.replace(")", "")
        multipliers = result.split(",")
        sum += int(multipliers[0]) * int(multipliers[1])

    return sum


sum = 0


dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"
dont_positions = [m.start() for m in re.finditer(dont_pattern, line)]

while len(dont_positions) > 0:
    print("Start loop")

    dont_position = dont_positions[0]

    # find next do position
    do_positions = [m.start() for m in re.finditer(do_pattern, line)]
    next_do = len(line) - 4
    for do_pos in do_positions:
        if do_pos > dont_position:
            next_do = do_pos
            print(f"found next do: {next_do}")
            break

    print(f"len line: {len(line)}")
    print(f"dont_position: {dont_position}")
    print(f"next_do: {next_do}")
    assert dont_position < next_do

    line = line[:dont_position] + line[next_do + 4 :]

    print(f"len line: {len(line)}")
    dont_positions = [m.start() for m in re.finditer(dont_pattern, line)]
    print(f"dont_pos: {dont_positions}")
    print("")

print(line)
sum = sum_mul(line)
print(sum)
