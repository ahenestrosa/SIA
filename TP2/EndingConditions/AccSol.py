

class AccSol:

    def __init__(self, fitness):
        self.limit = fitness

    def isFinished(self, characters):
        characters.sort(reverse=True)
        return characters[0].fitness > self.limit