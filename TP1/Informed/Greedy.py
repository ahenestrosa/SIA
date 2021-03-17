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
        self.explored = {}
        node = Node(rootBoard, self.depth)
        self.root = node
        # Frontier its a priority queue based on the heuristic
        self.frontier = []
        self.heuristic = heuristic
        heapq.heappush(self.frontier, (0, self.root))
        self.expandedNodes = 0


    def start(self):
        node = None
        while len(self.frontier) > 0 and (node == None or not node.sokoban.isGameFinished()):
            node = heapq.heappop(self.frontier)[1]
            self.expandedNodes += 1

            if not node.sokoban.gameIsDeadEnd:
                goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    # Inserting the node in the priority queue based on the heuristic(indicates priority)
                    heapq.heappush(self.frontier, (self.heuristic(goingUpNode), goingUpNode))
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    heapq.heappush(self.frontier, (self.heuristic(goingDownNode), goingDownNode))
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    heapq.heappush(self.frontier, (self.heuristic(goingLeftNode), goingLeftNode))
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    heapq.heappush(self.frontier, (self.heuristic(goingRightNode), goingRightNode))
            #node.sokoban.printBoard(mode='debug')

        
        success = node.sokoban.isGameFinished()
        solution = []
        if success:
            solution = node.buildPathToRoot()
        return Results(success, len(solution), len(solution), self.expandedNodes, len(self.frontier), solution)

    def _not_explored_board(self, node):
        if node not in self.explored:
            self.explored[node] = 1
            return True
        return False



