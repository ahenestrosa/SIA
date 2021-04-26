from PerceptronMultilayer import PerceptronMultilayer

from random import randrange, choice


def loadInput():
    f = open('./data/ej3b.txt')
    examples = []
    example = []
    inputNumber = 0
    while True:
        line = f.readline().split(" ")
        if line[0] == '':
            break
        for i in range(5):
            example.append(int(line[i]))
            inputNumber += 1

        if inputNumber >= 7*5:
            examples.append(example)
            inputNumber = 0
            example = []
    return examples

def printInput(inp):
    for i in range(len(inp)):
        if i%5 == 0:
            print()
        if inp[i] == 1:
            print(inp[i], end=' ')
        else:
            print(' ', end='')

inputs = loadInput()
ouputs = [[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]]




# Con conjunto de entrenamiento = conjunto de testing

print("----------------------------------------------------")
print("--------- Testing set = Training set ---------------")
print("----------------------------------------------------")

multiLayerPerceptron = PerceptronMultilayer(7*5,1,[8,4,2], 'tanh', 0.01, costFunction='entropic', momentum=0.9, adaptative=(0.0001, 0.00001))
multiLayerPerceptron.train(0.001, 500, inputs, ouputs, verbose=True)

for i in range(10):
    testInput = inputs[i]
    testOutput = ouputs[i]
    r, V, h = multiLayerPerceptron.calculateOutput(testInput)
    printInput(testInput)
    print("Expected: " + str(testOutput) + " Actual: " + str(r[0]))


# Con conjunto de entrenamiento separado del de testing
print("----------------------------------------------------")
print("--------- Testing set != Training set ---------------")
print("----------------------------------------------------")

#Training set
trainingSetInputs = []
trainingSetOutputs = []
for i in [0, 1, 4, 5, 7, 8]:
    trainingSetInputs.append(inputs[i])
    trainingSetOutputs.append(ouputs[i])

multiLayerPerceptron = PerceptronMultilayer(7*5,1,[8,4,2], 'tanh', 0.01, costFunction='entropic')
multiLayerPerceptron.train(0.01, 1000, trainingSetInputs, trainingSetOutputs, verbose=False)

#Test set
print("----------- Testing ---------------")
for i in [2,3,5,9]:
    testInput = inputs[i]
    testOutput = ouputs[i]
    r, V, h = multiLayerPerceptron.calculateOutput(testInput)
    printInput(testInput)
    print("Expected: " + str(testOutput) + " Actual: " + str(r[0]))


