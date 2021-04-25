from PerceptronSimpleStep import PerceptronSimpleStep 
from PerceptronMultilayer import PerceptronMultilayer

from random import randrange, choice

trainingSet = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
resultSet = [ [-1] if x[0] == x[1] else [1] for x in trainingSet ]
multiLayerPerceptron = PerceptronMultilayer(2,1,[2], 'tanh', 0.1)
multiLayerPerceptron.train(0.001, 1000, trainingSet, resultSet)


for i in range(len(trainingSet)):
    r, a, v = multiLayerPerceptron.calculateOutput(trainingSet[i])
    print(str(trainingSet[i]) + " Expected: " + str(resultSet[i]) + " Actual:" + str(r) )



