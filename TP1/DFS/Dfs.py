from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque


class Dfs:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]

    def __init__(self, rootBoard):
        self.explored = set()
        node = Node(rootBoard, self.depth)
        self.root = node
        self.stack = []
        self.stack.append(node)

    def start(self):
        node = {}
        while len(self.stack) > 0 and (node == {} or not node.sokoban.isGameFinished()):
            node = self.stack.pop()
            self.explored.add(node) #already explored

            goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
            goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

            if not node.sokoban.isDeadEnd():
                if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode)):
                    node.appendChild(goingUpNode)
                    self.stack.append(goingUpNode)
                if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode)):
                    node.appendChild(goingDownNode)
                    self.stack.append(goingDownNode)
                if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and self._not_explored_board(goingLeftNode)):
                    node.appendChild(goingLeftNode)
                    self.stack.append(goingLeftNode)
                if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode)):
                    node.appendChild(goingRightNode)
                    self.stack.append(goingRightNode)
            
                node.sokoban.printBoard()

        # node.sokoban.printBoard()
        self.root.sokoban.printBoard()
        print(node.sokoban.isGameFinished())


    def _not_explored_board(self, node):
        for exp in self.explored:
            if exp.redundant_equal(node):
                return False
        return True






# from collections import deque


# def dfs(graph, root):
    
#     visited = set()
#     stack = deque()
#     stack.append(root)


#     while stack:
#         current = stack.popleft()
#         print(current)

#         visited.add(current)
#         neighbours = graph[current]
#         for neighbour in neighbours:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 stack.append(neighbour)

        # if GANO
        #     return EL PATH QUE HIZO PARA GANAR Y PRINTEARLO

        # posible_moves = board.get_moves(current)

        # for move in posible_moves:
        #     stack.append(move)
        #     visited.add(move)

# graph = {9: [7, 3],
#          7: [5, 1],
#          5: [],
#          1: [],
#          3: [2, 4],
#          2: [],
#          4: []}

# dfs(graph, 9)
