from dataclasses import dataclass
import numpy as np

data = open("input").readlines()


@dataclass
class Machine:
    button_A: tuple
    button_B: tuple
    prize: tuple


def get_move(machine: Machine) -> tuple[int, int]:
    # Define the vectors and the point
    v1 = machine.button_A  # Replace v1x and v1y with the components of vector v1
    v2 = machine.button_B  # Replace v2x and v2y with the components of vector v2
    target = machine.prize  # Replace x and y with the coordinates of point A

    det = v1[0] * v2[1] - v1[1] * v2[0]
    print("Determinant:", det)

    if np.isclose(det, 0):  # Check if determinant is approximately zero
        # print("The vectors are linearly dependent.")
        # Check if A lies on the line spanned by v1 (or v2 if preferred)
        print("Point A is not reachable.")

        return None
    else:
        print("The vectors are linearly independent.")
        # Solve for a and b
        tx = target[0]
        ty = target[1]
        a = (tx * v2[1] - ty * v2[0]) / det
        b = (v1[0] * ty - v1[1] * tx) / det
        coefficients = (a, b)

        diff = np.sum(np.abs(np.array(coefficients) - np.round(coefficients)))
        print("diff: ", diff)
        epsilon = 1e-6
        if diff < epsilon:
            coefficients = np.round(coefficients).astype(
                int
            )  # Convert to integer if valid
            print("Integer solution:", coefficients)
            return coefficients

        else:
            print("No integer solution exists.")
            return None


def get_cost(move: tuple) -> int:
    return 3 * (move[0]) + (move[1])


machine_strs = [data[i : i + 4] for i in range(0, len(data), 4)]
machines = []

for machine_str in machine_strs:
    button_A = tuple(
        int(x)
        for x in "".join(c for c in machine_str[0] if c.isdigit() or c == ",").split(
            ","
        )
    )
    button_B = tuple(
        int(x)
        for x in "".join(c for c in machine_str[1] if c.isdigit() or c == ",").split(
            ","
        )
    )
    prize = tuple(
        int(x)
        for x in "".join(c for c in machine_str[2] if c.isdigit() or c == ",").split(
            ","
        )
    )
    prize = (10000000000000 + prize[0], 10000000000000 + prize[1])
    machine = Machine(button_A, button_B, prize)
    machines.append(machine)

sum = 0
for i, machine in enumerate(machines):
    print(f"Machine {i + 1}")
    print(machine)
    move = get_move(machine)
    print(f"move: {move}")

    if move is None:
        print("No move possible")
    else:
        cost = get_cost(move)
        sum += cost
        print("cost: ", cost)

    print("")

print(sum)
