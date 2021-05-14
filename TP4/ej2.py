from Hopfield import Hopfield

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





# patterns = [ [1,1,-1,-1], [-1, -1, 1, 1]]


patterns = loadInput()


hopfield = Hopfield(patterns)

testPattern = patterns[2].copy()
testPattern[3] = -testPattern[3]
testPattern[2] = -testPattern[2]
testPattern[22] = -testPattern[22]
# testPattern[15] = -testPattern[15]
testPattern[16] = -testPattern[16]
testPattern[17] = -testPattern[17]

testPattern[21] = -testPattern[21]
testPattern[9] = -testPattern[9]
testPattern[9] = -testPattern[10]

newPattern = hopfield.evaluate(testPattern)