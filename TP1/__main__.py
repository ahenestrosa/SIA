from game.Sokoban import Sokoban
from game import Constants
from NotInformed.Bfs import Bfs
from NotInformed.Dfs import Dfs
from NotInformed.Iddfs import Iddfs
from Informed.Greedy import Greedy
from Informed.AStar import AStar
from Informed.IdaIt import Ida
from Informed.IdaRec import IdaRec
from heuristics.heuristics import Heuristics
from collections import deque
from Node import Node
import sys
import time
import json


def main():
    sys.setrecursionlimit(15000)
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


    with open("maps/" + level_map +".txt") as map_file:
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

    heuristic_name = ""
    heuristic_function = None
    if heuristic == 1:
        heuristic_name = "boxObjDistance"
        heuristic_function = Heuristics.boxObjDistance
    elif heuristic == 2:
        heuristic_name = "playerBoxDistance"
        heuristic_function = Heuristics.playerBoxDistance
    elif heuristic == 3:
        heuristic_name = "playerBoxObjDistance"
        heuristic_function = Heuristics.playerBoxObjDistance
    elif heuristic == 4:
        heuristic_name = "boxObjEucDistance"
        heuristic_function = Heuristics.boxObjEucDistance
    elif heuristic == 5:
        heuristic_name = "minObjDistance"
        heuristic_function = Heuristics.minObjDistance

    
    toPrint = "//////////////////// SOKOBAN SUMMARY /////////////////////////////////"
    toPrint += "\n\n"
    toPrint += "MAP:             " + level_map + "\n" 
    toPrint += "Algorithm is:    " + algorithm + "\n"
    if heuristic_name != "":
        toPrint += "Heuristic is:    " + heuristic_name + "\n"
    toPrint += "Max Iddfs depth: " +  str(iddfs_max_depth)+ "\n\n"


    start_time = time.time()
    if algorithm == "bfs":
        aux = Bfs(sokoban)
        res = aux.start()
    elif algorithm == "dfs":
        aux = Dfs(sokoban)
        res = aux.start()
    elif algorithm == "iddfs":
        aux = Iddfs(sokoban, iddfs_max_depth)
        res = aux.start()
    elif algorithm == "greedy":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        aux = Greedy(sokoban, heuristic_function)
        res = aux.start()
    elif algorithm == "a*":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        aux = AStar(sokoban, heuristic_function)
        res = aux.start()
    elif algorithm == "ida":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        aux = Ida(sokoban, heuristic_function)
        res = aux.start()
    elif algorithm == "idaRec":
        if heuristic_function == None:
            print("Missing heuristic")
            exit(1)
        aux = IdaRec(sokoban, heuristic_function)
        res = aux.start()
    else:
        print("Invalid algorithm.")
        exit()
    end_time = time.time()


    # Printing results
    if res.result == True:
        message = "SUCCESS"
    else:
        message = "FAILURE"

    toPrint += "---------------------------- Results ------------------------------\n"
    toPrint += "Result:            " + message +"\n"
    toPrint += "Depth of solution: " + str(res.depthSolution) +"\n"
    toPrint += "Cost of solution:  " +  str(res.costSolution) +"\n"
    toPrint += "Expanded Nodes:    " + str(res.expandedNodes) +"\n"
    toPrint += "Frontier Nodes:    " + str(res.frontierNodes) +"\n"
    toPrint += "Time employed [s]: " + str(round(end_time - start_time, 4)) +"\n"

    print(toPrint)

    if res.result:
        toPrint += "\n\n------------------------------ Solution ---------------------------"
        for n in res.solutionNodePath:
            toPrint += n.sokoban.printBoard(mode='debug')
            


    f = open("./results/" + level_map + "-" + algorithm + "-" +heuristic_name+ ".txt", "a")
    f.truncate(0)
    f.write(toPrint)
    f.close()



if __name__ == "__main__":
    main()


