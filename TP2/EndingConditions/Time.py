
class Time:

    def __init__(self, time):
        self.limit = time


    def isFinished(self, time):
        return self.limit > time