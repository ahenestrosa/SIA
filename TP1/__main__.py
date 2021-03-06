from TP1.game.Board import Board
from TP1.game import Constants

objective = [(0,0), (1,1)]
dimensions = (5,5)
boxes = [(2,2), (1, 4)]
walls = [(3,3), (4,4)]
player = (0, 1)
board = Board(walls, objective, dimensions, player, boxes)
board.printBoard()
board.move(Constants.RIGHT)
board.move(Constants.RIGHT)
board.printBoard()
board.move(Constants.DOWN)
board.printBoard()
board.move(Constants.DOWN)
board.printBoard()
print(str(board.move(Constants.DOWN)))
board.move(Constants.LEFT)
board.move(Constants.LEFT)
board.move(Constants.DOWN)
board.printBoard()
print(str(board.move(Constants.LEFT)))
