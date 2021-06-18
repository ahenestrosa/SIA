
import numpy as np

def mapToBlack(digit):
    bitmap = np.zeros((7,5))
    i = 0
    for i in range(len(digit)):
        for j in range(len(digit[i])):
            elem = digit[i][j]
            r = 1
            if elem >= 0.5:
                r = 0
            bitmap[i][j] = r

    return bitmap

def printMatrix(mat):
    for i in range(len(mat)):
        line = ''
        for j in range(len(mat[1])):
            aux = '*' if mat[i][j] >= 0 else ' '
            line += aux + " "
        print(line)

def arrayTo2DMatrix(arr, shape0): #shape 1 is determined by len(arr)/shape0
    counter = 0
    matrix = []
    aux = []
    for i in arr:
        if counter == shape0:
            matrix.append(aux)
            aux = []
            counter = 0
        aux.append(i)

        counter += 1
    matrix.append(aux)

    return matrix
def outputFromLayerReshape(arr, shape0):
    counter = 0
    matrix = []
    aux = []
    for i in arr:
        if counter == shape0:
            matrix.append(aux)
            aux = []
            counter = 0
        aux.append(i[0])
        counter += 1
    matrix.append(aux)

    return matrix