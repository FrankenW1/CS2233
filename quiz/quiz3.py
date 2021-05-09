from random import uniform
from typing import Tuple
import math

x_cord = []
y_cord = []
radius = []

def random_coordinate() -> Tuple[float, float]:
    return uniform(0, 1), uniform(0, 1)

def num_in_circ():
    for i in range(1000):
        hold = random_coordinate()
        x_cord.append(hold[0])
        y_cord.append(hold[1])

def calculate_pi():
    num_in_circ()
    for item1, item2 in zip(x_cord, y_cord):
        radius.append((item1 ** 2 + item2 ** 2))
    for item in radius:
        item = math.sqrt(item)

    num_in_circle = 0
    for item in radius:
        if item < 1:
            num_in_circle = num_in_circle + 1

    val_pi = 4 * num_in_circle / len(radius)
    return val_pi

if __name__ == '__main__':
   print(calculate_pi())
