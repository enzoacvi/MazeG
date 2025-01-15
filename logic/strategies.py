from abc import ABC, abstractmethod
from auxiliary import factors, mprint, find_nearest, find_farthest, connect
from random import randint


class Strategy(ABC):

    @abstractmethod
    def construct(self):
        pass


class StrategyA(Strategy):

    def construct(self, size: int, s: int, n: int) -> list:

        # preconstruction (Random Scatter)
        maze_map = [['X' if i != 0 and i != size+1 and j != 0 and j != size+1
                     else 'M' for i in range(size + 2)]
                    for j in range(size + 2)]
        mprint(maze_map)
        maze_s = min(factors(size), key=lambda x: abs(x - s))
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
        mprint(maze_map)

        # connections (connect checkpoints)
        connect(maze_map, (1, 0), find_nearest((1, 0), checkpoints))
        connect(maze_map, (maze_s, size + 1), find_nearest((maze_s, size + 1), checkpoints))
        for checkp in checkpoints:
            farthest = find_farthest(checkp, checkpoints)
            connect(maze_map, checkp, farthest)
        mprint(maze_map)


if __name__ == "__main__":
    strategia = StrategyA()
    strategia.construct(size=10, s=5, n=2)
