from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import gc


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
        successFrontier = 0
        successExplored = 0
        successResult = None
        while maxDepthFloor <= maxDepthTop:
            maxDepth = (maxDepthTop + maxDepthFloor)//2
            print(maxDepth)
            result = self.startDls(maxDepth)
            # Si encontramos la solucion, puede haber una mas optima, me quedo con menos profundidad
            if result[0] == True:
                successResult = result[1]
                successFrontier = self.lastFrontier
                successExplored = self.lastExplored
                maxDepthTop = maxDepth-1
            # Si no encontramos la solucion, necesito mas profundidad
            else:
                maxDepthFloor = maxDepth+1

        # Nos quedamos con el ultimo exito
        solution = []
        success = False
        if successResult != None:
            solution = successResult.buildPathToRoot()
            success = True

        return Results(success, len(solution), len(solution), successExplored, successFrontier, solution)

                

    def startDls(self, maxDepth):
        stack = []
        stack.append(self.root)
        explored = {}
        node = None
        while len(stack) > 0 and (node == None or not node.sokoban.isGameFinished()):
            node = stack.pop()

            # Only go deeper if we haven't gone past max depth
            if node.depth < maxDepth:
                if not node.sokoban.gameIsDeadEnd:
                    goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                    goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                    goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                    goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
                    if(goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE and self._not_explored_board(goingUpNode, explored)):
                        stack.append(goingUpNode)
                    if(goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE and self._not_explored_board(goingDownNode, explored)):
                        stack.append(goingDownNode)
                    if(goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE and self._not_explored_board(goingLeftNode, explored)):
                        stack.append(goingLeftNode)
                    if(goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE and self._not_explored_board(goingRightNode, explored)):
                        stack.append(goingRightNode)
                
            #node.sokoban.printBoard(mode='debug')


        self.lastFrontier = len(stack)
        self.lastExplored = len(explored)

        return (node.sokoban.isGameFinished(), node)

    
    # def _not_explored_board(self, node, explored):
    #     if node not in explored:
    #         explored[node] = 1
    #         return True
    #     return False


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

