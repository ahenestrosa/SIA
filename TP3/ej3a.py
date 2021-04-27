from PerceptronSimpleStep import PerceptronSimpleStep 
from PerceptronMultilayer import PerceptronMultilayer

from random import randrange, choice
import matplotlib.pyplot as plt


def classify(num):
    if num > 0:
        return 1
    return -1

trainingSet = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
resultSet = [ [-1] if x[0] == x[1] else [1] for x in trainingSet ]
multiLayerPerceptron = PerceptronMultilayer(2,1,[2], 'tanh', 0.1)
errors, e = multiLayerPerceptron.train(0.001, 1000, trainingSet, resultSet)

plt.plot(range(0,len(errors),20), errors[::20] , marker='o', linestyle='--')
plt.xlabel('Epoch')
plt.ylabel('Error')
# plt.xscale('log')
plt.show()



print
print("---------------------------------------------------")
print("----------------- XOR RESULTS ---------------------")
print("---------------------------------------------------")

for i in range(len(trainingSet)):
    r, a, v = multiLayerPerceptron.calculateOutput(trainingSet[i])
    print(str(trainingSet[i][0]) + " XOR " + str(trainingSet[i][0]))
    print("Expected: " +  str(resultSet[i][0]))
    print("Actual:" + str(r[0,0]))
    print("Classified: " +  str(classify(r[0,0])))
    print()



