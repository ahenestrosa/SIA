import itertools
import math

class Heuristics:
    @classmethod
    #shoprtest cumulative distance between all boxes and objectives in permutations
    def boxObjDistance(cls, node): 
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
    #shortest cumulative distance between all boxes and objectives in permutations using euclidean formula
    def boxObjEucDistance(cls,node): # shortes
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
                dist1 += math.sqrt(math.pow(box[0] - obj[0], 2) + math.pow(box[1] - obj[1], 2))

            if min_distance == None or dist1 < min_distance:
                min_distance = dist1
        return min_distance

    @classmethod
    #shoprtest cumulative distance between all boxes and its closes objetive
    def minObjDistance(cls, node):
        sokoban = node.sokoban
        dist = 0
        for boxes in sokoban.boxes:
            min_dist = float("inf")
            for obj in sokoban.objectives:
                curr_dist = abs(boxes[0] - obj[0]) + abs(boxes[1] - obj[1])
                if curr_dist < min_dist:
                    min_dist = curr_dist
            dist += min_dist
        return dist



    # shortest way between player and any box thats not in a objetive
    @classmethod
    def playerBoxDistance(cls, node):
        sokoban = node.sokoban
        player = sokoban.player
        objectives = sokoban.objectives
        min_distance = None

        for box in sokoban.boxes:
            if box not in objectives:
                dist = abs(box[0] - player[0]) + abs(box[1] - player[1])
                if min_distance == None or dist < min_distance:
                    min_distance = dist


        if min_distance == None:
            min_distance = 0
        return min_distance


    @classmethod
    # shortest way between player and any box + that box to other aobjetive
    def playerBoxObjDistance(cls, node):
        sokoban = node.sokoban
        player = sokoban.player
        not_used_boxes = []
        not_used_objetives = sokoban.objectives.copy()

        for box in sokoban.boxes:
            if box in not_used_objetives:
                #box is same as objetive
                not_used_objetives.remove(box)
            else:
                not_used_boxes.append(box)

        combined_list = [[player], not_used_boxes, not_used_objetives]
        min_distance = None
        for triple in itertools.product(*combined_list):
            player = triple[0]
            box = triple[1]
            obj = triple[2]

            dist = abs(player[0]-box[0]) + abs(player[1] - box[1])\
                 + abs(box[0]-obj[0]) + abs(box[1]-obj[1])
            if min_distance == None or dist < min_distance:
                min_distance = dist

        # Para hacerlo admisible
        if min_distance != None:
            min_distance -= 2


        return min_distance if min_distance != None else 0








