from Hopfield import Hopfield
import random


def loadInput():
    f = open('./Resources/letters.txt')
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
    # for i in range(len(pattern)):
    #     print(i)
    for i in range(len(pattern)):
        m = random.uniform(0, 1)
        if m <= p:
            newP.append(pattern[i] * -1)
        else:
            newP.append(pattern[i])
    # print(pattern)
    # print(newP)
    return newP



# patterns = [ [1,1,-1,-1], [-1, -1, 1, 1]]
patterns = loadInput()
hopfield = Hopfield(patterns)

# testPattern = patterns[2].copy()

# testPattern[2] = -testPattern[2]
# testPattern[22] = -testPattern[22]

randomInput = random.randrange(4)
p = 0.3
tester = modifyInput(patterns[randomInput].copy(), p )

newPattern = hopfield.evaluate(tester)

