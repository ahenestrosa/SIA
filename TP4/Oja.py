import numpy as np


class Oja:
    def __init__(self, variablesSize, eta=0.01):
        self.eta = eta
        self.w = np.asmatrix(np.random.random(size=(1,variablesSize)))
        self.w /= np.linalg.norm(self.w) # w vector norm = 1


    def trainRule(self, X, epochs):
        eta = self.eta #eta value will change
        iteration = 0
        while iteration < epochs:
            wVal = self.w
            for var in X:
                s = np.dot(self.w, var.T)
                self.w = self.w + eta * s * (var - s * self.w)
            iteration += 1
            if np.abs(wVal - self.w).all() <= eta*10:
                eta /= 10