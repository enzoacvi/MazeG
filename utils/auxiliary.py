from functools import reduce
from math import dist


def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != n and i != 1)))


def mprint(maze: list) -> None:
    for list in maze:
        for elem in list:
            print(elem, end=' ')
        print('')


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
    nearest = None
    n_distance = 1000
    for ckp2 in checkpoints:
        distance = round(dist(ckp, ckp2), 3)
        if distance < n_distance:
            nearest = ckp2
            n_distance = distance
    return nearest
