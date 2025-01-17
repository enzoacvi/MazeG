from functools import reduce
from math import dist
from random import randint


def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != n and i != 1)))


def mprint(maze: list) -> None:
    for list in maze:
        for elem in list:
            print(elem, end=" ")
        print("")


def find_farthest(ckp: tuple, checkpoints: list) -> tuple:
    farthest = None
    f_distance = 0
    for ckp2 in checkpoints:
        distance = round(dist(ckp, ckp2), 3)
        if distance > f_distance:
            farthest = ckp2
            f_distance = distance
    return farthest


def find_nearest(ckp: tuple, checkpoints: list) -> tuple:
    if ckp in checkpoints:
        checkpoints.remove(ckp)
    nearest = None
    n_distance = 1000
    for ckp2 in checkpoints:
        distance = round(dist(ckp, ckp2), 3)
        if distance < n_distance:
            nearest = ckp2
            n_distance = distance
    return nearest


def set_checkpoints(maze_map: list, size: int, maze_s: int, maze_n: int) -> list:
    y = 1
    f = size // maze_s
    checkpoints_y = []
    checkpoints_x = []
    for i in range(f):
        x = 1
        for j in range(f):
            for k in range(maze_n):
                rand_y = randint(y, y + maze_s - 1)
                rand_x = randint(x, x + maze_s - 1)

                while rand_y in checkpoints_y[-maze_n - 1:] or rand_x in checkpoints_x[-maze_n - 1:]:
                    rand_y = randint(y, y + maze_s - 1)
                    rand_x = randint(x, x + maze_s - 1)

                maze_map[rand_y][rand_x] = " "
                checkpoints_y.append(rand_y)
                checkpoints_x.append(rand_x)
            x += maze_s
        y += maze_s
    return list(zip(checkpoints_y, checkpoints_x))
