from abc import ABC, abstractmethod

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
        self.N_connections = 2

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy: Strategy):
        self._strategy = new_strategy

    def generate(self, size: int):
        return self._strategy.construct(size, s=self.s, n=self.n, N=self.N_connections)


class StrategyA(Strategy):

    def construct(self, size: int, s: int, n: int, N: int) -> list:

        # preconstruction (Random Scatter)
        maze_s = min(utils.factors(size), key=lambda x: abs(x - s))
        maze_n = min(n, maze_s - 1)
        maze_map = [["X" for i in range(size)] for j in range(size)]
        maze_map[1][0] = " "  # entrada
        maze_map[maze_s][size - 1] = " "  # salida

        checkpoints = utils.set_checkpoints(maze_map, size, maze_s, maze_n)

        # connections (connect checkpoints with farthest)
        utils.connect(maze_map, (1, 0),
                      utils.find_nearest((1, 0), checkpoints))
        utils.connect(maze_map, (maze_s, size - 1),
                      utils.find_nearest((maze_s, size - 1), checkpoints))
        for checkp in checkpoints:
            farthest = utils.find_farthest(checkp, checkpoints)
            # conectamos con el más lejano
            utils.connect(maze_map, checkp, farthest)

        maze_map = utils.set_external_walls(maze_map, size)
        maze_map[2][0] = " "  # entrada
        maze_map[maze_s + 1][size + 1] = " "  # salida
        return maze_map


class StrategyB(Strategy):

    def construct(self, size: int, s: int, n: int, N: int) -> list:

        # preconstruction (Random Scatter)
        maze_s = min(utils.factors(size), key=lambda x: abs(x - s))
        maze_n = min(n, maze_s - 1)
        maze_map = [["X" for i in range(size)] for j in range(size)]
        maze_map[1][0] = " "  # entrada
        maze_map[maze_s][size - 1] = " "  # salida

        checkpoints = utils.set_checkpoints(maze_map, size, maze_s, maze_n)

        # connections (connect checkpoints)
        utils.connect(maze_map, (1, 0),
                      utils.find_nearest((1, 0), checkpoints))
        utils.connect(maze_map, (maze_s, size - 1),
                      utils.find_nearest((maze_s, size - 1), checkpoints))
        for checkp in checkpoints:
            nearest = utils.find_nearest(checkp, checkpoints)
            # conectamos con el más cercano
            utils.connect(maze_map, checkp, nearest)

        maze_map = utils.set_external_walls(maze_map, size)
        maze_map[2][0] = " "  # entrada
        maze_map[maze_s + 1][size + 1] = " "  # salida
        return maze_map


class StrategyC(Strategy):

    def construct(self, size: int, s: int, n: int, N: int) -> list:

        # preconstruction (Random Scatter)
        maze_s = min(utils.factors(size), key=lambda x: abs(x - s))
        maze_n = min(n, maze_s - 1)
        maze_map = [["X" for i in range(size)] for j in range(size)]
        maze_map[1][0] = " "  # entrada
        maze_map[maze_s][size - 1] = " "  # salida

        checkpoints = utils.set_checkpoints(maze_map, size, maze_s, maze_n)

        # connections (connect checkpoints)
        utils.connect(maze_map, (1, 0),
                      utils.find_nearest((1, 0), checkpoints))
        utils.connect(maze_map, (maze_s, size - 1),
                      utils.find_nearest((maze_s, size - 1), checkpoints))
        for checkp in checkpoints:
            nearests = utils.find_nearests(
                checkp, checkpoints, N)
            # conectamos con los más cercanos
            for i in range(N):
                utils.connect(maze_map, checkp, nearests[i])

        maze_map = utils.set_external_walls(maze_map, size)
        maze_map[2][0] = " "  # entrada
        maze_map[maze_s + 1][size + 1] = " "  # salida
        return maze_map


if __name__ == "__main__":
    strategia = StrategyA()
    strategia.construct(size=10, s=5, n=2)
