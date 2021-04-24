import numpy as np
import math

def test(x):
    return x+1


beta = 1
def tanh(x):
    return np.tanh(beta * x)

def tanhPrime(x):
    return beta* (1- math.pow(tanh(beta * x), 2))

class PerceptronMultilayer:

    def __init__(self, inputDim, outputDim, middleLayersDim, function,learningRate):
        self.inputDim = inputDim
        self.outputDim = outputDim
        self.middleLayersDim = middleLayersDim
        self.learningRate = learningRate

        self.weightsByLayer = []

        self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = (middleLayersDim[0], inputDim))))
        for i in range(0, len(middleLayersDim)-1):
            self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = ( middleLayersDim[i+1], middleLayersDim[i]))))
        self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = (outputDim, middleLayersDim[len(middleLayersDim)-1]))))
        
        if function == 'tanh':
            self.function = tanh
            self.functionDer = tanhPrime
        else:
            print("Invalid function")
            exit(1)

    #TODO: Add error ending condition
    def train(self, error, maxEpochs, inputData, outputData):

        for e in range(maxEpochs):
            for i in range(len(inputData)):
                res, activations, values = self.calculateOutput(inputData[i])
                deltaForLayer = self.backPropagate(outputData[i], activations, values)
                self.updateWeights(activations, deltaForLayer)

        
    def calculateOutput(self, inputData):
        if len(inputData) != self.inputDim:
            print("Invalid data size")
            exit(1)

        valueForLayer = [np.transpose(np.matrix(inputData))]
        activationsForLayer = [np.transpose(np.matrix(inputData))]

        # Para cada capa calculamos el output basados en los pesos y en lso valores de la capa anterior
        for l in range(len(self.weightsByLayer)):
            lastActivations = activationsForLayer[l]
            newValues = np.matmul(self.weightsByLayer[l], lastActivations)
            valueForLayer.append(newValues.copy())
            for i in range(len(newValues)):
                newValues[i] = self.function(newValues[i])
            activationsForLayer.append(newValues)

        # Emitimos los resultados, valores activados y valores no activados para cada capa
        return activationsForLayer[-1], activationsForLayer, valueForLayer

    
    def backPropagate(self, expectedOutput, activationForLayer, valueForLayer):
        
        #Calculo delta para la capa de salida
        deltaOutLayer = []
        actualOutput = activationForLayer[-1]
        for i in range(self.outputDim):
            di = (expectedOutput[i] - actualOutput[i]) * self.functionDer(valueForLayer[-1][i])
            deltaOutLayer.append(di)

        # Si hay n capas, habra n-1 deltas(el de la capa 0 no se calcula)
        M = len(valueForLayer) - 1

        deltaForLayer = [0] * M
        deltaForLayer[-1] = deltaOutLayer

        # Vamos de atras para adelante retropropagando el delta
        for m in range(M-1, 0, -1):
            #El delta de una capa mas que usamos para propagar
            nextDeltaLayer = deltaForLayer[m]
            deltaLayer = []
            #Este es el value de la capa actual, no de la capa siguiente
            valueLayer = valueForLayer[m]
            # Para cada elemento de esa capa calculo el di
            for i in range(len(valueLayer)):
                di = 0
                # Retropropaga los deltas de la capa siguiente
                for j in range(len(nextDeltaLayer)):
                    # Notar que es (j, i) porque M+1 --> filas, M --> columnas
                    di += self.weightsByLayer[m].item(j, i) * nextDeltaLayer[j]
                di =  self.functionDer(valueLayer.item(i)) * di
                deltaLayer.append(di)
                
            deltaForLayer[m-1] = deltaLayer

        return deltaForLayer

    def updateWeights(self, activationForLayer, deltaForLayer): 
        M = len(self.weightsByLayer)
        for m in range(M):
            weights = self.weightsByLayer[m]
            activationsPrevLayer = activationForLayer[m]
            deltasNextLayer = deltaForLayer[m]

            for i in range(len(deltasNextLayer)):
                for j in range(len(activationsPrevLayer)):
                    dW = deltasNextLayer[i] * activationsPrevLayer[j]
                    weights[i,j] += self.learningRate * dW





        



    
