import numpy as np
import math

class Kohonen:
    def __init__(self, variablesSize, K, initData=None, r=True):
        self.wSize = variablesSize
        self.K = K
        self.W = []
        if r == True:
            for i in range(K):
                aux = np.random.random(size=(K, variablesSize))
                self.W.append(aux)
        else:
            for i in range(K):
                index = np.random.randint(initData.shape[0], size=K)
                aux = initData[index, :]
                self.W.append(aux)

    def trainRule(self, data, epochs, R= 4, distEuc=True):
        iteration = 0

        while iteration < epochs:
            country = np.random.randint(data.shape[0])
            sx, sy = self._calculateMinDistance(data[country],False)
            self._neighbors_variation(self._R(iteration, R), sx, sy, data[country], iteration)
            iteration += 1


    def calculateNeuronsDistance(self):
        dist = []
        for i in range(self.K):
            distAux = []
            for j in range(self.K):
                xRow = [(i - 1) if (i - 1) >= 0 else 0,(i + 1) if (i + 1) < self.K else (self.K - 1)]  # to go through x axis
                yRow = [(j - 1) if (j - 1) >= 0 else 0,(j + 1) if (j + 1) < self.K else (self.K - 1)]  # to go through y axis
                distance = []
                for k in range(xRow[0], xRow[1]):
                    for l in range(yRow[0], yRow[1]):
                        distance.append(np.abs(self.W[i][j] - self.W[k][l]))
                distAux.append(np.mean(distance))
            dist.append(distAux)
        return dist




    def _calculateMinDistance(self, xp, distEuc):
        minx = 0
        miny = 0
        if distEuc:
            minDist = float("inf")
            for i in range(self.K):
                for j in range(self.K):
                    dist = np.linalg.norm(xp - self.W[i][j])
                    if dist < minDist:
                        minDist = dist
                        minx = i
                        miny = j
        else:
            maxArg = -float("inf")
            for i in range(self.K):
                for j in range(self.K):
                    dist = np.dot(xp, self.W[i][j].T)
                    if dist > maxArg:
                        maxArg = dist
                        minx = i
                        miny = j
        return minx, miny


    def _neighbors_variation(self,R, x, y, xp, iteration):
        pairs = []
        floorR = math.floor(R)
        xRow = [(x - floorR) if (x - floorR) >= 0 else 0,(x + floorR) if (x + floorR) < self.K else (self.K - 1)] #to go through x axis
        yRow = [(y - floorR) if (y - floorR) >= 0 else 0, (y + floorR) if (y + floorR) < self.K else (self.K - 1)] #to go through y axis

        for i in range(xRow[0], xRow[1]):
            for j in range(yRow[0], yRow[1]):
                process = True
                if i != x and j != y: #this is in the diagonal
                    if np.linalg.norm([x - i, y - j]) > R:
                        process = False

                if process == True:
                    self.W[i][j] = self.W[i][j] + self._eta(iteration) * (xp - self.W[i][j])
                    self.W[i][j] /= np.linalg.norm(self.W[i][j])

    def _R(self,t, R): #Boltzmann
        # return (1 + (R - 1) * math.exp(-0.002 * t))
        return 4


    def _eta(self, t):
        # return 1/(t + 1)
        return 0.05

