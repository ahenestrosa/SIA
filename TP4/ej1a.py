from Kohonen import Kohonen
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import math


def outputResults(outputFile, kohonen):
    location = []
    heatmap = np.zeros((4,4))
    for i in range(valuesStd.shape[0]):
        sx, sy, d = kohonen._calculateMinDistance(valuesStd[i], True)
        aux = [sx, sy, countries[i]]
        # xLoc.append(sx)
        # yLoc.append(sy)
        heatmap[sy][sx] += 1
        location.append(aux)
    distance = kohonen.calculateNeuronsDistance()

    plt.clf()
    plt.imshow(distance)
    plt.colorbar()
    plt.savefig(outputFile + 'distance', bbox_inches='tight')



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
    posDespMap = {}
    for country in sortedCountries:
        pos =  (country[0], country[1])
        desp = posDespMap.get(pos)
        if desp == None:
            posDespMap[pos] = 0.15
        else:
            posDespMap[pos] = desp + 0.15
            pos = (pos[0], pos[1] + desp)


        plt.annotate(country[2], (pos[0] - 0.4, pos[1] - 0.3), size=8)

    plt.savefig(outputFile, bbox_inches='tight')
    plt.show()

filePath = "./Resources/europe.csv"
outputDir = "./Output/"
oututDir = "./Resources/output"

matrix = pd.read_csv(filePath)



values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']
valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

netSize = 4

def testForConfiguration(configuration, valuesStd):
    outputFile = oututDir + configuration[0]
    kohonen = Kohonen(7, netSize,initData=valuesStd, r=configuration[1])
    trainData = kohonen.trainRule(valuesStd, 1000, configuration[2], configuration[3], configuration[4], configuration[5])
    outputResults(outputFile, kohonen)
    return trainData


#Configuration
# 1. Name
# 2. Initialize random(True) or with values(False)
# 3. Initial radius
# 4. Dist euc(True) or correlation (false)
# 5. Eta variable (True)
# 6. R variable (True)

configuration = []
configuration.append(('RFixedEtaFixed', True, math.sqrt(2), True, False, False ))
configuration.append(('RFixedEtaVar', True, math.sqrt(2), True, True, False))
configuration.append(('RVarEtaVar', True, 2, True, True, True))
configuration.append(('RVarEtaFixed', True,2, True, False, True))
configuration.append(('MVRFixedEtaFixed',False,math.sqrt(2), True, False, False))
configuration.append(('MVRFixedEtaVar', False, math.sqrt(2), True, True, False))
configuration.append(('MVRVarEtaVar',False, 2, True, True, True))
configuration.append(('MVRVarEtaFixed',False,True, False, False))
configuration.append(('MVRVarEtaVarCorrelate',False,2, False,  True, True))
configuration.append(('RVarEtaVarCorrelate', True, 2, False, True, True))



trainData = testForConfiguration(configuration[0], valuesStd)

fig, ax = plt.subplots()
ax.plot(range(len(trainData)), trainData)
ax.set_xlabel("Epoch")
ax.set_ylabel("Error")
plt.show()





