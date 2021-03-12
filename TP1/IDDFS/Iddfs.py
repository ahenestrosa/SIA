from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque


class Iddfs:
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]

    def __init__(self, rootBoard, iddfsMaxDepth):
        self.depth = 0
        self.root = Node(rootBoard, self.depth)
        self.iddfsMaxDepth = iddfsMaxDepth

    def start(self):
        maxDepth = 0
        result = False
        for maxDepth in range(0, self.iddfsMaxDepth):
            result = self.startDls(maxDepth)
            if result == True:
                break
        print(maxDepth)
        print(result)

    def startDls(self, maxDepth):
        stack = []
        stack.append(self.root)
        explored = set()
        node = {}
        while len(stack) > 0 and (node == {} or not node.sokoban.isGameFinished()):
            node = stack.pop()
            explored.add(node)

            # Only go deeper if we haven't gone past max depth
            if node.depth < maxDepth:
                goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

                if not node.sokoban.isDeadEnd():
                    if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode, explored)):
                        node.appendChild(goingUpNode)
                        stack.append(goingUpNode)
                    if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode, explored)):
                        node.appendChild(goingDownNode)
                        stack.append(goingDownNode)
                    if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and self._not_explored_board(goingLeftNode, explored)):
                        node.appendChild(goingLeftNode)
                        stack.append(goingLeftNode)
                    if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode, explored)):
                        node.appendChild(goingRightNode)
                        stack.append(goingRightNode)
                
                
            node.sokoban.printBoard()

        return node.sokoban.isGameFinished()


    def _not_explored_board(self, node, explored):
        for exp in explored:
            if exp.redundant_equal(node):
                return False
        return True


