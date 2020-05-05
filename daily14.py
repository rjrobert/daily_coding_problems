import random
from math import sqrt


def calculate_pi(r, precision):
    total_in_circle = 0.0
    for i in range(precision):
        rand_x, rand_y = random.uniform(-r, r), random.uniform(-r, r)
        distance_to_center = rand_x ** 2 + rand_y ** 2
        if sqrt(distance_to_center) <= r:
            total_in_circle += 1

    return (4 * total_in_circle / precision)


for i in range(10):
    print(calculate_pi(1, 1000))
