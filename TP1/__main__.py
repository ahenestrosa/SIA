from game.Sokoban import Sokoban
from game import Constants
from NotInformed.Bfs import Bfs
from NotInformed.Dfs import Dfs
from NotInformed.Iddfs import Iddfs
from Informed.Greedy import Greedy
from Informed.AStar import AStar
from heuristics.heuristics import Heuristics
from game.Maps import Maps
from collections import deque
import time
import json


def main():
    

    with open('TP1/config.json') as config:
        data = json.load(config)

    algorithm = data['algorithm']
    level_map = data['level_map']
    heuristic = data['heuristic']
    iddfs_max_depth = data["iddfs_max_depth"]
    print("Algorithm is:", algorithm)

    with open('TP1/maps/map3.txt') as map_file:
        lines = map_file.readlines()

    height = len(lines)
    width = len(lines[0]) - 1

    walls = []
    objectives = []
    player = ()
    boxes = []
    dimensions = (height,width)

    for i,line in enumerate(lines):
        for j, symbol in enumerate(line[:-1]): 
            if symbol == '#':
                walls.append((i,j))
            elif symbol == 'O':
                objectives.append((i,j))
            elif symbol == 'P':
                player = (i,j)
            elif symbol == 'B':
                boxes.append((i,j))

    sokoban = Sokoban(walls, objectives, dimensions, player, boxes)
    # sokoban.printBoard(mode="vis")

    # map_levels = [Maps.map1, Maps.map2, Maps.map3]
    # sokoban = None
    # if level_map in ["1", "2", "3"]:
    #     sokoban = map_levels[int(level_map)-1]()
    # else:
    #     print("Invalid Map")
    #     exit(1)
        
#    sokoban.printBoard(mode="vis")

    heuristic_function = None
    if heuristic == "boxObjDistance":
        heuristic_function = Heuristics.boxObjDistance
    elif heuristic == "playerObjDistane":
        heuristic_function = Heuristics.playerObjDistance
    elif heuristic == "playerBoxObjDistance":
        heuristic_function = Heuristics.playerBoxObjDistance

    start_time = time.time()
    if algorithm == "bfs":
        aux = Bfs(sokoban)
        res = aux.start()
    elif algorithm == "dfs":
        aux = Dfs(sokoban)
        res = aux.start()
    elif algorithm == "iddfs":
        print("Max depth for IDDFS is:", iddfs_max_depth)
        aux = Iddfs(sokoban, iddfs_max_depth)
        res = aux.start()
    elif algorithm == "greedy":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        print("Heuristic is: ", heuristic)
        aux = Greedy(sokoban, heuristic_function)
        res = aux.start()
    elif algorithm == "a*":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        print("Heuristic is: ", heuristic)
        aux = AStar(sokoban, heuristic_function)
        res = aux.start()
    else:
        print("Invalid algorithm.")
        exit()

    end_time = time.time()

    print("Result: ", res.result)
    print("Depth of solution: ", res.depthSolution)
    print("Cost of solution: ", res.costSolution)
    print("Expanded Nodes: ", res.expandedNodes)
    print("Frontier Nodes: ", res.frontierNodes)
    print("Time employed: ",  round(end_time - start_time, 4) )

    if res.result:
        for n in res.solutionNodePath:
            n.sokoban.printBoard(mode='vis')




if __name__ == "__main__":
    main()


