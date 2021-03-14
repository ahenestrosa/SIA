from game.Sokoban import Sokoban

class Maps:
    @classmethod
    def map1(cls):
        objective = [(0,0), (2,2)]
        dimensions = (5,5)
        boxes = [(0,1), (1, 2)]
        walls = [(3,3), (4,4),(3,2), (3,1)]
        player = (4, 3)
        return Sokoban(walls, objective, dimensions, player, boxes)

    @classmethod
    def map2(cls):
        objective = [(1,1),(7,7)]
        dimensions = (9,9)
        boxes = [(5,5), (3,5)]
        walls = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
                (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                (8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),
                (1,8),(2,8),(3,8), (4,8),(5,8),(6,8),(7,8)]
        player = (4, 5)
        return Sokoban(walls, objective, dimensions, player, boxes)

    @classmethod
    def map3(cls):
        objective = [(0,1), (0,4)]
        dimensions = (6,6)
        boxes = [(4,1),(4,2)]
        walls = [(2,2),(2,3)]
        player = (3, 4)
        return Sokoban(walls, objective, dimensions, player, boxes)
