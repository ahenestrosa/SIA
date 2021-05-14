import numpy as np
import math

class Hopfield:

    def __init__(self, patterns):
        self.patterns = np.array(patterns)
        self.patternsSize = len(patterns)
        self.N = len(patterns[0])

        # print(np.shape(patterns))
        # for i in range(4):
        #     for j in range(25):
        #         print(np.dot(patterns[i,:], patterns[j,:] ))
        
        K = np.asmatrix(self.patterns.T)
        self.weights = np.matrix((1/self.N) *  K * K.T) #- (np.identity(self.N) * 0.25 * self.patternsSize)

        for i in range(self.N):
            self.weights[i,i] = 0

        if(self.patternsSize > 0.15 * self.N):
            print('Warning: patterns stored is bigger than 0.15 of total neurons')



    def evaluate(self, pattern):
        if len(pattern) != self.N:
            print('Invalid pattern')
            exit(1)


        newPattern = np.array(pattern)
        lastPattern = None
        while not np.array_equal(newPattern, lastPattern):
            Hopfield.printLetter(newPattern)
            lastPattern = newPattern.copy()
            newPattern = np.array(np.sign(np.matmul(self.weights, lastPattern))).flatten()

        return newPattern

    @classmethod
    def printLetter(cls, input):
        for i in range(len(input)):
            if i%5 == 0:
                print()
            if input[i] == 1:
                print("* ", end='')
            else:
                print("  ", end ='')
        print()
