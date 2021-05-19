from Kohonen import Kohonen
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def outputResults(outputFile, kohonen):
    location = []
    heatmap = np.zeros((4,4))
    for i in range(valuesStd.shape[0]):
        sx, sy, d = kohonen._calculateMinDistance(valuesStd[i], True)
        aux = [sx, sy, countries[i]]
        # xLoc.append(sx)
        # yLoc.append(sy)
        heatmap[sx][sy] += 1
        location.append(aux)
    distance = kohonen.calculateNeuronsDistance()

    plt.clf()
    plt.imshow(distance, origin='lower')
    plt.colorbar()
    plt.savefig(outputFile + 'distance')



    sortedCountries = sorted(location, key=lambda x: (x[0], x[1]))
    outF = open(outputFile + '.csv', 'w')
    for country in sortedCountries:
        outF.write(str(country[0]) + ',' + str(country[1]) + ',' + country[2])
        outF.write('\n')

    outF.close()


    # heatmap, xedges, yedges = np.histogram2d(xLoc, yLoc, bins=netSize)
    # extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    print(heatmap)
    plt.imshow(heatmap)
    cb = plt.colorbar()
    plt.savefig(outputFile)
    plt.show()

filePath = "./Resources/europe.csv"
oututDir = "./Resources/output/"

matrix = pd.read_csv(filePath)



values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']
valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

netSize = 4
outputFile = oututDir + 'RFixedEtaFixed'
kohonen = Kohonen(7, netSize)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'RFixedEtaVar'
kohonen = Kohonen(7, netSize)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, True, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'RVarEtaVar'
kohonen = Kohonen(7, netSize)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, True, True)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'RVarEtaFixed'
kohonen = Kohonen(7, netSize)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, True)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'MVRFixedEtaFixed'
kohonen = Kohonen(7, netSize, valuesStd, False)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'MVRFixedEtaVar'
kohonen = Kohonen(7, netSize, valuesStd, False)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, True, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'MVRVarEtaVar'
kohonen = Kohonen(7, netSize, valuesStd, False)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, True, True)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'MVRVarEtaFixed'
kohonen = Kohonen(7, netSize, valuesStd, False)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'MVRVarEtaVarCorrelate'
kohonen = Kohonen(7, netSize, valuesStd, False)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, False)

outputResults(outputFile, kohonen)

outputFile = oututDir + 'RVarEtaVarCorrelate'
kohonen = Kohonen(7, netSize)
trainData = kohonen.trainRule(valuesStd, 1000, 2, True, False, False)


outputResults(outputFile, kohonen)














# fig, ax = plt.subplots()
#
# ax.scatter(range(len(trainData)), trainData)
#
# plt.show()

