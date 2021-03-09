from TP1.Node import Node
from TP1.game import Constants

class Bfs:
    id = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard):
        self.explored = []
        self.root = Node(rootBoard)
        self.queue = []
        self.queue.append()

    #
    # def start(self):
    #     while len(self.queue) > 0:


