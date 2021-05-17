from Kohonen import Kohonen
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

filePath = "/Users/franciscochoi/Desktop/SIA/TP4/Resources/europe.csv"

matrix = pd.read_csv(filePath)

outputFile = 'RFixedEtaFixedMaxArgs'

values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']
valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

kohonen = Kohonen(7, 20)
kohonen.trainRule(valuesStd, 3000, 2)


location = []
xLoc = []
yLoc = []
for i in range(valuesStd.shape[0]):
    sx, sy = kohonen._calculateMinDistance(valuesStd[i], True)
    aux = [sx,sy,countries[i]]
    xLoc.append(sx)
    yLoc.append(sy)
    location.append(aux)
    # print(aux)


distance = kohonen.calculateNeuronsDistance()


plt.clf()
plt.imshow(distance,origin='lower')
plt.colorbar()
plt.savefig(outputFile + 'distance')

plt.show()



outF = open(outputFile + '.csv', 'w')
for country in location:
    outF.write(str(country[0]) + ',' + str(country[1]) + ',' + country[2])
    outF.write('\n')

outF.close()

heatmap, xedges, yedges = np.histogram2d(xLoc, yLoc, bins=20)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

print(heatmap)
plt.clf()
plt.imshow(heatmap.T,  origin='lower')
cb = plt.colorbar()
plt.savefig(outputFile)
plt.show()
