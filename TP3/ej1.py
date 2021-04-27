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
        for i in range(len(trainingSet)):
            r = perceptron.calculateOutput(trainingSet[i])
            print(str(trainingSet[i][0]) + " AND " + str(trainingSet[i][1]))
            print("Expected: " +  str(resultSet[i]))
            print("Actual:" + str(r))
            print()

def xorPerceptron():
    perceptron = PerceptronSimpleStep(2, 0.1)
    trainingSet = [[1,1],[1,-1], [-1,-1],[-1,1]]
    resultSet = [-1,1,-1,1]

    #epocas
    for i in range(10):
        perceptron.trainPerceptron(trainingSet, resultSet)
    for i in range(len(trainingSet)):
        r = perceptron.calculateOutput(trainingSet[i])
        print(str(trainingSet[i][0]) + " XOR " + str(trainingSet[i][1]))
        print("Expected: " +  str(resultSet[i]))
        print("Actual:" + str(r))
        print()



perceptron = andPerceptron()

