from Oja import Oja
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



filePath = "/Users/franciscochoi/Desktop/SIA/TP4/Resources/europe.csv"

matrix = pd.read_csv(filePath)

values = matrix.iloc[:,1:8].values #only values
countries = matrix.iloc[:, 0].values #only country names
varHeaders = [c for c in matrix.columns if c != 'Country']

valuesStdMat = pd.DataFrame(StandardScaler().fit_transform(values), index=countries, columns=varHeaders) #standarization of values --> z = (x - u) / s
# valuesCov = np.cov(valuesStd.T) #we need transposed matrix as numpy calculates the array as X = [x_1, x_2, ... x_N]^T

valuesStd = valuesStdMat.values

ojaRule = Oja(valuesStd.shape[1])

ojaRule.trainRule(valuesStd, 10000)

print(ojaRule.w)

#pca calculation
pca = PCA().fit(valuesStd)

pca_factory = PCA(n_components=5) #0.96 covered
Y = pca_factory.fit_transform(valuesStd)

components = pca_factory.fit(valuesStd)

print(components.components_[0]) #this shows the influence of every variable in the first component
