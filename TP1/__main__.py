from TP1.game.Board import Board
from TP1.game import Constants

objective = [(0,0), (2,2)]
dimensions = (5,5)
boxes = [(0,1), (1, 2)]
walls = [(3,3), (4,4)]
player = (0, 2)
board = Board(walls, objective, dimensions, player, boxes)
board.printBoard()
board.move(Constants.UP)
board.printBoard()
board.move(Constants.DOWN)
board.move(Constants.RIGHT)
board.printBoard()
print(board.isGameFinished())
