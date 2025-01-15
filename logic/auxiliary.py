from functools import reduce
from abc import ABC, abstractmethod
from random import shuffle


def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 and i != n and i != 1)))


def mprint(maze: list) -> None:
    for list in maze:
        for elem in list:
            print(elem, end=' ')
        print('')


class Walker(ABC):

    @abstractmethod
    def walk(self):
        pass


class RandomWalker(Walker):
    def __init__(self, initial_pos: tuple, maze_size: int):
        super().__init__()
        self._position = initial_pos
        self._recent_path = set()
        self._maze_size = maze_size
        self._directions = {'up': 1, 'down': self._maze_size + 1,
                            'left': 1, 'right': self._maze_size + 1}

    @property
    def position(self) -> tuple:
        return self._position

    @property
    def recent_path(self) -> set:
        return self._recent_path

    def walk(self) -> None:
        # Idea: utilizar el recent_path para no repetir posiciones
        self._recent_path.add(self._position)

        posibilities = []
        for key, value in self._directions.items():
            if value not in self._position:
                posibilities.append(key)
        shuffle(posibilities)

        if posibilities[0] == 'up':
            self._position = (self._position[0], self._position[1] - 1)
        elif posibilities[0] == 'down':
            self._position = (self._position[0], self._position[1] + 1)
        elif posibilities[0] == 'left':
            self._position = (self._position[0] - 1, self._position[1])
        elif posibilities[0] == 'right':
            self._position = (self._position[0] + 1, self._position[1])
