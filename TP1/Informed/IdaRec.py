from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import heapq


class IdaRec:
    depth = 0
    counter = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    solution = {}
    def __init__(self, rootBoard, heuristic):
        node = Node(rootBoard, self.depth)
        self.root = node
        self.root.setHeuristic(heuristic(self.root))
        self.heuristic = heuristic
        self.limit = self.heuristic(self.root)




    def start(self):

        threshold = self.root.heuristic

        while 1:
            path = set([self.root])
            distance = self.search_rec(self.root,threshold, 0, path)
            if distance == True:
                return Results(True, len(self.solution), len(self.solution), self.counter, 100, self.solution)
            elif distance == float("inf"):
                return Results(False, 0, 0, self.counter,100, [])
            else:
                threshold = distance


    def search_rec(self, node,threshhold ,g, path):
        self.counter = self.counter + 1
        f = g + node.heuristic

        if f > threshhold:
            return f

        if node.sokoban.isGameFinished():
            self.solution = node.buildPathToRoot()
            return True

        minimum = float("inf")

        # if len(node.children) == 0:
        goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

        if not node.sokoban.gameIsDeadEnd:
            if (goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE):
                goingUpNode.appendParent(node)
                goingUpNode.setHeuristic(self.heuristic(goingUpNode))
                node.appendChild(goingUpNode)
            if (goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE):
                goingDownNode.appendParent(node)
                goingDownNode.setHeuristic(self.heuristic(goingDownNode))
                node.appendChild(goingDownNode)

            if (goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE):
                goingLeftNode.appendParent(node)
                goingLeftNode.setHeuristic(self.heuristic(goingLeftNode))
                node.appendChild(goingLeftNode)
            if (goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE):
                goingRightNode.appendParent(node)
                goingRightNode.setHeuristic(self.heuristic(goingRightNode))
                node.appendChild(goingRightNode)
        for n in node.children:
            if n not in path:
                path.add(n)
                distance= self.search_rec(n, threshhold, g, path)
                if distance == True:
                    return True
                if distance < minimum:
                    minimum = distance
        return minimum


