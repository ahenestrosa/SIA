from game.Sokoban import Sokoban
from game import Constants
from BFS.Bfs import Bfs
from DFS.Dfs import Dfs
from collections import deque
import time

# objective = [(0,0), (2,2)]
# dimensions = (5,5)
# boxes = [(0,1), (1, 2)]
# walls = [(3,3), (4,4)]
# player = (0, 2)
# sokoban = Sokoban(walls, objective, dimensions, player, boxes)


objective = [(2,1),(3,1)]
dimensions = (6,6)
boxes = [(2,3), (3,3)]
walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),
          (1,0),(2,0),(3,0),(4,0),(5,0),
          (5,1),(5,2),(5,3),(5,4),
          (1,5),(2,5),(3,5), (4,5)]
player = (1, 4)
sokoban = Sokoban(walls, objective, dimensions, player, boxes)


# board.printBoard()
# board.move(Constants.UP)
# board.printBoard()
# board.move(Constants.DOWN)
# board.move(Constants.RIGHT)
# board.printBoard()
# print(board.isGameFinished())
# newBoard = Board.from_game(board)
# newBoard.move(Constants.RIGHT)
# newBoard.printBoard()
#
# board.printBoard()
# print(newBoard.redundant_equal(board))
# print(sokoban.move(Constants.UP))
start = time.time()
algorithm = Bfs(sokoban)
algorithm.start()
end = time.time()

print(end - start)

