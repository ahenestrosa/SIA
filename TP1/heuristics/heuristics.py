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


    @classmethod
    def playerBoxObjDistance(cls, node):
        sokoban = node.sokoban
        player = sokoban.player
        
        combined_list = [[player], sokoban.boxes, sokoban.objectives]
        min_distance = None
        for triple in itertools.product(*combined_list):
            player = triple[0]
            box = triple[1]
            obj = triple[2]

            dist = abs(player[0]-box[0]) + abs(player[1] - box[1])\
                 + abs(box[0]-obj[0]) + abs(box[1]-obj[1])
            if min_distance == None or dist < min_distance:
                min_distance = dist

        return min_distance








