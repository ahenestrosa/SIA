from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import time

class Bfs:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard):
        self.explored = {}
        node = Node(rootBoard, self.depth)
        self.root = node
        self.queue = deque()
        self.queue.append(node)

    def start(self):
        node = None
        
        while len(self.queue) > 0 and (node == None or not node.sokoban.isGameFinished()):
            node = self.queue.popleft()
            sokoban = node.sokoban
            goingUpNode = Node(Sokoban.from_game(sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(sokoban), node.depth + 1, node)

            if not sokoban.gameIsDeadEnd:
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    goingUpNode.appendParent(node)
                    self.queue.append(goingUpNode)
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    goingDownNode.appendParent(node)
                    self.queue.append(goingDownNode)
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    goingLeftNode.appendParent(node)
                    self.queue.append(goingLeftNode)
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    goingRightNode.appendParent(node)
                    self.queue.append(goingRightNode)
            
            # node.sokoban.printBoard(mode='debug')

        success = node.sokoban.isGameFinished()
        solution = []
        if success:
            solution = node.buildPathToRoot()
        return Results(success, len(solution), len(solution), len(self.explored), len(self.queue), solution)


    def _not_explored_board(self, node):
        if node not in self.explored:
            self.explored[node] = 1
            return True
        return False



