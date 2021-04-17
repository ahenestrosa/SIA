import getPrimeFunction as primeFunction
from utils import parseFile as parser
from SimpleNonLinearPerceptron import SimpleNonLinearPerceptron
import numpy as np

g, gPrime = primeFunction.getPrimeFunction(0.05,'tanh') #puede ser 'tanh' o 'logistic'

trainingSet = parser.parseFile("resources/TP3-ej2-Conjuntoentrenamiento.txt")
resultSet = parser.parseFile("resources/TP3-ej2-Salida-deseada.txt")
# print(trainingSet)

X = []
counter = 0
for i in trainingSet:
    X.append([  i[0], i[1], i[2] ,resultSet[counter]])
    counter +=1

snlp = SimpleNonLinearPerceptron(len(trainingSet[0]), 0.05,g,gPrime)
