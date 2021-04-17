import sys
import numpy as np


class SimpleLinearPerceptron:

    def __init__(self, inputSize, learningRate):
        self.weightSize = inputSize + 1
        self.learningRate = learningRate
        self.weights = [0] * (self.weightSize)


    def trainPerceptron(self, trainingSet, epsilon, epoch):
        minW = self.weights
        X = [ [[-1, t[0] , t[1], t[2]] , t[3]] for t in trainingSet ]
        # print(X)
        error = sys.maxsize # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
        minError = error
        counter = 0
        while error > epsilon and counter < epoch:
            for x in X:
                excitation = np.dot(self.weights, x[0])
                deltaW = (x[1] - excitation ) * self.learningRate * np.array(x[0])
                self.weights = self.weights + deltaW
            
            err = 0
            for j in range(len(X)):
                resultValue = X[j][1]
                trainingValue = np.dot(self.weights,X[j][0])
                err = err + (resultValue - trainingValue) ** 2
            error = err / 2
            print(error)
            if error < minError:
                minError = error
                minW = self.weights 
            counter += 1
        self.weights = minW
        print(self.weights)
