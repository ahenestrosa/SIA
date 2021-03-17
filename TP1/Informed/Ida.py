from Node import Node
from game import Constants
from game.Sokoban import Sokoban
from collections import deque
from Results import Results
import heapq 


class Ida:
    depth = 0
    movements = [Constants.UP, Constants.DOWN,Constants.LEFT, Constants.RIGHT]
    def __init__(self, rootBoard, heuristic):
        node = Node(rootBoard, self.depth)
        self.explored = []
        self.root = node
        self.root.setHeuristic(heuristic(self.root))
        self.candidates = []
        # Frontier its a priority queue based on the f(n) = h(n) + g(n). Or h(n) when f(n) = f(n)
        self.frontier = []
        self.heuristic = heuristic
        self.limit = self.heuristic(self.root)
        
    def start(self):
        node = None
        solved = False
        while self.limit < 15000 and not solved:
            self.frontier = []
            self.candidates = []
            heapq.heappush(self.frontier, self.root)
            while len(self.frontier) > 0 and (node == None or not node.sokoban.isGameFinished()):
                # print(self.limit)
                # print('length ' + str(len(self.frontier)))
                node = heapq.heappop(self.frontier)
                node.sokoban.printBoard(mode='vis')
                if node.heuristic + node.depth > self.limit:
                    self.candidates.append(node.heuristic + node.depth)
                elif node.sokoban.isGameFinished():
                    solution = node.buildPathToRoot()
                    return Results(success, len(solution), len(solution), len(self.explored), len(self.frontier), solution)
                else:
                    if len(node.children) > 0:
                        newNodes = node.children
                    else:
                        self._appendNewMovements(node)
                        # heapq.heappush(self.frontier, (n.heuristic + n.depth, n.heuristic, n))
                    for n in node.children:
                        if n not in self.frontier:
                            heapq.heappush(self.frontier, n)
            self.limit = min(self.candidates)

                
                
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    def _appendNewMovements(self, node):
        print(node.depth + 1)
        goingUpNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingDownNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingLeftNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        goingRightNode = Node(Sokoban.from_game(node.sokoban), node.depth + 1, node)
        
        
        if not node.sokoban.gameIsDeadEnd and len(node.children) == 0:
            if (goingUpNode.sokoban.move(Constants.UP) == Constants.VALID_MOVE):
                goingUpNode.appendParent(node)
                goingUpNode.setHeuristic(self.heuristic(goingUpNode))
                node.appendChild(goingUpNode)
            if (goingDownNode.sokoban.move(Constants.DOWN) == Constants.VALID_MOVE):
                goingDownNode.appendParent(node)
                goingDownNode.setHeuristic(self.heuristic(goingDownNode))
                node.appendChild(goingDownNode)

            if (goingLeftNode.sokoban.move(Constants.LEFT) == Constants.VALID_MOVE):
                goingLeftNode.appendParent(node)
                goingLeftNode.setHeuristic(self.heuristic(goingLeftNode))
                node.appendChild(goingLeftNode)
            if (goingRightNode.sokoban.move(Constants.RIGHT) == Constants.VALID_MOVE):
                goingRightNode.appendParent(node)
                goingRightNode.setHeuristic(self.heuristic(goingRightNode))
                node.appendChild(goingRightNode)