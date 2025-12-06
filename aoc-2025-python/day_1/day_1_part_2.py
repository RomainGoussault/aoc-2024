import numpy as np
with open("input", "r") as file:
    lines = file.readlines()

dial = 50
sum_of_dial_pointing_at_zero = 0
initial_dial = dial
for line in lines:
    to_add = 0

    direction = line[0]
    step = int(line[1:])

    if direction == "R":
        dial += step
        to_add = np.floor(dial / 100)

    elif direction == "L":
        dial -= step
        if dial <= 0:
            to_add = 1 + np.floor(np.abs(dial / 100))
            if initial_dial == 0:
                to_add -= 1 # so that we count correctly if we start at 0

    sum_of_dial_pointing_at_zero += to_add



    dial = dial % 100
    if to_add > 0:
        print(f"Direction: {direction}, {step}, initial dial: {initial_dial}, Dial: {dial}, steps added: {to_add}")
    else:
        print(f"Direction: {direction}, {step}, initial dial: {initial_dial}, Dial: {dial}")

    initial_dial = dial



print(sum_of_dial_pointing_at_zero)
