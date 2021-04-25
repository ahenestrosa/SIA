import getPrimeFunction as primeFunction
from utils import parseFile as parser
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from SimpleNonLinearPerceptron import SimpleNonLinearPerceptron
from SimpleLinearPerceptron import SimpleLinearPerceptron
import numpy as np


##### SIMPLE LINEAL #####
# trainingSet = parser.parseFile("resources/TP3-ej2-Conjuntoentrenamiento.txt")
# resultSet = parser.parseFile("resources/TP3-ej2-Salida-deseada.txt")

# X = []
# counter = 0
# for i in trainingSet:
#     X.append([  i[0], i[1], i[2] ,resultSet[counter]])
#     counter +=1

# slp = SimpleLinearPerceptron(len(trainingSet[0]), 0.01)
# slp.trainPerceptron(X, 0.001,10000)

# counter = 0
# for x in X:
#     activation = slp.activation(np.array(x[0]))
#     # print('activation: {}'.format(activation))
#     prediction = activation[1] + activation[2]  + activation[3] 
#     print('prediction: {} - esperado: {}'.format(prediction,resultSet[counter]) )
#     counter +=1

################


##### SIMPLE NO LINEAL #####
# Normalizo solo para el NO LINEAL
normalized = parser.readAndNormalize("resources/TP3-ej2-Conjuntoentrenamiento.txt","resources/TP3-ej2-Salida-deseada.txt")

X = []
X = [ [[y[0], y[1], y[2]], y[3]] for y in normalized]

snlp = SimpleNonLinearPerceptron(len(X[0][0]), 0.03)
snlp.trainPerceptron(X, 0.001,10000)

output = snlp.get_output(X)

for x in range(len(output)):
    print("prediction: {} -- expected: {}" .format(output[x],X[x][1] ))
################
