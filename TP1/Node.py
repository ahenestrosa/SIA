class Node:
    def __init__(self, board,depth, node= None):
        self.board = board
        self.depth = depth
        self.children = node

    def appendChildren(self, children):
        for child in children:
            self.children.append(child)