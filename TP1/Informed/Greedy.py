from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import heapq 

class Greedy:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard, heuristic):
        self.explored = []
        node = Node(rootBoard, self.depth)
        self.root = node
        # Frontier its a priority queue based on the heuristic
        self.frontier = []
        heapq.heappush(self.frontier, (0, self.root))
        self.heuristic = heuristic


    def start(self):
        node = {}
        while len(self.frontier) > 0 and (node == {} or not node.sokoban.isGameFinished()):
            node = heapq.heappop(self.frontier)[1]
            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

            if not node.sokoban.isDeadEnd():
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    goingUpNode.appendParent(node)
                    # Inserting the node in the priority queue based on the heuristic(indicates priority)
                    heapq.heappush(self.frontier, (self.heuristic(goingUpNode), goingUpNode))
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    goingDownNode.appendParent(node)
                    heapq.heappush(self.frontier, (self.heuristic(goingDownNode), goingDownNode))
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    goingLeftNode.appendParent(node)
                    heapq.heappush(self.frontier, (self.heuristic(goingLeftNode), goingLeftNode))
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    goingRightNode.appendParent(node)
                    heapq.heappush(self.frontier, (self.heuristic(goingRightNode), goingRightNode))

                self.explored.append(node) #already explored
            #node.sokoban.printBoard(mode='debug')

        
        success = node.sokoban.isGameFinished()
        solution = []
        if success:
            solution = node.buildPathToRoot()
        return Results(success, len(solution), len(solution), len(self.explored), len(self.frontier), solution)

    def _not_explored_board(self, node):
        for exp in self.explored:
            # Nodo != Estado
            # Solo va a ser igual si el tablero es igual y el depth es mayor o igual al otro nodo
            if exp.redundant_equal(node) and node.depth >= exp.depth:
                return False
        return True



