from game.Sokoban import Sokoban
from game import Constants
from NotInformed.Bfs import Bfs
from NotInformed.Dfs import Dfs
from NotInformed.Iddfs import Iddfs
from Informed.Greedy import Greedy
from Informed.AStar import AStar
from Informed.Idaugusto import Ida
from heuristics.heuristics import Heuristics
from collections import deque
from Node import Node
import time
import json


def main():
    

    with open('config.json') as config:
        data = json.load(config)

    algorithm = data['algorithm']
    level_map = data['level_map']
    heuristic = data['heuristic']
    iddfs_max_depth = data["iddfs_max_depth"]
    visual = data["visual"]

    if iddfs_max_depth <= 0:
            print("iddfs_max_depth must be positive")
            exit(1)

    print("Algorithm is:", algorithm)

    with open('maps/map1.txt') as map_file:
        lines = map_file.readlines()

    height = len(lines)
    width = len(lines[0]) - 1

    walls = []
    objectives = []
    player = ()
    boxes = []
    dimensions = (height, width)

    for i,line in enumerate(lines):
        for j, symbol in enumerate(line[:-1]): 
            if symbol == '#':
                walls.append((j,height - i - 1))
            elif symbol == 'O':
                objectives.append((j, height - i - 1))
            elif symbol == 'P':
                player = (j,height - i - 1)
            elif symbol == 'B':
                boxes.append((j,height - i - 1))

    sokoban = Sokoban(walls, objectives, dimensions, player, boxes)
    # sokoban.printBoard(mode="vis")


    heuristic_function = None
    if heuristic == "boxObjDistance":
        heuristic_function = Heuristics.boxObjDistance
    elif heuristic == "playerBoxDistance":
        heuristic_function = Heuristics.playerBoxDistance
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
    elif algorithm == "ida":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        print("Heuristic is: ", heuristic)
        aux = Ida(sokoban, heuristic_function)
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
    print("Time employed [s]: ",  round(end_time - start_time, 4) )

    if visual :
        if res.result:
            for n in res.solutionNodePath:
                n.sokoban.printBoard(mode='vis')




if __name__ == "__main__":
    main()


