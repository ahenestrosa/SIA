import getPrimeFunction as primeFunction
from utils import parseFile as parser
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from SimpleNonLinearPerceptron import SimpleNonLinearPerceptron
from SimpleLinearPerceptron import SimpleLinearPerceptron
import numpy as np
import matplotlib.pyplot as plt
import argparse


def getError(training, perceptron):
    error = 0
    out = perceptron.get_output(training)
    for x in range(len(out)):
        error += (out[x] - training[x][1])**2
    return error/len(training)
        


##### SIMPLE LINEAL #####
def executeLinear():
    trainingSet = parser.parseFile("resources/TP3-ej2-Conjuntoentrenamiento.txt")
    resultSet = parser.parseFile("resources/TP3-ej2-Salida-deseada.txt")

    X = []
    counter = 0
    for i in trainingSet:
        X.append([ [ i[0], i[1], i[2] ],resultSet[counter]])
        counter +=1

    epochs = 10000
    slp = SimpleLinearPerceptron(len(trainingSet[0]), 0.01)
    slp.trainPerceptron(X, 0.001,epochs)

    output = slp.get_output(X)

    print("~~~~~~~~~~~~~~~~~~ Simple Linear Perceptron Results ~~~~~~~~~~~~~~~~~~ \n")
    for x in range(len(output)):
        print("prediction: {} -- expected: {}" .format(output[x],X[x][1] ))
    print(f'Min Error: {slp.minError}')

    plt.plot(range(len(slp.epochError)), slp.epochError , marker='o', linestyle='--')
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.xscale('log')
    plt.savefig(f'linear-{len(slp.epochError)}-error.png')
    plt.show()

################


##### SIMPLE NO LINEAL #####
def executeNonLinear():
    ## Normalizo solo para el NO LINEAL
    normalized = parser.readAndNormalize("resources/TP3-ej2-Conjuntoentrenamiento.txt",
                                            "resources/TP3-ej2-Salida-deseada.txt")

    X = []
    X = [ [[y[0], y[1], y[2]], y[3]] for y in normalized]

    split = int(len(X)*0.5)
    training = X[:split]
    test = X[split:]

    epochs = 10000
    snlp = SimpleNonLinearPerceptron(len(training[0][0]), 0.03)
    snlp.trainPerceptron(training, 0.001,epochs)

    output = snlp.get_output(test)

    print("~~~~~~~~~~~~~~~~~~ Simple Non Linear Perceptron Results ~~~~~~~~~~~~~~~~~~ \n")
    for x in range(len(output)):
        print("prediction: {} -- expected: {}" .format(output[x],test[x][1] ))
        print(snlp.minError)

    ## error por epoca
    plt.plot(range(len(snlp.epochError)), snlp.epochError , marker='o', linestyle='--')
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.xscale('log')
    plt.savefig(f'non-linear-{len(snlp.epochError)}-error.png')
    plt.show()

#########


def testMultipleEpochs():
    normalized = parser.readAndNormalize("resources/TP3-ej2-Conjuntoentrenamiento.txt",
                                            "resources/TP3-ej2-Salida-deseada.txt")

    X = []
    X = [ [[y[0], y[1], y[2]], y[3]] for y in normalized]

    split = int(len(X)*0.5)
    training = X[:split]
    test = X[split:]
    ## Error por epoca cambiandole el learning rate
    epochsError = {}
    for learningRate in [0.01, 0.03, 0.05]:
        epochsError[learningRate] = {'trainingError': [], 'testingError': [], 'epochs': []}
        for epochs in [10, 50, 500, 1000, 10000, 15000]:
            snlp = SimpleNonLinearPerceptron(len(training[0][0]), learningRate)
            snlp.trainPerceptron(training, 0.0,epochs)
            trainingError = getError(training, snlp)
            testingError = getError(test, snlp)
            epochsError[learningRate]['trainingError'].append(trainingError)
            epochsError[learningRate]['testingError'].append(testingError)
            epochsError[learningRate]['epochs'].append(epochs)

    for learningRate in [0.01, 0.03, 0.05]:
        plt.plot(epochsError[learningRate]['epochs'], epochsError[learningRate]['trainingError'], marker='o', linestyle='--', label="Training Error")
        plt.plot(epochsError[learningRate]['epochs'], epochsError[learningRate]['testingError'], marker='o', linestyle='--', label="Testing Error", color='red')
        plt.xlabel('Epochs')
        plt.ylabel('Mean Error')
        plt.xscale('log')
        plt.legend()
        plt.title(f'Learning Rate = {learningRate}')
        plt.savefig(f'fig-r-{learningRate}.png')
        plt.show()

################





def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-linear', dest='linear', required=False)
    parser.add_argument('-nonlinear', dest='nonlinear', required=False)
    parser.add_argument('-multipleNonLinear', dest='multipleNonLinear', required=False)
    args = parser.parse_args()

    linear = bool(args.linear)
    nonlinear = bool(args.nonlinear)
    multipleNonLinear = bool(args.multipleNonLinear)
    if linear:
        executeLinear()
    elif nonlinear:
        executeNonLinear()
    
    if multipleNonLinear:
        testMultipleEpochs()


if __name__ == "__main__":
    main()
