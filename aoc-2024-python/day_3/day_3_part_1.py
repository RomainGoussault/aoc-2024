import re


with open("input", "r") as file:
    lines = file.readlines()


sum = 0
for line in lines:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    results = re.findall(pattern, line)
    print(results)

    for result in results:
        result = result.replace("mul(", "")
        result = result.replace(")", "")
        multipliers = result.split(",")
        sum += int(multipliers[0]) * int(multipliers[1])

print(sum)
