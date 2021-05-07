from Kohonen import Kohonen
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

filePath = "/Users/franciscochoi/Desktop/SIA/TP4/Resources/europe.csv"

matrix = pd.read_csv(filePath)

values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']
valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

kohonen = Kohonen(7, 20,0.01)
kohonen.trainRule(valuesStd, 1000, 2)


location = []
for i in range(valuesStd.shape[0]):
    sx, sy = kohonen._calculateMinDistance(valuesStd[i], True)
    aux = [sx,sy,countries[i]]
    location.append(aux)
    print(aux)

plt.scatter([i[0] for i in location],[i[1] for i in location], label=[i[2] for i in location])

# for i, txt in enumerate(countries):
#     plt.annotate(txt, (location[i][0], location[i][1]))

plt.legend()
plt.grid()
plt.show()