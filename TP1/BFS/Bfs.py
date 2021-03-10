from TP1.Node import Node
from TP1.game import Constants
from TP1.game.Sokoban import Sokoban
from collections import deque

class Bfs:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard):
        self.explored = []
        node = Node(rootBoard, self.depth)
        self.root = node
        self.queue = deque()
        self.queue.append(node)

    def start(self):
        node = {}
        while len(self.queue) > 0 and (node == {} or not node.sokoban.isGameFinished()):
            node = self.queue.popleft()
            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

            if not node.sokoban.isDeadEnd():
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    self.queue.append(goingUpNode)
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    self.queue.append(goingDownNode)
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    self.queue.append(goingLeftNode)
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    self.queue.append(goingRightNode)

                self.explored.append(node) #already explored
        node.sokoban.printBoard();
        self.root.sokoban.printBoard()

    def _not_explored_board(self, node):
        for exp in self.explored:
            if exp.redundant_equal(node) and node.depth > exp.depth:
                return False
        return True




