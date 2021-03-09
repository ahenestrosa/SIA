from TP1.game.Sokoban import Sokoban
from TP1.game import Constants
from TP1.BFS.Bfs import Bfs
from collections import deque


objective = [(0,0), (2,2)]
dimensions = (5,5)
boxes = [(0,1), (1, 2)]
walls = [(3,3), (4,4)]
player = (0, 2)
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
algorithm = Bfs(sokoban)
algorithm.start()

