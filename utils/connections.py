from random import randint


def connect(maze: list, ckp1: tuple, ckp2: tuple) -> None:
    checkp1, checkp2 = list(ckp1), list(ckp2)
    direccion = True
    n = 5
    while checkp1 != checkp2:
        if randint(1, 5) < n:  # mantener dirección
            n = 5
            if direccion:
                if checkp1[0] > checkp2[0]:
                    checkp2[0] = checkp2[0] + 1
                elif checkp1[0] < checkp2[0]:
                    checkp2[0] = checkp2[0] - 1
                else:
                    direccion = False
                    n = 6
                    continue
            else:
                if checkp1[1] > checkp2[1]:
                    checkp2[1] = checkp2[1] + 1
                elif checkp1[1] < checkp2[1]:
                    checkp2[1] = checkp2[1] - 1
                else:
                    direccion = True
                    n = 6
                    continue
            maze[checkp2[0]][checkp2[1]] = " "
        else:  # cambiar direccion
            if direccion:
                direccion = False
            else:
                direccion = True
