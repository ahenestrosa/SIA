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




def main():
    # perceptron = xorPerceptron()
    # print(perceptron.calculateOutput([1,-1]))

    # multiLayerPerceptron = PerceptronMultilayer(2,1,[2,5,2], 'tanh', 1)
    # r,v,h = multiLayerPerceptron.calculateOutput([1,2])
    # deltas = multiLayerPerceptron.backPropagate([3,1], v, h)
    # multiLayerPerceptron.updateWeights(v, deltas)

    trainingSet = [[1,1], [1,-1], [-1,1], [-1,-1]]
    resultSet = [[-1],[1],[1],[-1]]
    multiLayerPerceptron = PerceptronMultilayer(2,1,[3], 'tanh', 10000)
    multiLayerPerceptron.train(0.01, 100, trainingSet, resultSet)
    r, a, v = multiLayerPerceptron.calculateOutput([1,-1])
    print(r)






if __name__ == "__main__":
    main()
