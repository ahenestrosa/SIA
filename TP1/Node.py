from collections import deque

class Node:
    sokoban = {}
    depth = 0
    heuristic = 0
    def __init__(self, sokoban,depth, parent = None):
        self.sokoban = sokoban
        self.depth = depth
        self.parent = parent

    def __eq__(self, other):
        if other == None:
            return False
        return self.sokoban == other.sokoban
    
    def __hash__(self):
        return hash(self.sokoban)
    
    # Definir la precendencia
    def __lt__(self, other):
        if not other.depth + other.heuristic == self.depth + self.heuristic:
            return self.depth + self.heuristic < other.depth + self.heuristic
        else:
            return self.heuristic < other.heuristic

    def appendParent(self, parent):
        self.parent = parent

    def redundant_equal(self, other):
        return self.sokoban.redundant_equal(other.sokoban)

    def getHeuristic(self, heuristic):
        #TODO: Agregar heuristica
        return 1
    
    def setHeuristic(self, heuristic):
        self.heuristic = heuristic
    
    def buildPathToRoot(self):
        nodeList = deque()
        currNode = self
        while currNode != None:
            nodeList.appendleft(currNode)
            currNode = currNode.parent
        return nodeList