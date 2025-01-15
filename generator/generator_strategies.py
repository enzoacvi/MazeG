from abc import ABC, abstractmethod
from random import randint

import utils


class Strategy(ABC):

    @abstractmethod
    def construct(self):
        pass


class Generator:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self.s = None
        self.n = None

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy: Strategy):
        self._strategy = new_strategy

    def generate(self, size: int):
        return self._strategy.construct(size, s=self.s, n=self.n)


class StrategyA(Strategy):

    def construct(self, size: int, s: int, n: int) -> list:

        # preconstruction (Random Scatter)
        maze_map = [['X' if i != 0 and i != size + 1 and j != 0 and j != size + 1
                     else 'M' for i in range(size + 2)]
                    for j in range(size + 2)]
        utils.mprint(maze_map)
        maze_s = min(utils.factors(size), key=lambda x: abs(x - s))
        maze_n = min(n, maze_s - 1)

        maze_map[1][0] = ' '  # entrada
        maze_map[maze_s][size+1] = ' '  # salida

        y = 1
        f = size // maze_s
        print(maze_s, maze_n, f)
        checkpoints = []
        for i in range(f):
            for j in range(f):
                x = 1
                for k in range(maze_n):
                    print(y, x)
                    rand_y = randint(y, y + maze_s - 1)
                    rand_x = randint(x, x + maze_s - 1)
                    maze_map[rand_y][rand_x] = ' '
                    checkpoints.append((rand_y, rand_x))
                    x += maze_s
            y += maze_s
        utils.mprint(maze_map)

        # connections (connect checkpoints)
        utils.connect(maze_map, (1, 0),
                      utils.find_nearest((1, 0), checkpoints))
        utils.connect(maze_map, (maze_s, size + 1),
                      utils.find_nearest((maze_s, size + 1), checkpoints))
        for checkp in checkpoints:
            farthest = utils.find_farthest(checkp, checkpoints)
            utils.connect(maze_map, checkp, farthest)
        utils.mprint(maze_map)
        return maze_map


if __name__ == "__main__":
    strategia = StrategyA()
    strategia.construct(size=10, s=5, n=2)
