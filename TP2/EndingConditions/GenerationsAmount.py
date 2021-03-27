

class GenerationsAmount:

    def __init__(self, amount):
        self.limit = amount

    def isFinished(self, iteration):
        return self.limit > iteration