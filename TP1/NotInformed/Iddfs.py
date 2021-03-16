from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results


class Iddfs:
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    lastFrontier = 0
    lastExplored = 0

    def __init__(self, rootBoard, iddfsMaxDepth):
        self.depth = 0
        self.root = Node(rootBoard, self.depth)
        self.iddfsMaxDepth = iddfsMaxDepth

    def start(self):
        result = False
        # Usamos bisection search
        maxDepthFloor = 0
        maxDepthTop = self.iddfsMaxDepth
        while maxDepthFloor < maxDepthTop:
            maxDepth = int((maxDepthTop - maxDepthFloor)/2 + maxDepthFloor)
            print(maxDepth)
            result = self.startDls(maxDepth)
            # Si encontramos la solucion, puede haber una mas optima, me quedo con menos profundidad
            if result[0] == True:
                maxDepthTop = maxDepth
            # Si no encontramos la solucion, necesito mas profundidad
            else:
                maxDepthFloor = maxDepth

        success = result[0]
        solution = []
        if success:
            solution = result[1].buildPathToRoot()
        return Results(success, len(solution), len(solution), self.lastExplored, self.lastFrontier, solution)

                

    def startDls(self, maxDepth):
        stack = []
        stack.append(self.root)
        explored = {}
        node = None
        while len(stack) > 0 and (node == None or not node.sokoban.isGameFinished()):
            node = stack.pop()

            # Only go deeper if we haven't gone past max depth
            if node.depth < maxDepth:
                goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)

                if not node.sokoban.gameIsDeadEnd:
                    if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode, explored)):
                        node.appendChild(goingUpNode)
                        goingUpNode.appendParent(node)
                        stack.append(goingUpNode)
                    if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode, explored)):
                        node.appendChild(goingDownNode)
                        goingDownNode.appendParent(node)
                        stack.append(goingDownNode)
                    if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and self._not_explored_board(goingLeftNode, explored)):
                        node.appendChild(goingLeftNode)
                        goingLeftNode.appendParent(node)
                        stack.append(goingLeftNode)
                    if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode, explored)):
                        node.appendChild(goingRightNode)
                        goingRightNode.appendParent(node)
                        stack.append(goingRightNode)
                
                
            #node.sokoban.printBoard(mode='debug')


        self.lastFrontier = len(stack)
        self.lastExplored = len(explored)

        return (node.sokoban.isGameFinished(), node)


    def _not_explored_board(self, node, explored):
        # Nodo != Estado
        # Solo va a ser igual si el tablero es igual y el depth es menor o igual al otro nodo
        # El diccionario usa un hash basado en la posicion del jugador y de las cajas
        if node in explored:
            depth_of_explored_node = explored[node]
            if node.depth >= depth_of_explored_node:
                return False
        explored[node] = node.depth
        return True

