DELTA = 0.2

class Content:
    def __init__(self, delta):
        self.delta = delta

    def isFinished(self, characters_gen, generations):
        gen = 0
        if len(characters_gen):
            return False

        while gen < len(characters_gen) - 1:
            if gen == 0:
                characters_gen[gen].sort(reverse=True)
            characters_gen[gen+1].sort(reverse=True)

            if abs(characters_gen[gen][0].fitness - characters_gen[gen + 1][0].fitness) > self.delta:
                return False
        return True