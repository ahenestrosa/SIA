from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import heapq 

class Ida:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard, heuristic):
        # explored = path for Ida
        node = Node(rootBoard, self.depth)
        self.root = node
        self.heuristic = heuristic
        self.limit = self.heuristic(self.root)
        self.solutionNode = None
        self.expandedNodes = 0
        self.frontierNodes = 0


    def start(self):
        limit = self.heuristic(self.root) + self.root.depth
        result = False
        while limit < 10000:
            print(limit)
            limit = self.startDls(limit)
            if self.solutionNode != None:
                result = True
                break
            if limit == float("inf"):
                break
        
        solution = []
        if result:
            solution = self.solutionNode.buildPathToRoot()
        return Results(result, len(solution), len(solution), self.expandedNodes, self.frontierNodes, solution)

    def startDls(self, limit):
        node = None
        stack = []
        stack.append(self.root)
        explored = {}
        minFValue = float("inf")
        while len(stack) > 0:
            self.expandedNodes += 1
            node = stack.pop()
            fValue = self.heuristic(node) + node.depth

            if node.sokoban.isGameFinished():
                self.solutionNode = node
                self.frontierNodes = len(stack)
                return fValue

            if node.sokoban.gameIsDeadEnd:
                continue 

            if fValue > limit:
                if fValue < minFValue:
                    minFValue = fValue
                continue

            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)


            if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode, explored)):
                stack.append(goingUpNode)
            if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode, explored)):
                stack.append(goingDownNode)               
            if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode, explored)):
                stack.append(goingLeftNode)
            if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode, explored)):
                stack.append(goingRightNode)

            # node.sokoban.printBoard(mode='debug')
        
        self.frontierNodes = len(stack)
        return minFValue
    


    def _not_explored_board(self, node, explored):
        # Nodo != Estado
        # Solo va a ser igual si el tablero es igual y el depth es menor o igual al otro nodo
        # El diccionario usa un hash basado en la posicion del jugador y de las cajas
        if node in explored:
            depth_of_explored_node = explored[node]
            if node.depth >= depth_of_explored_node:
                return False
        explored[node] = node.depth
        return True


