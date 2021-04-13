from PerceptronSimpleStep import PerceptronSimpleStep 

from random import randrange, choice

def andPerceptron():
    perceptron = PerceptronSimpleStep(2, 1)
    trainingSet = [[1,1], [1,-1], [-1,1], [-1,-1]]
    resultSet = [1,-1,-1,-1]

    #epocas
    for i in range(100):
        perceptron.trainPerceptron(trainingSet, resultSet)
    return perceptron

def xorPerceptron():
    perceptron = PerceptronSimpleStep(2, 1)
    trainingSet = [[1,1], [1,-1], [-1,1], [-1,-1]]
    resultSet = [-1,1,1,1]

    #epocas
    for i in range(100):
        perceptron.trainPerceptron(trainingSet, resultSet)
    return perceptron


def main():
    perceptron = xorPerceptron()
    print(perceptron.calculateOutput([1,1]))




if __name__ == "__main__":
    main()
