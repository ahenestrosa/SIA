from game.Sokoban import Sokoban
from game import Constants
from BFS.Bfs import Bfs
from DFS.Dfs import Dfs
from collections import deque
import time
import json


def main():
    
    # objective = [(2,5),(6,5)]
    # dimensions = (9,9)
    # boxes = [(5,5), (3,5)]
    # walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
    #         (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
    #         (8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),
    #         (1,8),(2,8),(3,8), (4,8),(5,8),(6,8),(7,8)]
    # player = (4, 5)
    # sokoban = Sokoban(walls, objective, dimensions, player, boxes)

    objective = [(0,0), (2,2)]
    dimensions = (5,5)
    boxes = [(0,1), (1, 2)]
    walls = [(3,3), (4,4)]
    player = (0, 2)
    sokoban = Sokoban(walls, objective, dimensions, player, boxes)

    with open('TP1/config.json') as config:
        data = json.load(config)

    algorithm = data['algorithm']
    level_map = data['level_map']
    iddfs_max_depth = data["iddfs_max_depth"]
    print("Algorithm is:", algorithm)
    print("Max depth for IDDFS is:", iddfs_max_depth)
    print()


    if algorithm == "bfs":
        start = time.time()
        aux = Bfs(sokoban)
        sol = aux.start
        print(time.time() - start)

    elif algorithm == "dfs":
        start = time.time()
        aux = Dfs(sokoban)
        sol = aux.start()
        print(time.time() - start)

    # elif algorithm == "iddfs":
    #     sol = iddfs(game, initial_node, iddfs_depth_limit)
    
    else:
        print("Invalid algorithm.")
        exit()


if __name__ == "__main__":
    main()


