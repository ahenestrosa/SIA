from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import heapq 

class AStar:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard, heuristic):
        self.explored = {}
        node = Node(rootBoard, self.depth)
        self.root = node
        # Frontier its a priority queue based on the f(n) = h(n) + g(n). Or h(n) when f(n) = f(n) 
        self.frontier = []
        heapq.heappush(self.frontier, (self.heuristic(self.root),self.heuristic(self.root), self.root))
        self.heuristic = heuristic
        self.limit = self.heuristic(self.root)


    def start(self):
        node = None
        while len(self.frontier) > 0 and (node == None or not node.sokoban.isGameFinished()):
            node = heapq.heappop(self.frontier)[2]
            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

            if not node.sokoban.gameIsDeadEnd:
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    goingUpNode.appendParent(node)
                    h = self.heuristic(goingUpNode)
                    heapq.heappush(self.frontier, (h+ node.depth, h , goingUpNode))
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    goingDownNode.appendParent(node)
                    h = self.heuristic(goingDownNode)                   
                    heapq.heappush(self.frontier, (h+ node.depth, h , goingDownNode))
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    goingLeftNode.appendParent(node)
                    h = self.heuristic(goingLeftNode)
                    heapq.heappush(self.frontier, (h+ node.depth, h , goingLeftNode))
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    goingRightNode.appendParent(node)
                    h = self.heuristic(goingRightNode)
                    heapq.heappush(self.frontier, (h+ node.depth, h , goingRightNode))

            # node.sokoban.printBoard(mode='debug')

        
        success = node.sokoban.isGameFinished()
        solution = []
        if success:
            solution = node.buildPathToRoot()
        return Results(success, len(solution), len(solution), len(self.explored), len(self.frontier), solution)

    def _not_explored_board(self, node):
        if node not in self.explored:
            self.explored[node] = 1
            return True
        return False


