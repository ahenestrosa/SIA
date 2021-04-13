

class PerceptronSimpleStep:
    inputSize = 0
    #pesos incluyendo el umbral(w0)
    weights = []

    def __init__(self, inputSize, learningRate):
        self.inputSize = inputSize
        self.weightSize = inputSize + 1
        self.learningRate = learningRate
        #inciializo en 0
        self.weights = [0] * (self.weightSize)



    def calculateOutput(self, input):
        total = 0
        # Se le agrega 1 entrada para el umbral
        input_ext = input + [1]
        for i in range(self.weightSize):
            total += self.weights[i] * input_ext[i]
        if total > 0:
            return 1
        return -1

        

    def trainPerceptron(self, inputs, ouputs):
        for i in range(len(inputs)):
            curr_input = inputs[i]
            o = self.calculateOutput(curr_input)
            #agrego el umbral
            curr_input_ext = curr_input + [1]
            for j in range(self.weightSize):
                deltaW = self.learningRate * (ouputs[i] - o) * curr_input_ext[j]
                self.weights[j] += deltaW
    