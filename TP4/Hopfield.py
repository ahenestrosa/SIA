import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import colors

class Hopfield:

    def __init__(self, patterns):
        self.patterns = np.array(patterns)
        self.patternsSize = len(patterns)
        self.N = len(patterns[0]) 
        self.energy = []  
        
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
        i = 0
        while not np.array_equal(newPattern, lastPattern) and i < 20:
            # Hopfield.printLetter(newPattern)
            # Hopfield.plotLetter(newPattern,i)
            i+=1
            self.energy.append(self.calculate_energy(newPattern))
            lastPattern = newPattern.copy()
            newPattern = np.array(np.sign(np.matmul(self.weights, lastPattern))).flatten()

        # self.plot_energy()
        return newPattern

    def calculate_energy(self, s):
        sum = 0
        for i in range(len(self.weights)):
            for j in range(i + 1, len(self.weights)):
                sum += self.weights[i,j] * s[i] * s[j]
        return -sum

    def plot_energy(self):
        x = [ i for i in range(len(self.energy)) ]
        plt.grid()
        plt.plot(x ,self.energy, marker='o')
        plt.xlabel('Iteración')
        plt.ylabel('Energía')
        plt.show()

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


    @classmethod
    def plotLetter(cls, input, index = 0):
        cmap = colors.ListedColormap(['black','red'])
        toPrint = [[0 for x in range(5)] for y in range(5)] 
        j,k = 0, 0
        for i in range(len(input)):
            if i%5 == 0:
                k += 1
                j  = 0
            if i == 0:
                k = 0
            if input[i] == 1:
                toPrint[k][j] = 1
                j += 1
            else:
                toPrint[k][j] = 0
                j+=1
        plt.figure(figsize=(5, 5))
        plt.pcolor(toPrint[::-1],cmap=cmap,edgecolors='k', linewidths=3)
        # plt.savefig(f'letter-{index}.png')
        plt.show()