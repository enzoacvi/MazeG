from abc import ABC, abstractmethod
from auxiliary import factors, RandomWalker
from random import randint


class Strategy(ABC):

    @abstractmethod
    def construct(self):
        pass


class StrategyA(Strategy):

    def construct(self, size: int, s: int, n: int) -> list:

        # preconstruction (Random Scatter)
        maze_map = [['X' for i in range(size + 1)] for j in range(size + 1)]  # +1 por los bordes
        maze_s = min(factors(size), key=lambda x: abs(x - s))
        maze_n = min(n, maze_s - 1)

        maze_map[1][0] = ' '  # entrada
        maze_map[maze_s][size] = ' '  # salida

        y = 1
        f = size / maze_s
        for i in range(f):
            x = 1
            for j in range(maze_n):
                for k in range(f):
                    maze_map[randint(y, y + maze_s)
                             # (0,0) es arriba a la izq
                             ][randint(x, x + maze_s)] = ' '
                    x += maze_s
            y += maze_s

        # connections
        walker1 = RandomWalker((1, 0), size)
        walker2 = RandomWalker((maze_s, size), size)
        seguir = True
        while seguir:  # o usar threading
            walker1.walk()
            walker2.walk()
            if walker1.position == walker2.position:
                maze_map[walker1.position[0]][walker1.position[1]]
                break
            maze_map[walker1.position[0]][walker1.position[1]] = ' '
            maze_map[walker2.position[0]][walker2.position[1]] = ' '

        return maze_map
