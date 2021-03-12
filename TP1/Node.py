from collections import deque

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

    def appendParent(self, parent):
        self.parent = parent

    def redundant_equal(self, other):
        return self.sokoban.redundant_equal(other.sokoban)
    
    #TODO: Despues moverlo a un lugar mas apropiado
    def printPathToNode(self):
        nodeList = deque()
        currNode = self
        while currNode != None:
            nodeList.appendleft(currNode)
            currNode = currNode.parent
        for n in nodeList:
            n.sokoban.printBoard(mode='vis') 