walker1 = RandomWalker((1, 0), size)
walker2 = RandomWalker((maze_s, size+1), size)
seguir = True
while seguir:  # o usar threading
    walker1.walk()
    walker2.walk()
    print(walker1.recent_path)
    print(walker2.recent_path)
    maze_map[walker1.position[0]][walker1.position[1]] = 'W'
    maze_map[walker2.position[0]][walker2.position[1]] = 'w'

    if walker1.position in walker2.recent_path:
        maze_map[walker1.position[0]][walker1.position[1]] = ' '
        break
    elif walker2.position in walker1.recent_path:
        maze_map[walker2.position[0]][walker2.position[1]] = ' '
        break
    mprint(maze_map)
