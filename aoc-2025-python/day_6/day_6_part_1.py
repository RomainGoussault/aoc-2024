import pandas as pd

df = pd.read_csv("input", header=None, sep="\s+")
print(df.head())


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


sum = 0
for col in df.columns:
    s = df[col]
    operator = s[len(s) - 1]

    if operator == "*":
        result = 1
        for idx, operand in s.items():
            if is_int(operand):
                result *= int(operand)
    elif operator == "+":
        result = 0
        for idx, operand in s.items():
            if is_int(operand):
                result += int(operand)
    else:
        raise Exception

    sum += result

print(sum)
