import sys
import numpy as np
import math


class SimpleNonLinearPerceptron:

    def __init__(self, inputSize, learningRate):
        self.weightSize = inputSize + 1
        self.learningRate = learningRate
        self.weights = np.random.random(self.weightSize)



    def trainPerceptron(self, trainingSet, epsilon, epoch):
        minW = self.weights
        X = [ [[1, t[0][0] , t[0][1], t[0][2]] , t[1]] for t in trainingSet ]
        # print(X)
        error = sys.maxsize # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
        minError = error
        counter = 0
        while error > epsilon and counter < epoch:

            i_x = np.random.randint(0, len(trainingSet))

            excitation = np.inner(self.weights, X[i_x][0])
            gPrimeValue = (1 - math.tanh(excitation)**2)
            deltaW = (X[i_x][1] - self.activation(excitation)) * gPrimeValue * self.learningRate * np.array(X[i_x][0])
            self.weights = self.weights + deltaW
            
            error = self.calculateError(X)

            if error < minError:
                minError = error
                minW = self.weights

            counter += 1
        # print(minError)
        self.weights = minW

    def calculateError(self, X):
        e = 0
        for j in range(len(X)):
            resultValue = X[j][1]
            excited = np.inner(self.weights, X[j][0])
            trainingValue = self.activation(excited)
            e = e + (resultValue - trainingValue)** 2
        return e * 0.5

    def activation(self, excited):
        return np.tanh(excited)

    def get_output(self, trainingSet):
        # print("MIN W: {}".format(self.weights))
        outputs = []
        X = [ [[1, y[0][0], y[0][1], y[0][2]]] for y in trainingSet]      
        for i in range(len(X)):
            excited_state = np.inner(X[i], self.weights)
            outputs.append(self.activation(excited_state))
        return outputs