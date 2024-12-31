from dataclasses import dataclass
from matplotlib import pyplot as plt
import numpy as np

data = open("input").readlines()

H = 103  # 7
W = 101  # 11
print("Height: ", H)
print("Width: ", W)


@dataclass
class Robot:
    position: tuple
    velocity: tuple


robots = []
for line in data:
    pos, vel = line.split(" ")
    pos = tuple(int(x) for x in pos[2:].split(","))
    vel = tuple(int(x) for x in vel[2:].split(","))
    robot = Robot(pos, vel)
    robots.append(robot)


def print_grid(robots: list):
    print("====================================")
    print("Printing grid")
    print("====================================")
    print("")

    grid = {(x, y): "." for x in range(W) for y in range(H)}

    for robot in robots:
        x, y = robot.position
        if grid[(x, y)] != ".":
            grid[(x, y)] = str(int(grid[(x, y)]) + 1)
        else:
            grid[(x, y)] = "1"

    for y in range(H):
        for x in range(W):
            print(grid[(x, y)], end="")
        print("")
    print("")
    print("")


def move_robot(robot: Robot, seconds: int = 1) -> Robot:
    for _ in range(seconds):
        x, y = robot.position
        vx, vy = robot.velocity
        x += vx
        y += vy
        x = x % W
        y = y % H
        robot.position = (x, y)

    return robot


quadrants = {}
quadrants["NW"] = 0
quadrants["NE"] = 0
quadrants["SW"] = 0
quadrants["SE"] = 0
mid_W = W // 2
mid_H = H // 2
s = 0
scores = []
for i in range(10000):
    quadrants["NW"] = 0
    quadrants["NE"] = 0
    quadrants["SW"] = 0
    quadrants["SE"] = 0
    s = 0
    for robot in robots:
        move_robot(robot, seconds=1)

        x, y = robot.position
        if x < W // 2 and y < H // 2:
            quadrants["NW"] += 1
        elif x > W // 2 and y < H // 2:
            quadrants["NE"] += 1
        elif x < W // 2 and y > H // 2:
            quadrants["SW"] += 1
        elif x > W // 2 and y > H // 2:
            quadrants["SE"] += 1
        else:
            s += 1
    score = quadrants["NW"] * quadrants["NE"] * quadrants["SW"] * quadrants["SE"]
    scores.append(score)

    a = 7671
    if i == a:
        print_grid(robots)


print(f" median score: {np.median(scores)}")
plt.plot(scores)
plt.show()
