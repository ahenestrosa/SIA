import itertools

class Heuristics:
    @classmethod
    def boxObjDistance(cls, node): #shoprtest distance between boxes and objectives
        min_distance = None
        sokoban = node.sokoban

        all_combinations = []
        list1_permutations = itertools.permutations(sokoban.boxes, len(sokoban.objectives))
        for each_permutation in list1_permutations:
            zipped = zip(each_permutation, sokoban.objectives)
            all_combinations.append(list(zipped))
    
        for combination in all_combinations:
            dist1 = 0
            for pair in combination:
                box = pair[0]
                obj = pair[1]
                dist1 += abs(box[0] - obj[0]) + abs(box[1] - obj[1])

            if min_distance == None or dist1 < min_distance:
                min_distance = dist1


        return min_distance



    @classmethod
    def playerBoxDistance(cls, node): #shortest way between player and any box
        sokoban = node.sokoban
        player = sokoban.player
        min_distance = None


        for box in sokoban.boxes:
            dist = abs(box[0] - player[0]) + abs(box[1] - player[1])
            if min_distance == None or dist < min_distance:
                min_distance = dist

        return min_distance        


    #TODO: Addapt to multple boxes!!!
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








