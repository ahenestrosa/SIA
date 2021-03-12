from TP1.game import Constants


class Sokoban():
    dimentions = ()
    board = {}
    player = ()
    objectives = ()

    def __init__(self, walls, objectives, dimentions, player, boxes):
        i = 0;
        j = 0;
        self.dimentions = dimentions
        self.player = player
        self.objectives = objectives
        self.boxes = boxes;
        for i in range(dimentions[0]): #first we locate empty locations to squares
            for j in range(dimentions[1]):
                self.board[i, j] = Constants.EMPTY_LOC;

        for wall in walls: #wall location
            self.board[wall[0], wall[1]] = Constants.WALLS_LOC;

        for box in boxes: #box location
            self.board[box[0], box[1]] = Constants.BOXES_LOC;

    @classmethod
    def from_game(cls, board):
        obj = cls.__new__(cls);
        auxBoard = board.board.copy()
        boxes = board.boxes.copy()
        objectives = board.objectives.copy()
        obj.dimentions = board.dimentions;
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
                    return Constants.VALID_MOVE;
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE;
            else:
                return Constants.INVALID_MOVE;


        elif(movement == Constants.DOWN):
            newPlayerPosition = (self.player[0], self.player[1] + 1)
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition);
                    return Constants.VALID_MOVE;
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE;
            else:
                return Constants.INVALID_MOVE;

        elif(movement == Constants.LEFT):
            newPlayerPosition = (self.player[0] - 1, self.player[1])
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition);
                    return Constants.VALID_MOVE;
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE;
            else:
                return Constants.INVALID_MOVE;

        elif(movement == Constants.RIGHT):
            newPlayerPosition = (self.player[0] + 1, self.player[1])
            if(self._tryMove(movement, newPlayerPosition) == Constants.VALID_MOVE):
                if (self.board[newPlayerPosition] == Constants.BOXES_LOC):
                    self._locatePlayer(newPlayerPosition)
                    self._moveBox(movement, newPlayerPosition);
                    return Constants.VALID_MOVE;
                else:
                    self._locatePlayer(newPlayerPosition)
                    return Constants.VALID_MOVE;
            else:
                return Constants.INVALID_MOVE;


    def _locatePlayer(self, newPosition):
        self.board[newPosition] = Constants.EMPTY_LOC
        self.player = newPosition

    def _moveBox(self, movement, position):
        index = 0;
        if self.boxes[0][0] == position[0] and self.boxes[0][1] == position[1]: #to know which box we have to move
            index = 0
        else:
            index = 1
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
        self.board[newBoxPosition] = Constants.BOXES_LOC;


    def _tryMove(self, movement, playerPosition): #returns valid or invalid movement
        newBoxPosition = ()
        if(playerPosition[0] < 0 or playerPosition[0] >= self.dimentions[0] or playerPosition[1] < 0 or playerPosition[1] >= self.dimentions[1]):
            return Constants.INVALID_MOVE
        if(self.board[playerPosition[0], playerPosition[1]] == Constants.WALLS_LOC):
            return Constants.INVALID_MOVE
        elif (self.board[playerPosition[0], playerPosition[1]] == Constants.EMPTY_LOC):
            return Constants.VALID_MOVE;
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
        if self.boxes[0] in self.objectives and self.boxes[1] in self.objectives:
            return True
        return False


    def printBoard(self):
        j = 0
        i = 0
        toPrint = ''
        for i in range(self.dimentions[0]):
            for j in range(self.dimentions[1]):
                if self.board[j, i] == Constants.EMPTY_LOC and ((j, i) != self.player and (j, i) not in self.objectives):
                    toPrint = toPrint + '%'
                elif self.board[j, i] == Constants.WALLS_LOC:
                    toPrint = toPrint + '#'
                elif self.board[j, i] == Constants.BOXES_LOC:
                    toPrint = toPrint + '□'
                if(self.player[0] == j and self.player[1] == i):
                    toPrint = toPrint + 'P'

                elif (self.board[j,i] != Constants.BOXES_LOC and ((j == self.objectives[0][0] and i == self.objectives[0][1]) or (j == self.objectives[1][0] and i == self.objectives[1][1]))):
                    toPrint = toPrint + 'O'
                if j == self.dimentions[1] - 1:
                    toPrint = toPrint + '\n'
        print(toPrint)

    def isDeadEnd(self):
        if(self._leftUp()):
            return True;
        if(self._rightUp()):
            return True;
        if(self._leftDown()):
            return True;
        if(self._leftUp()):
            return True;
        return False;

    def _leftUp(self):
        left1 = (self.boxes[0][0] - 1, self.boxes[0][1])
        up1 = (self.boxes[0][0], self.boxes[0][1] - 1)
        left2 = (self.boxes[1][0] - 1, self.boxes[1][1])
        up2 = (self.boxes[1][0],self.boxes[1][1] - 1)
        if(((left1[0] < 0 or left1[0] >= self.dimentions[0] or self.board[left1] == Constants.WALLS_LOC) and (up1[1] < 0  or up1[1] >= self.dimentions[1] or  self.board[up1] == Constants.WALLS_LOC))
            or ((left2[0] < 0 or left2[0] >= self.dimentions[0] or self.board[left2] == Constants.WALLS_LOC) and (up2[1] < 0  or up2[1] >= self.dimentions[1] or  self.board[up2] == Constants.WALLS_LOC))):
            return True;
        return False;

    def _leftDown(self):
        left1 = (self.boxes[0][0] - 1, self.boxes[0][1])
        down1 = (self.boxes[0][0], self.boxes[0][1] + 1)
        left2 = (self.boxes[1][0] - 1, self.boxes[1][1])
        down2 = (self.boxes[1][0],self.boxes[1][1] + 1)
        if(((left1[0] < 0 or left1[0] >= self.dimentions[0] or self.board[left1] == Constants.WALLS_LOC) and (down1[1] < 0  or down1[1] >= self.dimentions[1] or self.board[down1] == Constants.WALLS_LOC))
            or ((left2[0] < 0 or left2[0] >= self.dimentions[0] or self.board[left2] == Constants.WALLS_LOC) and (down2[1] < 0  or down2[1] >= self.dimentions[1] or self.board[down2] == Constants.WALLS_LOC))):
            return True;
        return False;

    def _rightUp(self):
        right1 = (self.boxes[0][0] + 1, self.boxes[0][1])
        up1 = (self.boxes[0][0], self.boxes[0][1] - 1)
        right2 = (self.boxes[1][0] + 1, self.boxes[1][1])
        up2 = (self.boxes[1][0],self.boxes[1][1] - 1)
        if(((right1[0] < 0 or right1[0] >= self.dimentions[0] or self.board[right1] == Constants.WALLS_LOC) and (up1[1] < 0  or up1[1] >= self.dimentions[1] or self.board[up1] == Constants.WALLS_LOC))
            or ((right2[0] < 0 or right2[0] >= self.dimentions[0] or self.board[right2] == Constants.WALLS_LOC) and (up2[1] < 0  or up2[1] >= self.dimentions[1] or self.board[up2] == Constants.WALLS_LOC))):
            return True;
        return False;

    def _rightDown(self):
        right1 = (self.boxes[0][0] + 1, self.boxes[0][1])
        down1 = (self.boxes[0][0], self.boxes[0][1] + 1)
        right2 = (self.boxes[1][0] + 1, self.boxes[1][1])
        down2 = (self.boxes[1][0],self.boxes[1][1] + 1)
        if(((right1[0] < 0 or right1[0] >= self.dimentions[0] or self.board[right1] == Constants.WALLS_LOC) and (down1[1] < 0  or down1[1] >= self.dimentions[1] or self.board[down1] == Constants.WALLS_LOC))
            or ((right2[0] < 0 or right2[0] >= self.dimentions[0] or self.board[right2] == Constants.WALLS_LOC) and (down2[1] < 0  or down2[1] >= self.dimentions[1] or self.board[down2] == Constants.WALLS_LOC))):
            return True;
        return False;

    def __eq__(self, other):
        return self.dimentions == other.dimensions and self.board == other.board and self.player == other.player and self.objectives == other.objectives

    def redundant_equal(self, other):
        return self.board == other.board and self.player == other.player and self.boxes == other.boxes
