class Node:
    sokoban = {}
    depth = 0
    children = []
    def __init__(self, sokoban,depth, parent = None):
        self.sokoban = sokoban
        self.depth = depth
        self.parent = parent


    def appendChildren(self, children):
        for child in children:
            self.children.append(child)

    def appendChild(self, child):
        self.children.append(child)

    def redundant_equal(self, other):
        return self.sokoban.redundant_equal(other.board)