# from Node import Node
# from game import Constants.py
# from game.Sokoban import Sokoban
# from collections import deque


# class Dfs:
#     depth = 0
#     movements = [Constants.py.UP, Constants.py.DOWN,Constants.py.LEFT, Constants.py.RIGHT]

#     def __init__(self, rootBoard):
#         self.explored = []
#         self.root = Node(rootBoard, self.depth)
#         self.queue = deque()
#         self.queue.append(rootBoard.board)

#     def start(self):
#         while len(self.queue) > 0:
#             node = self.queue.popleft()
            
#             node.board.printBoard()
#             self.explored.append(node) #already explored


#             goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
#             goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
#             goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
#             goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

#             #si el juego no termino me fijo cuales son los movimientos validos y los agrego al arbol
#             if node.sokoban.isGameFinished() == False:
#                 if(goingUpNode.sokoban.move(Constants.py.UP) == Constants.py.VALID_MOVE and self._not_explored_board(goingUpNode) == True):
#                     node.appendChild(goingUpNode)
#                     self.queue.append(goingUpNode)
#                 if(goingDownNode.sokoban.move(Constants.py.DOWN) == Constants.py.VALID_MOVE and self._not_explored_board(goingDownNode) == True):
#                     node.appendChild(goingDownNode)
#                     self.queue.append(goingDownNode)
#                 if(goingLeftNode.sokoban.move(Constants.py.LEFT) == Constants.py.VALID_MOVE and self._not_explored_board(goingLeftNode) == True):
#                     node.appendChild(goingLeftNode)
#                     self.queue.append(goingLeftNode)
#                 if(goingRightNode.sokoban.move(Constants.py.RIGHT) == Constants.py.VALID_MOVE and self._not_explored_board(goingRightNode) == True):
#                     node.appendChild(goingRightNode)
#                     self.queue.append(goingRightNode)

#             else:
#                 #game finishes
#                 print('game finished')

#     def _not_explored_board(self, node):
#         for exp in self.explored:
#             if exp.redundant_equal(node):
#                 return False
#         return True






from collections import deque


def dfs(graph, root):
    
    visited = set()
    in_order = []
    stack = []
    stack.append(root)

    while stack:
        print(stack)
        current = stack.pop()
        in_order.append(current)
        print(current)

        visited.add(current)
        neighbours = graph[current]
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
                

        # if GANO
        #     return EL PATH QUE HIZO PARA GANAR Y PRINTEARLO

        # posible_moves = board.get_moves(current)

        # for move in posible_moves:
        #     stack.append(move)
        #     visited.add(move)
    print(in_order)

graph = {
        9: [7, 3, 10 , 11 , 12 , 13],
        7: [5, 1, 88],
        5: [99],
        1: [76],
        88:[77],
        3: [2, 4],
        2: [],
        4: [66],
        10:[44],
        11:[],
        12:[],
        13:[],
        99:[],
        77:[],
        44:[],
        76:[],
        66:[]}

dfs(graph, 9)
