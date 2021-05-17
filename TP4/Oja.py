import numpy as np


class Oja:
    def __init__(self, variablesSize, eta=0.01):
        self.eta = eta
        self.w = np.random.random(size=(1,variablesSize))[0]
        self.w /= np.linalg.norm(self.w) # w vector norm = 1



    def trainRule(self, X, epochs):
        inflationUnemploymentW = []
        eta = self.eta #eta value will change
        printing = epochs/5000
        iteration = 0

        while iteration < epochs:
            if iteration % printing == 0:
                aux = [self.w[1], self.w[3]]
                inflationUnemploymentW.append(aux)
            wVal = self.w
            for var in X:
                s = np.dot(self.w, var.T)
                self.w = self.w + eta * s * (var - s * self.w)
            iteration += 1

            # if np.abs(wVal - self.w).all() <= eta*10:
            #     eta /= 10
        return inflationUnemploymentW