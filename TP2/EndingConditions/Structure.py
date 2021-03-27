import math

DELTA_HEIGHT = 0.1
DELTA_ATTACK_DEFENSE = 1.0
DELTA_FITNESS = 0.5
POB_PROP = 1/4

class Structure:
    def __init__(self, dh, dad, df, pp):
        self.dh = dh #delta height
        self.dad = dad #delta attack defense
        self.df = df #delta fitness
        self.pp = pp #delta pob prop
    def isFinished(self, characters_gen, generations):
        gen = 0
        if len(characters_gen) < generations:
            return False

        while gen < generations - 1:
            j = 0
            counter = 0
            if gen == 0:
                characters_gen[gen].sort()
            characters_gen[gen + 1].sort()

            while j < len(characters_gen[gen]):
                if abs(characters_gen[gen][j].height - characters_gen[gen + 1][j].height) > self.dh or abs(characters_gen[gen][j].attack - characters_gen[gen + 1][j].attack) > self.dad or abs(characters_gen[gen][j].defense - characters_gen[gen + 1][j].defense) > self.dad or abs(characters_gen[gen][j].fitness - characters_gen[gen + 1][j].fitness) > self.df:
                    counter += 1
                j += 1
            if counter < len(characters_gen[gen]) * self.pp:
                return False
            gen += 1


        if counter < len(characters_gen[0]) * self.pp * (generations - 1):
            return False
        else:
            return True
