

class Heuristics:
    @classmethod
    def boxObjDistance(cls, node): #shoprtest distance between boxes and objectives
        dist1 = abs(node.sokoban.boxes[0][0] - node.sokoban.objectives[0][0]) \
                + abs(node.sokoban.boxes[0][1] - node.sokoban.objectives[0][1]) \
                + abs(node.sokoban.boxes[1][0] - node.sokoban.objectives[1][0]) \
                + abs(node.sokoban.boxes[1][1] - node.sokoban.objectives[1][1])

        dist2 = abs(node.sokoban.boxes[0][0] - node.sokoban.objectives[1][0]) \
                + abs(node.sokoban.boxes[0][1] - node.sokoban.objectives[1][1]) \
                + abs(node.sokoban.boxes[1][0] - node.sokoban.objectives[0][0]) \
                + abs(node.sokoban.boxes[1][1] - node.sokoban.objectives[0][1])

        return min(dist1, dist2)



    @classmethod
    def playerObjDistance(cls, node): #shortest way between player and objectives
        playerPosition = node.sokoban.player
        dimentions = node.sokoban.dimentions
        objectives = node.sokoban.objectives

        way = 0

        dir00 = objectives[0][0] - playerPosition[0]
        dir01 = objectives[0][1] - playerPosition[1]

        dir10 = objectives[1][0] - playerPosition[0]
        dir11 = objectives[1][1] - playerPosition[1]

        firstObj = 0

        if abs(dir00) + abs(dir01) > abs(dir10) + abs(dir11):
            firstObj = 1 #it means the second objective is nearer than the first obj

        if firstObj == 0:
            way = way + abs(dir00) + abs(dir01) - 1 #distance player and first objective
            way = way + abs(objectives[0][0] - objectives[1][0]) + abs(objectives[0][1] - objectives[1][1]) - 2 #best case
        else:
            way = way + abs(dir10) + abs(dir11) - 1
            way = way + abs(objectives[0][0] - objectives[1][0]) + abs(objectives[0][1] - objectives[1][1]) - 2

        return way


    @classmethod
    def playerBoxObjDistance(cls, node):
        playerPosition = node.sokoban.player
        box0 = node.sokoban.boxes[0]
        box1 = node.sokoban.boxes[1]

        way = 0

        firstBox = 0
        dist0 = abs(playerPosition[0] - box0[0]) + abs(playerPosition[1] - box0[1])
        dist1 = abs(playerPosition[0] - box1[0]) + abs(playerPosition[1] - box1[1])

        if(dist1 > dist0):
            playerPosition = box0
            way = way + dist0 - 1
            firstBox = 0
        else:
            firstBox = 1
            playerPosition = box1
            way = way + dist1 - 1

        if firstBox == 1:
            dist0 = abs(playerPosition[0] - box0[0]) + abs(playerPosition[1] - box0[1])
            way = way + dist0 - 1
        else:
            dist1 = abs(playerPosition[0] - box1[0]) + abs(playerPosition[1] - box1[1])
            way = way + dist1 - 1

        way = way + Heuristics.boxObjDistance(node)

        return way








