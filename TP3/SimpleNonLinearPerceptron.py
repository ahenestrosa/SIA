import sys
import numpy as np


class SimpleNonLinearPerceptron:

    def __init__(self, inputSize, learningRate, g, gPrime):
        self.weightSize = inputSize + 1
        self.learningRate = learningRate
        self.weights = np.random.random(self.weightSize)
        # self.weights = [0] * (self.weightSize)
        self.g = g
        self.gPrime = gPrime


    def trainPerceptron(self, trainingSet, epsilon, epoch):
        minW = self.weights
        X = [ [[-1, t[0] , t[1], t[2]] , t[3]] for t in trainingSet ]
        # print(X)
        error = sys.maxsize # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
        minError = error
        counter = 0
        while error > epsilon and counter < epoch:

            i_x = np.random.randint(0, len(trainingSet))

            excitation = np.inner(self.weights, X[i_x][0])
            gPrimeValue = self.gPrime(excitation)
            deltaW = (X[i_x][1] - self.g(excitation)) * gPrimeValue * self.learningRate * np.array(X[i_x][0])
            self.weights = self.weights + deltaW
            
            
            error = self.calculateError(X)

            if error < minError:
                minError = error
                minW = self.weights

            counter += 1
        print(minError)
        self.weights = minW
        # print("Weights percep:")
        # print(self.weights)

    def calculateError(self, X):
        e = 0
        for j in range(len(X)):
            resultValue = X[j][1]
            trainingValue = np.inner(self.weights, X[j][0])
            e = e + (resultValue - trainingValue)** 2
        return e * 0.5