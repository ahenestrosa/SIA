from collections import deque

class Node:
    sokoban = {}
    depth = 0
    children = []
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
        return self.depth < other.depth

    def appendChildren(self, children):
        for child in children:
            self.children.append(child)

    def appendChild(self, child):
        self.children.append(child)

    def appendParent(self, parent):
        self.parent = parent

    def redundant_equal(self, other):
        return self.sokoban.redundant_equal(other.sokoban)

    def getHeuristic(self, heuristic):
        #TODO: Agregar heuristica
        return 1
    
    

    #TODO: Despues moverlo a un lugar mas apropiado
    def buildPathToRoot(self):
        nodeList = deque()
        currNode = self
        while currNode != None:
            nodeList.appendleft(currNode)
            currNode = currNode.parent
        return nodeList