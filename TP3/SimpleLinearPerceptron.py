import sys
import numpy as np


class SimpleLinearPerceptron:

    def __init__(self, inputSize, learningRate):
        self.weightSize = inputSize + 1
        self.learningRate = learningRate
        self.weights = [0] * (self.weightSize)


    def trainPerceptron(self, trainingSet, epsilon, epoch):
        minW = self.weights
        X = [ [[1, t[0][0] , t[0][1], t[0][2]] , t[1]] for t in trainingSet ]

        # print(X)
        error = 1 
        minError = 2 * len(trainingSet) * 1000
        counter = 0
        while error > epsilon and counter < epoch:

            i_x = np.random.randint(0, len(trainingSet))
            excitation = np.inner(X[i_x][0], self.weights)
            deltaW = (X[i_x][1] - excitation ) * self.learningRate * np.array(X[i_x][0])
            self.weights = self.weights + deltaW

            error = self.calculateError(X)
        
            if error < minError:
                minError = error
                minW = self.weights 
            counter += 1
        self.weights = minW

    def calculateError(self, X):
        e = 0
        for j in range(len(X)):
            resultValue = X[j][1]
            trainingValue = np.inner(self.weights, X[j][0])
            e = e + (resultValue - trainingValue)** 2
        return e * 0.5

    def activation(self,X):
        return X

    def get_output(self, trainingSet):
        print("MIN W: {}".format(self.weights))
        outputs = []
        print(trainingSet)
        X = [ [[1, y[0][0], y[0][1], y[0][2]]] for y in trainingSet]      
        for i in range(len(X)):
            excited_state = np.inner(X[i], self.weights)
            outputs.append(self.activation(excited_state))
        return outputs