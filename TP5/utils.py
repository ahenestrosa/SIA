def printMatrix(mat):
    for i in range(len(mat)):
        line = ''
        for j in range(len(mat[1])):
            aux = '1' if mat[i][j] >= 0 else ' '
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