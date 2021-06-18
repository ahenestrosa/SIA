import numpy as np
import math


def test(x):
    return x+1


beta = 1
def tanh(x):
    return np.tanh(beta * x)
def tanhPrime(x):
    return beta * (1 - np.power(tanh(beta * x), 2))

class PerceptronMultilayer:

    def __init__(self, inputDim, outputDim, middleLayersDim, function, learningRate, costFunction='default', momentum=None, adaptative=None):
        self.inputDim = inputDim
        self.outputDim = outputDim
        self.middleLayersDim = middleLayersDim
        self.learningRate = learningRate
        self.momentum = momentum
        self.adaptative = adaptative


        # Weights for each layer
        self.weightsByLayer = []
        self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = (middleLayersDim[0], inputDim))))
        for i in range(0, len(middleLayersDim)-1):
            self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = ( middleLayersDim[i+1], middleLayersDim[i]))))
        self.weightsByLayer.append(np.asmatrix(np.random.uniform(size = (outputDim, middleLayersDim[len(middleLayersDim)-1]))))
        
        # Bias for each layer
        self.biasByLayer = []
        self.biasByLayer.append(np.asmatrix(np.random.uniform(size=(1, middleLayersDim[0]))))
        for i in range(1, len(middleLayersDim)):
            self.biasByLayer.append(np.asmatrix(np.random.uniform(size=(1, middleLayersDim[i]))))
        self.biasByLayer.append(np.asmatrix(np.random.uniform(size=(1, outputDim)))) #Biases for layer M
        
        if costFunction == 'default':
            self.backPropagate = self.defaultPropagate
            self.calculateError = self.defaultError
        elif costFunction == 'entropic':
            if function != 'tanh':
                print('For entropic funciton should be tanh!')
                exit(1)
            self.backPropagate = self.entropicPropagate
            self.calculateError = self.entropicError
        else:
            print("Invalid cost function")

        if function == 'tanh':
            self.function = tanh
            self.functionDer = tanhPrime
        else:
            print("Invalid function")
            exit(1)

        if self.momentum != None:
            self.updateWeights = self.updateWeightsMomentum

            self.oldDeltaWByLayer = []
            self.oldDeltaWByLayer.append(np.asmatrix(np.zeros(shape = (middleLayersDim[0], inputDim))))
            for i in range(0, len(middleLayersDim)-1):
                self.oldDeltaWByLayer.append(np.asmatrix(np.zeros(shape = ( middleLayersDim[i+1], middleLayersDim[i]))))
            self.oldDeltaWByLayer.append(np.asmatrix(np.zeros(shape = (outputDim, middleLayersDim[len(middleLayersDim)-1]))))
            
            self.oldDeltaBiasByLayer = []
            self.oldDeltaBiasByLayer.append(np.asmatrix(np.zeros(shape=(1, middleLayersDim[0]))))
            for i in range(1, len(middleLayersDim)):
                self.oldDeltaBiasByLayer.append(np.asmatrix(np.zeros(shape=(1, middleLayersDim[i]))))
            self.oldDeltaBiasByLayer.append(np.asmatrix(np.zeros(shape=(1, outputDim)))) #Biases for layer M
        
            
        else: 
            self.updateWeights = self.updateWeightsDefault
            

        


    def train(self, maxError, maxEpochs, inputData, outputData, verbose=True):
        error = float('inf')
        errors = []
        for e in range(maxEpochs):
            if verbose:
                print("Epoch " + str(e))
                print("Error " + str(error))
            outputs = []
            for i in range(len(inputData)):
                res, activations, values = self.calculateOutput(inputData[i])
                deltaForLayer = self.backPropagate(outputData[i], activations, values)
                self.updateWeights(activations, deltaForLayer)
                outputs.append(res)
            
            lastError = error
            error = self.calculateError(outputData, outputs)
            if error < maxError:
                break
            errors.append(error)
            
            if self.adaptative != None:
                if error < lastError:
                    self.learningRate += self.adaptative[0]
                elif error > lastError:
                    self.learningRate -= self.adaptative[1] * self.learningRate


        print("############## FINISHED TRAINING ##################")
        print("Error: " + str(error))
        print("Epochs: " + str(e))

        return errors, e
        



    def calculateOutput(self, inputData):
        if len(inputData) != self.inputDim:
            print("Invalid data shape")
            exit(1)

        valueForLayer = [np.transpose(np.matrix(inputData))]
        activationsForLayer = [np.transpose(np.matrix(inputData))]
        currActivations = activationsForLayer[0]

        # Para cada capa calculamos el output basados en los pesos y en lso valores de la capa anterior
        for l in range(len(self.weightsByLayer)):
            # Los values se calculan segun los pesos y cada uno + el bias(threshold)
            newValues = np.matmul(self.weightsByLayer[l], currActivations)
            newValues += self.biasByLayer[l].T
            valueForLayer.append(newValues.copy())
            currActivations = self.function(newValues)
            activationsForLayer.append(currActivations)

        # Emitimos los resultados, valores activados y valores no activados para cada capa
        return activationsForLayer[-1], activationsForLayer, valueForLayer

    
    def defaultPropagate(self, expectedOutput, activationForLayer, valueForLayer):
        
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

    def entropicPropagate(self, expectedOutput, activationForLayer, valueForLayer):
    
        #Calculo delta para la capa de salida
        deltaOutLayer = []
        actualOutput = activationForLayer[-1]
        for i in range(self.outputDim):
            di = (expectedOutput[i] - actualOutput[i]) * beta
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
                di =  beta * di
                deltaLayer.append(di)
                
            deltaForLayer[m-1] = deltaLayer

        return deltaForLayer

    def updateWeightsDefault(self, activationForLayer, deltaForLayer): 
        M = len(self.weightsByLayer)
        for m in range(M):
            weights = self.weightsByLayer[m]
            biases = self.biasByLayer[m]
            activationsPrevLayer = activationForLayer[m]
            deltasNextLayer = deltaForLayer[m]

            for i in range(len(deltasNextLayer)):
                biases[0,i] += self.learningRate * deltasNextLayer[i]
                for j in range(len(activationsPrevLayer)):
                    dW = deltasNextLayer[i] * activationsPrevLayer[j]
                    weights[i,j] += self.learningRate * dW

    def updateWeightsMomentum(self, activationForLayer, deltaForLayer): 
        M = len(self.weightsByLayer)

        for m in range(M):
            weights = self.weightsByLayer[m]
            biases = self.biasByLayer[m]
            activationsPrevLayer = activationForLayer[m]
            deltasNextLayer = deltaForLayer[m]

            oldDeltaBias = self.oldDeltaBiasByLayer[m]
            oldDeltaW = self.oldDeltaWByLayer[m]

            for i in range(len(deltasNextLayer)):
                deltaBias = self.learningRate * deltasNextLayer[i] + self.momentum * oldDeltaBias[0, i]
                biases[0,i] += deltaBias 
                oldDeltaBias[0, i] = deltaBias
                for j in range(len(activationsPrevLayer)):
                    dW = deltasNextLayer[i] * activationsPrevLayer[j] * self.learningRate + self.momentum * oldDeltaW[i,j]
                    weights[i,j] += dW 
                    oldDeltaW[i,j] = dW




    def defaultError(self, realOutputs, ouputs):
        e = 0
        # Para cada ejemplo
        for u in range(len(realOutputs)):
            rO = realOutputs[u]
            o = ouputs[u]

            # Cada salida
            for i in range(len(rO)):
                e += math.pow(rO[i] - o[i], 2)
        
        return e/2

    def entropicError(self, realOutputs, ouputs):
        e = 0
        # Para cada ejemplo
        for u in range(len(realOutputs)):
            rO = realOutputs[u]
            o = ouputs[u]

            # Cada salida
            for i in range(len(rO)):
                leftTerm = 0
                rightTerm = 0
                if rO[i] != -1:
                    leftTerm  = (1/2) * (1+rO[i]) * math.log10((1+rO[i])/(1+o[i]))
                if rO[i] != 1:
                    rightTerm = (1/2) * (1-rO[i]) * math.log10((1-rO[i])/(1-o[i]))
                e += (leftTerm + rightTerm)
        
        return e

    def forwardPropagateFromLayer(self, input, layer):
        layers = len(self.weightsByLayer)
        output = [np.transpose(np.matrix(input))]
        output = output[0]
        if layer < 0 or layers < layer:
            return None
        #print()
        for nLay in range(layer , layers):
            newValues = np.matmul(self.weightsByLayer[nLay], output)
            newValues += self.biasByLayer[nLay].T
            output = self.function(newValues)
        return output

    def forwardPropagateFromToLayer(self, input, startLayer, endLayer):
        output = [np.transpose(np.matrix(input))]
        output = output[0]
        for nLay in range(startLayer , endLayer):
            newValues = np.matmul(self.weightsByLayer[nLay], output)
            newValues += self.biasByLayer[nLay].T
            output = self.function(newValues)
        return output








        



    
