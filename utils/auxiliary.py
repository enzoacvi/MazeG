from functools import reduce
from math import dist
from random import randint
from collections import deque


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
    ckps = list(checkpoints)
    if ckp in ckps:
        ckps.remove(ckp)
    nearest = None
    n_distance = 1000
    for ckp2 in ckps:
        distance = round(dist(ckp, ckp2), 3)
        if distance < n_distance:
            nearest = ckp2
            n_distance = distance
    return nearest


def find_nearests(ckp: tuple, checkpoints: list, N: int) -> tuple:
    ckps = list(checkpoints)
    if ckp in ckps:
        ckps.remove(ckp)

    nearest_list = []
    for i in range(N):
        nearest = None
        n_distance = 1000
        for ckp2 in ckps:
            distance = round(dist(ckp, ckp2), 3)
            if distance < n_distance:
                nearest = ckp2
                n_distance = distance
        nearest_list.append(nearest)
        ckps.remove(nearest)
    return nearest_list


def set_checkpoints(maze_map: list, size: int, maze_s: int, maze_n: int) -> list:
    y = 0
    f = size // maze_s
    ckps_y = []
    ckps_x = []
    for i in range(f):
        x = 0
        for j in range(f):
            for k in range(maze_n):
                rand_y = randint(y, y + maze_s - 1)
                rand_x = randint(x, x + maze_s - 1)

                while rand_y in ckps_y[-maze_n - 1:] or rand_x in ckps_x[-maze_n - 1:]:
                    rand_y = randint(y, y + maze_s - 1)
                    rand_x = randint(x, x + maze_s - 1)

                maze_map[rand_y][rand_x] = " "
                ckps_y.append(rand_y)
                ckps_x.append(rand_x)
            x += maze_s
        y += maze_s
    return list(zip(ckps_y, ckps_x))


def set_external_walls(maze_map: list, size: int) -> list:
    maze = [['M' for i in range(size + 2)]]
    for sublist in maze_map:
        dq = deque(sublist)
        dq.appendleft("M")
        dq.append("M")
        maze.append(list(dq))
    maze.append(['M' for i in range(size + 2)])
    return maze
