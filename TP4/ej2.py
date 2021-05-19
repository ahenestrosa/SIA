from Hopfield import Hopfield
import random
import numpy as np
import matplotlib.pyplot as plt

def loadInput():
    f = open('./Resources/letters2.txt')
    examples = []
    example = []
    inputNumber = 0
    while True:
        line = f.readline().strip("\n").split(" ")
        if line[0] == '':
            break
        for i in range(5):
            example.append(int(line[i]))
            inputNumber += 1

        if inputNumber >= 5*5:
            examples.append(example)
            inputNumber = 0
            example = []
            f.readline()
    return examples


def modifyInput(pattern, p):
    newP = []
    for i in range(len(pattern)):
        m = random.uniform(0, 1)
        if m <= p:
            newP.append(pattern[i] * -1)
        else:
            newP.append(pattern[i])

    return newP

# para ver el producto interno de las letras --> tiene que ser cercano a 0
def calculateOrthogonality(patterns):
    for i in range(4):
        for j in range(4):
            if j > i:
                print(np.dot(patterns[i], patterns[j] ))
                hopfield.printLetter(patterns[i])
                hopfield.printLetter(patterns[j])


def multipleTest(patterns, hopfield):
    p = [0.1, 0.15, 0.2, 0.25, 0.3 , 0.35, 0.4]
    for i in p:
        for j in range(len(patterns)):
            print("~~~~~ Initial Letter: ~~~~~")
            hopfield.printLetter(patterns[j]) 
            test = modifyInput(patterns[j].copy(), i)
            print(f"~~~~~ Results: {i} noise ~~~~~")
            hopfield.evaluate(test)


def inputVsObservable(hopfield, patterns):
    prob = 0
    inps = []
    results = []
    while prob <= 1:
        res = 0
        for pattern in patterns:
            test = modifyInput(pattern.copy(), prob)
            testResult = hopfield.evaluate(test)
            if np.array_equal(pattern, testResult):
                res += 1

        results.append(res/len(patterns))
        inps.append(prob)
        prob += 0.1


    fig, ax = plt.subplots()
    ax.plot(inps, results, '--ok')
    ax.set_xlabel('Probabilidad de mutación')
    ax.set_ylabel('Porcentaje de éxito')
    plt.grid()
    plt.show()

patterns = loadInput()
hopfield = Hopfield(patterns)

# inputVsObservable(hopfield, patterns)

randomInput = random.randrange(4)
p = 0.5

calculateOrthogonality(patterns)

print("~~~~~ Initial Letter: ~~~~~")
hopfield.printLetter(patterns[randomInput])
hopfield.plotLetter(patterns[randomInput])

tester = modifyInput(patterns[randomInput].copy(), p )
print("~~~~~ Results: ~~~~~")
newPattern = hopfield.evaluate(tester)

print(hopfield.energy)
multipleTest(patterns,hopfield)

