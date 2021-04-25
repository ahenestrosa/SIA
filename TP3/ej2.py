import getPrimeFunction as primeFunction
from utils import parseFile as parser
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from SimpleNonLinearPerceptron import SimpleNonLinearPerceptron
from SimpleLinearPerceptron import SimpleLinearPerceptron
import numpy as np

g, gPrime = primeFunction.getPrimeFunction(0.05,'logistic') #puede ser 'tanh' o 'logistic'

trainingSet = parser.parseFile("resources/TP3-ej2-Conjuntoentrenamiento.txt")
resultSet = parser.parseFile("resources/TP3-ej2-Salida-deseada.txt")

X = []
counter = 0
for i in trainingSet:
    X.append([  i[0], i[1], i[2] ,resultSet[counter]])
    counter +=1

slp = SimpleNonLinearPerceptron(len(trainingSet[0]), 0.01,g,gPrime)
slp.trainPerceptron(X, 0.001,10000)

# counter = 0
# for x in X:
#     activation = slp.activation(np.array(x[0]))
#     # print('activation: {}'.format(activation))
#     prediction = activation[1] + activation[2]  + activation[3] 
#     print('prediction: {} - esperado: {}'.format(prediction,resultSet[counter]) )
#     counter +=1

