import math

class EndingConditions:

    @classmethod
    def accSolutionEnding(cls, characters, limit):
        characters.sort(reverse=True)
        return characters[0].fitness >= limit

    @classmethod
    def contentEnding(cls, characters_gen, generations, delta):
        if len(characters_gen)-generations-1 < 0:
            return False
        startGen = len(characters_gen) - generations - 1
        endGen = len(characters_gen) - 1
        characters_gen[startGen].sort(reverse=True)
        characters_gen[endGen].sort(reverse=True)

        if abs(characters_gen[startGen][0].fitness - characters_gen[endGen][0].fitness) > delta:
            return False
        return True


    @classmethod
    def generationsAmmountEnding(cls, iteration, limit):
        return limit < iteration

    @classmethod
    def structureEnding(cls, characters_gen, generations, dh, dad, df, pp):

        if len(characters_gen) < generations:
            return False
        gen = len(characters_gen) - generations;
        while gen < generations - 1:
            j = 0
            counter = 0
            if gen == 0:
                characters_gen[gen].sort()
            characters_gen[gen + 1].sort()

            while j < len(characters_gen[gen]):
                if abs(characters_gen[gen][j].height - characters_gen[gen + 1][j].height) > dh or abs(characters_gen[gen][j].attack - characters_gen[gen + 1][j].attack) > dad or abs(characters_gen[gen][j].defense - characters_gen[gen + 1][j].defense) > dad or abs(characters_gen[gen][j].fitness - characters_gen[gen + 1][j].fitness) > df:
                    counter += 1
                j += 1
            if counter < len(characters_gen[gen]) * pp:
                return False
            gen += 1


        if counter < len(characters_gen[0]) * pp * (generations - 1):
            return False
        else:
            return True

    @classmethod
    def timeEnding(cls, time, limit):
        return limit <= time

