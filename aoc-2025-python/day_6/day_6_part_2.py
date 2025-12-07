import numpy as np

filename = "input"

with open(filename) as f:
    arr = np.array([list(line.rstrip("\n")) for line in f])


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


print(arr)
transposed_arr = np.transpose(arr)
print("Transposed")
print(transposed_arr)

transposed_filename = "transposed_" + filename
np.savetxt(transposed_filename, transposed_arr, fmt="%s", delimiter="")

with open(transposed_filename, "r") as file:
    lines = file.readlines()

first_line = True
num_to_process = []  # Use list instead of set to allow duplicates
sum = 0
counter = 0
lines.append("" * len(lines[0]))

for line in lines:
    line = line.strip()
    print("line:", line)
    if first_line:
        chars = list(line)
        operator = chars[-1]
        first_line = False
        print("operator", operator)
        chars[-1] = ""
        line = "".join(chars)

    if is_int(line):
        num = int(line)
        num_to_process.append(num)

    else:  # end of number, time to calculate
        print("num_to_process", num_to_process)

        if operator == "*":
            result = 1
            for num in num_to_process:
                result *= int(num)
        elif operator == "+":
            result = 0
            for num in num_to_process:
                result += int(num)
        print("result", result)
        print()
        print("========")
        print()
        print("new line")
        sum += result
        num_to_process = []
        first_line = True


print(sum)
