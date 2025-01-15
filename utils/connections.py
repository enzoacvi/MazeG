from random import randint


def connect(maze: list, ckp1: tuple, ckp2: tuple):
    checkp1, checkp2 = list(ckp1), list(ckp2)
    direccion = True
    while checkp1 != checkp2:
        if randint(1, 5) < 5:  # mantener dirección
            if direccion:
                if checkp1[0] > checkp2[0]:
                    checkp2[0] = checkp2[0] + 1
                elif checkp1[0] < checkp2[0]:
                    checkp2[0] = checkp2[0] - 1
            else:
                if checkp1[1] > checkp2[1]:
                    checkp2[1] = checkp2[1] + 1
                elif checkp1[1] < checkp2[1]:
                    checkp2[1] = checkp2[1] - 1
            maze[checkp2[0]][checkp2[1]] = ' '
        else:  # cambiar direccion
            if direccion:
                direccion = False
            else:
                direccion = True
