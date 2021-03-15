from game import Constants
from matplotlib import pyplot as plt
from matplotlib import colors


class Sokoban():
    dimentions = ()
    board = {}
    player = ()
    objectives = []
    boxes = []
    gameIsDeadEnd = False

    def __init__(self, walls, objectives, dimentions, player, boxes):
        self.dimentions = dimentions
        self.player = player
        self.objectives = objectives
        self.boxes = boxes
        self.gameIsDeadEnd = False
        for i in range(dimentions[0]): #first we locate empty locations to squares
            for j in range(dimentions[1]):
                self.board[i, j] = Constants.EMPTY_LOC

        for wall in walls: #wall location
            self.board[wall[0], wall[1]] = Constants.WALLS_LOC

        for box in boxes: #box location
            self.board[box[0], box[1]] = Constants.BOXES_LOC

        if len(self.objectives) != len(self.boxes):
            print("Box number must equal objetive number")
            exit(1)

    @classmethod
    def from_game(cls, board):
        obj = cls.__new__(cls)
        auxBoard = board.board.copy()
        boxes = board.boxes.copy()
        objectives = board.objectives.copy()
        obj.dimentions = board.dimentions
        obj.board = auxBoard
        obj.player = board.player
        obj.boxes = boxes
        obj.objectives = objectives
        return obj

    def move(self, movement):
        newPlayerPosition = ()
        if(movement == Constants.UP):
            newPlayerPosition =  (self.player[0], self.player[1] - 1)
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if(self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition)
                    return Constants.VALID_MOVE
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE
            else:
                return Constants.INVALID_MOVE


        elif(movement == Constants.DOWN):
            newPlayerPosition = (self.player[0], self.player[1] + 1)
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition)
                    return Constants.VALID_MOVE
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE
            else:
                return Constants.INVALID_MOVE

        elif(movement == Constants.LEFT):
            newPlayerPosition = (self.player[0] - 1, self.player[1])
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition)
                    return Constants.VALID_MOVE
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE
            else:
                return Constants.INVALID_MOVE

        elif(movement == Constants.RIGHT):
            newPlayerPosition = (self.player[0] + 1, self.player[1])
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition)
                    return Constants.VALID_MOVE
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE
            else:
                return Constants.INVALID_MOVE


    def _locatePlayer(self, newPosition):
        self.board[newPosition] = Constants.EMPTY_LOC
        self.player = newPosition

    def _moveBox(self, movement, position):
        index = 0
        #to know which box we have to move
        for box in self.boxes:
            if box [0]==position[0] and box[1] == position[1]:
                break
            index += 1    
        newBoxPosition = ()
        if(movement == Constants.UP):
            newBoxPosition = (position[0] , position[1] - 1)
        elif(movement == Constants.DOWN):
            newBoxPosition = (position[0], position[1] + 1)
        elif(movement == Constants.LEFT):
            newBoxPosition = (position[0] - 1, position[1])
        elif(movement == Constants.RIGHT):
            newBoxPosition = (position[0] + 1, position[1])
        self.boxes[index] = newBoxPosition
        self.board[newBoxPosition] = Constants.BOXES_LOC
        self.gameIsDeadEnd = self.isDeadEnd(index)


    def _tryMove(self, movement, playerPosition): #returns valid or invalid movement
        newBoxPosition = ()
        if(playerPosition[0] < 0 or playerPosition[0] >= self.dimentions[0] or playerPosition[1] < 0 or playerPosition[1] >= self.dimentions[1]):
            return Constants.INVALID_MOVE
        if(self.board[playerPosition[0], playerPosition[1]] == Constants.WALLS_LOC):
            return Constants.INVALID_MOVE
        elif (self.board[playerPosition[0], playerPosition[1]] == Constants.EMPTY_LOC):
            return Constants.VALID_MOVE
        elif (self.board[playerPosition[0], playerPosition[1]] == Constants.BOXES_LOC): #we want to move and there is a box in the position we want to move
            if(movement == Constants.UP):
                newBoxPosition = (playerPosition[0],playerPosition[1] - 1)
                #if there is a wall or a box it cannot be moved
                if(newBoxPosition[0] < 0 or  newBoxPosition[0] >= self.dimentions[0] or newBoxPosition[1] < 0 or newBoxPosition[1] >= self.dimentions[1]):
                    return Constants.INVALID_MOVE
                if(self.board[newBoxPosition] == Constants.BOXES_LOC or self.board[newBoxPosition] == Constants.WALLS_LOC):
                    return Constants.INVALID_MOVE
                else:
                    return Constants.VALID_MOVE
            elif(movement == Constants.DOWN):
                newBoxPosition = (playerPosition[0],playerPosition[1] + 1)
                if(newBoxPosition[0] < 0 or  newBoxPosition[0] >= self.dimentions[0] or newBoxPosition[1] < 0 or newBoxPosition[1] >= self.dimentions[1]):
                    return Constants.INVALID_MOVE
                if(self.board[newBoxPosition] == Constants.BOXES_LOC or self.board[newBoxPosition] == Constants.WALLS_LOC):
                    return Constants.INVALID_MOVE
                else:
                    return Constants.VALID_MOVE

            elif(movement == Constants.LEFT):
                newBoxPosition = (playerPosition[0] - 1,playerPosition[1])
                if(newBoxPosition[0] < 0 or  newBoxPosition[0] >= self.dimentions[0] or newBoxPosition[1] < 0 or newBoxPosition[1] >= self.dimentions[1]):
                    return Constants.INVALID_MOVE
                if(self.board[newBoxPosition] == Constants.BOXES_LOC or self.board[newBoxPosition] == Constants.WALLS_LOC):
                    return Constants.INVALID_MOVE
                else:
                    return Constants.VALID_MOVE
            elif(movement == Constants.RIGHT):
                newBoxPosition = (playerPosition[0] + 1,playerPosition[1])
                if(newBoxPosition[0] < 0 or  newBoxPosition[0] >= self.dimentions[0] or newBoxPosition[1] < 0 or newBoxPosition[1] >= self.dimentions[1]):
                    return Constants.INVALID_MOVE
                if(self.board[newBoxPosition] == Constants.BOXES_LOC or self.board[newBoxPosition] == Constants.WALLS_LOC):
                    return Constants.INVALID_MOVE
                else:
                    return Constants.VALID_MOVE


    def isGameFinished(self):
        for box in self.boxes:
            if box not in self.objectives:
                return False
        return True



    def printBoard(self, mode= 'debug'):
        dimX = self.dimentions[0]
        dimY = self.dimentions[1]

        if mode == 'debug':
            toPrint = ''
            for i in range(self.dimentions[0]):
                i=dimX-i-1
                for j in range(self.dimentions[1]):
                    if self.board[j, i] == Constants.EMPTY_LOC and ((j, i) != self.player and (j, i) not in self.objectives):
                        toPrint = toPrint + '%'
                    elif self.board[j, i] == Constants.WALLS_LOC:
                        toPrint = toPrint + '#'
                    elif self.board[j, i] == Constants.BOXES_LOC:
                        toPrint = toPrint + '□'
                    if(self.player[0] == j and self.player[1] == i):
                        toPrint = toPrint + 'P'

                    elif (j, i) in self.objectives:
                        toPrint = toPrint + 'O'
                    if j == dimY-1:
                        toPrint = toPrint + '\n'
            toPrint = toPrint + '\n'
            f = open("demofile2.txt", "a")
            f.write(toPrint)
            f.close()
            
        elif mode == 'vis':
            toPrint = [[0 for x in range(self.dimentions[0])] for y in range(self.dimentions[1])] 
            for i in range(self.dimentions[0]):
                for j in range(self.dimentions[1]):
                    if self.board[j, i] == Constants.EMPTY_LOC and ((j, i) != self.player and (j, i) not in self.objectives):
                        toPrint[dimY-i-1][j] = 0
                    elif self.board[j, i] == Constants.WALLS_LOC:
                        toPrint[dimY-i-1][j] = 1
                    elif self.board[j, i] == Constants.BOXES_LOC:
                        toPrint[dimY-i-1][j] = 2
                    if(self.player[0] == j and self.player[1] == i):
                        toPrint[dimY-i-1][j] = 3
                    elif (j, i) in self.objectives:
                        toPrint[dimY-i-1][j] = 4

            cmap = colors.ListedColormap(['white','black', 'red', 'blue', 'green'])
            plt.figure(figsize=(self.dimentions[0], self.dimentions[1]))
            plt.pcolor(toPrint[::-1],cmap=cmap,edgecolors='k', linewidths=3)
            plt.show()


    def isDeadEnd(self, boxIndex):
        return  (self.boxes[boxIndex] not in self.objectives) and (self._leftUp(boxIndex) or self._rightUp(boxIndex) or self._leftDown(boxIndex) or self._leftUp(boxIndex))

    def _leftUp(self, boxIndex):
        box = self.boxes[boxIndex]
        left1 = (box[0] - 1, box[1])
        up1 = (box[0], box[1] - 1)
        if((left1[0] < 0 or left1[0] >= self.dimentions[0] or self.board[left1] == Constants.WALLS_LOC) 
                and (up1[1] < 0  or up1[1] >= self.dimentions[1] or  self.board[up1] == Constants.WALLS_LOC)):
            return True
        return False

    def _leftDown(self, boxIndex):
        box = self.boxes[boxIndex]
        left1 = (box[0] - 1, box[1])
        down1 = (box[0], box[1] + 1)
        if((left1[0] < 0 or left1[0] >= self.dimentions[0] or self.board[left1] == Constants.WALLS_LOC) and (down1[1] < 0  or down1[1] >= self.dimentions[1] or self.board[down1] == Constants.WALLS_LOC)):
            return True
        return False

    def _rightUp(self, boxIndex):
        box = self.boxes[boxIndex]
        right1 = (box[0] + 1, box[1])
        up1 = (box[0], box[1] - 1)
        if((right1[0] < 0 or right1[0] >= self.dimentions[0] or self.board[right1] == Constants.WALLS_LOC) and (up1[1] < 0  or up1[1] >= self.dimentions[1] or self.board[up1] == Constants.WALLS_LOC)):
            return True
        return False

    def _rightDown(self, boxIndex):
        box = self.boxes[boxIndex]
        right1 = (box[0] + 1, box[1])
        down1 = (box[0], box[1] + 1)
        if((right1[0] < 0 or right1[0] >= self.dimentions[0] or self.board[right1] == Constants.WALLS_LOC) and (down1[1] < 0  or down1[1] >= self.dimentions[1] or self.board[down1] == Constants.WALLS_LOC)):
            return True
        return False

    def __eq__(self, other):
        return self.dimentions == other.dimensions and self.board == other.board and self.player == other.player and self.objectives == other.objectives

    def redundant_equal(self, other):
        return self.board == other.board and self.player == other.player and self.boxes == other.boxes
