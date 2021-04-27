from PerceptronSimpleStep import PerceptronSimpleStep 
from PerceptronMultilayer import PerceptronMultilayer

from random import randrange, choice

def andPerceptron():
    perceptron = PerceptronSimpleStep(2, 0.1)
    trainingSet = [[1,1], [1,-1], [-1,1], [-1,-1]]
    resultSet = [1,-1,-1,-1]

    #epocas
    for i in range(100):
        perceptron.trainPerceptron(trainingSet, resultSet)
    return perceptron

def xorPerceptron():
    perceptron = PerceptronSimpleStep(2, 0.1)
    trainingSet = [[1,1],[1,-1], [-1,-1],[-1,1]]
    resultSet = [-1,1,-1,1]

    #epocas
    for i in range(10):
        perceptron.trainPerceptron(trainingSet, resultSet)
    return perceptron


perceptron = andPerceptron()
print(perceptron.calculateOutput([1,-1]))