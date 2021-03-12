from Node import Node
from game import Constants
from game.Sokoban import Sokoban
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
            print("hello")
            node = self.queue.popleft()
            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

            if not node.sokoban.isDeadEnd():
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    self.queue.append(goingUpNode)
                    goingUpNode.appendParent(node)
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    self.queue.append(goingDownNode)
                    goingDownNode.appendParent(node)
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and  self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    self.queue.append(goingLeftNode)
                    goingLeftNode.appendParent(node)
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    self.queue.append(goingRightNode)
                    goingRightNode.appendParent(node)

                self.explored.append(node) #already explored
            node.sokoban.printBoard(mode='debug')

        if node.sokoban.isGameFinished():
            node.printPathToNode()

    def _not_explored_board(self, node):
        for exp in self.explored:
            # Nodo != Estado
            # Solo va a ser igual si el tablero es igual y el depth es mayor o igual al otro nodo
            if exp.redundant_equal(node) and node.depth >= exp.depth:
                return False
        return True



